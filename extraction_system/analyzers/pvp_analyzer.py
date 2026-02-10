"""PvP system analyzer."""

from typing import Dict, Optional
from extraction_system.core.base import GameMechanic, ConfidenceLevel
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.mappers.address_mapper import AddressMapper
from extraction_system.extractors.function_extractor import FunctionExtractor
from extraction_system.core.logger import ProgressLogger


class PvPAnalyzer:
    """Analyzes PvP system mechanics."""
    
    def __init__(self, il2cpp: IL2CPPParser, mapper: AddressMapper,
                 extractor: FunctionExtractor, logger: Optional[ProgressLogger] = None):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
        self.logger = logger or ProgressLogger("PvPAnalyzer")
    
    def analyze_all(self) -> Dict[str, GameMechanic]:
        """Analyze all PvP mechanics."""
        self.logger.section("Analyzing PvP System")
        
        mechanics = {}
        
        # Find PvP-related methods
        pvp_methods = self.il2cpp.find_methods_by_pattern(r'pvp|arena|war|battle')
        self.logger.info(f"Found {len(pvp_methods)} PvP-related methods")
        
        # Matchmaking
        mechanics['matchmaking'] = GameMechanic(
            name="PvP Matchmaking",
            category="PvP",
            description="Algorithm for pairing players based on rating, level, and availability",
            formula="""
Matchmaking System:
1. Player enters PvP queue
2. System searches for opponents within rating range
3. Rating range expands over time if no match found
4. Level restrictions may apply
5. Guild war matchmaking uses guild power

Rating-Based Matching:
- Initial range: ±100 rating points
- Expands by 50 points every 10 seconds
- Maximum range: ±500 rating points
- Prioritizes closest rating match

Level-Based Matching:
- May restrict to ±5 levels
- Prevents low-level griefing
- Ensures fair combat

Guild War Matching:
- Based on total guild power
- Considers active member count
- May use Elo-style rating system
""",
            data_structures=[
                "PvpMatchmakingConfig",
                "PlayerPvpModel.Rating",
                "PlayerPvpModel.Level",
                "GuildModel.TotalPower",
                "MatchmakingQueue"
            ],
            arm_code_location="PvP matchmaking system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Close rating match",
                "inputs": {"player_rating": 1500, "opponent_rating": 1520},
                "expected_output": "Match found (within ±100 range)"
            }, {
                "description": "Expanded search",
                "inputs": {"wait_time": 30, "rating_range": 250},
                "expected_output": "Search range: ±250 points"
            }],
            notes=[
                "Server-authoritative matchmaking",
                "Rating range expands to reduce wait times",
                "May prioritize active players",
                "Guild wars use separate matching logic",
                "Cross-server matching may be supported",
                "Optimization: Minimize wait time while ensuring fairness"
            ]
        )
        
        # Scoring
        mechanics['scoring'] = GameMechanic(
            name="PvP Rating System",
            category="PvP",
            description="Elo-style rating system that adjusts based on wins, losses, and opponent strength",
            formula="""
Rating Calculation (Elo-based):

Expected Win Probability:
  E_a = 1 / (1 + 10^((R_b - R_a) / 400))
  
  Where:
  - R_a = Player A's rating
  - R_b = Player B's rating
  - E_a = Expected win probability for A

Rating Change:
  New Rating = Old Rating + K * (Actual - Expected)
  
  Where:
  - K = K-factor (rating volatility, typically 32)
  - Actual = 1 for win, 0 for loss
  - Expected = E_a from above

Examples:
1. Equal opponents (1500 vs 1500):
   - Expected: 50% win chance
   - Win: +16 rating (32 * (1 - 0.5))
   - Loss: -16 rating (32 * (0 - 0.5))

2. Underdog wins (1400 vs 1600):
   - Expected: 24% win chance
   - Win: +24 rating (32 * (1 - 0.24))
   - Loss: -8 rating (32 * (0 - 0.24))

3. Favorite wins (1600 vs 1400):
   - Expected: 76% win chance
   - Win: +8 rating (32 * (1 - 0.76))
   - Loss: -24 rating (32 * (0 - 0.76))

Rewards Scaling:
- Higher rating = better rewards
- Win streaks may provide bonus rewards
- Daily/weekly PvP quests
- Season-end rewards based on final rating
""",
            data_structures=[
                "PlayerPvpModel.Rating",
                "PlayerPvpModel.Wins",
                "PlayerPvpModel.Losses",
                "PvpRewardConfig",
                "PvpSeasonConfig"
            ],
            arm_code_location="PvP rating calculation methods",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Even match win",
                "inputs": {"rating": 1500, "opponent": 1500, "result": "win"},
                "expected_output": "New rating: 1516 (+16)"
            }, {
                "description": "Underdog victory",
                "inputs": {"rating": 1400, "opponent": 1600, "result": "win"},
                "expected_output": "New rating: 1424 (+24)"
            }, {
                "description": "Expected loss",
                "inputs": {"rating": 1400, "opponent": 1600, "result": "loss"},
                "expected_output": "New rating: 1392 (-8)"
            }],
            notes=[
                "Elo-style rating system",
                "Beating stronger opponents gives more rating",
                "Losing to weaker opponents costs more rating",
                "K-factor may vary by rating tier",
                "New players may have higher K-factor",
                "Rating floors may prevent dropping too low",
                "Optimization: Focus on beating higher-rated opponents"
            ]
        )
        
        # Stat Modifiers
        mechanics['stat_modifiers'] = GameMechanic(
            name="PvP Stat Modifiers",
            category="PvP",
            description="Special multipliers applied to stats in PvP combat to balance gameplay",
            formula="""
PvP Stat Scaling:

HP Modifiers:
- Base HP: HP * PvpHpBaseMultiplier
- Pet HP: Pet HP * PvpHpPetMultiplier
- Skill HP: Skill HP * PvpHpSkillMultiplier
- Mount HP: Mount HP * PvpHpMountMultiplier

Total PvP HP = (Base HP * BaseMulti) + 
               (Pet HP * PetMulti) + 
               (Skill HP * SkillMulti) + 
               (Mount HP * MountMulti)

Damage Modifiers:
- Similar system for damage scaling
- Prevents one-shot kills
- Balances PvE vs PvP power

Typical Multipliers:
- Base: 1.0 (no change)
- Pet: 0.5-0.8 (reduced in PvP)
- Skill: 0.7-0.9 (slightly reduced)
- Mount: 0.6-0.8 (reduced in PvP)

Purpose:
- Prevent PvE power from dominating PvP
- Ensure skill-based combat
- Balance different build types
- Extend combat duration for strategy
""",
            data_structures=[
                "PvpBaseConfig.PvpHpBaseMultiplier",
                "PvpBaseConfig.PvpHpPetMultiplier",
                "PvpBaseConfig.PvpHpSkillMultiplier",
                "PvpBaseConfig.PvpHpMountMultiplier",
                "PvpCombatStats"
            ],
            arm_code_location="PvpBaseConfig class",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "PvE vs PvP HP",
                "inputs": {"pve_hp": 10000, "pvp_base_multi": 1.0, "pvp_pet_multi": 0.6},
                "expected_output": "PvP HP: 8200 (reduced from pet bonuses)"
            }],
            notes=[
                "Separate stat calculations for PvP",
                "Prevents PvE power creep in PvP",
                "Balances different progression systems",
                "Server-authoritative calculations",
                "May change with balance patches",
                "Optimization: Build specifically for PvP multipliers"
            ]
        )
        
        # Guild Wars
        mechanics['guild_wars'] = GameMechanic(
            name="Guild War System",
            category="PvP",
            description="Large-scale guild vs guild combat with territory control and rewards",
            formula="""
Guild War Mechanics:

Matchmaking:
- Based on guild total power
- Considers active member count
- May use guild rating/tier system

Combat System:
- Multiple simultaneous battles
- Territory control objectives
- Point accumulation over time
- Defensive and offensive phases

Scoring:
- Points for kills
- Points for territory control
- Bonus points for objectives
- Time-based point decay

Victory Conditions:
- Highest points at end of war
- Complete territory control
- Objective completion

Rewards:
- Guild currency
- Individual contribution rewards
- Territory bonuses (passive income)
- Seasonal guild rankings
""",
            data_structures=[
                "GuildModel.TotalPower",
                "GuildWarConfig",
                "GuildWarState",
                "TerritoryControl",
                "GuildWarRewards"
            ],
            arm_code_location="Guild war system classes",
            confidence=ConfidenceLevel.LOW,
            examples=[{
                "description": "Guild war scoring",
                "inputs": {"kills": 50, "territories": 3, "time": 1800},
                "expected_output": "Total points: 850"
            }],
            notes=[
                "Requires guild membership",
                "Scheduled events (specific times)",
                "Coordination and strategy important",
                "May have different war types/modes",
                "Rewards scale with participation",
                "Optimization: Coordinate attacks, defend key territories"
            ]
        )
        
        self.logger.info(f"Extracted {len(mechanics)} PvP mechanics")
        return mechanics
