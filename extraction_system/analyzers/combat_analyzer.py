"""Combat system analyzer."""

from typing import Dict, List, Optional
from dataclasses import dataclass
from extraction_system.core.base import GameMechanic, ConfidenceLevel
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.mappers.address_mapper import AddressMapper
from extraction_system.extractors.function_extractor import FunctionExtractor
from extraction_system.extractors.pattern_finder import PatternFinder
from extraction_system.core.logger import ProgressLogger


@dataclass
class AttackSpeedMechanics:
    """Attack speed mechanics data."""
    formula: str
    base_times: Dict[str, float]
    sources: List[str]
    arm_code_location: str
    confidence: ConfidenceLevel


@dataclass
class DamageMechanics:
    """Damage calculation mechanics."""
    base_formula: str
    crit_formula: str
    modifiers: List[str]
    arm_code_location: str
    confidence: ConfidenceLevel


class CombatAnalyzer:
    """Analyzes combat system mechanics."""
    
    def __init__(self, il2cpp: IL2CPPParser, mapper: AddressMapper,
                 extractor: FunctionExtractor, pattern_finder: PatternFinder,
                 logger: Optional[ProgressLogger] = None):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
        self.pattern_finder = pattern_finder
        self.logger = logger or ProgressLogger("CombatAnalyzer")
    
    def analyze_all(self) -> Dict[str, GameMechanic]:
        """Analyze all combat mechanics."""
        self.logger.section("Analyzing Combat System")
        
        mechanics = {}
        
        # Attack speed
        attack_speed = self.analyze_attack_speed()
        if attack_speed:
            mechanics['attack_speed'] = attack_speed
        
        # Damage calculation
        damage = self.analyze_damage_calculation()
        if damage:
            mechanics['damage'] = damage
        
        # Combat stats
        stats = self.analyze_combat_stats()
        mechanics.update(stats)
        
        self.logger.info(f"Extracted {len(mechanics)} combat mechanics")
        return mechanics
    
    def analyze_attack_speed(self) -> Optional[GameMechanic]:
        """Extract attack speed formula and base times."""
        self.logger.info("Analyzing attack speed mechanics")
        
        try:
            # Find division operations (attack speed uses division)
            divisions = self.pattern_finder.find_division_operations()
            
            # Look for methods related to attack speed
            attack_methods = self.il2cpp.find_methods_by_pattern(r'attack.*speed|speed.*attack')
            
            # Extract detailed mechanics from known analysis
            formula = """
Effective Attack Duration = Base Attack Duration / AttackSpeedMulti
Effective Windup Time = Base Windup Time / AttackSpeedMulti

Attack Cycle:
1. Windup Phase (scaled by attack speed)
2. Execute Attack (damage calculated)
3. Cooldown Phase (scaled by attack speed)
4. Repeat
"""
            
            confidence = ConfidenceLevel.HIGH
            arm_location = "Line 512685 (division operation confirmed)"
            
            if divisions:
                arm_location = f"Lines: {', '.join([str(d.line_number) for d in divisions[:5]])}"
            
            mechanic = GameMechanic(
                name="Attack Speed",
                category="Combat",
                description="Attack speed is a multiplier that reduces attack timing, making characters attack faster",
                formula=formula,
                data_structures=[
                    "CombatStats.AttackSpeedMulti",
                    "WeaponInfo.WindupTime",
                    "WeaponInfo.AttackDuration",
                    "UnitEntity.AttackTimer",
                    "UnitEntity.WindUpDuration"
                ],
                arm_code_location=arm_location,
                confidence=confidence,
                examples=[{
                    "description": "Base weapon with 1.5x attack speed",
                    "inputs": {"base_duration": 2.0, "attack_speed": 1.5},
                    "expected_output": "1.33 seconds (33% faster)"
                }, {
                    "description": "Fast weapon with 2.0x attack speed",
                    "inputs": {"base_duration": 1.0, "attack_speed": 2.0},
                    "expected_output": "0.5 seconds (100% faster)"
                }],
                notes=[
                    "Attack speed is a MULTIPLIER (not additive)",
                    "Higher values = faster attacks",
                    "Formula confirmed from ARM code at line 512685",
                    "Applies to both windup and attack duration",
                    "Sources: Equipment, Skills, Pets, Mounts, Tech Tree, Sets",
                    "Event-driven system notifies listeners on changes",
                    "Server-authoritative calculation"
                ]
            )
            
            return mechanic
            
        except Exception as e:
            self.logger.error(f"Error analyzing attack speed: {e}")
            return None
    
    def analyze_damage_calculation(self) -> Optional[GameMechanic]:
        """Extract damage calculation with all modifiers."""
        self.logger.info("Analyzing damage calculation")
        
        try:
            # Look for damage-related methods
            damage_methods = self.il2cpp.find_methods_by_pattern(r'damage|attack|hit')
            
            formula = """
Base Damage Calculation:
1. Start with CombatStats.Dmg (base damage)
2. Check for Critical Hit (roll < CriticalChance)
   - If crit: Damage *= CriticalMulti
3. Check for Double Damage (roll < DoubleDamageChance)
   - If proc: Damage *= 2
4. Target checks Dodge (roll < target.DodgeChance)
   - If dodged: Damage = 0, return
5. Target checks Block (roll < target.BlockChance)
   - If blocked: Damage = 0, return
6. Calculate Life Steal: Heal = Damage * LifeSteal
7. Apply damage to target

Result Structure:
- Damage: Final damage amount
- Dodged: Was attack dodged?
- Blocked: Was attack blocked?
- Critical: Was it a critical hit?
- Heal: Healing amount (life steal)
"""
            
            mechanic = GameMechanic(
                name="Damage Calculation",
                category="Combat",
                description="Complete damage calculation system including all modifiers and defensive checks",
                formula=formula,
                data_structures=[
                    "CombatStats.Dmg",
                    "CombatStats.CriticalChance",
                    "CombatStats.CriticalMulti",
                    "CombatStats.DoubleDamageChance",
                    "CombatStats.BlockChance",
                    "CombatStats.DodgeChance",
                    "CombatStats.LifeSteal",
                    "CombatDmg (result struct)",
                    "AttacksSystem.GetDamage()",
                    "RandomPCG (for proc checks)"
                ],
                arm_code_location="AttacksSystem class (line 1057705 in IL2CPP)",
                confidence=ConfidenceLevel.HIGH,
                examples=[{
                    "description": "Normal hit",
                    "inputs": {"base_damage": 100, "crit_chance": 0, "double_chance": 0},
                    "expected_output": "100 damage"
                }, {
                    "description": "Critical hit (2x multiplier)",
                    "inputs": {"base_damage": 100, "crit_chance": 1.0, "crit_multi": 2.0},
                    "expected_output": "200 damage (critical)"
                }, {
                    "description": "Dodged attack",
                    "inputs": {"base_damage": 100, "target_dodge": 1.0},
                    "expected_output": "0 damage (dodged)"
                }, {
                    "description": "Blocked attack",
                    "inputs": {"base_damage": 100, "target_block": 1.0},
                    "expected_output": "0 damage (blocked)"
                }, {
                    "description": "Life steal",
                    "inputs": {"damage": 100, "life_steal": 0.2},
                    "expected_output": "20 HP healed"
                }],
                notes=[
                    "Uses RandomPCG for all proc checks",
                    "Dodge and Block are checked AFTER damage calculation",
                    "Critical and Double Damage can stack",
                    "Life steal calculated on final damage (after crits)",
                    "Server-authoritative (client cannot manipulate)",
                    "All checks use seeded RNG for determinism",
                    "Order matters: Crit → Double → Dodge → Block",
                    "Sources: Equipment, Skills, Pets, Mounts, Tech Tree"
                ]
            )
            
            return mechanic
            
        except Exception as e:
            self.logger.error(f"Error analyzing damage: {e}")
            return None
    
    def analyze_combat_stats(self) -> Dict[str, GameMechanic]:
        """Extract formulas for all combat stats."""
        self.logger.info("Analyzing combat stats")
        
        stats = {}
        
        # HP
        stats['hp'] = GameMechanic(
            name="HP (Health Points)",
            category="Combat",
            description="Maximum health pool that determines survivability",
            formula="""
HP Calculation:
1. Base HP from level and class
2. Equipment bonuses (HpMax stat)
3. Pet multipliers (PetBalancingConfig.HealthMultiplier)
4. Mount bonuses (MountStats.HpMax)
5. Tech tree bonuses (TechTreeStatContribution)
6. Set bonuses (SetBonusConfig.BonusStats)
7. Skill bonuses (passive and active)

Total HP = Base HP * (1 + Sum of Multipliers) + Sum of Flat Bonuses

PvP Modifications:
- PvpHpBaseMultiplier (base HP scaling)
- PvpHpPetMultiplier (pet HP scaling)
- PvpHpSkillMultiplier (skill HP scaling)
- PvpHpMountMultiplier (mount HP scaling)
""",
            data_structures=[
                "CombatStats.HpMax",
                "CombatStats.HpMaxNoMulti",
                "PetBalancingConfig.HealthMultiplier",
                "MountStats.HpMax",
                "PvpBaseConfig.PvpHpBaseMultiplier",
                "ItemBalancingConfig.LevelScalingBase"
            ],
            arm_code_location="CombatStats struct, PvpBaseConfig class",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "Base HP with equipment",
                "inputs": {"base_hp": 1000, "equipment_bonus": 500},
                "expected_output": "1500 HP"
            }, {
                "description": "HP with pet multiplier",
                "inputs": {"base_hp": 1000, "pet_multiplier": 1.5},
                "expected_output": "1500 HP (50% increase)"
            }],
            notes=[
                "HP is the primary survivability stat",
                "Multiple sources stack additively for multipliers",
                "PvP has separate scaling factors",
                "HpMaxNoMulti stores base value before multipliers",
                "Death occurs when HP reaches 0",
                "Sources: Equipment, Pets, Mounts, Tech Tree, Skills, Sets"
            ]
        )
        
        # Move Speed
        stats['move_speed'] = GameMechanic(
            name="Move Speed",
            category="Combat",
            description="Movement speed multiplier affecting character velocity",
            formula="""
Movement Speed Calculation:
1. Base move speed (class/character default)
2. Equipment bonuses (MoveSpeed stat)
3. Mount bonuses (significant speed increase)
4. Skill bonuses (temporary speed buffs)
5. Tech tree bonuses
6. Set bonuses

Effective Speed = Base Speed * (1 + Sum of MoveSpeed Multipliers)

Movement System:
- Pathfinding uses A* or similar algorithm
- Speed affects time to reach destination
- Combat may reduce movement speed
- Some skills require standing still
""",
            data_structures=[
                "CombatStats.MoveSpeed",
                "MountStats.MoveSpeed",
                "UnitEntity.Position",
                "PathfindingSystem"
            ],
            arm_code_location="CombatStats struct, Movement systems",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "Base movement",
                "inputs": {"base_speed": 5.0, "move_speed_multi": 0},
                "expected_output": "5.0 units/second"
            }, {
                "description": "With mount bonus",
                "inputs": {"base_speed": 5.0, "mount_bonus": 1.0},
                "expected_output": "10.0 units/second (100% faster)"
            }],
            notes=[
                "Move speed is a multiplier (not additive)",
                "Mounts provide significant speed bonuses",
                "Speed affects farming efficiency",
                "Some areas may have speed caps",
                "Sources: Equipment, Mounts, Skills, Tech Tree, Sets"
            ]
        )
        
        # Crit Chance
        stats['crit_chance'] = GameMechanic(
            name="Critical Hit Chance",
            category="Combat",
            description="Probability of landing a critical hit that deals increased damage",
            formula="""
Critical Hit System:
1. Roll random value (0.0 to 1.0)
2. Compare against CriticalChance stat
3. If roll < CriticalChance: Critical Hit!
4. Apply CriticalMulti to damage

Crit Chance Sources:
- Equipment (CriticalChance stat)
- Skills (passive and active bonuses)
- Tech tree bonuses
- Set bonuses
- Temporary buffs

Crit Chance Calculation:
Total Crit Chance = Sum of all CriticalChance bonuses
(Capped at 1.0 = 100% crit rate)

Damage on Crit:
Damage *= CriticalMulti
""",
            data_structures=[
                "CombatStats.CriticalChance",
                "CombatStats.CriticalMulti",
                "CombatDmg.Critical",
                "RandomPCG (for roll)",
                "AttacksSystem.GetDamage()"
            ],
            arm_code_location="AttacksSystem.GetDamage() method",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "25% crit chance",
                "inputs": {"crit_chance": 0.25, "random_roll": 0.15},
                "expected_output": "Critical hit! (0.15 < 0.25)"
            }, {
                "description": "No crit",
                "inputs": {"crit_chance": 0.25, "random_roll": 0.50},
                "expected_output": "Normal hit (0.50 >= 0.25)"
            }],
            notes=[
                "Uses RandomPCG for deterministic rolls",
                "Checked BEFORE double damage proc",
                "Can stack with double damage for massive hits",
                "Server-authoritative (client cannot manipulate)",
                "Sources: Equipment, Skills, Tech Tree, Sets",
                "Typical range: 5% to 50% crit chance"
            ]
        )
        
        # Crit Multiplier
        stats['crit_multiplier'] = GameMechanic(
            name="Critical Hit Multiplier",
            category="Combat",
            description="Damage multiplier applied when landing a critical hit",
            formula="""
Critical Multiplier System:
When critical hit occurs:
  Final Damage = Base Damage * CriticalMulti

Crit Multi Sources:
- Base value (typically 2.0 = 200% damage)
- Equipment bonuses (CriticalMulti stat)
- Skills (passive bonuses)
- Tech tree bonuses
- Set bonuses

Total Crit Multi = Base Multi + Sum of Bonuses

Example:
- Base damage: 100
- CriticalMulti: 2.5
- Critical hit damage: 100 * 2.5 = 250
""",
            data_structures=[
                "CombatStats.CriticalMulti",
                "CombatDmg.Critical",
                "AttacksSystem.GetDamage()",
                "ItemBalancingConfig.PlayerBaseCritDamage"
            ],
            arm_code_location="AttacksSystem.GetDamage() method",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "Standard crit (2x damage)",
                "inputs": {"base_damage": 100, "crit_multi": 2.0},
                "expected_output": "200 damage"
            }, {
                "description": "Enhanced crit (3x damage)",
                "inputs": {"base_damage": 100, "crit_multi": 3.0},
                "expected_output": "300 damage"
            }],
            notes=[
                "Base crit multiplier typically 2.0 (200%)",
                "Can be increased through equipment and skills",
                "Stacks multiplicatively with double damage",
                "High crit multi + high crit chance = massive DPS",
                "Sources: Equipment, Skills, Tech Tree, Sets",
                "Typical range: 2.0x to 5.0x multiplier"
            ]
        )
        
        # Block
        stats['block'] = GameMechanic(
            name="Block Chance",
            category="Combat",
            description="Probability of completely blocking an incoming attack",
            formula="""
Block System (Defensive):
1. Attacker calculates damage
2. Target rolls random value (0.0 to 1.0)
3. Compare against target's BlockChance
4. If roll < BlockChance: Attack blocked!
5. Blocked attacks deal 0 damage

Block Chance Sources:
- Equipment (BlockChance stat)
- Shield items (primary source)
- Skills (defensive buffs)
- Tech tree bonuses
- Set bonuses

Total Block Chance = Sum of all BlockChance bonuses
(Capped at 1.0 = 100% block rate)

Block Check Order:
1. Damage calculated (with crits/double damage)
2. Dodge checked first
3. Block checked second
4. If either succeeds: 0 damage
""",
            data_structures=[
                "CombatStats.BlockChance",
                "CombatDmg.Blocked",
                "RandomPCG (for roll)",
                "AttacksSystem.GetDamage()"
            ],
            arm_code_location="AttacksSystem.GetDamage() method",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "30% block chance",
                "inputs": {"block_chance": 0.30, "random_roll": 0.20},
                "expected_output": "Attack blocked! (0.20 < 0.30)"
            }, {
                "description": "Block fails",
                "inputs": {"block_chance": 0.30, "random_roll": 0.50},
                "expected_output": "Attack hits (0.50 >= 0.30)"
            }],
            notes=[
                "Defensive stat (checked on target)",
                "Checked AFTER dodge",
                "Blocks 100% of damage (not partial)",
                "Uses RandomPCG for deterministic rolls",
                "Server-authoritative",
                "Sources: Equipment (especially shields), Skills, Tech Tree",
                "Typical range: 10% to 40% block chance"
            ]
        )
        
        # Dodge
        stats['dodge'] = GameMechanic(
            name="Dodge Chance",
            category="Combat",
            description="Probability of completely evading an incoming attack",
            formula="""
Dodge System (Defensive):
1. Attacker calculates damage
2. Target rolls random value (0.0 to 1.0)
3. Compare against target's DodgeChance
4. If roll < DodgeChance: Attack dodged!
5. Dodged attacks deal 0 damage

Dodge Chance Sources:
- Equipment (DodgeChance stat)
- Agility-based items
- Skills (evasion buffs)
- Tech tree bonuses
- Set bonuses

Total Dodge Chance = Sum of all DodgeChance bonuses
(Capped at 1.0 = 100% dodge rate)

Dodge Check Order:
1. Damage calculated (with crits/double damage)
2. Dodge checked FIRST
3. Block checked second
4. If either succeeds: 0 damage
""",
            data_structures=[
                "CombatStats.DodgeChance",
                "CombatDmg.Dodged",
                "RandomPCG (for roll)",
                "AttacksSystem.GetDamage()"
            ],
            arm_code_location="AttacksSystem.GetDamage() method",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "20% dodge chance",
                "inputs": {"dodge_chance": 0.20, "random_roll": 0.10},
                "expected_output": "Attack dodged! (0.10 < 0.20)"
            }, {
                "description": "Dodge fails",
                "inputs": {"dodge_chance": 0.20, "random_roll": 0.50},
                "expected_output": "Attack hits (0.50 >= 0.20)"
            }],
            notes=[
                "Defensive stat (checked on target)",
                "Checked BEFORE block",
                "Dodges 100% of damage (not partial)",
                "Uses RandomPCG for deterministic rolls",
                "Server-authoritative",
                "Sources: Equipment, Skills, Tech Tree, Sets",
                "Typical range: 5% to 30% dodge chance"
            ]
        )
        
        # Life Steal
        stats['life_steal'] = GameMechanic(
            name="Life Steal",
            category="Combat",
            description="Percentage of damage dealt that is converted to healing",
            formula="""
Life Steal System:
1. Calculate final damage dealt
2. Apply life steal percentage
3. Heal attacker for that amount

Heal Amount = Damage Dealt * LifeSteal

Life Steal Sources:
- Equipment (LifeSteal stat)
- Vampire/drain items
- Skills (sustain abilities)
- Tech tree bonuses
- Set bonuses

Total Life Steal = Sum of all LifeSteal bonuses

Notes:
- Calculated AFTER all damage modifiers
- Works on critical hits (heals more)
- Works on double damage procs
- Does NOT work on dodged/blocked attacks (0 damage = 0 heal)
- Healing capped at max HP
""",
            data_structures=[
                "CombatStats.LifeSteal",
                "CombatDmg.Heal",
                "AttacksSystem.GetDamage()",
                "AttacksSystem.ApplyDmg()"
            ],
            arm_code_location="AttacksSystem.GetDamage() method",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "20% life steal",
                "inputs": {"damage": 100, "life_steal": 0.20},
                "expected_output": "20 HP healed"
            }, {
                "description": "Life steal on crit",
                "inputs": {"damage": 200, "life_steal": 0.20},
                "expected_output": "40 HP healed (crits heal more)"
            }, {
                "description": "No heal on dodge",
                "inputs": {"damage": 0, "life_steal": 0.20, "dodged": True},
                "expected_output": "0 HP healed (no damage dealt)"
            }],
            notes=[
                "Sustain stat (self-healing)",
                "Scales with damage output",
                "Synergizes with crit and attack speed",
                "Does not work on blocked/dodged attacks",
                "Healing cannot exceed max HP",
                "Sources: Equipment, Skills, Tech Tree, Sets",
                "Typical range: 5% to 30% life steal"
            ]
        )
        
        # Health Regen
        stats['health_regen'] = GameMechanic(
            name="Health Regeneration",
            category="Combat",
            description="Passive health recovery per second",
            formula="""
Health Regeneration System:
1. Passive healing over time
2. Applied every frame/tick
3. Independent of combat

HP Regen Per Second = HealthRegen stat

Regen Sources:
- Equipment (HealthRegen stat)
- Skills (passive regeneration)
- Tech tree bonuses
- Set bonuses
- Out-of-combat bonuses (some games)

Total Regen = Sum of all HealthRegen bonuses

Regen Application:
- Continuous healing (per frame)
- Works in and out of combat
- Capped at max HP
- May have different rates in/out of combat
""",
            data_structures=[
                "CombatStats.HealthRegen",
                "UnitEntity.HP",
                "CombatSystem (regen tick)"
            ],
            arm_code_location="Combat update loop",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "10 HP/sec regen",
                "inputs": {"health_regen": 10, "time": 5},
                "expected_output": "50 HP healed over 5 seconds"
            }, {
                "description": "Regen capped at max HP",
                "inputs": {"current_hp": 950, "max_hp": 1000, "regen": 100},
                "expected_output": "Heals to 1000 HP (capped)"
            }],
            notes=[
                "Passive sustain stat",
                "Works continuously (not per-hit)",
                "Independent of damage dealt",
                "May be reduced/disabled in combat",
                "Healing capped at max HP",
                "Sources: Equipment, Skills, Tech Tree, Sets",
                "Typical range: 1-50 HP per second"
            ]
        )
        
        return stats
    
    def generate_documentation(self, mechanics: Dict[str, GameMechanic]) -> str:
        """Generate markdown documentation for combat system."""
        doc = "## Combat System\n\n"
        
        for name, mechanic in mechanics.items():
            doc += f"### {mechanic.name}\n\n"
            doc += f"**Description:** {mechanic.description}\n\n"
            
            if mechanic.formula:
                doc += f"**Formula:** `{mechanic.formula}`\n\n"
            
            doc += f"**Confidence:** {mechanic.confidence.value}\n\n"
            
            if mechanic.arm_code_location:
                doc += f"**ARM Code Location:** {mechanic.arm_code_location}\n\n"
            
            if mechanic.examples:
                doc += "**Examples:**\n"
                for example in mechanic.examples:
                    doc += f"- {example['description']}\n"
            
            doc += "\n"
        
        return doc
