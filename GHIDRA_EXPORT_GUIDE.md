# How to Export Ghidra Analysis for AI Analysis

## What I Need from Ghidra

I can analyze several types of Ghidra exports to find the summon mechanics. Here are the best options:

---

## Option 1: Export Decompiled Functions (BEST)

This gives me the C pseudocode that Ghidra generated.

### Step 1: Find Functions Related to Summoning

In Ghidra's **Symbol Tree** or **Functions** window, search for:
- `Summon`
- `Mount`
- `Pet`
- `Egg`
- `Random`
- `DropChance`

### Step 2: Export Individual Functions

For each relevant function:
1. Right-click the function in the **Decompiler** window
2. Select **Copy C Output**
3. Paste into a text file

**OR** use Ghidra's script:

1. Go to **Window → Script Manager**
2. Search for `ExportFunctionsScript.java`
3. Run it and select functions to export

### Step 3: Save to Workspace

Save the decompiled code to:
```
./ghidra-exports/decompiled-functions.c
```

**What to Export**:
- Any function with "Summon" in the name
- Any function with "Mount" or "Pet" in the name
- Any function with "Random" in the name
- Any function that references the addresses from IL2CPP dump

---

## Option 2: Export Symbol Table (GOOD)

This gives me all function names and addresses.

### Steps:

1. In Ghidra, go to **File → Export Program**
2. Format: **ASCII** or **CSV**
3. Check **Symbol Table**
4. Save to: `./ghidra-exports/symbol-table.csv`

**What This Gives Me**:
- All function names
- All function addresses
- All global variables
- All string references

---

## Option 3: Search for Specific Patterns (TARGETED)

Use Ghidra's search to find specific code patterns.

### Search for Floating-Point Constants

1. Go to **Search → Memory**
2. Search Type: **Float**
3. Search for these values:
   - `50.0` (likely Common drop chance)
   - `100.0` (percentage conversion)
   - `4294967295.0` (uint max)

4. For each result:
   - Note the address
   - Open in **Decompiler**
   - Export that function

### Search for String References

1. Go to **Search → For Strings**
2. Search for:
   - "MountSummon"
   - "PetSummon"
   - "RandomSeed"
   - "DropChance"
   - "Common"
   - "Rare"
   - "Epic"
   - "Legendary"

3. For each result:
   - Right-click → **References → Show References to Address**
   - Export functions that reference these strings

---

## Option 4: Export Entire Program (COMPREHENSIVE)

This exports everything but creates a large file.

### Steps:

1. **File → Export Program**
2. Format: **C/C++**
3. Save to: `./ghidra-exports/libil2cpp-decompiled.c`

**Warning**: This file will be HUGE (possibly 100+ MB). Only do this if other methods don't work.

---

## Option 5: Use Ghidra Python Script (AUTOMATED)

I can provide you with a Python script to run in Ghidra that automatically finds and exports relevant functions.

### Create this script in Ghidra:

Save as `export_summon_functions.py` in Ghidra's script directory:

```python
# Export functions related to summoning mechanics
# @category Analysis

from ghidra.program.model.symbol import SymbolType
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import os

# Initialize decompiler
decompiler = DecompInterface()
decompiler.openProgram(currentProgram)

# Output file
output_file = "C:/path/to/workspace/ghidra-exports/summon-functions.c"
output = open(output_file, 'w')

# Keywords to search for
keywords = [
    "Summon", "Mount", "Pet", "Egg", "Random", 
    "DropChance", "Rarity", "PCG"
]

# Get all functions
function_manager = currentProgram.getFunctionManager()
functions = function_manager.getFunctions(True)

print("Searching for relevant functions...")
found_count = 0

for function in functions:
    func_name = function.getName()
    
    # Check if function name contains any keyword
    for keyword in keywords:
        if keyword.lower() in func_name.lower():
            print("Found: " + func_name)
            found_count += 1
            
            # Decompile function
            results = decompiler.decompileFunction(function, 30, ConsoleTaskMonitor())
            
            if results.decompileCompleted():
                decomp_code = results.getDecompiledFunction().getC()
                
                # Write to file
                output.write("// Function: " + func_name + "\n")
                output.write("// Address: " + str(function.getEntryPoint()) + "\n")
                output.write(decomp_code + "\n\n")
                output.write("=" * 80 + "\n\n")
            
            break  # Don't check other keywords for this function

output.close()
print("Exported " + str(found_count) + " functions to " + output_file)
```

### To Run:

1. Open Ghidra Script Manager (**Window → Script Manager**)
2. Click **New** and paste the script above
3. Update the `output_file` path to your workspace
4. Run the script
5. Check the output file

---

## Option 6: Export Specific Addresses (PRECISE)

If you know the addresses from the IL2CPP dump, export those specific functions.

### Known Addresses from IL2CPP Dump:

From `dump.cs`, we have some function addresses (these might be relative):
- `AttacksSystem.HandleUnits`: 0x5AF7094
- `AttacksSystem.Execute`: 0x5AEE300
- `AttacksSystem.ExecuteAttack`: 0x5AF96F4

### Steps:

1. In Ghidra, press **G** (Go To)
2. Enter address (try both with and without base offset)
3. If you find a function, export it using **Copy C Output**

---

## What Format Works Best for Me?

### Best Formats (in order):

1. **Decompiled C code** - I can read this directly
2. **CSV symbol table** - I can search for function names
3. **Plain text with addresses and code** - I can parse this
4. **JSON export** (if available) - Easy to parse

### Formats I Can't Use:

- Binary files (.gzf, .rep)
- Ghidra project files
- Screenshots (unless they contain text I can read)

---

## Recommended Workflow

### Quick Method (10 minutes):

1. Search for "Summon" in Symbol Tree
2. Export 5-10 most relevant functions using **Copy C Output**
3. Save to `./ghidra-exports/summon-functions.txt`
4. I'll analyze those first

### Thorough Method (30 minutes):

1. Run the Python script above to auto-export all relevant functions
2. Export symbol table as CSV
3. Search for floating-point constants and export those functions
4. I'll have everything I need

### Nuclear Option (if nothing else works):

1. Export entire program as C/C++
2. I'll search through it (will take longer)

---

## What to Look For Manually

If you want to explore in Ghidra yourself before exporting:

### 1. Find RandomPCG::Next()

Look for a function with:
- Multiplication by `6364136223846793005` (0x5851F42D4C957F2D)
- Addition of `1442695040888963407` (0x14057B7EF767814F)
- Bit shifting operations (>> 18, >> 27, >> 59)

### 2. Find Summon Function

Look for a function that:
- Loads a 64-bit value (the seed)
- Calls RandomPCG::Next()
- Compares result with floating-point values
- Has multiple if/else branches (for different rarities)

### 3. Find Drop Chance Config

Look for:
- Array or struct with 6-7 float values
- Values that look like percentages (0-100)
- Accessed by an index (the level)

---

## File Structure I Need

Please create this folder structure:

```
./ghidra-exports/
├── summon-functions.c          # Decompiled summon-related functions
├── random-functions.c          # RandomPCG and related functions
├── symbol-table.csv            # All symbols
├── float-constants.txt         # Functions with float constants
└── string-references.txt       # Functions referencing summon strings
```

---

## After You Export

Once you've exported the files to `./ghidra-exports/`, I can:

1. Search for the exact summon algorithm
2. Find the actual drop chance values
3. Confirm the RandomPCG implementation
4. Find the level progression logic
5. Extract any hardcoded constants

Just let me know when the files are ready and I'll analyze them!

---

## Quick Start Command

If you just want to get started quickly:

1. In Ghidra, search for "Summon" in the Symbol Tree
2. Find the most promising function (probably named something like `PlayerMountCollectionModel_SummonMount`)
3. Right-click in Decompiler → **Copy C Output**
4. Create `./ghidra-exports/summon-functions.txt` and paste it
5. Tell me it's ready!

That alone might give me 80% of what I need.
