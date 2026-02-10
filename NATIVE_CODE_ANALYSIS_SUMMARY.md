# Native ARM Code Analysis - Summary

## What We're Doing

We're analyzing the **native ARM machine code** in `libil2cpp.so` to find the **exact attack speed formula** that the game uses.

## Why?

The IL2CPP dump (`dump.cs`) shows us the **structure** (classes, fields, method signatures) but not the **implementation** (actual calculation logic). The real code is compiled to ARM assembly in `libil2cpp.so`.

## Tools Installed

### ✅ Ghidra 12.0.2
- **Location**: `C:\ghidra\ghidra_12.0.2_PUBLIC`
- **Purpose**: Reverse engineering tool that decompiles ARM code to readable C
- **Status**: Installed and ready

### ✅ Target File
- **File**: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
- **Size**: 119 MB
- **Type**: ARM 32-bit native library (armeabi-v7a)
- **Contains**: All game logic compiled from C# to ARM assembly

## What We Know (From IL2CPP Dump)

### Data Structures
```csharp
// WeaponInfo - Base configuration
public class WeaponInfo {
    public F64 WindupTime;       // Base windup time
    public F64 AttackDuration;   // Base attack duration
}

// UnitEntity - Runtime state
public struct UnitEntity {
    public FD6 AttackTimer;      // Offset: 0x50
    public FD6 AttackDuration;   // Offset: 0x58 (after speed applied)
    public FD6 WindUpDuration;   // Offset: 0x68 (after speed applied)
}

// CombatStats - Character stats
public struct CombatStats {
    public FD6 AttackSpeedMulti; // The multiplier!
}
```

### Key Functions (RVA Addresses)
| Function | Address | Purpose |
|----------|---------|---------|
| `AttacksSystem.HandleUnits` | 0x5AF7094 | Main combat update loop |
| `AttacksSystem.Execute` | 0x5AEE300 | Combat system entry point |
| `AttacksSystem.ExecuteAttack` | 0x5AF96F4 | Executes attack action |
| `AttacksSystem.GetDamage` | 0x5AF8E08 | Calculates damage |
| `AttacksSystem.ApplyDmg` | 0x5AF87D4 | Applies damage to target |

## What We're Looking For

### Expected Formula
```c
// We believe the formula is:
effectiveTime = baseTime / attackSpeedMulti;

// Specifically:
unit->AttackDuration = weapon->AttackDuration / stats->AttackSpeedMulti;
unit->WindUpDuration = weapon->WindupTime / stats->AttackSpeedMulti;
```

### In ARM Assembly
```assembly
; Load base duration from weapon config
VLDR.32   s0, [r4, #offset]    ; s0 = base duration

; Load attack speed multiplier from stats
VLDR.32   s1, [r5, #offset]    ; s1 = AttackSpeedMulti

; Perform division
VDIV.F32  s2, s0, s1           ; s2 = s0 / s1 (PROOF!)

; Store result in unit entity
VSTR.32   s2, [r6, #0x58]      ; Store to AttackDuration (offset 0x58)
```

### Alternative: Could It Be Multiplication?
```assembly
; If the formula is actually: effectiveTime = baseTime * attackSpeedMulti
VMUL.F32  s2, s0, s1           ; s2 = s0 * s1

; But this would mean higher AttackSpeedMulti = SLOWER attacks
; Which contradicts the field name "Multi" and game behavior
```

## Analysis Process

### Step 1: Import to Ghidra
- Load `libil2cpp.so` into Ghidra
- Let Ghidra analyze the binary (10-30 minutes)
- Ghidra will:
  - Disassemble ARM instructions
  - Identify functions
  - Decompile to pseudo-C code

### Step 2: Locate Functions
- Navigate to known addresses (0x5AF7094, etc.)
- Or use automated script: `find_attack_speed.py`
- Identify the combat update loop

### Step 3: Find the Division
- Look for `VDIV.F32` instructions (ARM floating-point division)
- Check if they reference offsets 0x50, 0x58, or 0x68
- Examine surrounding code for context

### Step 4: Verify the Formula
- Confirm the operands match our expected data:
  - Dividend: Base time from WeaponInfo
  - Divisor: AttackSpeedMulti from CombatStats
  - Result: Stored in UnitEntity fields
- Check the decompiled C code for clarity

## Expected Findings

### Scenario 1: Division (Most Likely)
```c
void UpdateAttackSpeed(UnitEntity* unit, WeaponInfo* weapon, CombatStats* stats) {
    // Higher speed = faster attacks
    unit->AttackDuration = weapon->AttackDuration / stats->AttackSpeedMulti;
    unit->WindUpDuration = weapon->WindupTime / stats->AttackSpeedMulti;
}
```

**Evidence:**
- Field named "AttackSpeedMulti" (multiplicative)
- Higher values should = faster attacks
- Division achieves this: 2.0 / 2.0 = 1.0 (half the time)

### Scenario 2: Multiplication (Less Likely)
```c
void UpdateAttackSpeed(UnitEntity* unit, WeaponInfo* weapon, CombatStats* stats) {
    // Higher speed = slower attacks (counterintuitive!)
    unit->AttackDuration = weapon->AttackDuration * stats->AttackSpeedMulti;
    unit->WindUpDuration = weapon->WindupTime * stats->AttackSpeedMulti;
}
```

**Why unlikely:**
- Would mean AttackSpeedMulti < 1.0 for faster attacks
- Contradicts naming convention
- Less intuitive for game designers

### Scenario 3: Inverse Multiplication
```c
void UpdateAttackSpeed(UnitEntity* unit, WeaponInfo* weapon, CombatStats* stats) {
    // Store as "attacks per second" instead of "time per attack"
    float attacksPerSecond = 1.0f / weapon->AttackDuration;
    attacksPerSecond *= stats->AttackSpeedMulti;
    unit->AttackDuration = 1.0f / attacksPerSecond;
}
```

**Possible but complex:**
- More calculations
- Less efficient
- Unlikely for mobile game

## Success Criteria

We've definitively found the formula when we can:

1. ✅ **Locate the exact ARM instructions** that calculate attack timing
2. ✅ **Identify the operation** (division, multiplication, or other)
3. ✅ **Verify the operands** match our known data structures
4. ✅ **Confirm the memory offsets** (0x50, 0x58, 0x68)
5. ✅ **Export the decompiled code** showing the calculation

## Files Created

| File | Purpose |
|------|---------|
| `GHIDRA_QUICK_START.md` | Quick reference for Ghidra usage |
| `GHIDRA_ANALYSIS_GUIDE.md` | Detailed step-by-step guide |
| `find_attack_speed.py` | Automated Ghidra script |
| `CODE_LOCATIONS.md` | IL2CPP dump reference |
| `NATIVE_CODE_ANALYSIS_SUMMARY.md` | This file |

## Next Steps

1. **Launch Ghidra**: `C:\ghidra\ghidra_12.0.2_PUBLIC\ghidraRun.bat`
2. **Follow Quick Start**: See `GHIDRA_QUICK_START.md`
3. **Run Automated Script**: `find_attack_speed.py`
4. **Examine Results**: Look for division operations
5. **Document Findings**: Export code and take screenshots

## Why This Matters

Understanding the exact formula allows us to:
- **Accurately simulate combat** in our tournament calculator
- **Verify game mechanics** against player observations
- **Optimize build calculations** for maximum DPS
- **Understand stat interactions** for better theorycrafting

## Technical Notes

### ARM Floating-Point Instructions
- `VDIV.F32` - 32-bit float division
- `VMUL.F32` - 32-bit float multiplication
- `VADD.F32` - 32-bit float addition
- `VSUB.F32` - 32-bit float subtraction
- `VLDR.32` - Load 32-bit float from memory
- `VSTR.32` - Store 32-bit float to memory

### Fixed-Point Types
The game uses custom fixed-point types:
- `F64` - 64-bit fixed-point
- `FD6` - Fixed-point with 6 decimal places

These are likely converted to/from floats for calculations.

### Memory Layout
```
UnitEntity structure:
+0x00: [other fields]
+0x50: AttackTimer (FD6)
+0x58: AttackDuration (FD6)
+0x60: [other fields]
+0x68: WindUpDuration (FD6)
+0x70: [other fields]
```

## Alternative Approaches

If Ghidra analysis is too complex:

1. **Dynamic Analysis**: Use Frida to hook functions at runtime
2. **Memory Inspection**: Attach debugger and watch values change
3. **Game Testing**: Empirically test with different attack speed values
4. **Community Research**: Check if others have reverse-engineered this

But Ghidra is the most direct path to the answer!

---

**Status**: Ready to analyze! Ghidra is installed and waiting.

**Time Estimate**: 
- Ghidra analysis: 10-30 minutes (automated)
- Finding the code: 15-60 minutes (manual exploration)
- Total: ~1-2 hours for definitive answer

**Confidence**: High - We have exact addresses and know what to look for!
