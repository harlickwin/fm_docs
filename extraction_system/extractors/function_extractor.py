"""Function extractor for Ghidra exports."""

import re
from pathlib import Path
from typing import Dict, List, Optional
from extraction_system.core.base import FunctionCode
from extraction_system.core.logger import ProgressLogger


class FunctionExtractor:
    """Extracts complete function implementations from Ghidra export."""
    
    def __init__(self, ghidra_file: str, logger: Optional[ProgressLogger] = None):
        self.ghidra_file = Path(ghidra_file)
        self.logger = logger or ProgressLogger("FunctionExtractor")
        self.function_cache: Dict[str, FunctionCode] = {}
        self._file_content: Optional[str] = None
    
    def _load_file(self):
        """Load Ghidra file into memory."""
        if self._file_content is None:
            self.logger.info(f"Loading Ghidra export: {self.ghidra_file}")
            with open(self.ghidra_file, 'r', encoding='utf-8', errors='ignore') as f:
                self._file_content = f.read()
            file_size = len(self._file_content) / (1024 * 1024)
            self.logger.info(f"Loaded {file_size:.2f} MB")
    
    def extract_function(self, func_name: str) -> Optional[FunctionCode]:
        """Extract complete function implementation."""
        # Check cache first
        if func_name in self.function_cache:
            return self.function_cache[func_name]
        
        self._load_file()
        
        try:
            # Find function definition
            # Pattern: undefined8 FUN_05af7094(...)
            pattern = rf'\w+\s+{re.escape(func_name)}\s*\([^)]*\)'
            match = re.search(pattern, self._file_content)
            
            if not match:
                self.logger.debug(f"Function not found: {func_name}")
                return None
            
            # Find the start position
            start_pos = match.start()
            
            # Find line number
            line_number = self._file_content[:start_pos].count('\n') + 1
            
            # Extract signature
            signature = match.group(0)
            
            # Find opening brace
            brace_start = self._file_content.find('{', start_pos)
            if brace_start == -1:
                return None
            
            # Find matching closing brace
            brace_count = 1
            pos = brace_start + 1
            while pos < len(self._file_content) and brace_count > 0:
                if self._file_content[pos] == '{':
                    brace_count += 1
                elif self._file_content[pos] == '}':
                    brace_count -= 1
                pos += 1
            
            if brace_count != 0:
                self.logger.warning(f"Unmatched braces for {func_name}")
                return None
            
            # Extract complete function code
            code = self._file_content[start_pos:pos]
            
            # Extract constants
            constants = self._extract_constants(code)
            
            func_code = FunctionCode(
                name=func_name,
                line_number=line_number,
                code=code,
                signature=signature,
                constants=constants
            )
            
            # Cache it
            self.function_cache[func_name] = func_code
            
            return func_code
            
        except Exception as e:
            self.logger.error(f"Error extracting function {func_name}: {e}")
            return None
    
    def extract_with_context(self, func_name: str, context_lines: int = 10) -> Optional[FunctionCode]:
        """Extract function with surrounding context."""
        func_code = self.extract_function(func_name)
        if not func_code:
            return None
        
        # Add context lines before and after
        lines = self._file_content.split('\n')
        start_line = max(0, func_code.line_number - context_lines - 1)
        end_line = min(len(lines), func_code.line_number + func_code.code.count('\n') + context_lines)
        
        context_code = '\n'.join(lines[start_line:end_line])
        
        return FunctionCode(
            name=func_code.name,
            line_number=start_line + 1,
            code=context_code,
            signature=func_code.signature,
            constants=func_code.constants
        )
    
    def _extract_constants(self, code: str) -> Dict[str, List]:
        """Extract numeric constants from function code."""
        constants = {
            'integers': [],
            'floats': [],
            'hex_values': [],
            'large_numbers': []
        }
        
        # Extract hex values
        hex_pattern = r'0x[0-9A-Fa-f]+'
        constants['hex_values'] = list(set(re.findall(hex_pattern, code)))
        
        # Extract floats
        float_pattern = r'\b\d+\.\d+[fF]?\b'
        floats = [float(x.rstrip('fF')) for x in re.findall(float_pattern, code)]
        constants['floats'] = list(set(floats))
        
        # Extract integers (excluding hex)
        int_pattern = r'\b\d+\b'
        integers = []
        for match in re.finditer(int_pattern, code):
            # Skip if it's part of a float
            if match.start() > 0 and code[match.start()-1] == '.':
                continue
            if match.end() < len(code) and code[match.end()] == '.':
                continue
            integers.append(int(match.group()))
        
        constants['integers'] = list(set(integers))
        
        # Identify large numbers (potential seeds/multipliers)
        constants['large_numbers'] = [x for x in constants['integers'] if x > 1000]
        
        return constants
    
    def extract_multiple(self, func_names: List[str]) -> Dict[str, Optional[FunctionCode]]:
        """Extract multiple functions."""
        self.logger.info(f"Extracting {len(func_names)} functions")
        results = {}
        
        for i, func_name in enumerate(func_names):
            results[func_name] = self.extract_function(func_name)
            
            if (i + 1) % 100 == 0:
                self.logger.progress(i + 1, len(func_names), "functions extracted")
        
        return results
