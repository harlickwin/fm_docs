# Egg Summoning Mechanics - Confidence Analysis

## What I'm 100% Sure Of (Direct Evidence from IL2CPP Dump)

### ✅ Data Structures Exist (100% Confirmed)

**Evidence**: Direct class definitions in dump.cs

```csharp
// Line 1070882 - PlayerMountCollectionModel
public class PlayerMountCollectionModel {
    [MetaMember(3, 0)]
    public ulong SummonSeed { get; set; }           // ✅ EXISTS
    
    [MetaMember(4, 0)]
    public ulong MountRandomSeed { get; set; }      // ✅ EXISTS
    
    [MetaMember(5, 0)]
    public int MountSummonLevel { get; set; }       // ✅ EXISTS
    
    [MetaMember(6, 0)]
    public int MountSummonCount { get; set; }       // ✅ EXISTS
}

// Line 1070629 - MountSummonDropChanceConfig
public class MountSummonDropChanceConfig {
    [MetaMember(1, 0)]
    public int Level { get; set; }                  // ✅ EXISTS
    
    [MetaMember(2, 0)]
    public F64 Common { get; set; }                 // ✅ EXISTS
    
    [MetaMember(3, 0)]
    public F64 Rare { get; set; }                   // ✅ EXISTS
    
    [MetaMember(4, 0)]
    public F64 Epic { get; set; }                   // ✅ EXISTS
    
    [MetaMember(5, 0)]
    public F64 Legendary { get; set; }              // ✅ EXISTS
    
    [MetaMember(6, 0)]
    public F64 Ultimate { get; set; }               // ✅ EXISTS
    
    [MetaMember(7, 0)]
    public F64 Mythic { get; set; }                 // ✅ EXISTS
}

// Similar for PlayerPetCollectionModel
public class PlayerPetCollectionModel {
    [MetaMember(4, 0)]
    public ulong PetRandomSeed { get; set; }        // ✅ EXISTS
}

// Each egg has its own seed
public class PlayerEggModel {
    [MetaMember(2, 0)]
    public ulong RandomSeed { get; set; }           // ✅ EXISTS
}
```

**Confidence**: 100% - These classes are in the decompiled code

### ✅ RandomPCG Algorithm Exists (100% Confirmed)

**Evidence**: Class definition in dump.cs

```csharp
public struct RandomPCG {
    [MetaMember(1, 0)]
    private ulong _state;  // ✅ EXISTS - 64-bit seed state
    
    public uint Next() { }  // ✅ METHOD EXISTS
}
```

**Confidence**: 100% - The PRNG class exists and uses 64-bit state

### ✅ Metaplay Framework is Server-Authoritative (100% Confirmed)

**Evidence**: 
- All player model classes inherit from `PlayerModelBase`
- All actions inherit from `PlayerAction` 
- `[MetaMember]` attributes indicate server-serialized data
- Action-based architecture throughout codebase

**Confidence**: 100% - This is standard Metaplay framework design

---

## What I'm 95% Sure Of (Strong Inference from Structure)

### 🟢 Seeded RNG is Used for Summoning (95% Confident)

**Evidence**:
- Seeds exist in player models
- RandomPCG class exists
- Drop chance configs exist with level-based tables
- Standard game design pattern

**What's Missing**: The actual method that calls `RandomPCG.Next()` and uses the drop chance config

**To Confirm**: Find in ARM code:
```c
// Look for function that:
1. Loads player.MountRandomSeed
2. Initializes RandomPCG with that seed
3. Calls RandomPCG.Next()
4. Uses result with MountSummonDropChanceConfig
```

### 🟢 Summon Level Affects Drop Chances (95% Confident)

**Evidence**:
- `MountSummonDropChanceConfig` has a `Level` field
- `PlayerMountCollectionModel` has `MountSummonLevel` field
- Multiple drop chance configs exist (implied by config structure)
- Standard progression system design

**What's Missing**: The code that selects which drop chance config based on summon level

**To Confirm**: Find in ARM code:
```c
// Look for function like:
MountSummonDropChanceConfig* GetDropChanceForLevel(int summonLevel) {
    // Returns different config based on level
}
```

### 🟢 Seed Advances After Each Summon (95% Confident)

**Evidence**:
- RandomPCG has internal `_state` that changes
- Standard PRNG behavior
- Prevents getting same result repeatedly

**What's Missing**: The code that saves the new seed state back to player model

**To Confirm**: Find in ARM code:
```c
// Look for:
player->MountRandomSeed = rng.GetState();  // or similar
```

---

## What I'm 70% Sure Of (Reasonable Inference)

### 🟡 The Exact Algorithm for Rarity Determination (70% Confident)

**My Assumption**:
```csharp
PetRarity DeterminePetRarity(uint randomValue, MountSummonDropChanceConfig dropChance) {
    float roll = (randomValue / (float)uint.MaxValue) * 100.0f;
    
    if (roll < dropChance.Common) return PetRarity.Common;
    roll -= dropChance.Common;
    
    if (roll < dropChance.Rare) return PetRarity.Rare;
    roll -= dropChance.Rare;
    
    // ... etc
}
```

**Why 70%**: This is the standard algorithm, but could be:
- Weighted random selection
- Cumulative probability
- Inverse CDF sampling
- Something else entirely

**To Confirm**: Find in ARM code:
```c
// Look for:
1. Division by 0xFFFFFFFF (uint.MaxValue)
2. Multiplication by 100.0
3. Series of comparisons with drop chance values
4. Subtraction pattern (roll -= value)
```

### 🟡 MountSummonUpgradeConfig Controls Level Progression (70% Confident)

**My Assumption**:
```csharp
public class MountSummonUpgradeConfig {
    public int Level { get; set; }
    public int Summons { get; set; }  // Summons needed to reach this level
}
```

**Why 70%**: I found the class name in serialization code, but didn't see the full definition

**To Confirm**: 
1. Search dump.cs for full `MountSummonUpgradeConfig` class definition
2. Find in ARM code where `MountSummonCount` is compared to upgrade thresholds

---

## What I'm 50% Sure Of (Educated Guess)

### 🟠 The Exact Drop Chance Values (50% Confident)

**My Examples**:
```
Level 1: Common 50%, Rare 30%, Epic 15%, Legendary 4%, Ultimate 0.9%, Mythic 0.1%
Level 5: Common 30%, Rare 35%, Epic 20%, Legendary 10%, Ultimate 4%, Mythic 1%
```

**Why 50%**: These are typical game balance values, but actual values are in:
- `SharedGameConfig.mpa` (binary config file)
- Or hardcoded in ARM code

**To Confirm**: 
1. Parse `SharedGameConfig.mpa` file
2. Find floating-point constants in ARM code near summon logic

### 🟠 The Exact Summon Level Thresholds (50% Confident)

**My Examples**:
```
Level 1: 0-9 summons
Level 2: 10-24 summons
Level 3: 25-49 summons
```

**Why 50%**: Pure speculation based on typical game progression

**To Confirm**: Parse config file or find in ARM code

---

## What to Extract from ARM Code to Be 100% Sure

### Priority 1: Core Summon Logic

**Function to Find**: `MountSummon` or `PetSummon` or similar

**What to Look For**:
```c
void ExecuteMountSummon(PlayerModel* player) {
    // 1. Load seed
    uint64_t seed = player->MountRandomSeed;  // ✅ CONFIRMS seed is used
    
    // 2. Initialize RNG
    RandomPCG rng;
    RandomPCG_Init(&rng, seed);  // ✅ CONFIRMS seeded RNG
    
    // 3. Get drop chance config
    int level = player->MountSummonLevel;  // ✅ CONFIRMS level is used
    MountSummonDropChanceConfig* dropChance = GetDropChanceForLevel(level);  // ✅ CONFIRMS level affects drops
    
    // 4. Generate random value
    uint32_t randomValue = RandomPCG_Next(&rng);  // ✅ CONFIRMS RNG call
    
    // 5. Determine rarity
    float roll = (float)randomValue / 4294967295.0f * 100.0f;  // ✅ CONFIRMS algorithm
    
    MountRarity rarity;
    if (roll < dropChance->Common) {
        rarity = MOUNT_RARITY_COMMON;
    } else if (roll < dropChance->Common + dropChance->Rare) {
        rarity = MOUNT_RARITY_RARE;
    }
    // ... etc
    
    // 6. Update seed
    player->MountRandomSeed = rng._state;  // ✅ CONFIRMS seed advancement
    
    // 7. Increment counters
    player->MountSummonCount++;  // ✅ CONFIRMS counter tracking
    
    // 8. Check for level up
    if (ShouldLevelUp(player->MountSummonCount, player->MountSummonLevel)) {
        player->MountSummonLevel++;  // ✅ CONFIRMS level progression
    }
}
```

### Priority 2: Drop Chance Config Loading

**Function to Find**: `GetDropChanceForLevel` or config initialization

**What to Look For**:
```c
MountSummonDropChanceConfig* GetDropChanceForLevel(int level) {
    // Option 1: Array lookup
    return &dropChanceConfigs[level];
    
    // Option 2: Dictionary/map lookup
    return configMap.Get(level);
    
    // Option 3: Hardcoded switch
    switch(level) {
        case 1: return &level1Config;
        case 2: return &level2Config;
        // ...
    }
}
```

**This will show**:
- How many levels exist
- Whether configs are loaded from file or hardcoded

### Priority 3: Actual Drop Chance Values

**What to Look For**:
```c
// Option 1: Hardcoded constants
MountSummonDropChanceConfig level1Config = {
    .Level = 1,
    .Common = 50.0f,      // ✅ ACTUAL VALUE
    .Rare = 30.0f,        // ✅ ACTUAL VALUE
    .Epic = 15.0f,        // ✅ ACTUAL VALUE
    .Legendary = 4.0f,    // ✅ ACTUAL VALUE
    .Ultimate = 0.9f,     // ✅ ACTUAL VALUE
    .Mythic = 0.1f        // ✅ ACTUAL VALUE
};

// Option 2: Loaded from config file
// Look for floating-point constants in .rodata section
```

### Priority 4: RandomPCG Implementation

**What to Look For**:
```c
uint32_t RandomPCG_Next(RandomPCG* rng) {
    uint64_t oldState = rng->_state;
    
    // PCG algorithm constants
    rng->_state = oldState * 6364136223846793005ULL + 1442695040888963407ULL;  // ✅ CONFIRMS PCG
    
    uint32_t xorshifted = (uint32_t)(((oldState >> 18) ^ oldState) >> 27);
    int rot = (int)(oldState >> 59);
    
    return (xorshifted >> rot) | (xorshifted << ((-rot) & 31));
}
```

**This confirms**: The exact PRNG algorithm used

---

## How to Find These in Ghidra

### Step 1: Find String References

Search for strings like:
- "MountSummon"
- "PetSummon"
- "RandomSeed"
- "DropChance"

### Step 2: Find Known Function Addresses

From IL2CPP dump, we know some addresses (though they might be relative):
- Look for functions with names containing "Summon"
- Look for functions that reference the data structures

### Step 3: Look for Floating-Point Constants

Search for:
- `50.0` (likely Common drop chance)
- `100.0` (likely for percentage conversion)
- `4294967295.0` or `0xFFFFFFFF` (uint.MaxValue)

### Step 4: Follow Data Flow

1. Find where `player->MountRandomSeed` is loaded
2. Follow that value to see where it's used
3. Find the function that uses it with RandomPCG
4. Find where the result is used with drop chance configs

---

## Summary Table

| Claim | Confidence | Evidence Type | To Confirm 100% |
|-------|-----------|---------------|-----------------|
| Seeds exist in player data | 100% | IL2CPP dump | ✅ Already confirmed |
| RandomPCG class exists | 100% | IL2CPP dump | ✅ Already confirmed |
| Drop chance configs exist | 100% | IL2CPP dump | ✅ Already confirmed |
| Summon level field exists | 100% | IL2CPP dump | ✅ Already confirmed |
| Server-authoritative | 100% | Metaplay framework | ✅ Already confirmed |
| Seeded RNG is used | 95% | Strong inference | Find summon function in ARM |
| Level affects drop chances | 95% | Strong inference | Find config selection in ARM |
| Seed advances after summon | 95% | Standard PRNG | Find seed update in ARM |
| Rarity determination algorithm | 70% | Common pattern | Find comparison logic in ARM |
| Level progression system | 70% | Config class name | Find level-up logic in ARM |
| Actual drop chance values | 50% | Typical values | Parse config file or find constants |
| Summon level thresholds | 50% | Speculation | Parse config file or find constants |

---

## Bottom Line

**What I'm certain of**: The data structures and framework architecture  
**What I'm very confident of**: The general mechanics (seeded RNG, level-based drops)  
**What I need ARM code for**: The exact algorithms, values, and implementation details

The ARM code will transform my 95% confidence into 100% certainty and reveal the actual numbers used in the game.
