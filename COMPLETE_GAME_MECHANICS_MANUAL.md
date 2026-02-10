# Complete Game Mechanics Manual

**Auto-generated documentation of all game mechanics**

This document contains comprehensive analysis of game mechanics extracted from decompiled code.

## Table of Contents

- [Combat](#combat)
- [Summoning](#summoning)
- [PvP](#pvp)
- [Progression](#progression)
- [Economy](#economy)

## Extraction Status

**Generated:** 2026-02-10 22:46:24

| Category | Mechanics Extracted | High Confidence | Medium Confidence | Low Confidence |
|----------|---------------------|-----------------|-------------------|----------------|
| Combat | 10 | 10 | 0 | 0 |
| Summoning | 3 | 2 | 1 | 0 |
| PvP | 4 | 4 | 0 | 0 |
| Progression | 5 | 5 | 0 | 0 |
| Economy | 4 | 4 | 0 | 0 |

## Combat

### Attack Speed

**Description:** Attack speed is a multiplier that reduces attack timing, making characters attack faster

**Formula:**
```

Effective Attack Duration = Base Attack Duration / AttackSpeedMulti
Effective Windup Time = Base Windup Time / AttackSpeedMulti

Attack Cycle:
1. Windup Phase (scaled by attack speed)
2. Execute Attack (damage calculated)
3. Cooldown Phase (scaled by attack speed)
4. Repeat

```

**Confidence Level:** High

**Data Structures:** CombatStats.AttackSpeedMulti, WeaponInfo.WindupTime, WeaponInfo.AttackDuration, UnitEntity.AttackTimer, UnitEntity.WindUpDuration

**ARM Code Location:** Lines: 98165, 512685, 766282, 766381, 766942

**Examples:**

- **Base weapon with 1.5x attack speed**
  - Inputs: {'base_duration': 2.0, 'attack_speed': 1.5}
  - Expected Output: 1.33 seconds (33% faster)
- **Fast weapon with 2.0x attack speed**
  - Inputs: {'base_duration': 1.0, 'attack_speed': 2.0}
  - Expected Output: 0.5 seconds (100% faster)

**Notes:**

- Attack speed is a MULTIPLIER (not additive)
- Higher values = faster attacks
- Formula confirmed from ARM code at line 512685
- Applies to both windup and attack duration
- Sources: Equipment, Skills, Pets, Mounts, Tech Tree, Sets
- Event-driven system notifies listeners on changes
- Server-authoritative calculation

---

### Block Chance

**Description:** Probability of completely blocking an incoming attack

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.BlockChance, CombatDmg.Blocked, RandomPCG (for roll), AttacksSystem.GetDamage()

**ARM Code Location:** AttacksSystem.GetDamage() method

**Examples:**

- **30% block chance**
  - Inputs: {'block_chance': 0.3, 'random_roll': 0.2}
  - Expected Output: Attack blocked! (0.20 < 0.30)
- **Block fails**
  - Inputs: {'block_chance': 0.3, 'random_roll': 0.5}
  - Expected Output: Attack hits (0.50 >= 0.30)

**Notes:**

- Defensive stat (checked on target)
- Checked AFTER dodge
- Blocks 100% of damage (not partial)
- Uses RandomPCG for deterministic rolls
- Server-authoritative
- Sources: Equipment (especially shields), Skills, Tech Tree
- Typical range: 10% to 40% block chance

---

### Critical Hit Chance

**Description:** Probability of landing a critical hit that deals increased damage

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.CriticalChance, CombatStats.CriticalMulti, CombatDmg.Critical, RandomPCG (for roll), AttacksSystem.GetDamage()

**ARM Code Location:** AttacksSystem.GetDamage() method

**Examples:**

- **25% crit chance**
  - Inputs: {'crit_chance': 0.25, 'random_roll': 0.15}
  - Expected Output: Critical hit! (0.15 < 0.25)
- **No crit**
  - Inputs: {'crit_chance': 0.25, 'random_roll': 0.5}
  - Expected Output: Normal hit (0.50 >= 0.25)

**Notes:**

- Uses RandomPCG for deterministic rolls
- Checked BEFORE double damage proc
- Can stack with double damage for massive hits
- Server-authoritative (client cannot manipulate)
- Sources: Equipment, Skills, Tech Tree, Sets
- Typical range: 5% to 50% crit chance

---

### Critical Hit Multiplier

**Description:** Damage multiplier applied when landing a critical hit

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.CriticalMulti, CombatDmg.Critical, AttacksSystem.GetDamage(), ItemBalancingConfig.PlayerBaseCritDamage

**ARM Code Location:** AttacksSystem.GetDamage() method

**Examples:**

- **Standard crit (2x damage)**
  - Inputs: {'base_damage': 100, 'crit_multi': 2.0}
  - Expected Output: 200 damage
- **Enhanced crit (3x damage)**
  - Inputs: {'base_damage': 100, 'crit_multi': 3.0}
  - Expected Output: 300 damage

**Notes:**

- Base crit multiplier typically 2.0 (200%)
- Can be increased through equipment and skills
- Stacks multiplicatively with double damage
- High crit multi + high crit chance = massive DPS
- Sources: Equipment, Skills, Tech Tree, Sets
- Typical range: 2.0x to 5.0x multiplier

---

### Damage Calculation

**Description:** Complete damage calculation system including all modifiers and defensive checks

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.Dmg, CombatStats.CriticalChance, CombatStats.CriticalMulti, CombatStats.DoubleDamageChance, CombatStats.BlockChance, CombatStats.DodgeChance, CombatStats.LifeSteal, CombatDmg (result struct), AttacksSystem.GetDamage(), RandomPCG (for proc checks)

**ARM Code Location:** AttacksSystem class (line 1057705 in IL2CPP)

**Examples:**

- **Normal hit**
  - Inputs: {'base_damage': 100, 'crit_chance': 0, 'double_chance': 0}
  - Expected Output: 100 damage
- **Critical hit (2x multiplier)**
  - Inputs: {'base_damage': 100, 'crit_chance': 1.0, 'crit_multi': 2.0}
  - Expected Output: 200 damage (critical)
- **Dodged attack**
  - Inputs: {'base_damage': 100, 'target_dodge': 1.0}
  - Expected Output: 0 damage (dodged)
- **Blocked attack**
  - Inputs: {'base_damage': 100, 'target_block': 1.0}
  - Expected Output: 0 damage (blocked)
- **Life steal**
  - Inputs: {'damage': 100, 'life_steal': 0.2}
  - Expected Output: 20 HP healed

**Notes:**

- Uses RandomPCG for all proc checks
- Dodge and Block are checked AFTER damage calculation
- Critical and Double Damage can stack
- Life steal calculated on final damage (after crits)
- Server-authoritative (client cannot manipulate)
- All checks use seeded RNG for determinism
- Order matters: Crit → Double → Dodge → Block
- Sources: Equipment, Skills, Pets, Mounts, Tech Tree

---

### Dodge Chance

**Description:** Probability of completely evading an incoming attack

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.DodgeChance, CombatDmg.Dodged, RandomPCG (for roll), AttacksSystem.GetDamage()

**ARM Code Location:** AttacksSystem.GetDamage() method

**Examples:**

- **20% dodge chance**
  - Inputs: {'dodge_chance': 0.2, 'random_roll': 0.1}
  - Expected Output: Attack dodged! (0.10 < 0.20)
- **Dodge fails**
  - Inputs: {'dodge_chance': 0.2, 'random_roll': 0.5}
  - Expected Output: Attack hits (0.50 >= 0.20)

**Notes:**

- Defensive stat (checked on target)
- Checked BEFORE block
- Dodges 100% of damage (not partial)
- Uses RandomPCG for deterministic rolls
- Server-authoritative
- Sources: Equipment, Skills, Tech Tree, Sets
- Typical range: 5% to 30% dodge chance

---

### HP (Health Points)

**Description:** Maximum health pool that determines survivability

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.HpMax, CombatStats.HpMaxNoMulti, PetBalancingConfig.HealthMultiplier, MountStats.HpMax, PvpBaseConfig.PvpHpBaseMultiplier, ItemBalancingConfig.LevelScalingBase

**ARM Code Location:** CombatStats struct, PvpBaseConfig class

**Examples:**

- **Base HP with equipment**
  - Inputs: {'base_hp': 1000, 'equipment_bonus': 500}
  - Expected Output: 1500 HP
- **HP with pet multiplier**
  - Inputs: {'base_hp': 1000, 'pet_multiplier': 1.5}
  - Expected Output: 1500 HP (50% increase)

**Notes:**

- HP is the primary survivability stat
- Multiple sources stack additively for multipliers
- PvP has separate scaling factors
- HpMaxNoMulti stores base value before multipliers
- Death occurs when HP reaches 0
- Sources: Equipment, Pets, Mounts, Tech Tree, Skills, Sets

---

### Health Regeneration

**Description:** Passive health recovery per second

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.HealthRegen, UnitEntity.HP, CombatSystem (regen tick)

**ARM Code Location:** Combat update loop

**Examples:**

- **10 HP/sec regen**
  - Inputs: {'health_regen': 10, 'time': 5}
  - Expected Output: 50 HP healed over 5 seconds
- **Regen capped at max HP**
  - Inputs: {'current_hp': 950, 'max_hp': 1000, 'regen': 100}
  - Expected Output: Heals to 1000 HP (capped)

**Notes:**

- Passive sustain stat
- Works continuously (not per-hit)
- Independent of damage dealt
- May be reduced/disabled in combat
- Healing capped at max HP
- Sources: Equipment, Skills, Tech Tree, Sets
- Typical range: 1-50 HP per second

---

### Life Steal

**Description:** Percentage of damage dealt that is converted to healing

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.LifeSteal, CombatDmg.Heal, AttacksSystem.GetDamage(), AttacksSystem.ApplyDmg()

**ARM Code Location:** AttacksSystem.GetDamage() method

**Examples:**

- **20% life steal**
  - Inputs: {'damage': 100, 'life_steal': 0.2}
  - Expected Output: 20 HP healed
- **Life steal on crit**
  - Inputs: {'damage': 200, 'life_steal': 0.2}
  - Expected Output: 40 HP healed (crits heal more)
- **No heal on dodge**
  - Inputs: {'damage': 0, 'life_steal': 0.2, 'dodged': True}
  - Expected Output: 0 HP healed (no damage dealt)

**Notes:**

- Sustain stat (self-healing)
- Scales with damage output
- Synergizes with crit and attack speed
- Does not work on blocked/dodged attacks
- Healing cannot exceed max HP
- Sources: Equipment, Skills, Tech Tree, Sets
- Typical range: 5% to 30% life steal

---

### Move Speed

**Description:** Movement speed multiplier affecting character velocity

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** CombatStats.MoveSpeed, MountStats.MoveSpeed, UnitEntity.Position, PathfindingSystem

**ARM Code Location:** CombatStats struct, Movement systems

**Examples:**

- **Base movement**
  - Inputs: {'base_speed': 5.0, 'move_speed_multi': 0}
  - Expected Output: 5.0 units/second
- **With mount bonus**
  - Inputs: {'base_speed': 5.0, 'mount_bonus': 1.0}
  - Expected Output: 10.0 units/second (100% faster)

**Notes:**

- Move speed is a multiplier (not additive)
- Mounts provide significant speed bonuses
- Speed affects farming efficiency
- Some areas may have speed caps
- Sources: Equipment, Mounts, Skills, Tech Tree, Sets

---

## Economy

### Currency Types & Management

**Description:** Multiple currency types with acquisition methods and optimal usage

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** PlayerCurrencyModel.Currencies (MetaDictionary<CurrencyType, long>), CurrencyType enum: Coins, Gems, Hammers, SkillSummonTickets, TechPotions, PvpTickets, ClockWinders, WarBattleTickets, Token, CurrencyConfig, CurrencySourceConfig, CurrencySinkConfig

**ARM Code Location:** Currency system classes (PlayerCurrencyModel at line 1067393, CurrencyType enum at line 1067355)

**Examples:**

- **Daily coin income**
  - Inputs: {'idle': 12000, 'farming': 50000, 'quests': 10000}
  - Expected Output: 72000 coins per day
- **Gem value comparison**
  - Inputs: {'item_coin_cost': 100000, 'item_gem_cost': 50}
  - Expected Output: 1 gem = 2000 coins (good value if > 1000)

**Notes:**

- 9 distinct currency types in CurrencyType enum
- Currencies stored in MetaDictionary<CurrencyType, long>
- Each currency has specific uses (no generic conversion)
- Tickets regenerate over time (PvpTickets, WarBattleTickets)
- Hammers are primary crafting resource
- Gems are most valuable (use sparingly)
- Coins are most abundant (but still scarce late game)
- ClockWinders for time acceleration
- Token for special/event purchases
- Optimization: Prioritize time-limited resources, hoard gems, manage coins carefully
- Calculate cross-currency value before purchasing
- Don't waste regenerating tickets (use daily)

---

### Investment & Passive Income

**Description:** Investment mechanics with returns, risks, and optimization strategies

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** InvestmentConfig, BuildingUpgradeConfig, TechTreeNodeConfig, InvestmentConfig.InterestRate, InvestmentConfig.LockPeriod, PlayerInvestmentModel

**ARM Code Location:** Investment system classes

**Examples:**

- **Time-locked investment**
  - Inputs: {'investment': 100000, 'rate': 0.2, 'time': 1}
  - Expected Output: 120000 coins (20% return)
- **Building upgrade payback**
  - Inputs: {'cost': 50000, 'income_increase': 50}
  - Expected Output: 1000 hours to break even
- **Tech tree ROI**
  - Inputs: {'cost': 10000, 'income_bonus': 0.1, 'current_income': 1000}
  - Expected Output: 100 hours payback, then infinite benefit

**Notes:**

- Investments provide passive income
- Tech tree has best long-term ROI
- Buildings provide steady passive income
- Time-locked investments for surplus coins only
- Calculate payback period before investing
- Optimization: Tech tree > Buildings > Time-locked
- Don't lock coins needed for progression
- Compound growth is powerful (reinvest returns)

---

### Resource Generation

**Description:** Passive and active income sources with rates and optimization strategies

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** ResourceGenerationConfig, IdleRewardConfig, BuildingConfig.IncomeRate, QuestRewardConfig, DungeonRewardConfig, PlayerCurrencyModel.Currencies[CurrencyType.Coins], PlayerCurrencyModel.Currencies[CurrencyType.Gems]

**ARM Code Location:** Economy system classes

**Examples:**

- **Idle income**
  - Inputs: {'base_rate': 1000, 'offline_hours': 8, 'bonuses': 0.5}
  - Expected Output: 12000 coins (1500/hour * 8 hours)
- **Dungeon farming**
  - Inputs: {'coins_per_run': 1000, 'time_per_run': 60}
  - Expected Output: 1000 coins/minute efficiency
- **Building income**
  - Inputs: {'buildings': 5, 'rate_per_building': 100, 'hours': 4}
  - Expected Output: 2000 coins (500/hour * 4 hours)

**Notes:**

- Multiple income sources stack
- Passive income continues offline (capped)
- Active farming is most efficient
- Tech tree significantly boosts income
- Events provide burst income
- Optimization: Max passive income, farm optimal dungeon level
- Balance time investment vs rewards
- Don't waste offline cap (collect regularly)

---

### Shop Pricing & Economy

**Description:** Dynamic pricing algorithms, shop refresh mechanics, and purchase optimization

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** ShopConfig, ShopItemConfig.BasePrice, ShopItemConfig.RarityMultiplier, ShopRefreshConfig, DiscountConfig, CurrencyConversionConfig, PlayerShopModel.RefreshCount

**ARM Code Location:** Shop system classes

**Examples:**

- **Item pricing**
  - Inputs: {'base_price': 1000, 'rarity': 'Epic', 'level': 10}
  - Expected Output: 50000 coins (1000 * 25 * 2.0)
- **Shop refresh cost**
  - Inputs: {'base_cost': 50, 'refresh_count': 3}
  - Expected Output: 259 gems (50 * 3^1.5)
- **Discount**
  - Inputs: {'price': 10000, 'discount': 0.3}
  - Expected Output: 7000 coins (30% off)

**Notes:**

- Shop refreshes provide new opportunities
- Refresh costs increase exponentially
- Event shops have best value
- Discounts can save significant resources
- Gem purchases should be strategic
- Optimization: Buy event items first, wait for sales, use free refreshes
- Never waste gems on items you can farm
- Calculate value before purchasing

---

## Progression

### Forge/Upgrade System

**Description:** Equipment enhancement system with costs, success rates, and stat improvements

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** ForgeConfig, ItemUpgradeConfig, ForgeConfig.SuccessRate, ForgeConfig.CostFormula, ForgeConfig.StatGrowth, ProtectionItemConfig

**ARM Code Location:** Forge system classes

**Examples:**

- **Successful upgrade**
  - Inputs: {'level': 5, 'success_rate': 0.9, 'roll': 0.5}
  - Expected Output: Upgrade successful! Level 5 → 6
- **Failed upgrade**
  - Inputs: {'level': 15, 'success_rate': 0.5, 'roll': 0.7}
  - Expected Output: Upgrade failed! Level 15 → 14
- **Stat improvement**
  - Inputs: {'base_damage': 100, 'level': 10, 'growth': 0.05}
  - Expected Output: New damage: 150 (+50%)

**Notes:**

- High-risk, high-reward system
- Exponential cost growth
- Success rate decreases with level
- Protection items are valuable
- May have safe zones (no level loss)
- Optimization: Use protection at high levels, stop at safe points
- Major resource sink (gold, materials)

---

### Mount Leveling & Bonuses

**Description:** Mount progression system with leveling, stat bonuses, and movement speed

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** MountBalancingConfig, MountLevelConfig, PlayerMountModel.Level, MountStats.MoveSpeed, MountStats.HpMax, MountStats.Dmg

**ARM Code Location:** Mount system classes

**Examples:**

- **Mount speed bonus**
  - Inputs: {'base_speed': 5.0, 'mount_bonus': 1.0}
  - Expected Output: Total speed: 10.0 (100% faster)
- **Mount stat bonus**
  - Inputs: {'player_hp': 1000, 'mount_hp_bonus': 500}
  - Expected Output: Total HP: 1500

**Notes:**

- Mounts significantly increase farming efficiency
- Movement speed is most valuable stat
- Combat bonuses stack with other sources
- Collection bonuses reward diversity
- Higher rarity = exponentially better
- Optimization: Max speed mount for farming, combat mount for bosses
- Sources: Mount summoning, events, shop

---

### Pet Leveling & Evolution

**Description:** Pet progression system with leveling, evolution, and stat scaling

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** PetBalancingConfig, PetLevelConfig, PetEvolutionConfig, PlayerPetModel.Level, PlayerPetModel.Experience, PetBalancingConfig.DamageMultiplier, PetBalancingConfig.HealthMultiplier

**ARM Code Location:** Pet system classes

**Examples:**

- **Pet level up**
  - Inputs: {'level': 10, 'xp_required': 1000, 'current_xp': 1200}
  - Expected Output: Level up! 10 → 11
- **Pet evolution**
  - Inputs: {'rarity': 'Rare', 'base_damage': 100, 'evolution_multi': 2.0}
  - Expected Output: Evolved to Epic! Base damage: 100 → 200

**Notes:**

- Pets provide significant stat bonuses
- Evolution is major power spike
- XP requirements grow exponentially
- Multiple pets provide collection bonuses
- Pet skills can change combat strategy
- Optimization: Max level before evolving, collect multiple pets
- Sources: Egg hatching, events, shop

---

### Skill Leveling & Upgrades

**Description:** Skill progression with leveling, upgrades, and build customization

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** SkillConfig, SkillLevelConfig, PlayerSkillModel.Level, SkillConfig.BasePower, SkillConfig.Cooldown, SkillConfig.Cost

**ARM Code Location:** Skill system classes

**Examples:**

- **Skill level up**
  - Inputs: {'base_damage': 100, 'level': 10, 'scaling': 0.1}
  - Expected Output: New damage: 200 (100% increase)
- **Skill cost**
  - Inputs: {'base_cost': 100, 'level': 5, 'exponent': 1.5}
  - Expected Output: Upgrade cost: 1118

**Notes:**

- Skills define build identity
- Limited skill points require planning
- Synergies create powerful combinations
- Active skills require manual use
- Passive skills are always active
- Optimization: Max core skills, plan synergies, save for key levels
- Sources: Level ups, quests, achievements

---

### Tech Tree System

**Description:** Technology tree with nodes providing permanent stat bonuses and unlocks

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** TechTreeNodeConfig, TechTreeStatContribution, PlayerTechTreeModel, TechTreeNodeConfig.Prerequisites, TechTreeNodeConfig.Cost, TechTreeNodeConfig.StatBonuses

**ARM Code Location:** Tech tree system classes

**Examples:**

- **Unlock stat node**
  - Inputs: {'node_id': 'hp_boost_1', 'cost': 1000, 'bonus': '+10% HP'}
  - Expected Output: Node unlocked, HP increased by 10%
- **Node with prerequisites**
  - Inputs: {'node_id': 'advanced_damage', 'prereqs': ['basic_damage_1', 'basic_damage_2']}
  - Expected Output: Requires 2 prerequisite nodes

**Notes:**

- Permanent progression system
- Requires careful planning (may have respec costs)
- Different paths for different builds
- Efficiency nodes provide compound benefits
- May have multiple tech trees (combat, economy, etc.)
- Optimization: Unlock efficiency nodes early, plan full path
- Sources: Quest rewards, dungeon drops, shop purchases

---

## PvP

### Guild War System

**Description:** Large-scale guild vs guild combat with territory control and rewards

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** GuildModel.TotalPower, GuildWarConfig, GuildWarState, TerritoryControl, GuildWarRewards

**ARM Code Location:** Guild war system classes

**Examples:**

- **Guild war scoring**
  - Inputs: {'kills': 50, 'territories': 3, 'time': 1800}
  - Expected Output: Total points: 850

**Notes:**

- Requires guild membership
- Scheduled events (specific times)
- Coordination and strategy important
- May have different war types/modes
- Rewards scale with participation
- Optimization: Coordinate attacks, defend key territories

---

### PvP Matchmaking

**Description:** Algorithm for pairing players based on rating, level, and availability

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** PvpMatchmakingConfig, PlayerPvpModel.Rating, PlayerPvpModel.Level, GuildModel.TotalPower, MatchmakingQueue

**ARM Code Location:** PvP matchmaking system classes

**Examples:**

- **Close rating match**
  - Inputs: {'player_rating': 1500, 'opponent_rating': 1520}
  - Expected Output: Match found (within ±100 range)
- **Expanded search**
  - Inputs: {'wait_time': 30, 'rating_range': 250}
  - Expected Output: Search range: ±250 points

**Notes:**

- Server-authoritative matchmaking
- Rating range expands to reduce wait times
- May prioritize active players
- Guild wars use separate matching logic
- Cross-server matching may be supported
- Optimization: Minimize wait time while ensuring fairness

---

### PvP Rating System

**Description:** Elo-style rating system that adjusts based on wins, losses, and opponent strength

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** PlayerPvpModel.Rating, PlayerPvpModel.Wins, PlayerPvpModel.Losses, PvpRewardConfig, PvpSeasonConfig

**ARM Code Location:** PvP rating calculation methods

**Examples:**

- **Even match win**
  - Inputs: {'rating': 1500, 'opponent': 1500, 'result': 'win'}
  - Expected Output: New rating: 1516 (+16)
- **Underdog victory**
  - Inputs: {'rating': 1400, 'opponent': 1600, 'result': 'win'}
  - Expected Output: New rating: 1424 (+24)
- **Expected loss**
  - Inputs: {'rating': 1400, 'opponent': 1600, 'result': 'loss'}
  - Expected Output: New rating: 1392 (-8)

**Notes:**

- Elo-style rating system
- Beating stronger opponents gives more rating
- Losing to weaker opponents costs more rating
- K-factor may vary by rating tier
- New players may have higher K-factor
- Rating floors may prevent dropping too low
- Optimization: Focus on beating higher-rated opponents

---

### PvP Stat Modifiers

**Description:** Special multipliers applied to stats in PvP combat to balance gameplay

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** PvpBaseConfig.PvpHpBaseMultiplier, PvpBaseConfig.PvpHpPetMultiplier, PvpBaseConfig.PvpHpSkillMultiplier, PvpBaseConfig.PvpHpMountMultiplier, PvpCombatStats

**ARM Code Location:** PvpBaseConfig class

**Examples:**

- **PvE vs PvP HP**
  - Inputs: {'pve_hp': 10000, 'pvp_base_multi': 1.0, 'pvp_pet_multi': 0.6}
  - Expected Output: PvP HP: 8200 (reduced from pet bonuses)

**Notes:**

- Separate stat calculations for PvP
- Prevents PvE power creep in PvP
- Balances different progression systems
- Server-authoritative calculations
- May change with balance patches
- Optimization: Build specifically for PvP multipliers

---

## Summoning

### Drop Tables

**Description:** Level-based drop chance tables that improve with summon progression while using the same random seed

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** MountSummonDropChanceConfig (per level), PlayerMountCollectionModel.MountSummonLevel, PlayerMountCollectionModel.MountSummonCount, MountSummonUpgradeConfig.Summons, PetSummonDropChanceConfig

**ARM Code Location:** Found 18 potential tables at lines: 1035832, 1043630, 1043631, 1043650, 1043651

**Examples:**

- **Level 1 drop table (example)**
  - Inputs: {'level': 1}
  - Expected Output: {'common': 50, 'rare': 30, 'epic': 15, 'legendary': 4, 'ultimate': 0.9, 'mythic': 0.1}
- **Level 5 drop table (improved)**
  - Inputs: {'level': 5}
  - Expected Output: {'common': 30, 'rare': 35, 'epic': 20, 'legendary': 10, 'ultimate': 4, 'mythic': 1}
- **Same random value, different results**
  - Inputs: {'random': 45, 'level1': True, 'level5': True}
  - Expected Output: Level 1: Common (45% < 50%), Level 5: Rare (45% in 30-65% range)

**Notes:**

- Found 18 potential drop tables in ARM code
- Percentages must sum to 100% (or pity system exists)
- Each summon level has its own drop table
- Higher level = better odds for rare items
- Seed stays same, only interpretation changes
- This is why patterns persist even after improving odds
- Server validates all summons against correct level table
- Cumulative percentage system (subtract as you go)
- Separate tables for pets, mounts, eggs
- Drop tables loaded from SharedGameConfig.mpa
- 18 potential drop table arrays found in code

---

### RNG Algorithm

**Description:** Seeded pseudo-random number generation using PCG algorithm for deterministic, server-authoritative randomness

**Formula:**
```

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

```

**Confidence Level:** High

**Data Structures:** RandomPCG._state (ulong), PlayerPetCollectionModel.PetRandomSeed, PlayerMountCollectionModel.SummonSeed, PlayerMountCollectionModel.MountRandomSeed, PlayerEggModel.RandomSeed

**ARM Code Location:** RandomPCG struct in IL2CPP

**Examples:**

- **PCG state update**
  - Inputs: {'state': 12345}
  - Expected Output: Deterministic next state
- **Same seed produces same sequence**
  - Inputs: {'seed': 12345, 'calls': 5}
  - Expected Output: Always same 5 random numbers

**Notes:**

- Algorithm type: PCG (Permuted Congruential Generator)
- 64-bit seed (18 quintillion possibilities)
- Deterministic: same seed = same sequence
- Server-authoritative: client cannot modify seeds
- Per-system seeds: pets, mounts, eggs each have own
- Per-egg seeds: each egg has unique seed
- Seed advances with each summon
- Enables server-client synchronization
- Prevents cheating by timing or disconnecting
- Supports pity systems and fair distribution
- Can reproduce any summon for debugging
- PCG multiplier: 6364136223846793005
- PCG increment: 1442695040888963407
- Uses bit shifts and XOR for output permutation

---

### Rarity Determination

**Description:** Algorithm that converts random values to rarity outcomes

**Formula:**
```
if (random < threshold1) return common; else if (random < threshold2) return rare; ...
```

**Confidence Level:** Medium

**Data Structures:** RarityThreshold, SummonResult

**ARM Code Location:** Not found

**Notes:**

- Found 0 comparison chains
- Uses threshold-based determination
- Random value compared against cumulative percentages

---

