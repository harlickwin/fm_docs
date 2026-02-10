"""
Configuration for mechanics cleanup extraction.

Defines paths, search patterns, and extraction settings.
"""

from pathlib import Path
from typing import Dict, List


class Config:
    """Configuration for mechanics cleanup extraction."""
    
    # File paths
    DUMP_PATH = Path(r"C:\apktool\il2cpp-output\dump.cs")
    DOCS_PATH = Path("docs")
    INDEX_HTML = DOCS_PATH / "index.html"
    WAR_PVP_HTML = DOCS_PATH / "war-pvp.html"
    OUTPUT_DIR = Path("extraction_system/mechanics_cleanup/output")
    KNOWLEDGE_GAPS_FILE = Path("KNOWLEDGE_GAPS.md")
    
    # Logging
    LOG_DIR = Path("extraction_system/logs")
    LOG_LEVEL = "INFO"
    
    # Search patterns for different mechanics
    SEARCH_PATTERNS: Dict[str, List[str]] = {
        "guild_war": [
            r"class GuildWar.*Config",
            r"class GuildTier.*",
            r"class.*War.*Match.*",
            r"WarPoints",
            r"GuildTier\s*{",
        ],
        "dungeon": [
            r"class Dungeon.*Config",
            r"DifficultyMultiplier",
            r"DungeonLevel",
            r"class.*Dungeon.*Reward",
        ],
        "pvp": [
            r"class Pvp.*Config",
            r"class.*League.*Config",
            r"PromotionEnd",
            r"DemotionStart",
            r"PvpMatchmaking",
        ],
        "shop": [
            r"class ShopRefreshConfig",
            r"class PlayerShopModel",
            r"class ShopItem.*",
            r"ShopSeed",
        ],
        "rng_drops": [
            r"class.*DropChance.*Config",
            r"class.*Summon.*Config",
            r"RandomSeed",
            r"DungeonDrop",
        ],
        "combat": [
            r"class AttacksSystem",
            r"class UnitEntity",
            r"class WeaponInfo",
            r"DamageCalculation",
        ],
        "stats": [
            r"AttackSpeedMulti",
            r"CriticalHit",
            r"Dodge",
            r"Block",
            r"LifeSteal",
        ],
    }
    
    # Confidence level thresholds
    CONFIDENCE_LEVELS = {
        "HIGH": "Fully verified from code with all values present",
        "MEDIUM": "Logic verified but some config values not found",
        "LOW": "Partial code found, significant gaps in understanding",
        "UNVERIFIED": "No code evidence found, cannot validate claim"
    }
    
    # HTML template settings
    HTML_ENCODING = "utf-8"
    PRESERVE_FORMATTING = True
    
    # Extraction settings
    MAX_CONTEXT_LINES = 10  # Lines of context to extract around matches
    MAX_SEARCH_RESULTS = 100  # Maximum number of search results per pattern
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate configuration settings.
        
        Returns:
            True if configuration is valid, False otherwise
        """
        # Check if dump.cs exists
        if not cls.DUMP_PATH.exists():
            print(f"ERROR: dump.cs not found at {cls.DUMP_PATH}")
            print("Please ensure the IL2CPP dump is available at the specified path.")
            return False
        
        # Check if docs directory exists
        if not cls.DOCS_PATH.exists():
            print(f"ERROR: docs directory not found at {cls.DOCS_PATH}")
            return False
        
        # Create output directory if it doesn't exist
        cls.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
        # Create log directory if it doesn't exist
        cls.LOG_DIR.mkdir(parents=True, exist_ok=True)
        
        return True
    
    @classmethod
    def get_search_patterns(cls, category: str) -> List[str]:
        """
        Get search patterns for a specific category.
        
        Args:
            category: Category name
            
        Returns:
            List of regex patterns
        """
        return cls.SEARCH_PATTERNS.get(category, [])
    
    @classmethod
    def get_all_categories(cls) -> List[str]:
        """
        Get all available categories.
        
        Returns:
            List of category names
        """
        return list(cls.SEARCH_PATTERNS.keys())
