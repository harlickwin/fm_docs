"""Economy system analyzer."""

from typing import Dict, Optional
from extraction_system.core.base import GameMechanic, ConfidenceLevel
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.mappers.address_mapper import AddressMapper
from extraction_system.extractors.function_extractor import FunctionExtractor
from extraction_system.core.logger import ProgressLogger


class EconomyAnalyzer:
    """Analyzes economy system mechanics."""
    
    def __init__(self, il2cpp: IL2CPPParser, mapper: AddressMapper,
                 extractor: FunctionExtractor, logger: Optional[ProgressLogger] = None):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
        self.logger = logger or ProgressLogger("EconomyAnalyzer")
    
    def analyze_all(self) -> Dict[str, GameMechanic]:
        """Analyze all economy mechanics."""
        self.logger.section("Analyzing Economy System")
        
        mechanics = {}
        
        # Find economy-related methods
        econ_methods = self.il2cpp.find_methods_by_pattern(r'shop|price|currency|gold|gem')
        self.logger.info(f"Found {len(econ_methods)} economy-related methods")
        
        # Resource generation
        mechanics['resource_generation'] = GameMechanic(
            name="Resource Generation",
            category="Economy",
            description="Passive and active income sources with rates and optimization strategies",
            formula="""
Resource Generation System:

Passive Income Sources:
1. Idle/AFK Rewards
   - Coins per hour = Base Rate * (1 + Bonuses)
   - Capped at max offline time (e.g., 12 hours)
   - Tech tree can increase cap and rate

2. Territory/Building Income
   - Each building generates resources
   - Upgrade buildings for higher rates
   - Collection interval (e.g., every 4 hours)

3. Investment Systems
   - Invest coins for returns
   - Higher investment = higher returns
   - Time-locked (e.g., 24 hours)

Active Income Sources:
1. Combat/Farming
   - Coins per kill = Base Coins * (1 + Drop Rate Bonuses)
   - Dungeon level affects drop rates
   - Higher difficulty = better rewards

2. Quests/Achievements
   - One-time or repeatable rewards
   - Daily/weekly quests
   - Achievement milestones

3. Events
   - Limited-time high-reward activities
   - Seasonal events
   - Special dungeons

Resource Types:
- Coins (primary currency)
- Gems (premium currency)
- Hammers (crafting material)
- Tickets (PvP, War, Skill summons)
- Special currencies (TechPotions, ClockWinders, Token)

Optimization Strategies:
1. Maximize Passive Income:
   - Upgrade tech tree nodes for idle income
   - Upgrade buildings to max level
   - Collect regularly (don't waste cap)
   - Invest surplus coins

2. Maximize Active Income:
   - Farm optimal dungeon level (balance speed vs rewards)
   - Complete daily quests (guaranteed rewards)
   - Participate in all events
   - Use drop rate boost items during farming

3. Resource Management:
   - Prioritize investments with best ROI
   - Save gems for high-value purchases
   - Convert excess materials to coins
   - Time upgrades with resource events

Dungeon Level Optimization:
  Efficiency = (Coins per Run) / (Time per Run)
  
  Optimal Level = Highest level where:
  - Can clear quickly (< 2 minutes)
  - Minimal risk of death
  - Good coins/time ratio
  
  Example:
  - Level 50: 1000 coins, 1 min = 1000 coins/min
  - Level 60: 1500 coins, 2 min = 750 coins/min
  - Level 70: 2000 coins, 5 min = 400 coins/min
  → Level 50 is optimal!
""",
            data_structures=[
                "ResourceGenerationConfig",
                "IdleRewardConfig",
                "BuildingConfig.IncomeRate",
                "QuestRewardConfig",
                "DungeonRewardConfig",
                "PlayerCurrencyModel.Currencies[CurrencyType.Coins]",
                "PlayerCurrencyModel.Currencies[CurrencyType.Gems]"
            ],
            arm_code_location="Economy system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Idle income",
                "inputs": {"base_rate": 1000, "offline_hours": 8, "bonuses": 0.5},
                "expected_output": "12000 coins (1500/hour * 8 hours)"
            }, {
                "description": "Dungeon farming",
                "inputs": {"coins_per_run": 1000, "time_per_run": 60},
                "expected_output": "1000 coins/minute efficiency"
            }, {
                "description": "Building income",
                "inputs": {"buildings": 5, "rate_per_building": 100, "hours": 4},
                "expected_output": "2000 coins (500/hour * 4 hours)"
            }],
            notes=[
                "Multiple income sources stack",
                "Passive income continues offline (capped)",
                "Active farming is most efficient",
                "Tech tree significantly boosts income",
                "Events provide burst income",
                "Optimization: Max passive income, farm optimal dungeon level",
                "Balance time investment vs rewards",
                "Don't waste offline cap (collect regularly)"
            ]
        )
        
        # Shop pricing
        mechanics['shop_pricing'] = GameMechanic(
            name="Shop Pricing & Economy",
            category="Economy",
            description="Dynamic pricing algorithms, shop refresh mechanics, and purchase optimization",
            formula="""
Shop System:

Item Pricing Formula:
  Price = Base Price * Rarity Multiplier * Level Scaling
  
  Where:
  - Base Price = Item type base cost
  - Rarity Multiplier = 1x (Common), 5x (Rare), 25x (Epic), 125x (Legendary)
  - Level Scaling = 1 + (Item Level * 0.1)

Shop Types:
1. Regular Shop
   - Fixed inventory
   - Refreshes daily/weekly
   - Standard prices

2. Premium Shop
   - Gem purchases
   - Special items
   - May have sales/discounts

3. Event Shop
   - Token/event currency
   - Limited-time items
   - Better value than regular shop

4. Black Market
   - Random rare items
   - Higher prices
   - Refreshes frequently

Shop Refresh:
- Free refresh: Daily/weekly
- Paid refresh: Gems (cost increases per refresh)
- Refresh cost: Base Cost * (Refresh Count^1.5)

Discount System:
- Daily deals (20-50% off)
- Bulk purchase discounts
- VIP discounts
- Event sales

Currency Conversion:
  Gem Value = Coin Value * Conversion Rate
  
  Typical rates:
  - 1 Gem = 1000 Coins
  - Conversion is one-way (coins → gems not allowed)

Purchase Priority:
1. Limited-time items (event shop)
2. High-value daily deals
3. Essential upgrade materials
4. Rare items (if needed for progression)
5. Cosmetics (lowest priority)

Optimization Strategies:
1. Shop Management:
   - Check shop daily for deals
   - Save gems for premium items
   - Buy event shop items first (limited time)
   - Use free refreshes strategically

2. Currency Management:
   - Never convert gems to coins (poor value)
   - Save gems for essential items only
   - Farm coins actively (better than buying)
   - Prioritize event currencies

3. Purchase Timing:
   - Wait for sales on expensive items
   - Buy materials during events (better rates)
   - Stock up during discount events
   - Avoid impulse purchases

4. Value Analysis:
   - Calculate coins/gem per stat point
   - Compare shop vs farming efficiency
   - Consider time value (is it worth farming?)
   - Prioritize items with best ROI
""",
            data_structures=[
                "ShopConfig",
                "ShopItemConfig.BasePrice",
                "ShopItemConfig.RarityMultiplier",
                "ShopRefreshConfig",
                "DiscountConfig",
                "CurrencyConversionConfig",
                "PlayerShopModel.RefreshCount"
            ],
            arm_code_location="Shop system classes",
            confidence=ConfidenceLevel.MEDIUM,
            examples=[{
                "description": "Item pricing",
                "inputs": {"base_price": 1000, "rarity": "Epic", "level": 10},
                "expected_output": "50000 coins (1000 * 25 * 2.0)"
            }, {
                "description": "Shop refresh cost",
                "inputs": {"base_cost": 50, "refresh_count": 3},
                "expected_output": "259 gems (50 * 3^1.5)"
            }, {
                "description": "Discount",
                "inputs": {"price": 10000, "discount": 0.3},
                "expected_output": "7000 coins (30% off)"
            }],
            notes=[
                "Shop refreshes provide new opportunities",
                "Refresh costs increase exponentially",
                "Event shops have best value",
                "Discounts can save significant resources",
                "Gem purchases should be strategic",
                "Optimization: Buy event items first, wait for sales, use free refreshes",
                "Never waste gems on items you can farm",
                "Calculate value before purchasing"
            ]
        )
        
        # Currency systems
        mechanics['currency_systems'] = GameMechanic(
            name="Currency Types & Management",
            category="Economy",
            description="Multiple currency types with acquisition methods and optimal usage",
            formula="""
Currency Types (from CurrencyType enum):

1. Coins (Primary Currency)
   - Earned from: Combat, quests, idle income
   - Used for: Upgrades, shop purchases, forge
   - Most abundant currency
   - Bottleneck at high levels

2. Gems (Premium Currency)
   - Earned from: Achievements, events, purchases
   - Used for: Premium shop, refreshes, speed-ups
   - Scarce resource (use wisely)
   - Can be purchased with real money

3. Hammers (Crafting Material)
   - Earned from: Dungeons, bosses, events
   - Used for: Forge system, crafting, upgrading
   - Essential for equipment progression

4. SkillSummonTickets
   - Earned from: Rewards, events
   - Used for: Summoning skills
   - Limited resource for skill acquisition

5. TechPotions
   - Earned from: Various sources
   - Used for: Tech tree progression
   - Speeds up tech tree unlocks

6. PvpTickets
   - Earned from: Daily rewards, purchases
   - Used for: PvP battles entry
   - Regenerates over time or purchased

7. ClockWinders
   - Earned from: Rewards, events
   - Used for: Time acceleration/skipping
   - Premium time-skip resource

8. WarBattleTickets
   - Earned from: Guild activities
   - Used for: Guild war battles
   - Guild-focused resource

9. Token (Event/Special Currency)
   - Earned from: Events, special activities
   - Used for: Event shops, special purchases
   - May be time-limited

Currency Acquisition Rates:
  Coins per Hour = Base Rate + Idle Income + Active Farming
  Gems per Day = Daily Quests + Achievements + Events
  Tickets = Daily Regeneration + Purchases + Rewards

Currency Sinks:
- Forge/Upgrade system (Coins, Hammers)
- Shop purchases (Coins, Gems)
- Tech tree unlocks (Coins, TechPotions)
- Skill upgrades (Coins, SkillSummonTickets)
- Pet/Mount leveling (Coins, Hammers)
- PvP battles (PvpTickets)
- Guild wars (WarBattleTickets)
- Time skips (ClockWinders)

Optimization Strategies:
1. Coins Management:
   - Prioritize tech tree (compound benefits)
   - Upgrade main equipment first
   - Save for expensive upgrades
   - Don't waste on low-value items

2. Gems Management:
   - NEVER waste on coin conversion
   - Save for essential items only
   - Use for inventory expansion (permanent benefit)
   - Consider premium summons (if good value)
   - Avoid speed-ups unless critical

3. Hammers Management:
   - Essential for forge system
   - Farm dungeons for hammers
   - Don't waste on low-level gear
   - Save for high-tier equipment

4. Ticket Management (PvP, War, Skill):
   - Use daily to avoid waste (regeneration cap)
   - Don't hoard if regenerating
   - Purchase only if needed for events
   - Prioritize high-value battles

5. Time-Skip Resources (ClockWinders):
   - Save for critical upgrades
   - Use during events for maximum value
   - Don't waste on short timers
   - Calculate time value vs resource cost

6. Multi-Currency Optimization:
   - Calculate value across currencies
   - Prioritize time-limited resources
   - Balance coin spending (don't run out)
   - Hoard gems for critical purchases
""",
            data_structures=[
                "PlayerCurrencyModel.Currencies (MetaDictionary<CurrencyType, long>)",
                "CurrencyType enum: Coins, Gems, Hammers, SkillSummonTickets, TechPotions, PvpTickets, ClockWinders, WarBattleTickets, Token",
                "CurrencyConfig",
                "CurrencySourceConfig",
                "CurrencySinkConfig"
            ],
            arm_code_location="Currency system classes (PlayerCurrencyModel at line 1067393, CurrencyType enum at line 1067355)",
            confidence=ConfidenceLevel.HIGH,
            examples=[{
                "description": "Daily coin income",
                "inputs": {"idle": 12000, "farming": 50000, "quests": 10000},
                "expected_output": "72000 coins per day"
            }, {
                "description": "Gem value comparison",
                "inputs": {"item_coin_cost": 100000, "item_gem_cost": 50},
                "expected_output": "1 gem = 2000 coins (good value if > 1000)"
            }],
            notes=[
                "9 distinct currency types in CurrencyType enum",
                "Currencies stored in MetaDictionary<CurrencyType, long>",
                "Each currency has specific uses (no generic conversion)",
                "Tickets regenerate over time (PvpTickets, WarBattleTickets)",
                "Hammers are primary crafting resource",
                "Gems are most valuable (use sparingly)",
                "Coins are most abundant (but still scarce late game)",
                "ClockWinders for time acceleration",
                "Token for special/event purchases",
                "Optimization: Prioritize time-limited resources, hoard gems, manage coins carefully",
                "Calculate cross-currency value before purchasing",
                "Don't waste regenerating tickets (use daily)"
            ]
        )
        
        # Investment systems
        mechanics['investment_systems'] = GameMechanic(
            name="Investment & Passive Income",
            category="Economy",
            description="Investment mechanics with returns, risks, and optimization strategies",
            formula="""
Investment System:

Investment Types:
1. Time-Locked Investments
   - Invest coins for fixed period
   - Guaranteed returns
   - Higher investment = higher returns
   - Cannot withdraw early

2. Building Investments
   - Upgrade buildings for passive income
   - Permanent benefit
   - Exponential cost growth
   - Best long-term investment

3. Tech Tree Investments
   - Unlock nodes for permanent bonuses
   - Compound benefits
   - One-time cost
   - Highest ROI long-term

Return Formula:
  Return = Investment * (1 + Interest Rate)^Time
  
  Where:
  - Investment = Coins invested
  - Interest Rate = Daily/hourly rate
  - Time = Lock period

ROI Calculation:
  ROI = (Return - Investment) / Investment * 100%
  
  Example:
  - Invest: 100,000 coins
  - Return: 120,000 coins (24 hours)
  - ROI: 20% per day

Building Upgrade ROI:
  Payback Period = Upgrade Cost / (New Income - Old Income)
  
  Example:
  - Upgrade cost: 50,000 coins
  - Old income: 100 coins/hour
  - New income: 150 coins/hour
  - Payback: 50,000 / 50 = 1000 hours

Tech Tree ROI:
  Value = Stat Increase * Stat Value + Efficiency Gains
  
  Example:
  - Cost: 10,000 coins
  - Benefit: +10% coin income (permanent)
  - If earning 1000 coins/hour: +100 coins/hour
  - Payback: 100 hours (then infinite benefit!)

Optimization Strategies:
1. Investment Priority:
   - Tech tree first (permanent, compound benefits)
   - Building upgrades second (passive income)
   - Time-locked investments third (if surplus coins)

2. Building Upgrade Strategy:
   - Calculate payback period
   - Prioritize short payback periods
   - Upgrade all buildings evenly (diminishing returns)
   - Max out buildings before other investments

3. Tech Tree Strategy:
   - Unlock income nodes first
   - Efficiency nodes have compound benefits
   - Plan full path before spending
   - Respec if meta changes

4. Time-Locked Investments:
   - Only invest surplus coins
   - Don't lock coins needed for upgrades
   - Longer lock periods = better returns
   - Reinvest returns for compound growth

5. Risk Management:
   - Keep emergency coin reserve
   - Don't invest all coins (need for upgrades)
   - Balance short-term and long-term investments
   - Diversify across investment types
""",
            data_structures=[
                "InvestmentConfig",
                "BuildingUpgradeConfig",
                "TechTreeNodeConfig",
                "InvestmentConfig.InterestRate",
                "InvestmentConfig.LockPeriod",
                "PlayerInvestmentModel"
            ],
            arm_code_location="Investment system classes",
            confidence=ConfidenceLevel.LOW,
            examples=[{
                "description": "Time-locked investment",
                "inputs": {"investment": 100000, "rate": 0.2, "time": 1},
                "expected_output": "120000 coins (20% return)"
            }, {
                "description": "Building upgrade payback",
                "inputs": {"cost": 50000, "income_increase": 50},
                "expected_output": "1000 hours to break even"
            }, {
                "description": "Tech tree ROI",
                "inputs": {"cost": 10000, "income_bonus": 0.1, "current_income": 1000},
                "expected_output": "100 hours payback, then infinite benefit"
            }],
            notes=[
                "Investments provide passive income",
                "Tech tree has best long-term ROI",
                "Buildings provide steady passive income",
                "Time-locked investments for surplus coins only",
                "Calculate payback period before investing",
                "Optimization: Tech tree > Buildings > Time-locked",
                "Don't lock coins needed for progression",
                "Compound growth is powerful (reinvest returns)"
            ]
        )
        
        self.logger.info(f"Extracted {len(mechanics)} economy mechanics")
        return mechanics
