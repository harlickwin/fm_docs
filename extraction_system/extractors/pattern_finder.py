"""Pattern finder for searching code patterns in Ghidra exports."""

import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from extraction_system.core.logger import ProgressLogger


@dataclass
class Match:
    """A pattern match with context."""
    pattern_name: str
    line_number: int
    matched_text: str
    context_before: List[str]
    context_after: List[str]
    full_context: str


class PatternFinder:
    """Searches for specific code patterns in Ghidra export."""
    
    # Predefined patterns
    PATTERNS = {
        'pcg_multiplier': r'6364136223846793005|0x5851f42d4c957f2d',
        'pcg_increment': r'1442695040888963407|0x14057b7ef767814f',
        'pcg_shifts': r'>>\s*18.*\^.*>>\s*27|>>\s*59',
        'drop_table': r'float.*\[\s*[567]\s*\]',
        'division': r'[a-zA-Z_][a-zA-Z0-9_]*\s*/\s*[a-zA-Z_][a-zA-Z0-9_]*',
        'comparison_chain': r'(if\s*\([^)]+\)\s*{[^}]*}){4,}',
        'bit_shift': r'<<|>>',
        'xor_operation': r'\^',
        'array_access': r'\[[^\]]+\]',
        'large_constant': r'\b[1-9]\d{6,}\b',  # Numbers with 7+ digits
    }
    
    def __init__(self, ghidra_file: str, logger: Optional[ProgressLogger] = None):
        self.ghidra_file = Path(ghidra_file)
        self.logger = logger or ProgressLogger("PatternFinder")
        self._file_lines: Optional[List[str]] = None
    
    def _load_file(self):
        """Load Ghidra file into memory as lines."""
        if self._file_lines is None:
            self.logger.info(f"Loading Ghidra export for pattern search")
            with open(self.ghidra_file, 'r', encoding='utf-8', errors='ignore') as f:
                self._file_lines = f.readlines()
            self.logger.info(f"Loaded {len(self._file_lines)} lines")
    
    def find_pcg_algorithm(self) -> List[Match]:
        """Find PCG RNG implementation."""
        self.logger.info("Searching for PCG algorithm")
        matches = []
        
        # Search for PCG multiplier
        matches.extend(self.find_custom_pattern(
            self.PATTERNS['pcg_multiplier'],
            pattern_name="PCG Multiplier"
        ))
        
        # Search for PCG increment
        matches.extend(self.find_custom_pattern(
            self.PATTERNS['pcg_increment'],
            pattern_name="PCG Increment"
        ))
        
        # Search for PCG bit shifts
        matches.extend(self.find_custom_pattern(
            self.PATTERNS['pcg_shifts'],
            pattern_name="PCG Bit Shifts"
        ))
        
        self.logger.info(f"Found {len(matches)} PCG-related matches")
        return matches
    
    def find_drop_tables(self) -> List[Match]:
        """Find drop chance tables (arrays of floats)."""
        self.logger.info("Searching for drop tables")
        matches = self.find_custom_pattern(
            self.PATTERNS['drop_table'],
            pattern_name="Drop Table"
        )
        self.logger.info(f"Found {len(matches)} potential drop tables")
        return matches
    
    def find_division_operations(self) -> List[Match]:
        """Find division operations (stat calculations)."""
        self.logger.info("Searching for division operations")
        matches = self.find_custom_pattern(
            self.PATTERNS['division'],
            pattern_name="Division Operation",
            max_matches=200  # More divisions expected
        )
        self.logger.info(f"Found {len(matches)} division operations")
        return matches
    
    def find_comparison_chains(self) -> List[Match]:
        """Find chains of if statements (rarity determination)."""
        self.logger.info("Searching for comparison chains")
        matches = self.find_custom_pattern(
            self.PATTERNS['comparison_chain'],
            pattern_name="Comparison Chain"
        )
        self.logger.info(f"Found {len(matches)} comparison chains")
        return matches
    
    def find_custom_pattern(self, regex: str, context_lines: int = 10,
                           pattern_name: str = "Custom Pattern",
                           max_matches: int = 100) -> List[Match]:
        """Search for custom regex pattern."""
        self._load_file()
        matches = []
        
        try:
            pattern = re.compile(regex, re.MULTILINE | re.DOTALL)
            
            for line_num, line in enumerate(self._file_lines):
                if len(matches) >= max_matches:
                    self.logger.warning(f"Reached max matches ({max_matches}) for {pattern_name}")
                    break
                
                match = pattern.search(line)
                if match:
                    # Get context
                    start_line = max(0, line_num - context_lines)
                    end_line = min(len(self._file_lines), line_num + context_lines + 1)
                    
                    context_before = self._file_lines[start_line:line_num]
                    context_after = self._file_lines[line_num + 1:end_line]
                    full_context = ''.join(self._file_lines[start_line:end_line])
                    
                    matches.append(Match(
                        pattern_name=pattern_name,
                        line_number=line_num + 1,
                        matched_text=match.group(0),
                        context_before=context_before,
                        context_after=context_after,
                        full_context=full_context
                    ))
        
        except Exception as e:
            self.logger.error(f"Error searching for pattern {pattern_name}: {e}")
        
        return matches
    
    def find_constants(self, min_value: int = 1000) -> List[Match]:
        """Find large numeric constants."""
        self.logger.info(f"Searching for constants >= {min_value}")
        matches = self.find_custom_pattern(
            self.PATTERNS['large_constant'],
            pattern_name="Large Constant"
        )
        
        # Filter by value
        filtered = []
        for match in matches:
            try:
                value = int(match.matched_text)
                if value >= min_value:
                    filtered.append(match)
            except ValueError:
                continue
        
        self.logger.info(f"Found {len(filtered)} large constants")
        return filtered
    
    def find_all_patterns(self, max_matches_per_pattern: int = 100) -> Dict[str, List[Match]]:
        """Find all predefined patterns."""
        self.logger.section("Searching for All Patterns")
        
        results = {
            'pcg_algorithm': self.find_pcg_algorithm(),
            'drop_tables': self.find_drop_tables(),
            'divisions': self.find_division_operations(),
            'comparison_chains': self.find_comparison_chains(),
            'large_constants': self.find_constants()
        }
        
        total_matches = sum(len(matches) for matches in results.values())
        self.logger.info(f"Total matches found: {total_matches}")
        
        return results
