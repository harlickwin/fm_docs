"""IL2CPP dump parser."""

import re
import mmap
from pathlib import Path
from typing import Dict, List, Optional
from extraction_system.core.base import MethodInfo, ClassInfo
from extraction_system.core.logger import ProgressLogger


class IL2CPPParser:
    """Parser for IL2CPP dump files."""
    
    def __init__(self, dump_file_path: str, logger: Optional[ProgressLogger] = None):
        self.dump_file = Path(dump_file_path)
        self.logger = logger or ProgressLogger("IL2CPPParser")
        self.classes: Dict[str, ClassInfo] = {}
        self.methods: Dict[str, MethodInfo] = {}
        self.addresses: Dict[str, str] = {}  # RVA -> method_name
        
    def parse(self) -> Dict[str, ClassInfo]:
        """Parse IL2CPP dump and extract all metadata."""
        self.logger.section("Parsing IL2CPP Dump")
        
        if not self.dump_file.exists():
            self.logger.error(f"IL2CPP dump file not found: {self.dump_file}")
            return {}
        
        try:
            # Use memory-mapped file for large files
            file_size = self.dump_file.stat().st_size
            self.logger.info(f"IL2CPP dump size: {file_size / (1024*1024):.2f} MB")
            
            with open(self.dump_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            self._parse_classes(content)
            self.logger.info(f"Parsed {len(self.classes)} classes")
            self.logger.info(f"Extracted {len(self.methods)} methods")
            self.logger.info(f"Found {len(self.addresses)} RVA addresses")
            
            return self.classes
            
        except Exception as e:
            self.logger.error(f"Error parsing IL2CPP dump: {e}")
            return {}
    
    def _parse_classes(self, content: str):
        """Parse class definitions from IL2CPP dump."""
        # Pattern to match class definitions
        class_pattern = r'(?:public\s+)?(?:abstract\s+)?class\s+(\w+)(?:\s*:\s*(\w+))?'
        
        # Pattern to match RVA comments
        rva_pattern = r'//\s*RVA:\s*(0x[0-9A-Fa-f]+)'
        
        # Pattern to match method signatures
        method_pattern = r'(?:public|private|protected)?\s*(?:static\s+)?(?:virtual\s+)?(\w+(?:<[^>]+>)?)\s+(\w+)\s*\('
        
        lines = content.split('\n')
        current_class = None
        
        for i, line in enumerate(lines):
            # Check for class definition
            class_match = re.search(class_pattern, line)
            if class_match:
                class_name = class_match.group(1)
                base_class = class_match.group(2) or "object"
                current_class = ClassInfo(name=class_name, base_class=base_class)
                self.classes[class_name] = current_class
                continue
            
            # Check for RVA address
            rva_match = re.search(rva_pattern, line)
            if rva_match and current_class:
                rva_address = rva_match.group(1)
                
                # Look ahead for method signature
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    method_match = re.search(method_pattern, next_line)
                    if method_match:
                        return_type = method_match.group(1)
                        method_name = method_match.group(2)
                        
                        full_method_name = f"{current_class.name}.{method_name}"
                        
                        method_info = MethodInfo(
                            name=method_name,
                            class_name=current_class.name,
                            rva_address=rva_address,
                            return_type=return_type
                        )
                        
                        current_class.methods.append(method_info)
                        self.methods[full_method_name] = method_info
                        self.addresses[rva_address] = full_method_name
    
    def get_methods_with_addresses(self) -> Dict[str, str]:
        """Return mapping of method_name -> RVA_address."""
        return {name: method.rva_address for name, method in self.methods.items()}
    
    def get_class_structure(self, class_name: str) -> Optional[ClassInfo]:
        """Get complete structure for a specific class."""
        return self.classes.get(class_name)
    
    def find_methods_by_pattern(self, pattern: str) -> List[MethodInfo]:
        """Find methods matching a name pattern."""
        regex = re.compile(pattern, re.IGNORECASE)
        return [method for name, method in self.methods.items() if regex.search(name)]
