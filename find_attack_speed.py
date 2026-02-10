#!/usr/bin/env python3
"""
Ghidra Script: Find Attack Speed Calculation
This script searches for the attack speed division operation in libil2cpp.so

Usage:
1. Open libil2cpp.so in Ghidra
2. Wait for analysis to complete
3. Run this script: Window -> Script Manager -> find_attack_speed.py
"""

from ghidra.program.model.listing import CodeUnit
from ghidra.program.model.symbol import SourceType
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

def find_attack_speed_functions():
    """Find functions related to attack speed calculations"""
    
    print("=" * 80)
    print("SEARCHING FOR ATTACK SPEED CALCULATION")
    print("=" * 80)
    
    # Get current program
    program = getCurrentProgram()
    listing = program.getListing()
    function_manager = program.getFunctionManager()
    
    # Known RVAs from IL2CPP dump
    known_rvas = {
        "AttacksSystem.HandleUnits": 0x5AF7094,
        "AttacksSystem.Execute": 0x5AEE300,
        "AttacksSystem.ExecuteAttack": 0x5AF96F4,
        "AttacksSystem.GetDamage": 0x5AF8E08,
        "AttacksSystem.ApplyDmg": 0x5AF87D4
    }
    
    print("\n[1] Searching for known function addresses...")
    print("-" * 80)
    
    found_functions = []
    
    for func_name, rva in known_rvas.items():
        addr = toAddr(rva)
        func = function_manager.getFunctionAt(addr)
        
        if func:
            print("FOUND: {} at 0x{:08X}".format(func_name, rva))
            print("  Current name: {}".format(func.getName()))
            found_functions.append((func_name, func))
            
            # Rename if not already named
            if "FUN_" in func.getName():
                func.setName(func_name.replace(".", "_"), SourceType.USER_DEFINED)
                print("  Renamed to: {}".format(func_name.replace(".", "_")))
        else:
            print("NOT FOUND: {} at 0x{:08X}".format(func_name, rva))
    
    # Search for division operations
    print("\n[2] Searching for floating-point division operations...")
    print("-" * 80)
    
    division_count = 0
    instruction_iter = listing.getInstructions(True)
    
    for instruction in instruction_iter:
        mnemonic = instruction.getMnemonicString()
        
        # Look for ARM floating-point division
        if mnemonic in ["VDIV.F32", "VDIV.F64", "FDIV", "FDIVS", "FDIVD"]:
            division_count += 1
            
            # Get the function containing this instruction
            func = function_manager.getFunctionContaining(instruction.getAddress())
            
            if func:
                print("Division at 0x{:08X} in function: {}".format(
                    instruction.getAddress().getOffset(),
                    func.getName()
                ))
                
                # Check if this is near our known offsets
                # UnitEntity offsets: AttackTimer=0x50, AttackDuration=0x58, WindUpDuration=0x68
                operands = instruction.getDefaultOperandRepresentation(1)
                if any(offset in operands for offset in ["0x50", "0x58", "0x68", "#0x50", "#0x58", "#0x68"]):
                    print("  *** POTENTIAL MATCH: Uses known UnitEntity offset! ***")
    
    print("\nTotal division operations found: {}".format(division_count))
    
    # Search for string references
    print("\n[3] Searching for relevant strings...")
    print("-" * 80)
    
    search_strings = [
        "AttackSpeed",
        "AttackTimer",
        "AttackDuration",
        "WindupTime",
        "WindUpDuration",
        "CombatStats",
        "UnitEntity"
    ]
    
    for search_str in search_strings:
        # Search for string in memory
        addr = find(toAddr(0), search_str)
        if addr:
            print("Found string '{}' at 0x{:08X}".format(search_str, addr.getOffset()))
            
            # Find references to this string
            refs = getReferencesTo(addr)
            for ref in refs:
                ref_func = function_manager.getFunctionContaining(ref.getFromAddress())
                if ref_func:
                    print("  Referenced by: {}".format(ref_func.getName()))
    
    # Decompile key functions
    print("\n[4] Decompiling key functions...")
    print("-" * 80)
    
    decompiler = DecompInterface()
    decompiler.openProgram(program)
    
    for func_name, func in found_functions:
        print("\n--- {} ---".format(func_name))
        
        try:
            results = decompiler.decompileFunction(func, 30, ConsoleTaskMonitor())
            
            if results.decompileCompleted():
                decomp_code = results.getDecompiledFunction().getC()
                
                # Look for division operations in decompiled code
                lines = decomp_code.split('\n')
                for i, line in enumerate(lines):
                    if '/' in line and not '//' in line and not '/*' in line:
                        print("Line {}: {}".format(i+1, line.strip()))
                        
                        # Check for our known field names
                        if any(field in line for field in ['AttackSpeed', 'AttackTimer', 'AttackDuration', 'WindUp']):
                            print("  *** POTENTIAL ATTACK SPEED CALCULATION! ***")
            else:
                print("  Decompilation failed: {}".format(results.getErrorMessage()))
                
        except Exception as e:
            print("  Error decompiling: {}".format(str(e)))
    
    # Summary
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print("\nFunctions found: {}".format(len(found_functions)))
    print("Division operations: {}".format(division_count))
    print("\nNext steps:")
    print("1. Review the functions listed above")
    print("2. Double-click addresses to navigate to them")
    print("3. Look for division operations with offsets 0x50, 0x58, 0x68")
    print("4. Export decompiled code: Right-click function -> Export -> C/C++")
    print("\n" + "=" * 80)

# Run the analysis
if __name__ == "__main__":
    find_attack_speed_functions()
