"""Address mapper for IL2CPP RVA to Ghidra function names."""

import json
from pathlib import Path
from typing import Dict, Optional
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.core.logger import ProgressLogger


class AddressMapper:
    """Maps IL2CPP RVA addresses to Ghidra function names."""
    
    def __init__(self, il2cpp_parser: IL2CPPParser, ghidra_file: str, 
                 logger: Optional[ProgressLogger] = None):
        self.il2cpp = il2cpp_parser
        self.ghidra_file = Path(ghidra_file)
        self.logger = logger or ProgressLogger("AddressMapper")
        self.address_map: Dict[str, str] = {}  # RVA -> Ghidra function name
        self.reverse_map: Dict[str, str] = {}  # Ghidra function name -> IL2CPP method
    
    def build_mapping(self) -> Dict[str, str]:
        """Build complete address mapping."""
        self.logger.section("Building Address Mapping")
        
        methods_with_addresses = self.il2cpp.get_methods_with_addresses()
        total = len(methods_with_addresses)
        
        for i, (method_name, rva) in enumerate(methods_with_addresses.items()):
            ghidra_name = self.rva_to_ghidra_name(rva)
            self.address_map[rva] = ghidra_name
            self.reverse_map[ghidra_name] = method_name
            
            if (i + 1) % 1000 == 0:
                self.logger.progress(i + 1, total, "addresses mapped")
        
        self.logger.info(f"Built mapping for {len(self.address_map)} addresses")
        return self.address_map
    
    def rva_to_ghidra_name(self, rva: str) -> str:
        """Convert RVA address to Ghidra function name.
        
        Example: 0x5AF7094 -> FUN_05af7094
        """
        # Remove 0x prefix
        hex_addr = rva.replace('0x', '').lower()
        
        # Pad to 8 characters
        hex_addr = hex_addr.zfill(8)
        
        # Format as Ghidra function name
        return f"FUN_{hex_addr}"
    
    def get_il2cpp_name(self, ghidra_func: str) -> Optional[str]:
        """Get IL2CPP method name for Ghidra function."""
        return self.reverse_map.get(ghidra_func)
    
    def save_mapping(self, output_file: str):
        """Save mapping to file for reuse."""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        mapping_data = {
            'address_map': self.address_map,
            'reverse_map': self.reverse_map
        }
        
        with open(output_path, 'w') as f:
            json.dump(mapping_data, f, indent=2)
        
        self.logger.info(f"Saved address mapping to {output_file}")
    
    def load_mapping(self, input_file: str):
        """Load previously saved mapping."""
        input_path = Path(input_file)
        
        if not input_path.exists():
            self.logger.warning(f"Mapping file not found: {input_file}")
            return
        
        with open(input_path, 'r') as f:
            mapping_data = json.load(f)
        
        self.address_map = mapping_data.get('address_map', {})
        self.reverse_map = mapping_data.get('reverse_map', {})
        
        self.logger.info(f"Loaded {len(self.address_map)} address mappings from {input_file}")
