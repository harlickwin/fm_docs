"""Progression system analyzer."""

from typing import Dict, Optional
from extraction_system.core.base import GameMechanic, ConfidenceLevel
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.mappers.address_mapper import AddressMapper
from extraction_system.extractors.function_extractor import FunctionExtractor
from extraction_system.core.logger import ProgressLogger


class ProgressionAnalyzer:
    """Analyzes progression system mechanics."""
    
    def __init__(self, il2cpp: IL2CPPParser, mapper: AddressMapper,
                 extractor: FunctionExtractor, logger: Optional[ProgressLogger] = None):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
        self.logger = logger or ProgressLogger("ProgressionAnalyzer")
    
    def analyze_all(self) -> Dict[str, GameMechanic]:
        """Analyze all progression mechanics."""
        self.logger.section("Analyzing Progression System")
        
        mechanics = {}
        
        # Find progression-related methods
        prog_methods = self.il2cpp.find_methods_by_pattern(r'tech|forge|upgrade|level')
        self.logger.info(f"Found {len(prog_methods)} progression-related methods")
        
        # Tech tree
        mechanics['tech_tree'] = GameMechanic(
            name="Tech Tree System",
            category="Progression",
            description="Technology tree with nodes providing permanent stat bonuses and unlocks",
            formula="""
Tech Tree Structure:

Node System:
- Each node has prerequisites (parent nodes)
- Nodes cost resources to unlock
- Nodes provide stat bonuses or unlocks

Node Types:
1. Stat Bonus Nodes
   - Increase specific stats (HP, Damage, etc.)
   - Percentage or flat bonuses
   - Permanent once unlocked

2. Unlock Nodes
   - Unlock new features/systems
   - Enable new equipment slots
   - Unlock new areas/dungeons

3. Efficiency Nodes
   - Reduce costs (forge, upgrade)
   - Increase drop rates
   - Improve resource generation

Cost Formula:
  Node Cost = Base Cost * (1 + Level * Cost Scaling)
  
  Where:
  - Base Cost = Initial resource requirement
  - Level = Node tier/level
  - Cost Scaling = Exponential growth factor

Stat Contribution:
  Total Stat Bonus = Sum of all unlocked node bonuses
  
  Example:
  - Node 1: +5% HP
  - Node 2: +10% HP
  - Node 3: +100 flat HP
  - Total: +15% HP + 100 flat HP

Optimization Strategy:
- Prioritize stat nodes for main stats
- Unlock efficiency nodes early (compound benefits)
- Follow optimal path for build type
- Consider prerequisite chains
- Balance immediate power vs long-term efficiency
""",
            data_structures=[
                "TechTreeNodeConfig",
                "TechTreeStatContribution",
                "PlayerTechTreeModel",
                "TechTreeNodeConfig.Prerequisites",
                "TechTreeNodeConfig.Cost",
                "TechTreeNodeConfig.StatBonuses"
            ],
            arm_code_location="Tech tree system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Unlock stat node",
                "inputs": {"node_id": "hp_boost_1", "cost": 1000, "bonus": "+10% HP"},
                "expected_output": "Node unlocked, HP increased by 10%"
            }, {
                "description": "Node with prerequisites",
                "inputs": {"node_id": "advanced_damage", "prereqs": ["basic_damage_1", "basic_damage_2"]},
                "expected_output": "Requires 2 prerequisite nodes"
            }],
            notes=[
                "Permanent progression system",
                "Requires careful planning (may have respec costs)",
                "Different paths for different builds",
                "Efficiency nodes provide compound benefits",
                "May have multiple tech trees (combat, economy, etc.)",
                "Optimization: Unlock efficiency nodes early, plan full path",
                "Sources: Quest rewards, dungeon drops, shop purchases"
            ]
        )
        
        # Forge
        mechanics['forge'] = GameMechanic(
            name="Forge/Upgrade System",
            category="Progression",
            description="Equipment enhancement system with costs, success rates, and stat improvements",
            formula="""
Forge System:

Upgrade Levels:
- Equipment can be upgraded multiple times
- Each level increases stats
- Costs increase exponentially

Upgrade Cost Formula:
  Cost = Base Cost * (Level^Cost Exponent) * Rarity Multiplier
  
  Where:
  - Base Cost = Initial upgrade cost
  - Level = Current upgrade level
  - Cost Exponent = Growth rate (typically 1.5-2.0)
  - Rarity Multiplier = Higher for rare items

Success Rate:
  Success Rate = Base Rate * (1 - Level * Failure Scaling)
  
  Typical rates:
  - Level 1-5: 100% success
  - Level 6-10: 90% success
  - Level 11-15: 70% success
  - Level 16-20: 50% success
  - Level 21+: 30% success

Failure Consequences:
- Item may lose levels (safe zones exist)
- Item may be destroyed (at high levels)
- Resources are always consumed

Stat Improvement:
  New Stat = Base Stat * (1 + Level * Stat Growth)
  
  Example:
  - Base Damage: 100
  - Level 10 upgrade: +50% damage
  - New Damage: 150

Protection Items:
- Prevent level loss on failure
- Prevent item destruction
- Increase success rate
- Consumed on use

Optimization Strategy:
- Use protection items at high levels
- Upgrade during success rate events
- Focus on main equipment first
- Consider cost vs benefit ratio
- Stop at safe breakpoints (e.g., +15)
""",
            data_structures=[
                "ForgeConfig",
                "ItemUpgradeConfig",
                "ForgeConfig.SuccessRate",
                "ForgeConfig.CostFormula",
                "ForgeConfig.StatGrowth",
                "ProtectionItemConfig"
            ],
            arm_code_location="Forge system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Successful upgrade",
                "inputs": {"level": 5, "success_rate": 0.9, "roll": 0.5},
                "expected_output": "Upgrade successful! Level 5 → 6"
            }, {
                "description": "Failed upgrade",
                "inputs": {"level": 15, "success_rate": 0.5, "roll": 0.7},
                "expected_output": "Upgrade failed! Level 15 → 14"
            }, {
                "description": "Stat improvement",
                "inputs": {"base_damage": 100, "level": 10, "growth": 0.05},
                "expected_output": "New damage: 150 (+50%)"
            }],
            notes=[
                "High-risk, high-reward system",
                "Exponential cost growth",
                "Success rate decreases with level",
                "Protection items are valuable",
                "May have safe zones (no level loss)",
                "Optimization: Use protection at high levels, stop at safe points",
                "Major resource sink (gold, materials)"
            ]
        )
        
        # Pet System
        mechanics['pet_system'] = GameMechanic(
            name="Pet Leveling & Evolution",
            category="Progression",
            description="Pet progression system with leveling, evolution, and stat scaling",
            formula="""
Pet Leveling:

Experience Formula:
  XP Required = Base XP * (Level^XP Exponent)
  
  Where:
  - Base XP = Initial XP requirement
  - Level = Current pet level
  - XP Exponent = Growth rate (typically 1.8-2.2)

Stat Scaling:
  Pet Stat = Base Stat * (1 + Level * Level Scaling) * Rarity Multiplier
  
  Where:
  - Base Stat = Initial stat value
  - Level Scaling = Growth per level (e.g., 0.05 = 5% per level)
  - Rarity Multiplier = Higher for rare pets

Evolution System:
- Pets can evolve at specific levels
- Evolution increases rarity tier
- Evolution resets level but increases base stats
- Evolution requires special materials

Evolution Stat Boost:
  New Base Stat = Old Base Stat * Evolution Multiplier
  
  Typical multipliers:
  - Common → Rare: 1.5x
  - Rare → Epic: 2.0x
  - Epic → Legendary: 2.5x

Pet Bonuses:
- Passive stat bonuses to player
- Active skills (combat abilities)
- Collection bonuses (multiple pets)

Optimization Strategy:
- Level main pet to max before evolving
- Collect multiple pets for collection bonuses
- Focus on pets with desired stat bonuses
- Evolve pets during material events
- Balance leveling costs vs stat gains
""",
            data_structures=[
                "PetBalancingConfig",
                "PetLevelConfig",
                "PetEvolutionConfig",
                "PlayerPetModel.Level",
                "PlayerPetModel.Experience",
                "PetBalancingConfig.DamageMultiplier",
                "PetBalancingConfig.HealthMultiplier"
            ],
            arm_code_location="Pet system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Pet level up",
                "inputs": {"level": 10, "xp_required": 1000, "current_xp": 1200},
                "expected_output": "Level up! 10 → 11"
            }, {
                "description": "Pet evolution",
                "inputs": {"rarity": "Rare", "base_damage": 100, "evolution_multi": 2.0},
                "expected_output": "Evolved to Epic! Base damage: 100 → 200"
            }],
            notes=[
                "Pets provide significant stat bonuses",
                "Evolution is major power spike",
                "XP requirements grow exponentially",
                "Multiple pets provide collection bonuses",
                "Pet skills can change combat strategy",
                "Optimization: Max level before evolving, collect multiple pets",
                "Sources: Egg hatching, events, shop"
            ]
        )
        
        # Mount System
        mechanics['mount_system'] = GameMechanic(
            name="Mount Leveling & Bonuses",
            category="Progression",
            description="Mount progression system with leveling, stat bonuses, and movement speed",
            formula="""
Mount Leveling:

Similar to pets but focused on:
- Movement speed bonuses
- Combat stat bonuses
- Passive bonuses

Mount Stat Formula:
  Mount Stat = Base Stat * (1 + Level * Level Scaling) * Rarity Multiplier

Movement Speed Bonus:
  Total Speed = Base Speed * (1 + Mount Speed Bonus)
  
  Typical bonuses:
  - Common mount: +50% speed
  - Rare mount: +100% speed
  - Epic mount: +150% speed
  - Legendary mount: +200% speed

Combat Bonuses:
- HP increase
- Damage increase
- Special abilities

Mount Collection:
- Multiple mounts provide collection bonuses
- Higher rarity = better bonuses
- Synergizes with pet bonuses

Optimization Strategy:
- Prioritize movement speed for farming efficiency
- Level combat mounts for difficult content
- Collect multiple mounts for collection bonuses
- Focus on highest rarity mounts
- Balance speed vs combat bonuses
""",
            data_structures=[
                "MountBalancingConfig",
                "MountLevelConfig",
                "PlayerMountModel.Level",
                "MountStats.MoveSpeed",
                "MountStats.HpMax",
                "MountStats.Dmg"
            ],
            arm_code_location="Mount system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Mount speed bonus",
                "inputs": {"base_speed": 5.0, "mount_bonus": 1.0},
                "expected_output": "Total speed: 10.0 (100% faster)"
            }, {
                "description": "Mount stat bonus",
                "inputs": {"player_hp": 1000, "mount_hp_bonus": 500},
                "expected_output": "Total HP: 1500"
            }],
            notes=[
                "Mounts significantly increase farming efficiency",
                "Movement speed is most valuable stat",
                "Combat bonuses stack with other sources",
                "Collection bonuses reward diversity",
                "Higher rarity = exponentially better",
                "Optimization: Max speed mount for farming, combat mount for bosses",
                "Sources: Mount summoning, events, shop"
            ]
        )
        
        # Skill System
        mechanics['skill_system'] = GameMechanic(
            name="Skill Leveling & Upgrades",
            category="Progression",
            description="Skill progression with leveling, upgrades, and build customization",
            formula="""
Skill Leveling:

Skill Level Formula:
  Skill Power = Base Power * (1 + Level * Power Scaling)
  Skill Cost = Base Cost * (Level^Cost Exponent)
  
  Where:
  - Base Power = Initial skill effectiveness
  - Power Scaling = Growth per level (e.g., 0.1 = 10% per level)
  - Cost Exponent = Resource cost growth (typically 1.5)

Skill Types:
1. Active Skills
   - Direct damage abilities
   - Buffs and debuffs
   - Cooldown-based

2. Passive Skills
   - Permanent stat bonuses
   - Proc-based effects
   - Always active

3. Ultimate Skills
   - High-power abilities
   - Long cooldowns
   - Game-changing effects

Skill Points:
- Earned through leveling
- Limited resource (requires planning)
- May have respec options (with cost)

Skill Synergies:
- Some skills enhance others
- Build-defining combinations
- Meta builds emerge

Optimization Strategy:
- Max core skills first
- Balance active and passive skills
- Consider skill synergies
- Plan full build before spending points
- Save points for key breakpoints
- Respec during meta shifts
""",
            data_structures=[
                "SkillConfig",
                "SkillLevelConfig",
                "PlayerSkillModel.Level",
                "SkillConfig.BasePower",
                "SkillConfig.Cooldown",
                "SkillConfig.Cost"
            ],
            arm_code_location="Skill system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Skill level up",
                "inputs": {"base_damage": 100, "level": 10, "scaling": 0.1},
                "expected_output": "New damage: 200 (100% increase)"
            }, {
                "description": "Skill cost",
                "inputs": {"base_cost": 100, "level": 5, "exponent": 1.5},
                "expected_output": "Upgrade cost: 1118"
            }],
            notes=[
                "Skills define build identity",
                "Limited skill points require planning",
                "Synergies create powerful combinations",
                "Active skills require manual use",
                "Passive skills are always active",
                "Optimization: Max core skills, plan synergies, save for key levels",
                "Sources: Level ups, quests, achievements"
            ]
        )
        
        self.logger.info(f"Extracted {len(mechanics)} progression mechanics")
        return mechanics
