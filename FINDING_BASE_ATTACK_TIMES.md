# Finding Base Attack Times

## Question
Can we see the base attack speed time values (WindupTime, AttackDuration) from the code?

## Answer
**Not directly from the IL2CPP dump**, but **YES from Ghidra analysis**!

## Why Not in IL2CPP Dump?

The IL2CPP dump (`dump.cs`) shows us:
- **Class structures** ✅
- **Method signatures** ✅  
- **Field names and types** ✅
- **Method bodies** ❌ (empty stubs)
- **Config values** ❌ (loaded at runtime)

### Where Are the Values?

1. **Game Configuration**: `SharedGameConfig.mpa` (binary format)
   - Location: `C:\apktool\main-apk-out\assets\SharedGameConfig.mpa`
   - Size: 69,988 bytes
   - Format: MCA! (Metaplay Config Archive) - compressed/serialized
   - Contains: All weapon stats, timing values, damage multipliers, etc.

2. **Native Code**: `libil2cpp.so` (ARM binary)
   - Location: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
   - Size: 119 MB
   - Contains: The actual calculation code that loads and uses these values

## How to Get the Values

### Method 1: Ghidra Analysis (BEST)

When you analyze `libil2cpp.so` in Ghidra, you'll see:

1. **Config Loading Code**:
```c
// Ghidra will decompile to something like:
WeaponInfo* loadWeaponConfig(int weaponId) {
    WeaponInfo* weapon = allocate(sizeof(WeaponInfo));
    weapon->WindupTime = 0.5f;      // ← ACTUAL VALUE!
    weapon->AttackDuration = 1.0f;  // ← ACTUAL VALUE!
    weapon->AttackRange = 2.5f;
    return weapon;
}
```

2. **Hardcoded Constants**:
```assembly
; ARM assembly with literal values
VMOV.F32  s0, #0.5    ; WindupTime = 0.5 seconds
VMOV.F32  s1, #1.0    ; AttackDuration = 1.0 seconds
```

3. **Data Section**:
Ghidra will show constant pools with floating-point values:
```
.rodata:
  0x12345678: 0x3F000000  ; 0.5f (WindupTime)
  0x1234567C: 0x3F800000  ; 1.0f (AttackDuration)
```

### Method 2: Runtime Memory Inspection

Use a debugger or memory inspector on a running game:
- Attach to game process
- Find WeaponInfo instances in memory
- Read the float values at offsets 0xC (WindupTime) and 0x10 (AttackTime)

### Method 3: Config File Parser

Write a parser for the `.mpa` format:
- Reverse engineer the MCA! format
- Decompress/deserialize the data
- Extract weapon configurations

## What We Know From Code Structure

### WeaponData Class (Line 713706)
```csharp
public class WeaponData {
    public float AttackRange;    // 0x8
    public float WindUpTime;     // 0xC  ← Base windup time
    public float AttackTime;     // 0x10 ← Base attack duration
    public bool IsRanged;        // 0x14
    // ...
}
```

### WeaponInfo Class (Line 1050834)
```csharp
public class WeaponInfo : IGameConfigData<ItemId> {
    [MetaMember(4, 0)]
    public F64 WindupTime { get; set; }      // Base windup
    
    [MetaMember(5, 0)]
    public F64 AttackDuration { get; set; }  // Base duration
    
    [MetaMember(3, 0)]
    public F64 AttackRange { get; set; }
}
```

## Expected Values (Educated Guess)

Based on typical game design and the calculator data:

| Weapon Type | WindupTime | AttackDuration | Total Time |
|-------------|------------|----------------|------------|
| Fast (Dagger) | 0.3s | 0.7s | 1.0s |
| Normal (Sword) | 0.5s | 1.0s | 1.5s |
| Slow (Hammer) | 0.7s | 1.3s | 2.0s |

**Note**: These are estimates! The actual values will be visible in Ghidra.

## Why Ghidra Will Show Them

When you analyze `libil2cpp.so` in Ghidra and navigate to the combat functions:

1. **Config Initialization**: Functions that load weapon data will have the values
2. **Default Values**: Constructors may set default timing values
3. **Constant References**: Code that uses these values will reference them
4. **Data Sections**: Floating-point constants are stored in `.rodata` section

### Example of What You'll See

```c
// Decompiled by Ghidra
void AttacksSystem_HandleUnits(AttacksSystem* this, Entities* entities, F64 dt) {
    for (int i = 0; i < entities->unitCount; i++) {
        UnitEntity* unit = &entities->units[i];
        
        // Update attack timer
        unit->AttackTimer = unit->AttackTimer - dt;
        
        if (unit->AttackTimer <= 0.0) {
            // Execute attack
            ExecuteAttack(entities, unit);
            
            // Reset timer with attack speed applied
            WeaponInfo* weapon = GetWeaponInfo(unit->WeaponId);
            CombatStats* stats = &unit->CombatStats;
            
            // HERE'S THE FORMULA!
            unit->AttackDuration = weapon->AttackDuration / stats->AttackSpeedMulti;
            unit->WindUpDuration = weapon->WindupTime / stats->AttackSpeedMulti;
            unit->AttackTimer = unit->AttackDuration;
        }
    }
}
```

## Next Steps

1. **Complete Ghidra analysis** (currently in progress)
2. **Navigate to combat functions** (addresses: 0x5AF7094, 0x5AEE300)
3. **Look for floating-point constants** near weapon initialization
4. **Check data sections** for constant pools
5. **Document the actual values** found in the code

## Summary

- ❌ Can't see values in IL2CPP dump (it's just structure)
- ✅ **CAN see values in Ghidra** (decompiled native code)
- ✅ **CAN see values in config file** (if we parse .mpa format)
- ✅ **CAN see values at runtime** (with debugger)

**Best approach**: Use Ghidra - it will show both the formula AND the actual timing values used!

---

**Status**: Waiting for Ghidra analysis to complete, then we'll have the definitive answer with actual numbers!
