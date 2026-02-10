"""
Mechanics Cleanup Extraction System

This module extracts missing game mechanics from the IL2CPP dump and updates
the GitHub Pages documentation with code-verified information.

Core Principle: VERIFY EVERYTHING. ASSUME NOTHING. HALLUCINATE NOTHING.
"""

__version__ = "1.0.0"

# Import main classes for easy access
from extraction_system.mechanics_cleanup.code_extractor import (
    CodeExtractor,
    ClassMatch,
    ConfigMatch,
    MethodMatch,
    FormulaExtraction
)

from extraction_system.mechanics_cleanup.code_verifier import (
    CodeVerifier,
    ConfidenceLevel,
    Formula,
    Extraction,
    VerificationException
)

from extraction_system.mechanics_cleanup.knowledge_gap_tracker import (
    KnowledgeGapTracker,
    KnowledgeGap,
    GapPriority,
    get_tracker,
    init_tracker
)

from extraction_system.mechanics_cleanup.logger import (
    MechanicsCleanupLogger,
    get_logger,
    init_logger
)

from extraction_system.mechanics_cleanup.error_handler import (
    ErrorHandler,
    ErrorSeverity,
    ExtractionError,
    MechanicsCleanupException,
    CodeExtractionException
)

from extraction_system.mechanics_cleanup.config import Config

__all__ = [
    # Code Extraction
    'CodeExtractor',
    'ClassMatch',
    'ConfigMatch',
    'MethodMatch',
    'FormulaExtraction',
    
    # Code Verification
    'CodeVerifier',
    'ConfidenceLevel',
    'Formula',
    'Extraction',
    'VerificationException',
    
    # Knowledge Gap Tracking
    'KnowledgeGapTracker',
    'KnowledgeGap',
    'GapPriority',
    'get_tracker',
    'init_tracker',
    
    # Logging
    'MechanicsCleanupLogger',
    'get_logger',
    'init_logger',
    
    # Error Handling
    'ErrorHandler',
    'ErrorSeverity',
    'ExtractionError',
    'MechanicsCleanupException',
    'CodeExtractionException',
    
    # Configuration
    'Config',
]
