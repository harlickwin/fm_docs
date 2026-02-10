#!/usr/bin/env python3
"""
Find specific game mechanics patterns in Ghidra decompiled code.
Searches for RNG algorithms, drop tables, stat calculations, etc.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple

class MechanicsFinder:
    def __init__(self, ghidra_file: str):
        self.ghidra_file = Path(ghidra_file)
        self.results = {}
        
    def search_pattern(self, pattern: str, context_lines: int = 10) -> List[Tuple[int, List[str]]]:
        """Search for a regex pattern and return matches with context."""
        matches = []
        
        with open(self.ghidra_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                context = lines[start:end]
                matches.append((i + 1, context))  # Line numbers start at 1
        
        return matches
    
    def find_pcg_algorithm(self) -> List[Tuple[int, List[str]]]:
        """Find PCG random number generator implementation."""
        print("Searching for PCG algorithm...")
        
        # PCG uses specific constants
        patterns = [
            r'6364136223846793005',  # Decimal
            r'5851f42d4c957f2d',      # Hex
            r'1442695040888963407',   # Decimal
            r'14057b7ef767814f',      # Hex
        ]
        
        all_matches = []
        for pattern in patterns:
            matches = self.search_pattern(pattern, context_lines=20)
            if matches:
                print(f"  Found PCG constant: {pattern}")
                all_matches.extend(matches)
        
        # Also search for characteristic bit operations
        if not all_matches:
            print("  Searching for PCG bit operations...")
            bit_patterns = [
                r'>>\s*18.*\^.*>>\s*27',  # xorshift pattern
                r'>>\s*59',                # rotation amount
            ]
            for pattern in bit_patterns:
                matches = self.search_pattern(pattern, context_lines=30)
                if matches:
                    all_matches.extend(matches)
        
        return all_matches
    
    def find_drop_tables(self) -> List[Tuple[int, List[str]]]:
        """Find drop chance tables (arrays of percentages)."""
        print("Searching for drop chance tables...")
        
        # Look for arrays of float values that look like percentages
        patterns = [
            r'float.*\[\s*[567]\s*\]',  # Array of 5-7 floats (rarities)
            r'\{[^}]*\d+\.\d+[^}]*\d+\.\d+[^}]*\d+\.\d+[^}]*\}',  # Struct with multiple floats
        ]
        
        all_matches = []
        for pattern in patterns:
            matches = self.search_pattern(pattern, context_lines=15)
            all_matches.extend(matches)
        
        return all_matches
    
    def find_division_operations(self) -> List[Tuple[int, List[str]]]:
        """Find division operations (likely stat calculations like attack speed)."""
        print("Searching for division operations...")
        
        # Look for division with float/double types
        pattern = r'[a-zA-Z_][a-zA-Z0-9_]*\s*/\s*[a-zA-Z_][a-zA-Z0-9_]*'
        matches = self.search_pattern(pattern, context_lines=5)
        
        # Filter to only those with float operations nearby
        filtered = []
        for line_num, context in matches:
            context_str = ''.join(context)
            if 'float' in context_str.lower() or '.0f' in context_str:
                filtered.append((line_num, context))
        
        return filtered[:100]  # Limit to first 100 to avoid spam
    
    def find_comparison_chains(self) -> List[Tuple[int, List[str]]]:
        """Find chains of if statements (likely rarity determination)."""
        print("Searching for comparison chains...")
        
        matches = []
        with open(self.ghidra_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            # Count consecutive if statements
            if_count = 0
            start_line = i
            
            while i < len(lines) and 'if' in lines[i]:
                if_count += 1
                i += 1
                # Skip a few lines to account for if body
                i += 2
            
            # If we found 4+ consecutive ifs, this might be rarity determination
            if if_count >= 4:
                start = max(0, start_line - 5)
                end = min(len(lines), i + 10)
                matches.append((start_line + 1, lines[start:end]))
            
            i += 1
        
        return matches[:50]  # Limit results
    
    def find_stat_calculations(self) -> Dict[str, List[Tuple[int, List[str]]]]:
        """Find stat calculation patterns."""
        print("Searching for stat calculations...")
        
        stats = {
            'attack_speed': [],
            'damage': [],
            'crit': [],
            'health': []
        }
        
        # Attack speed: look for divisions
        stats['attack_speed'] = self.find_division_operations()[:20]
        
        # Damage: look for multiplications
        damage_pattern = r'\*.*(?:damage|dmg|attack)'
        stats['damage'] = self.search_pattern(damage_pattern, context_lines=10)[:20]
        
        # Crit: look for percentage comparisons
        crit_pattern = r'(?:crit|critical).*[<>]'
        stats['crit'] = self.search_pattern(crit_pattern, context_lines=10)[:20]
        
        # Health: look for HP calculations
        health_pattern = r'(?:health|hp|hitpoint).*[+\-*/]'
        stats['health'] = self.search_pattern(health_pattern, context_lines=10)[:20]
        
        return stats
    
    def find_large_constants(self) -> List[Tuple[int, List[str]]]:
        """Find large numeric constants (potential config values)."""
        print("Searching for large constants...")
        
        # Look for numbers with 4+ digits
        pattern = r'\b\d{4,}\b'
        matches = self.search_pattern(pattern, context_lines=3)
        
        return matches[:100]  # Limit results
    
    def analyze_all(self, output_file: str):
        """Run all searches and save results."""
        print("=" * 80)
        print("COMPREHENSIVE MECHANICS SEARCH")
        print("=" * 80)
        print()
        
        results = {
            'pcg_algorithm': self.find_pcg_algorithm(),
            'drop_tables': self.find_drop_tables(),
            'comparison_chains': self.find_comparison_chains(),
            'stat_calculations': self.find_stat_calculations(),
            'large_constants': self.find_large_constants()
        }
        
        # Save results
        print(f"\nSaving results to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Game Mechanics Pattern Search Results\n\n")
            
            # PCG Algorithm
            f.write("## PCG Random Number Generator\n\n")
            if results['pcg_algorithm']:
                f.write(f"Found {len(results['pcg_algorithm'])} potential PCG implementations:\n\n")
                for line_num, context in results['pcg_algorithm'][:5]:  # Top 5
                    f.write(f"### Line {line_num}\n```c\n")
                    f.write(''.join(context))
                    f.write("\n```\n\n")
            else:
                f.write("No PCG algorithm found (may use different RNG)\n\n")
            
            # Drop Tables
            f.write("## Drop Chance Tables\n\n")
            if results['drop_tables']:
                f.write(f"Found {len(results['drop_tables'])} potential drop tables:\n\n")
                for line_num, context in results['drop_tables'][:10]:  # Top 10
                    f.write(f"### Line {line_num}\n```c\n")
                    f.write(''.join(context))
                    f.write("\n```\n\n")
            else:
                f.write("No obvious drop tables found\n\n")
            
            # Comparison Chains
            f.write("## Comparison Chains (Rarity Determination)\n\n")
            if results['comparison_chains']:
                f.write(f"Found {len(results['comparison_chains'])} comparison chains:\n\n")
                for line_num, context in results['comparison_chains'][:10]:
                    f.write(f"### Line {line_num}\n```c\n")
                    f.write(''.join(context))
                    f.write("\n```\n\n")
            else:
                f.write("No comparison chains found\n\n")
            
            # Stat Calculations
            f.write("## Stat Calculations\n\n")
            for stat_name, matches in results['stat_calculations'].items():
                f.write(f"### {stat_name.replace('_', ' ').title()}\n\n")
                if matches:
                    f.write(f"Found {len(matches)} occurrences:\n\n")
                    for line_num, context in matches[:5]:  # Top 5 per stat
                        f.write(f"#### Line {line_num}\n```c\n")
                        f.write(''.join(context))
                        f.write("\n```\n\n")
                else:
                    f.write("No matches found\n\n")
            
            # Large Constants
            f.write("## Large Constants (Config Values)\n\n")
            if results['large_constants']:
                f.write(f"Found {len(results['large_constants'])} large constants:\n\n")
                # Group by value
                constants_by_value = {}
                for line_num, context in results['large_constants']:
                    for line in context:
                        nums = re.findall(r'\b(\d{4,})\b', line)
                        for num in nums:
                            if num not in constants_by_value:
                                constants_by_value[num] = []
                            constants_by_value[num].append(line_num)
                
                # Show most common constants
                sorted_constants = sorted(constants_by_value.items(), 
                                        key=lambda x: len(x[1]), reverse=True)
                
                f.write("Most common large constants:\n\n")
                for value, line_nums in sorted_constants[:20]:
                    f.write(f"- `{value}` appears {len(line_nums)} times\n")
                f.write("\n")
        
        print(f"✓ Analysis complete! Results saved to {output_file}")
        
        # Print summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"PCG Algorithm matches: {len(results['pcg_algorithm'])}")
        print(f"Drop tables found: {len(results['drop_tables'])}")
        print(f"Comparison chains: {len(results['comparison_chains'])}")
        print(f"Attack speed calculations: {len(results['stat_calculations']['attack_speed'])}")
        print(f"Damage calculations: {len(results['stat_calculations']['damage'])}")
        print(f"Large constants: {len(results['large_constants'])}")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python find_game_mechanics.py <ghidra_file> [output_file]")
        sys.exit(1)
    
    ghidra_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "mechanics_patterns.md"
    
    finder = MechanicsFinder(ghidra_file)
    finder.analyze_all(output_file)

if __name__ == "__main__":
    main()
