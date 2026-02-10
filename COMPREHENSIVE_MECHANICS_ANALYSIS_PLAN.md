# Comprehensive Game Mechanics Analysis Plan

## Challenge

The Ghidra export (`libil2cpp.so.c`, 27 MB, 954,614 lines) contains decompiled ARM code with:
- ❌ No meaningful function names (all are `FUN_<address>`)
- ❌ No meaningful variable names (all are `param_1`, `iVar2`, etc.)
- ❌ No comments or documentation
- ✅ Complete implementation logic
- ✅ All constants and calculations

## Strategy

We need to **cross-reference** the IL2CPP dump (which has structure but no implementation) with the Ghidra export (which has implementation but no structure).

### Phase 1: Map Known Addresses

From `dump.cs`, we have function addresses. We can find these in Ghidra output:

**Known Addresses from IL2CPP Dump:**
```
AttacksSystem.HandleUnits: 0x5AF7094
AttacksSystem.Execute: 0x5AEE300
AttacksSystem.ExecuteAttack: 0x5AF96F4
```

**Search Pattern:**
```c
void FUN_05af7094(...)  // This is AttacksSystem.HandleUnits
void FUN_05aee300(...)  // This is AttacksSystem.Execute
void FUN_05af96f4(...)  // This is AttacksSystem.ExecuteAttack
```

### Phase 2: Identify Key Mechanics by Pattern

Even without names, we can identify mechanics by:

1. **Floating-point operations** → Damage/stat calculations
2. **Modulo operations** → RNG, drop tables
3. **Array lookups** → Config tables
4. **Bit shifts** → PCG algorithm
5. **Comparison chains** → Rarity determination

### Phase 3: Extract Mechanics Systematically

For each mechanic, we need:
1. **Find the function** (using addresses or patterns)
2. **Understand the algorithm** (read decompiled C)
3. **Extract constants** (actual values used)
4. **Document the formula** (mathematical representation)
5. **Verify against IL2CPP** (cross-check structure)

---

## Mechanics to Document

### 1. Combat System

#### 1.1 Attack Speed
**Goal**: Find exact formula for attack speed calculation

**What to Find:**
- Base attack times for each weapon
- How `AttackSpeedMulti` is applied
- Windup vs attack duration calculation

**Search Strategy:**
- Find `AttacksSystem.HandleUnits` at address 0x5AF7094
- Look for division operations (attack speed is divisive)
- Find floating-point constants (base times)

**Expected Formula:**
```c
effective_time = base_time / attack_speed_multi
```

#### 1.2 Damage Calculation
**Goal**: Exact damage formula with all modifiers

**What to Find:**
- Base damage calculation
- Crit chance and multiplier application
- Double damage proc
- Dodge/block checks
- Life steal calculation

**Search Strategy:**
- Find `AttacksSystem.GetDamage` function
- Look for RNG calls (for procs)
- Find percentage comparisons (for chances)

**Expected Formula:**
```c
damage = base_damage
if (random() < crit_chance) damage *= crit_multi
if (random() < double_damage_chance) damage *= 2
if (random() < dodge_chance) damage = 0
if (random() < block_chance) damage = 0
heal = damage * life_steal
```

#### 1.3 All Combat Stats
**Goal**: Document how EVERY stat is calculated

**Stats to Cover:**
- HP Max
- Damage
- Move Speed
- Critical Chance
- Critical Multiplier
- Double Damage Chance
- Attack Speed Multi
- Block Chance
- Dodge Chance
- Health Regen
- Life Steal

**For Each Stat:**
- Base value
- Scaling formula
- Sources (equipment, pets, skills, etc.)
- Caps/limits

### 2. Summoning System

#### 2.1 Random Number Generation
**Goal**: Confirm PCG algorithm and seed management

**What to Find:**
- PCG constants (6364136223846793005, 1442695040888963407)
- Seed initialization
- Seed advancement
- State management

**Search Strategy:**
- Look for 64-bit multiplication
- Look for specific constants in hex
- Find functions that manipulate 64-bit state

**Expected Algorithm:**
```c
uint32_t RandomPCG_Next(uint64_t *state) {
    uint64_t oldState = *state;
    *state = oldState * 6364136223846793005ULL + 1442695040888963407ULL;
    uint32_t xorshifted = (uint32_t)(((oldState >> 18) ^ oldState) >> 27);
    int rot = (int)(oldState >> 59);
    return (xorshifted >> rot) | (xorshifted << ((-rot) & 31));
}
```

#### 2.2 Drop Chance Tables
**Goal**: Extract EXACT drop percentages for all levels

**What to Find:**
- Drop chance arrays/structs
- Level-based table selection
- Rarity determination algorithm

**Search Strategy:**
- Look for arrays of 6-7 floats (Common, Rare, Epic, Legendary, Ultimate, Mythic)
- Find functions that index into these arrays
- Extract the actual percentage values

**Expected Data:**
```c
struct DropChanceConfig {
    int level;
    float common;     // Actual value: ???
    float rare;       // Actual value: ???
    float epic;       // Actual value: ???
    float legendary;  // Actual value: ???
    float ultimate;   // Actual value: ???
    float mythic;     // Actual value: ???
};
```

#### 2.3 Summon Level Progression
**Goal**: Find thresholds for leveling up summon level

**What to Find:**
- Summon count tracking
- Level-up thresholds
- Progression table

**Expected Data:**
```c
struct SummonLevelThreshold {
    int level;
    int summons_required;
};
```

### 3. Progression Systems

#### 3.1 Tech Tree
**Goal**: Upgrade costs and stat bonuses

**What to Find:**
- Cost formulas per level
- Stat increases per level
- Unlock requirements

#### 3.2 Forge System
**Goal**: Crafting mechanics and costs

**What to Find:**
- Forge cost formula
- Item level scaling
- Secondary stat generation
- Auto-forge logic

#### 3.3 Pet/Mount Leveling
**Goal**: Experience and stat scaling

**What to Find:**
- XP requirements per level
- Stat growth formulas
- Merge mechanics

#### 3.4 Skill System
**Goal**: Skill damage and scaling

**What to Find:**
- Base damage per skill
- Level scaling
- Cooldown calculations

### 4. PvP System

#### 4.1 Arena Matchmaking
**Goal**: How opponents are selected

**What to Find:**
- Power calculation
- Matchmaking algorithm
- Rank progression

#### 4.2 Guild War
**Goal**: War mechanics and scoring

**What to Find:**
- Matchup determination
- Point calculation
- Tier progression

#### 4.3 PvP Stat Multipliers
**Goal**: How stats are modified in PvP

**What to Find:**
- HP multipliers
- Damage multipliers
- Skill multipliers

### 5. Economy

#### 5.1 Resource Generation
**Goal**: Idle income and resource rates

**What to Find:**
- Coins per second formula
- Hammers per minute formula
- Offline cap calculation

#### 5.2 Shop Pricing
**Goal**: How prices are determined

**What to Find:**
- Base prices
- Scaling formulas
- Daily deal generation

### 6. Hidden Mechanics

#### 6.1 Pity Systems
**Goal**: Guaranteed drops after X summons

**What to Find:**
- Pity counters
- Guaranteed rarity thresholds
- Reset conditions

#### 6.2 Luck Manipulation
**Goal**: Ways to improve RNG outcomes

**What to Find:**
- Seed influence factors
- Time-based patterns
- Exploit opportunities

---

## Extraction Methodology

### Step 1: Create Address Map

Build a mapping file:
```
IL2CPP Address → Ghidra Function → Purpose
0x5AF7094 → FUN_05af7094 → AttacksSystem.HandleUnits
0x5AEE300 → FUN_05aee300 → AttacksSystem.Execute
...
```

### Step 2: Extract Functions

For each key function:
1. Find in Ghidra export
2. Copy decompiled C code
3. Annotate with IL2CPP structure info
4. Identify constants and formulas

### Step 3: Document Formulas

Create formula sheets:
```
Mechanic: Attack Speed
Formula: effective_time = base_time / attack_speed_multi
Constants:
  - Dagger base time: 1.0s
  - Sword base time: 1.5s
  - Hammer base time: 2.0s
Evidence: FUN_05af7094, lines 123-145
```

### Step 4: Create Optimization Guide

For each mechanic, document:
- How it works
- What affects it
- How to optimize it
- Best strategies

---

## Deliverables

### 1. Complete Mechanics Manual
**File**: `COMPLETE_GAME_MECHANICS_MANUAL.md`

**Contents:**
- Every mechanic explained
- Every formula documented
- Every constant extracted
- Cross-referenced with code

### 2. Optimization Guide
**File**: `OPTIMIZATION_STRATEGIES.md`

**Contents:**
- Best ways to manipulate loot tables
- Optimal progression paths
- Resource efficiency strategies
- PvP optimization

### 3. Formula Reference
**File**: `FORMULA_REFERENCE.md`

**Contents:**
- Quick reference for all formulas
- Calculator-ready equations
- Constant tables

### 4. Code Evidence
**File**: `CODE_EVIDENCE.md`

**Contents:**
- Extracted C code for each mechanic
- Annotated with explanations
- Cross-referenced with IL2CPP dump

---

## Timeline

Given the scope, this is a multi-hour project:

**Phase 1** (1-2 hours): Address mapping and key function extraction
**Phase 2** (2-3 hours): Combat system analysis
**Phase 3** (2-3 hours): Summoning system analysis
**Phase 4** (2-3 hours): Progression systems analysis
**Phase 5** (1-2 hours): PvP and economy analysis
**Phase 6** (1-2 hours): Documentation and optimization guide

**Total**: 9-15 hours of detailed analysis

---

## Next Steps

1. **Create address mapping tool** - Script to find functions by address
2. **Extract key functions** - Pull out combat and summon functions
3. **Begin systematic analysis** - Work through each mechanic
4. **Document as we go** - Build the manual incrementally

---

## Current Status

✅ Ghidra export complete (27 MB, 954K lines)
✅ IL2CPP dump available (60 MB, 1.2M lines)
✅ Analysis plan created
⏳ Ready to begin extraction

**Recommendation**: Start with combat system (attack speed and damage) as these are most critical and we have good address references.

