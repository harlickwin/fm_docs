"""
Logging configuration for mechanics cleanup extraction.

Provides structured logging with different levels for extraction operations,
verification steps, and knowledge gap tracking.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional


class MechanicsCleanupLogger:
    """Logger for mechanics cleanup extraction operations."""
    
    def __init__(self, log_dir: str = "extraction_system/logs", log_level: int = logging.INFO):
        """
        Initialize logger with file and console handlers.
        
        Args:
            log_dir: Directory to store log files
            log_level: Logging level (default: INFO)
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Create logger
        self.logger = logging.getLogger("mechanics_cleanup")
        self.logger.setLevel(log_level)
        
        # Prevent duplicate handlers
        if self.logger.handlers:
            self.logger.handlers.clear()
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        
        # File handler - detailed logs
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.log_dir / f"mechanics_cleanup_{timestamp}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        
        # Console handler - important messages only
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"Logging initialized. Log file: {log_file}")
    
    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(message)
    
    def error(self, message: str, exc_info: bool = False) -> None:
        """Log error message."""
        self.logger.error(message, exc_info=exc_info)
    
    def critical(self, message: str, exc_info: bool = False) -> None:
        """Log critical message."""
        self.logger.critical(message, exc_info=exc_info)
    
    def extraction_start(self, category: str) -> None:
        """Log start of extraction for a category."""
        self.logger.info(f"=" * 60)
        self.logger.info(f"Starting extraction: {category}")
        self.logger.info(f"=" * 60)
    
    def extraction_complete(self, category: str, found: int, missing: int) -> None:
        """Log completion of extraction for a category."""
        self.logger.info(f"Extraction complete: {category}")
        self.logger.info(f"  Found: {found} items")
        self.logger.info(f"  Missing: {missing} items")
        self.logger.info(f"=" * 60)
    
    def search_pattern(self, pattern: str, location: str) -> None:
        """Log search pattern being used."""
        self.logger.debug(f"Searching pattern: {pattern} in {location}")
    
    def match_found(self, pattern: str, line_number: int, class_name: str) -> None:
        """Log when a match is found."""
        self.logger.info(f"✓ Match found: {class_name} at line {line_number} (pattern: {pattern})")
    
    def no_match(self, pattern: str, location: str) -> None:
        """Log when no match is found."""
        self.logger.warning(f"✗ No match: pattern '{pattern}' in {location}")
    
    def confidence_assessment(self, mechanic: str, level: str, reason: str) -> None:
        """Log confidence level assessment."""
        self.logger.info(f"Confidence [{mechanic}]: {level} - {reason}")
    
    def knowledge_gap(self, category: str, title: str, priority: str) -> None:
        """Log knowledge gap identification."""
        self.logger.warning(f"Knowledge Gap [{priority}] {category}: {title}")
    
    def verification_result(self, item: str, verified: bool, reason: str = "") -> None:
        """Log verification result."""
        status = "✓ VERIFIED" if verified else "✗ UNVERIFIED"
        msg = f"{status}: {item}"
        if reason:
            msg += f" - {reason}"
        
        if verified:
            self.logger.info(msg)
        else:
            self.logger.warning(msg)


# Global logger instance
_logger: Optional[MechanicsCleanupLogger] = None


def get_logger() -> MechanicsCleanupLogger:
    """Get or create the global logger instance."""
    global _logger
    if _logger is None:
        _logger = MechanicsCleanupLogger()
    return _logger


def init_logger(log_dir: str = "extraction_system/logs", log_level: int = logging.INFO) -> MechanicsCleanupLogger:
    """
    Initialize the global logger with custom settings.
    
    Args:
        log_dir: Directory to store log files
        log_level: Logging level
        
    Returns:
        Initialized logger instance
    """
    global _logger
    _logger = MechanicsCleanupLogger(log_dir, log_level)
    return _logger
