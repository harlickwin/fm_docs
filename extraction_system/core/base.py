"""Base classes and data structures for the extraction system."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional, Tuple


class ConfidenceLevel(Enum):
    """Confidence level for extracted mechanics."""
    HIGH = "High"      # ARM code found and verified
    MEDIUM = "Medium"  # IL2CPP structure found, ARM not verified
    LOW = "Low"        # Inferred from patterns only
    UNKNOWN = "Unknown"  # Not yet analyzed


@dataclass
class MethodInfo:
    """Information about a method from IL2CPP dump."""
    name: str
    class_name: str
    rva_address: str  # e.g., "0x5AF7094"
    return_type: str
    parameters: List[str] = field(default_factory=list)
    attributes: List[str] = field(default_factory=list)


@dataclass
class ClassInfo:
    """Information about a class from IL2CPP dump."""
    name: str
    base_class: str
    methods: List[MethodInfo] = field(default_factory=list)
    fields: List[Dict[str, Any]] = field(default_factory=list)
    properties: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class FunctionCode:
    """Extracted function code from Ghidra."""
    name: str
    line_number: int
    code: str
    signature: str
    constants: Dict[str, List[Any]] = field(default_factory=dict)


@dataclass
class GameMechanic:
    """Base class for all game mechanics."""
    name: str
    category: str  # Combat, Summoning, PvP, Progression, Economy
    description: str
    formula: Optional[str] = None
    data_structures: List[str] = field(default_factory=list)
    arm_code_location: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.UNKNOWN
    examples: List[Dict[str, Any]] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class ExtractionProgress:
    """Track extraction progress."""
    total_systems: int = 0
    completed_systems: int = 0
    current_system: Optional[str] = None
    errors: List[str] = field(default_factory=list)
    start_time: Optional[float] = None
    last_checkpoint: Optional[float] = None
