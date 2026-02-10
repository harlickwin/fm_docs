#!/usr/bin/env python3
"""
Extract functions from Ghidra decompiled C code by address.
Cross-references with IL2CPP dump to identify function purposes.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class GhidraFunctionExtractor:
    def __init__(self, ghidra_file: str, il2cpp_file: str):
        self.ghidra_file = Path(ghidra_file)
        self.il2cpp_file = Path(il2cpp_file)
        self.address_map = {}
        self.functions = {}
        
    def extract_il2cpp_addresses(self) -> Dict[str, str]:
        """Extract function addresses from IL2CPP dump comments."""
        print("Extracting addresses from IL2CPP dump...")
        addresses = {}
        
        with open(self.il2cpp_file, 'r', encoding='utf-8', errors='ignore') as f:
            current_class = None
            current_method = None
            
            for line in f:
                # Track current class
                if 'public class ' in line or 'public struct ' in line:
                    match = re.search(r'(?:class|struct)\s+(\w+)', line)
                    if match:
                        current_class = match.group(1)
                
                # Find method with RVA comment
                if '// RVA:' in line:
                    # Extract address
                    addr_match = re.search(r'// RVA: (0x[0-9A-Fa-f]+)', line)
                    if addr_match:
                        address = addr_match.group(1)
                        
                        # Try to find method name on same or previous line
                        method_match = re.search(r'(?:public|private|protected).*?(\w+)\s*\(', line)
                        if method_match:
                            method_name = method_match.group(1)
                            full_name = f"{current_class}.{method_name}" if current_class else method_name
                            addresses[address.lower()] = full_name
                            
        print(f"Found {len(addresses)} function addresses in IL2CPP dump")
        return addresses
    
    def find_function_in_ghidra(self, address: str) -> Optional[Tuple[str, List[str]]]:
        """Find a function by address in Ghidra output."""
        # Convert address format: 0x5AF7094 -> FUN_05af7094
        addr_hex = address.replace('0x', '').lower().zfill(8)
        func_name = f"FUN_{addr_hex}"
        
        print(f"Searching for {func_name} (address {address})...")
        
        with open(self.ghidra_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        # Find function definition
        for i, line in enumerate(lines):
            if func_name in line and ('void ' in line or 'int ' in line or 'undefined' in line):
                # Extract function and its body
                func_lines = [line]
                brace_count = 0
                started = False
                
                for j in range(i + 1, min(i + 1000, len(lines))):  # Max 1000 lines per function
                    func_lines.append(lines[j])
                    
                    if '{' in lines[j]:
                        started = True
                        brace_count += lines[j].count('{')
                    if '}' in lines[j]:
                        brace_count -= lines[j].count('}')
                    
                    if started and brace_count == 0:
                        break
                
                return (func_name, func_lines)
        
        return None
    
    def extract_constants_from_function(self, func_lines: List[str]) -> Dict[str, List]:
        """Extract numeric constants from function code."""
        constants = {
            'integers': [],
            'floats': [],
            'hex': [],
            'large_numbers': []
        }
        
        for line in func_lines:
            # Find integer constants
            int_matches = re.findall(r'\b(\d{3,})\b', line)
            constants['integers'].extend(int_matches)
            
            # Find hex constants
            hex_matches = re.findall(r'0x([0-9a-fA-F]{4,})', line)
            constants['hex'].extend(hex_matches)
            
            # Find float constants
            float_matches = re.findall(r'\b(\d+\.\d+)f?\b', line)
            constants['floats'].extend(float_matches)
            
            # Find large numbers (potential seeds/multipliers)
            large_matches = re.findall(r'\b(\d{10,})[UuLl]*\b', line)
            constants['large_numbers'].extend(large_matches)
        
        # Remove duplicates
        for key in constants:
            constants[key] = list(set(constants[key]))
        
        return constants
    
    def analyze_function_pattern(self, func_lines: List[str]) -> Dict[str, bool]:
        """Identify what kind of function this might be based on patterns."""
        code = ''.join(func_lines)
        
        patterns = {
            'has_division': '/' in code and 'float' in code.lower(),
            'has_multiplication': '*' in code,
            'has_modulo': '%' in code,
            'has_random': 'random' in code.lower() or 'rand' in code.lower(),
            'has_comparison_chain': code.count('if') > 3,
            'has_bit_shift': '>>' in code or '<<' in code,
            'has_array_access': '[' in code and ']' in code,
            'has_loop': 'for' in code or 'while' in code or 'do' in code,
            'has_float_ops': 'float' in code.lower() or '.0f' in code,
            'has_large_constants': any(len(n) > 10 for n in re.findall(r'\d+', code))
        }
        
        return patterns
    
    def extract_all_key_functions(self, output_file: str):
        """Extract all functions we care about and save to file."""
        # Get address mapping from IL2CPP
        self.address_map = self.extract_il2cpp_addresses()
        
        results = []
        
        print(f"\nExtracting {len(self.address_map)} functions from Ghidra output...")
        
        for address, name in self.address_map.items():
            result = self.find_function_in_ghidra(address)
            
            if result:
                func_name, func_lines = result
                constants = self.extract_constants_from_function(func_lines)
                patterns = self.analyze_function_pattern(func_lines)
                
                results.append({
                    'address': address,
                    'il2cpp_name': name,
                    'ghidra_name': func_name,
                    'code': ''.join(func_lines),
                    'constants': constants,
                    'patterns': patterns
                })
                
                print(f"✓ Found {name} at {address}")
            else:
                print(f"✗ Could not find {name} at {address}")
        
        # Save results
        print(f"\nSaving results to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Extracted Functions from Ghidra\n\n")
            f.write(f"Total functions extracted: {len(results)}\n\n")
            f.write("=" * 80 + "\n\n")
            
            for r in results:
                f.write(f"## {r['il2cpp_name']}\n\n")
                f.write(f"**Address**: {r['address']}\n")
                f.write(f"**Ghidra Function**: {r['ghidra_name']}\n\n")
                
                f.write("**Patterns Detected**:\n")
                for pattern, detected in r['patterns'].items():
                    if detected:
                        f.write(f"- {pattern}\n")
                f.write("\n")
                
                f.write("**Constants Found**:\n")
                for const_type, values in r['constants'].items():
                    if values:
                        f.write(f"- {const_type}: {', '.join(values[:10])}\n")
                f.write("\n")
                
                f.write("**Decompiled Code**:\n```c\n")
                f.write(r['code'])
                f.write("\n```\n\n")
                f.write("=" * 80 + "\n\n")
        
        print(f"✓ Extraction complete! Results saved to {output_file}")
        return results

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_functions_by_address.py <ghidra_file> <il2cpp_file> [output_file]")
        sys.exit(1)
    
    ghidra_file = sys.argv[1]
    il2cpp_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else "extracted_functions.md"
    
    extractor = GhidraFunctionExtractor(ghidra_file, il2cpp_file)
    extractor.extract_all_key_functions(output_file)

if __name__ == "__main__":
    main()
