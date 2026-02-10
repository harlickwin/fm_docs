# How to Export Everything from Ghidra for Complete Analysis

## Goal
Export all of Ghidra's analysis so I can create a comprehensive guide on ALL game mechanics (combat, summoning, damage, progression, etc.)

---

## Best Method: Export as C/C++ Header Files

This gives me all decompiled functions in a searchable format.

### Steps:

1. In Ghidra, go to **File → Export Program...**
2. Format: Select **C/C++**
3. Options:
   - ✅ Check **Create Header File (.h)**
   - ✅ Check **Use Decompiler** (IMPORTANT!)
   - ✅ Check **Create Function Signatures**
   - ⬜ Uncheck **Create Undefined Data** (optional, reduces size)
4. Output file: Save to your workspace as `libil2cpp-decompiled.c`
5. Click **OK**

**Expected file size**: 50-200 MB (text file, I can handle it)

**What this gives me**:
- All decompiled functions as C pseudocode
- All function signatures
- All global variables
- All data structures

---

## Alternative Method: Export Symbol Table + Selected Functions

If the full export is too large or fails, do this instead:

### Part 1: Export Symbol Table

1. **File → Export Program**
2. Format: **ASCII** or **CSV**
3. Check **Symbol Table**
4. Save as: `symbol-table.csv`

### Part 2: Export Function List

1. **Window → Functions**
2. Select all functions (Ctrl+A)
3. Right-click → **Export** → **CSV**
4. Save as: `function-list.csv`

### Part 3: Use Ghidra Script to Export Key Functions

Run this Python script in Ghidra (**Window → Script Manager → New**):

```python
# Export all functions to text file
# @category Analysis

from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Initialize decompiler
decompiler = DecompInterface()
decompiler.openProgram(currentProgram)

# Output file - CHANGE THIS PATH TO YOUR WORKSPACE
output_file = "D:/Kiro/tournament-pro/ghidra-exports/all-functions.c"

# Create output directory if needed
import os
output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output = open(output_file, 'w', encoding='utf-8')

# Get all functions
function_manager = currentProgram.getFunctionManager()
functions = function_manager.getFunctions(True)

print("Exporting all functions...")
count = 0
skipped = 0

for function in functions:
    func_name = function.getName()
    
    # Skip thunk functions (they're just redirects)
    if function.isThunk():
        skipped += 1
        continue
    
    count += 1
    if count % 100 == 0:
        print("Processed " + str(count) + " functions...")
    
    # Decompile function
    results = decompiler.decompileFunction(function, 30, ConsoleTaskMonitor())
    
    if results.decompileCompleted():
        decomp_code = results.getDecompiledFunction().getC()
        
        # Write to file
        output.write("// ========================================\n")
        output.write("// Function: " + func_name + "\n")
        output.write("// Address: " + str(function.getEntryPoint()) + "\n")
        output.write("// ========================================\n")
        output.write(decomp_code + "\n\n")
    else:
        output.write("// Function: " + func_name + " (decompilation failed)\n\n")

output.close()
print("Exported " + str(count) + " functions (skipped " + str(skipped) + " thunks)")
print("Output: " + output_file)
```

**To run this script:**
1. Open Script Manager (**Window → Script Manager**)
2. Click **New** (the green + icon)
3. Name it `ExportAllFunctions.py`
4. Paste the code above
5. **IMPORTANT**: Change the `output_file` path to your actual workspace path
6. Save and run the script
7. Wait (this might take 10-30 minutes for a large binary)

---

## What to Export to This Workspace

Create this folder structure in your workspace:

```
./ghidra-exports/
├── all-functions.c              # All decompiled functions (from script or File→Export)
├── symbol-table.csv             # All symbols and addresses
├── function-list.csv            # List of all functions
├── strings.txt                  # All strings found in binary (optional)
└── data-types.txt               # All data structures (optional)
```

---

## Quick Export Commands

### Option A: Full Export (Easiest)
```
File → Export Program
Format: C/C++
Options: ✅ Use Decompiler
Save to: D:\Kiro\tournament-pro\ghidra-exports\libil2cpp-decompiled.c
```

### Option B: Script Export (Most Reliable)
```
1. Window → Script Manager
2. New → ExportAllFunctions.py
3. Paste script above
4. Change output path
5. Run
```

### Option C: Symbol Table Only (Fastest)
```
File → Export Program
Format: CSV
Options: ✅ Symbol Table
Save to: D:\Kiro\tournament-pro\ghidra-exports\symbol-table.csv
```

---

## Additional Useful Exports

### Export All Strings
1. **Search → For Strings...**
2. Click **Search All**
3. In results window: **File → Export** → **CSV**
4. Save as: `strings.csv`

### Export Data Types
1. **Window → Data Type Manager**
2. Right-click on program name
3. **Export** → **C Header File**
4. Save as: `data-types.h`

---

## File Size Expectations

| Export Type | Expected Size | Time to Export |
|-------------|---------------|----------------|
| Full C/C++ export | 50-200 MB | 5-15 minutes |
| Script export | 50-200 MB | 10-30 minutes |
| Symbol table CSV | 5-20 MB | 1 minute |
| Function list CSV | 2-10 MB | 1 minute |
| Strings CSV | 1-5 MB | 1 minute |

**Note**: These are text files, so they compress well. The actual analysis data is much smaller.

---

## What I Can Do With Full Export

Once you export everything, I can:

### Combat Mechanics
- ✅ Confirm attack speed formula
- ✅ Find base attack times for all weapons
- ✅ Confirm damage calculation
- ✅ Find crit/dodge/block formulas
- ✅ Discover any hidden mechanics

### Summoning Mechanics
- ✅ Confirm seeded RNG algorithm
- ✅ Find exact drop chance percentages
- ✅ Find level progression thresholds
- ✅ Discover pity system (if any)
- ✅ Find all rarity tiers

### Progression Systems
- ✅ Tech tree upgrade costs
- ✅ Forge mechanics
- ✅ Pet/Mount leveling formulas
- ✅ Skill scaling
- ✅ Equipment stat calculations

### PvP Mechanics
- ✅ Arena matchmaking algorithm
- ✅ PvP stat multipliers
- ✅ Guild war mechanics
- ✅ Ranking calculations

### Economy
- ✅ Resource generation rates
- ✅ Shop pricing formulas
- ✅ IAP configurations
- ✅ Daily deal mechanics

### Hidden Mechanics
- ✅ Any undocumented features
- ✅ Debug/cheat detection
- ✅ Anti-cheat measures
- ✅ Server validation logic

---

## Recommended Approach

### For Complete Analysis:

**Step 1**: Export everything using the Python script
```
Run ExportAllFunctions.py → all-functions.c
```

**Step 2**: Export symbol table for quick reference
```
File → Export → CSV → symbol-table.csv
```

**Step 3**: Export strings for context
```
Search → For Strings → Export → strings.csv
```

**Step 4**: Let me know it's ready!

---

## After Export

Once files are in `./ghidra-exports/`, I will:

1. **Index all functions** - Create searchable database
2. **Find key mechanics** - Search for combat, summon, progression functions
3. **Extract formulas** - Pull out all calculations
4. **Document everything** - Create comprehensive mechanics guide
5. **Verify IL2CPP findings** - Confirm what we found in dump.cs
6. **Discover new mechanics** - Find anything we missed

---

## Troubleshooting

### Export is too slow
- Use the Python script instead of File→Export
- Export in chunks (by address range)
- Skip thunk functions (script does this automatically)

### Export fails
- Try CSV exports instead (symbol table, function list)
- Export specific address ranges
- Increase Ghidra's memory (Edit → Tool Options → Memory)

### File is too large
- Compress it (zip/7z) - text compresses very well
- Split into multiple files by address range
- Export only non-thunk functions (script does this)

---

## What Format Works Best

I can work with any of these:

1. ✅ **Plain text C code** - Best, most readable
2. ✅ **CSV files** - Easy to parse and search
3. ✅ **JSON** (if you can export to JSON) - Structured data
4. ✅ **XML** - Also structured
5. ✅ **Large text files** - I can handle 100+ MB files

---

## Ready to Start?

**Quickest path to full analysis:**

1. Run the Python script above (change the output path)
2. Wait for it to finish
3. Tell me when `./ghidra-exports/all-functions.c` is ready
4. I'll create a complete game mechanics guide!

**Estimated time**: 
- Export: 10-30 minutes
- My analysis: 30-60 minutes
- Complete documentation: 2-3 hours

Let's do this! 🚀
