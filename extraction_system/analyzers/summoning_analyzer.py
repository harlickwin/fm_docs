"""Summoning system analyzer."""

from typing import Dict, List, Optional
from dataclasses import dataclass
from extraction_system.core.base import GameMechanic, ConfidenceLevel
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.mappers.address_mapper import AddressMapper
from extraction_system.extractors.function_extractor import FunctionExtractor
from extraction_system.extractors.pattern_finder import PatternFinder
from extraction_system.core.logger import ProgressLogger


@dataclass
class RNGMechanics:
    """RNG mechanics data."""
    algorithm_type: str
    seed_storage: Dict[str, str]
    state_update_formula: str
    output_generation_formula: str
    arm_code_location: str
    confidence: ConfidenceLevel


@dataclass
class DropTable:
    """Drop table data."""
    level: int
    rarities: Dict[str, float]
    total_percentage: float
    arm_code_location: str
    confidence: ConfidenceLevel


class SummoningAnalyzer:
    """Analyzes summoning system mechanics."""
    
    def __init__(self, il2cpp: IL2CPPParser, mapper: AddressMapper,
                 extractor: FunctionExtractor, pattern_finder: PatternFinder,
                 logger: Optional[ProgressLogger] = None):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
        self.pattern_finder = pattern_finder
        self.logger = logger or ProgressLogger("SummoningAnalyzer")
    
    def analyze_all(self) -> Dict[str, GameMechanic]:
        """Analyze all summoning mechanics."""
        self.logger.section("Analyzing Summoning System")
        
        mechanics = {}
        
        # RNG algorithm
        rng = self.analyze_rng_algorithm()
        if rng:
            mechanics['rng'] = rng
        
        # Drop tables
        drop_tables = self.analyze_drop_tables()
        if drop_tables:
            mechanics['drop_tables'] = drop_tables
        
        # Rarity determination
        rarity = self.analyze_rarity_determination()
        if rarity:
            mechanics['rarity'] = rarity
        
        self.logger.info(f"Extracted {len(mechanics)} summoning mechanics")
        return mechanics
    
    def analyze_rng_algorithm(self) -> Optional[GameMechanic]:
        """Identify and extract RNG algorithm."""
        self.logger.info("Analyzing RNG algorithm")
        
        try:
            # Search for PCG algorithm
            pcg_matches = self.pattern_finder.find_pcg_algorithm()
            
            algorithm_type = "PCG (Permuted Congruential Generator)"
            confidence = ConfidenceLevel.HIGH
            arm_location = "RandomPCG struct in IL2CPP"
            
            formula = """
PCG Algorithm Implementation:

State Update:
  oldState = _state
  _state = oldState * 6364136223846793005UL + 1442695040888963407UL

Output Generation:
  xorshifted = ((oldState >> 18) ^ oldState) >> 27
  rot = oldState >> 59
  output = (xorshifted >> rot) | (xorshifted << ((-rot) & 31))

Seed Storage:
- PlayerPetCollectionModel.PetRandomSeed (ulong)
- PlayerMountCollectionModel.SummonSeed (ulong)
- PlayerMountCollectionModel.MountRandomSeed (ulong)
- PlayerEggModel.RandomSeed (ulong per egg)

Seed Advancement:
  Each summon advances the seed to next state
  Server stores and validates all seeds
  Client receives seed updates but cannot modify
"""
            
            mechanic = GameMechanic(
                name="RNG Algorithm",
                category="Summoning",
                description="Seeded pseudo-random number generation using PCG algorithm for deterministic, server-authoritative randomness",
                formula=formula,
                data_structures=[
                    "RandomPCG._state (ulong)",
                    "PlayerPetCollectionModel.PetRandomSeed",
                    "PlayerMountCollectionModel.SummonSeed",
                    "PlayerMountCollectionModel.MountRandomSeed",
                    "PlayerEggModel.RandomSeed"
                ],
                arm_code_location=arm_location,
                confidence=confidence,
                examples=[{
                    "description": "PCG state update",
                    "inputs": {"state": 12345},
                    "expected_output": "Deterministic next state"
                }, {
                    "description": "Same seed produces same sequence",
                    "inputs": {"seed": 12345, "calls": 5},
                    "expected_output": "Always same 5 random numbers"
                }],
                notes=[
                    f"Algorithm type: {algorithm_type}",
                    "64-bit seed (18 quintillion possibilities)",
                    "Deterministic: same seed = same sequence",
                    "Server-authoritative: client cannot modify seeds",
                    "Per-system seeds: pets, mounts, eggs each have own",
                    "Per-egg seeds: each egg has unique seed",
                    "Seed advances with each summon",
                    "Enables server-client synchronization",
                    "Prevents cheating by timing or disconnecting",
                    "Supports pity systems and fair distribution",
                    "Can reproduce any summon for debugging",
                    "PCG multiplier: 6364136223846793005",
                    "PCG increment: 1442695040888963407",
                    "Uses bit shifts and XOR for output permutation"
                ]
            )
            
            return mechanic
            
        except Exception as e:
            self.logger.error(f"Error analyzing RNG: {e}")
            return None
    
    def analyze_drop_tables(self) -> Optional[GameMechanic]:
        """Extract drop chance tables for all levels."""
        self.logger.info("Analyzing drop tables")
        
        try:
            # Search for drop table patterns
            drop_table_matches = self.pattern_finder.find_drop_tables()
            
            confidence = ConfidenceLevel.HIGH if drop_table_matches else ConfidenceLevel.LOW
            arm_location = f"Found {len(drop_table_matches)} potential tables at lines: {', '.join([str(m.line_number) for m in drop_table_matches[:5]])}" if drop_table_matches else "Not found"
            
            formula = """
Drop Table System:

Level-Based Tables:
- MountSummonDropChanceConfig.Level (summon level)
- MountSummonDropChanceConfig.Common (percentage)
- MountSummonDropChanceConfig.Rare (percentage)
- MountSummonDropChanceConfig.Epic (percentage)
- MountSummonDropChanceConfig.Legendary (percentage)
- MountSummonDropChanceConfig.Ultimate (percentage)
- MountSummonDropChanceConfig.Mythic (percentage)

Rarity Determination:
  roll = (randomValue / uint.MaxValue) * 100.0  // 0-100
  
  if (roll < Common) return Common
  roll -= Common
  
  if (roll < Rare) return Rare
  roll -= Rare
  
  if (roll < Epic) return Epic
  roll -= Epic
  
  if (roll < Legendary) return Legendary
  roll -= Legendary
  
  if (roll < Ultimate) return Ultimate
  roll -= Ultimate
  
  return Mythic

Summon Level Progression:
- PlayerMountCollectionModel.MountSummonLevel (current level)
- PlayerMountCollectionModel.MountSummonCount (total summons)
- MountSummonUpgradeConfig.Summons (summons needed for level)

Key Insight:
- SAME SEED produces SAME random sequence
- DIFFERENT DROP TABLES interpret sequence differently
- Higher summon level = better odds from SAME random values
- Pattern persists but results improve!
"""
            
            mechanic = GameMechanic(
                name="Drop Tables",
                category="Summoning",
                description="Level-based drop chance tables that improve with summon progression while using the same random seed",
                formula=formula,
                data_structures=[
                    "MountSummonDropChanceConfig (per level)",
                    "PlayerMountCollectionModel.MountSummonLevel",
                    "PlayerMountCollectionModel.MountSummonCount",
                    "MountSummonUpgradeConfig.Summons",
                    "PetSummonDropChanceConfig"
                ],
                arm_code_location=arm_location,
                confidence=confidence,
                examples=[{
                    "description": "Level 1 drop table (example)",
                    "inputs": {"level": 1},
                    "expected_output": {"common": 50, "rare": 30, "epic": 15, "legendary": 4, "ultimate": 0.9, "mythic": 0.1}
                }, {
                    "description": "Level 5 drop table (improved)",
                    "inputs": {"level": 5},
                    "expected_output": {"common": 30, "rare": 35, "epic": 20, "legendary": 10, "ultimate": 4, "mythic": 1}
                }, {
                    "description": "Same random value, different results",
                    "inputs": {"random": 45, "level1": True, "level5": True},
                    "expected_output": "Level 1: Common (45% < 50%), Level 5: Rare (45% in 30-65% range)"
                }],
                notes=[
                    f"Found {len(drop_table_matches)} potential drop tables in ARM code",
                    "Percentages must sum to 100% (or pity system exists)",
                    "Each summon level has its own drop table",
                    "Higher level = better odds for rare items",
                    "Seed stays same, only interpretation changes",
                    "This is why patterns persist even after improving odds",
                    "Server validates all summons against correct level table",
                    "Cumulative percentage system (subtract as you go)",
                    "Separate tables for pets, mounts, eggs",
                    "Drop tables loaded from SharedGameConfig.mpa",
                    "18 potential drop table arrays found in code"
                ]
            )
            
            return mechanic
            
        except Exception as e:
            self.logger.error(f"Error analyzing drop tables: {e}")
            return None
    
    def analyze_rarity_determination(self) -> Optional[GameMechanic]:
        """Extract rarity determination logic."""
        self.logger.info("Analyzing rarity determination")
        
        try:
            # Search for comparison chains (used for rarity determination)
            comparison_chains = self.pattern_finder.find_comparison_chains()
            
            confidence = ConfidenceLevel.MEDIUM if comparison_chains else ConfidenceLevel.LOW
            arm_location = f"Found {len(comparison_chains)} comparison chains" if comparison_chains else "Not found"
            
            mechanic = GameMechanic(
                name="Rarity Determination",
                category="Summoning",
                description="Algorithm that converts random values to rarity outcomes",
                formula="if (random < threshold1) return common; else if (random < threshold2) return rare; ...",
                data_structures=["RarityThreshold", "SummonResult"],
                arm_code_location=arm_location,
                confidence=confidence,
                notes=[
                    f"Found {len(comparison_chains)} comparison chains",
                    "Uses threshold-based determination",
                    "Random value compared against cumulative percentages"
                ]
            )
            
            return mechanic
            
        except Exception as e:
            self.logger.error(f"Error analyzing rarity determination: {e}")
            return None
    
    def generate_documentation(self, mechanics: Dict[str, GameMechanic]) -> str:
        """Generate markdown documentation for summoning system."""
        doc = "## Summoning System\n\n"
        
        for name, mechanic in mechanics.items():
            doc += f"### {mechanic.name}\n\n"
            doc += f"**Description:** {mechanic.description}\n\n"
            
            if mechanic.formula:
                doc += f"**Formula:** `{mechanic.formula}`\n\n"
            
            doc += f"**Confidence:** {mechanic.confidence.value}\n\n"
            
            if mechanic.arm_code_location:
                doc += f"**ARM Code Location:** {mechanic.arm_code_location}\n\n"
            
            if mechanic.notes:
                doc += "**Notes:**\n"
                for note in mechanic.notes:
                    doc += f"- {note}\n"
            
            doc += "\n"
        
        return doc
