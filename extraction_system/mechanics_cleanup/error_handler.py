"""
Error handling for mechanics cleanup extraction.

Provides custom exceptions and error handling utilities following the
zero-hallucination policy: when in doubt, mark as unverified.
"""

from typing import Optional, List
from dataclasses import dataclass
from enum import Enum


class ErrorSeverity(Enum):
    """Severity levels for extraction errors."""
    LOW = "low"  # Minor issue, extraction can continue
    MEDIUM = "medium"  # Significant issue, affects confidence level
    HIGH = "high"  # Critical issue, extraction cannot proceed
    CRITICAL = "critical"  # System-level failure


@dataclass
class ExtractionError:
    """Represents an error during extraction."""
    severity: ErrorSeverity
    category: str  # "extraction", "verification", "documentation", "system"
    message: str
    context: Optional[str] = None
    line_number: Optional[int] = None
    class_name: Optional[str] = None
    suggested_action: Optional[str] = None


class MechanicsCleanupException(Exception):
    """Base exception for mechanics cleanup operations."""
    
    def __init__(self, message: str, error: Optional[ExtractionError] = None):
        super().__init__(message)
        self.error = error


class CodeExtractionException(MechanicsCleanupException):
    """Exception raised during code extraction."""
    pass


class VerificationException(MechanicsCleanupException):
    """Exception raised during verification."""
    pass


class DocumentationException(MechanicsCleanupException):
    """Exception raised during documentation generation."""
    pass


class HTMLUpdateException(MechanicsCleanupException):
    """Exception raised during HTML update operations."""
    pass


class ConfigurationException(MechanicsCleanupException):
    """Exception raised for configuration errors."""
    pass


class ErrorHandler:
    """Handles errors during extraction with zero-hallucination policy."""
    
    def __init__(self):
        """Initialize error handler."""
        self.errors: List[ExtractionError] = []
        self.warnings: List[ExtractionError] = []
    
    def add_error(self, error: ExtractionError) -> None:
        """
        Add an error to the error list.
        
        Args:
            error: ExtractionError instance
        """
        if error.severity in [ErrorSeverity.HIGH, ErrorSeverity.CRITICAL]:
            self.errors.append(error)
        else:
            self.warnings.append(error)
    
    def handle_class_not_found(
        self,
        class_name: str,
        search_location: str,
        patterns_used: List[str]
    ) -> ExtractionError:
        """
        Handle case where a class is not found in dump.cs.
        
        Following zero-hallucination policy: mark as unverified, don't guess.
        
        Args:
            class_name: Name of the class that wasn't found
            search_location: Where the search was performed
            patterns_used: List of search patterns attempted
            
        Returns:
            ExtractionError with details
        """
        error = ExtractionError(
            severity=ErrorSeverity.MEDIUM,
            category="extraction",
            message=f"Class '{class_name}' not found in {search_location}",
            context=f"Searched patterns: {', '.join(patterns_used)}",
            class_name=class_name,
            suggested_action=(
                "Mark mechanic as UNVERIFIED. This mechanic may not exist, "
                "may use different naming, or may be in native ARM code."
            )
        )
        self.add_error(error)
        return error
    
    def handle_multiple_matches(
        self,
        pattern: str,
        matches: List[tuple],
        search_location: str
    ) -> ExtractionError:
        """
        Handle case where multiple matches are found for a pattern.
        
        Following zero-hallucination policy: extract all, don't choose arbitrarily.
        
        Args:
            pattern: Search pattern used
            matches: List of (class_name, line_number) tuples
            search_location: Where the search was performed
            
        Returns:
            ExtractionError with details
        """
        match_details = ", ".join([f"{name} (line {line})" for name, line in matches])
        error = ExtractionError(
            severity=ErrorSeverity.LOW,
            category="extraction",
            message=f"Multiple matches found for pattern '{pattern}'",
            context=f"Matches: {match_details} in {search_location}",
            suggested_action=(
                "Extract all matches. Manual review required to determine "
                "which is the correct class or if all are relevant."
            )
        )
        self.add_error(error)
        return error
    
    def handle_partial_match(
        self,
        expected: str,
        found: str,
        line_number: int,
        search_location: str
    ) -> ExtractionError:
        """
        Handle case where a similar but not exact match is found.
        
        Following zero-hallucination policy: mark as LOW confidence, explain difference.
        
        Args:
            expected: Expected class/method name
            found: Actual class/method name found
            line_number: Line number where found
            search_location: Where the search was performed
            
        Returns:
            ExtractionError with details
        """
        error = ExtractionError(
            severity=ErrorSeverity.MEDIUM,
            category="extraction",
            message=f"Partial match: expected '{expected}', found '{found}'",
            context=f"Line {line_number} in {search_location}",
            line_number=line_number,
            class_name=found,
            suggested_action=(
                "Mark confidence as LOW. Document what was found vs what was expected. "
                "May be related but cannot confirm without further analysis."
            )
        )
        self.add_error(error)
        return error
    
    def handle_complex_formula(
        self,
        method_name: str,
        line_number: int,
        reason: str
    ) -> ExtractionError:
        """
        Handle case where formula extraction is complex or ambiguous.
        
        Following zero-hallucination policy: show full code, don't simplify.
        
        Args:
            method_name: Name of the method containing the formula
            line_number: Line number of the method
            reason: Reason why formula is complex
            
        Returns:
            ExtractionError with details
        """
        error = ExtractionError(
            severity=ErrorSeverity.LOW,
            category="verification",
            message=f"Complex formula in {method_name}",
            context=reason,
            line_number=line_number,
            suggested_action=(
                "Mark confidence as LOW. Extract entire method body. "
                "Do NOT simplify or interpret. Show actual code and let users interpret."
            )
        )
        self.add_error(error)
        return error
    
    def handle_missing_config_value(
        self,
        config_class: str,
        value_name: str,
        referenced_in: str,
        line_number: int
    ) -> ExtractionError:
        """
        Handle case where a formula references config values not in dump.cs.
        
        Following zero-hallucination policy: mark missing explicitly, set confidence to MEDIUM.
        
        Args:
            config_class: Name of the config class
            value_name: Name of the missing value
            referenced_in: Where the value is referenced
            line_number: Line number of the reference
            
        Returns:
            ExtractionError with details
        """
        error = ExtractionError(
            severity=ErrorSeverity.MEDIUM,
            category="verification",
            message=f"Missing config value: {config_class}.{value_name}",
            context=f"Referenced in {referenced_in} at line {line_number}",
            line_number=line_number,
            class_name=config_class,
            suggested_action=(
                "Mark confidence as MEDIUM. Document that formula structure is verified "
                "but actual value is unknown. Cannot calculate without this value."
            )
        )
        self.add_error(error)
        return error
    
    def handle_external_source_conflict(
        self,
        external_claim: str,
        code_shows: str,
        source: str
    ) -> ExtractionError:
        """
        Handle case where external source conflicts with code.
        
        Following zero-hallucination policy: ignore external source, document only code.
        
        Args:
            external_claim: What external source claims
            code_shows: What the code actually shows
            source: Source of external claim
            
        Returns:
            ExtractionError with details
        """
        error = ExtractionError(
            severity=ErrorSeverity.LOW,
            category="verification",
            message=f"External source conflict: {source}",
            context=f"External claims: {external_claim}, Code shows: {code_shows}",
            suggested_action=(
                "IGNORE external source. Document only code-verified behavior. "
                "Add note explaining the discrepancy."
            )
        )
        self.add_error(error)
        return error
    
    def handle_file_not_found(
        self,
        file_path: str,
        operation: str
    ) -> ExtractionError:
        """
        Handle file not found errors.
        
        Args:
            file_path: Path to the missing file
            operation: Operation that failed
            
        Returns:
            ExtractionError with details
        """
        error = ExtractionError(
            severity=ErrorSeverity.CRITICAL,
            category="system",
            message=f"File not found: {file_path}",
            context=f"Operation: {operation}",
            suggested_action="Verify file path and ensure file exists before proceeding."
        )
        self.add_error(error)
        return error
    
    def get_error_summary(self) -> dict:
        """
        Get summary of all errors and warnings.
        
        Returns:
            Dictionary with error statistics
        """
        return {
            "total_errors": len(self.errors),
            "total_warnings": len(self.warnings),
            "critical": len([e for e in self.errors if e.severity == ErrorSeverity.CRITICAL]),
            "high": len([e for e in self.errors if e.severity == ErrorSeverity.HIGH]),
            "medium": len([e for e in self.errors + self.warnings if e.severity == ErrorSeverity.MEDIUM]),
            "low": len([e for e in self.warnings if e.severity == ErrorSeverity.LOW]),
            "errors": self.errors,
            "warnings": self.warnings
        }
    
    def has_critical_errors(self) -> bool:
        """Check if there are any critical errors."""
        return any(e.severity == ErrorSeverity.CRITICAL for e in self.errors)
    
    def clear(self) -> None:
        """Clear all errors and warnings."""
        self.errors.clear()
        self.warnings.clear()
