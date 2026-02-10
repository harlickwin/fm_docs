# Ghidra Analysis Guide - Finding Attack Speed Formula

## Setup Complete! ✓

- **Ghidra Location**: `C:\ghidra\ghidra_12.0.2_PUBLIC`
- **Target File**: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
- **File Size**: 119 MB (ARM native code)

## Step-by-Step Analysis

### 1. Create a New Project

1. Ghidra should now be open (if not, run `C:\ghidra\ghidra_12.0.2_PUBLIC\ghidraRun.bat`)
2. Click **File → New Project**
3. Choose **Non-Shared Project**
4. Set location: `C:\ghidra\projects`
5. Project name: `LegendOfCivilizations`
6. Click **Finish**

### 2. Import libil2cpp.so

1. Click **File → Import File**
2. Navigate to: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
3. Click **Select File to Import**
4. Ghidra will auto-detect:
   - **Format**: ELF (Executable and Linkable Format)
   - **Language**: ARM:LE:32:v7 (ARM 32-bit Little Endian v7)
5. Click **OK**
6. Click **OK** again on the import summary

### 3. Analyze the Binary

1. Double-click `libil2cpp.so` in the project window
2. When prompted "Would you like to analyze it now?", click **Yes**
3. In the Analysis Options dialog:
   - Keep all default options checked
   - **Important**: Make sure "Decompiler Parameter ID" is checked
   - Click **Analyze**
4. **Wait for analysis to complete** (this will take 10-30 minutes for a 119 MB file)
   - You'll see a progress bar in the bottom-right
   - The status will show "Analyzing..." then "Ready" when done

### 4. Find Attack Speed Functions

Once analysis is complete, we need to find the functions that handle attack speed calculations.

#### Method 1: Search for Function Names

1. Press **Ctrl+Shift+E** or go to **Search → For Strings**
2. Search for: `HandleUnits`
3. Double-click results to navigate to the function

#### Method 2: Use Symbol Tree

1. Open **Window → Symbol Tree** (if not already open)
2. Expand **Functions**
3. Look for these functions:
   - `AttacksSystem_HandleUnits`
   - `AttacksSystem_Execute`
   - `AttacksSystem_ExecuteAttack`
   - `AttacksSystem_GetDamage`

#### Method 3: Search by Address (if you have RVA from dump.cs)

From our IL2CPP dump, we know:
- `AttacksSystem.HandleUnits` is at RVA: `0x5AF7094`
- `AttacksSystem.Execute` is at RVA: `0x5AEE300`

1. Press **G** (Go To)
2. Enter the address: `5AF7094`
3. Press **Enter**

### 5. Analyze the Decompiled Code

Once you've found the function:

1. **Disassembly View** (left panel): Shows ARM assembly instructions
2. **Decompiler View** (right panel): Shows pseudo-C code

Look for patterns like:
```c
// Division operation for attack speed
float effectiveTime = baseTime / attackSpeedMulti;

// Or in ARM assembly:
VDIV.F32  s0, s1, s2  // Floating point division
```

### 6. Key Functions to Examine

#### AttacksSystem.HandleUnits (RVA: 0x5AF7094)
This is the main combat update loop. Look for:
- Timer updates: `AttackTimer -= deltaTime`
- Attack execution conditions: `if (AttackTimer <= 0)`
- Timer reset logic

#### AttacksSystem.ExecuteAttack (RVA: 0x5AF96F4)
This executes the actual attack. Look for:
- Damage calculation calls
- Projectile spawning
- Timer resets

### 7. What to Look For

#### Attack Speed Division
```c
// We expect to see something like:
unit.AttackDuration = weapon.AttackDuration / stats.AttackSpeedMulti;
unit.WindUpDuration = weapon.WindupTime / stats.AttackSpeedMulti;
```

#### In ARM Assembly
```assembly
; Load base attack duration
VLDR.32   s0, [r4, #0x58]    ; Load AttackDuration

; Load attack speed multiplier
VLDR.32   s1, [r5, #0x??]    ; Load AttackSpeedMulti

; Divide
VDIV.F32  s2, s0, s1         ; s2 = s0 / s1 (duration / speed)

; Store result
VSTR.32   s2, [r4, #0x58]    ; Store back to AttackDuration
```

### 8. Export Your Findings

Once you find the relevant code:

1. **Right-click** on the function
2. Select **Export → C/C++**
3. Save to: `C:\ghidra\attack_speed_code.c`

Or take screenshots:
1. **File → Export → Screenshot**

## Tips for Navigation

- **F** - Follow pointer/reference
- **G** - Go to address
- **Ctrl+E** - Search for text
- **Ctrl+Shift+E** - Search for strings
- **L** - Rename symbol
- **;** - Add comment
- **Ctrl+Shift+G** - Find references to this function
- **Space** - Toggle between disassembly and decompiler

## Common ARM Instructions

- `VLDR` - Load floating point value
- `VSTR` - Store floating point value
- `VDIV.F32` - Floating point division
- `VMUL.F32` - Floating point multiplication
- `VADD.F32` - Floating point addition
- `VSUB.F32` - Floating point subtraction
- `VCMP.F32` - Floating point compare
- `BL` - Branch with link (function call)
- `MOV` - Move data
- `LDR` - Load register
- `STR` - Store register

## Expected Findings

Based on the data structures, we expect to find:

1. **Timer Update Loop**:
   ```c
   for each unit in entities {
       unit.AttackTimer -= deltaTime;
       if (unit.AttackTimer <= 0) {
           ExecuteAttack(unit);
           unit.AttackTimer = unit.AttackDuration;
       }
   }
   ```

2. **Attack Speed Application**:
   ```c
   void InitializeUnit(Unit* unit, WeaponInfo* weapon, CombatStats* stats) {
       unit->AttackDuration = weapon->AttackDuration / stats->AttackSpeedMulti;
       unit->WindUpDuration = weapon->WindupTime / stats->AttackSpeedMulti;
       unit->AttackTimer = unit->AttackDuration;
   }
   ```

3. **Stat Update Handler**:
   ```c
   void OnAttackSpeedChanged(Unit* unit, float newAttackSpeed) {
       // Recalculate durations with new speed
       unit->AttackDuration = unit->BaseAttackDuration / newAttackSpeed;
       unit->WindUpDuration = unit->BaseWindUpDuration / newAttackSpeed;
   }
   ```

## Troubleshooting

### Ghidra Won't Start
- Make sure Java is installed: `java -version`
- Try running as administrator
- Check Windows Defender isn't blocking it

### Analysis Takes Too Long
- This is normal for large files (119 MB)
- Let it complete - it's building the database
- You can work on other things while it analyzes

### Can't Find Functions
- Make sure analysis is complete (status bar shows "Ready")
- Try searching in the Symbol Tree
- Use string search to find function names
- Search for known addresses from the IL2CPP dump

### Decompiler Shows Messy Code
- This is normal for optimized ARM code
- Look for patterns rather than perfect C code
- Focus on the mathematical operations (division, multiplication)
- Cross-reference with the data structures we know

## Next Steps After Finding the Code

Once you locate the attack speed calculation:

1. **Document the exact assembly instructions**
2. **Note the memory offsets** (e.g., `[r4, #0x58]`)
3. **Verify against our data structures**:
   - UnitEntity.AttackDuration is at offset 0x58
   - UnitEntity.WindUpDuration is at offset 0x68
   - UnitEntity.AttackTimer is at offset 0x50
4. **Export the decompiled C code**
5. **Take screenshots of key sections**

## Alternative: Automated Script

If you want to automate the search, I can create a Ghidra Python script that:
- Searches for division operations
- Finds references to known offsets (0x50, 0x58, 0x68)
- Exports matching functions

Let me know if you'd like me to create this script!

## Resources

- **Ghidra Documentation**: `C:\ghidra\ghidra_12.0.2_PUBLIC\docs\index.html`
- **ARM Architecture Reference**: https://developer.arm.com/documentation/
- **IL2CPP Reverse Engineering**: https://katyscode.wordpress.com/2021/02/23/il2cpp-finding-obfuscated-global-metadata/

---

**Ready to start?** Ghidra should be open now. Follow the steps above and let me know what you find!
