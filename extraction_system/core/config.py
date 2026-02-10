"""Configuration management."""

import yaml
from pathlib import Path
from typing import Any, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class ExtractionConfig:
    """Configuration for extraction pipeline."""
    # Input files
    il2cpp_dump_path: str
    ghidra_export_path: str
    config_file_path: Optional[str] = None
    
    # Output files
    output_manual_path: str = "COMPLETE_GAME_MECHANICS_MANUAL.md"
    checkpoint_path: str = "extraction_system/checkpoints/progress.json"
    address_mapping_path: str = "extraction_system/cache/address_mapping.json"
    il2cpp_cache_path: str = "extraction_system/cache/il2cpp_parsed.json"
    
    # Processing options
    use_cache: bool = True
    parallel_processing: bool = True
    max_workers: int = 4
    
    # Pattern search options
    context_lines: int = 10
    max_matches_per_pattern: int = 100
    
    # Verification options
    run_verification: bool = True
    verification_strictness: str = "medium"
    
    # Output options
    include_code_evidence: bool = True
    include_optimization_strategies: bool = True
    generate_json_export: bool = True
    generate_csv_export: bool = True
    
    # Priority systems
    priority_systems: list = field(default_factory=lambda: [
        "Combat", "Summoning", "PvP", "Progression", "Economy"
    ])
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "extraction_system/logs/extraction.log"
    
    @classmethod
    def from_yaml(cls, config_path: str) -> 'ExtractionConfig':
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            config_dict = yaml.safe_load(f)
        return cls(**config_dict)
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'ExtractionConfig':
        """Create configuration from dictionary."""
        return cls(**config_dict)
