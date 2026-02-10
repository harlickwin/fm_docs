"""Logging system with progress indicators."""

import logging
import sys
from pathlib import Path
from typing import Optional


class ProgressLogger:
    """Logger with progress tracking capabilities."""
    
    def __init__(self, name: str, log_file: Optional[str] = None, level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level))
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, level))
        console_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        
        # File handler
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_format = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(file_format)
            self.logger.addHandler(file_handler)
    
    def info(self, message: str):
        """Log info message."""
        self.logger.info(message)
    
    def debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)
    
    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)
    
    def error(self, message: str):
        """Log error message."""
        self.logger.error(message)
    
    def progress(self, current: int, total: int, message: str = ""):
        """Log progress indicator."""
        percentage = (current / total * 100) if total > 0 else 0
        progress_msg = f"Progress: {current}/{total} ({percentage:.1f}%) {message}"
        self.info(progress_msg)
    
    def section(self, title: str):
        """Log section header."""
        separator = "=" * 80
        self.info(separator)
        self.info(title)
        self.info(separator)
