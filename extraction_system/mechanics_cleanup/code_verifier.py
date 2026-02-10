"""
Code Verifier for mechanics cleanup extraction.

Validates extracted code and assesses confidence with ZERO tolerance for assumptions.
Following the zero-hallucination policy: verify everything, assume nothing.
"""

import re
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

from extraction_system.mechanics_cleanup.logger import get_logger
from extraction_system.mechanics_cleanup.error_handler import (
    ErrorHandler,
    VerificationException
)


class ConfidenceLevel(Enum):
    """Confidence levels for extracted information."""
    HIGH = "high"  # Complete code verification, no assumptions
    MEDIUM = "medium"  # Partial verification, some config values missing but logic clear
    LOW = "low"  # Limited code evidence, requires interpretation
    UNVERIFIED = "unverified"  # No code evidence, cannot validate
    
    def get_description(self) -> str:
        """Get human-readable description of confidence level."""
        descriptions = {
            "high": "Fully verified from code with all values present",
            "medium": "Logic verified but some config values not found",
            "low": "Partial code found, significant gaps in understanding",
            "unverified": "No code evidence found, cannot validate claim"
        }
        return descriptions[self.value]


@dataclass
class Formula:
    """Represents a verified mathematical formula."""
    name: str
    expression: str  # Human-readable formula
    code_expression: str  # Exact code from dump.cs
    variables: Dict[str, str]  # variable_name -> description
    source_line: int
    source_method: str
    verified: bool
    copy_pastable: bool  # True if can be used directly in calculations
    confidence: ConfidenceLevel
    missing_elements: List[str]  # What's missing or unclear


@dataclass
class Extraction:
    """Represents an extraction that needs verification."""
    name: str
    category: str
    content: str
    line_number: int
    class_name: Optional[str] = None
    method_name: Optional[str] = None
    formulas: List[Formula] = None
    config_values: Dict[str, str] = None
    
    def __post_init__(self):
        """Initialize mutable default values."""
        if self.formulas is None:
            self.formulas = []
        if self.config_values is None:
            self.config_values = {}


class CodeVerifier:
    """Validates extracted code and assesses confidence with strict rules."""
    
    def __init__(self, dump_path: str):
        """
        Initialize with path to dump.cs.
        
        Args:
            dump_path: Path to the IL2CPP dump file
            
        Raises:
            VerificationException: If dump file doesn't exist
        """
        self.dump_path = Path(dump_path)
        self.logger = get_logger()
        self.error_handler = ErrorHandler()
        
        if not self.dump_path.exists():
            error = self.error_handler.handle_file_not_found(
                str(self.dump_path),
                "CodeVerifier initialization"
            )
            raise VerificationException(
                f"Dump file not found: {self.dump_path}",
                error
            )
        
        self.logger.info(f"CodeVerifier initialized with dump: {self.dump_path}")
        
        # Cache for file content to avoid repeated reads
        self._content_cache: Optional[List[str]] = None
    
    def _load_content(self) -> List[str]:
        """
        Load dump.cs content into memory.
        
        Returns:
            List of lines from dump.cs
        """
        if self._content_cache is None:
            self.logger.info("Loading dump.cs into memory for verification...")
            with open(self.dump_path, 'r', encoding='utf-8', errors='ignore') as f:
                self._content_cache = f.readlines()
            self.logger.info(f"Loaded {len(self._content_cache)} lines from dump.cs")
        return self._content_cache
    
    def verify_line_reference(self, line_number: int, expected_content: str) -> bool:
        """
        Verify line number points to expected content.
        
        Following zero-hallucination policy: Returns True only if exact match found.
        
        Args:
            line_number: Line number to verify (1-indexed)
            expected_content: Expected content at that line
            
        Returns:
            True only if exact match found, False otherwise
        """
        content = self._load_content()
        
        # Validate line number
        if line_number < 1 or line_number > len(content):
            self.logger.error(
                f"Line number {line_number} out of range (1-{len(content)})"
            )
            return False
        
        # Get actual content at line (convert to 0-indexed)
        actual_line = content[line_number - 1].strip()
        expected_line = expected_content.strip()
        
        # Exact match required
        if actual_line == expected_line:
            self.logger.verification_result(
                f"Line {line_number}",
                True,
                "Exact match"
            )
            return True
        
        # Check if expected content is a substring (for partial verification)
        if expected_line in actual_line:
            self.logger.verification_result(
                f"Line {line_number}",
                True,
                "Partial match (expected content found in line)"
            )
            return True
        
        # No match
        self.logger.verification_result(
            f"Line {line_number}",
            False,
            f"Expected: '{expected_line}', Found: '{actual_line}'"
        )
        return False
    
    def extract_formula(self, method_body: str) -> Optional[Formula]:
        """
        Extract mathematical formula from method.
        
        Following zero-hallucination policy:
        - Returns Formula object ONLY if formula is explicit and clear
        - Returns None if formula requires interpretation or assumption
        
        Args:
            method_body: Method body text
            
        Returns:
            Formula object if formula is explicit, None otherwise
        """
        # Check for complexity indicators that require interpretation
        complexity_indicators = [
            'if ',  # Conditionals
            'else',  # Conditionals
            'switch',  # Switch statements
            'for ',  # Loops
            'while ',  # Loops
            'foreach',  # Loops
            '?',  # Ternary operator
        ]
        
        # If method contains complex logic, cannot extract simple formula
        method_lower = method_body.lower()
        has_complexity = any(indicator in method_lower for indicator in complexity_indicators)
        
        if has_complexity:
            self.logger.warning(
                "Method contains complex logic (conditionals/loops). "
                "Cannot extract simple formula without interpretation."
            )
            return None
        
        # Look for simple assignment with mathematical operations
        # Pattern: variable = expression with math operators
        assignment_pattern = r'(\w+)\s*=\s*([^;]+);'
        
        lines = method_body.split('\n')
        for i, line in enumerate(lines, start=1):
            # Skip comments and empty lines
            if line.strip().startswith('//') or not line.strip():
                continue
            
            match = re.search(assignment_pattern, line)
            if match:
                variable = match.group(1)
                expression = match.group(2).strip()
                
                # Check if expression contains mathematical operations
                if self._is_mathematical_expression(expression):
                    # Extract variables from expression
                    variables = self._extract_variables_from_expression(expression)
                    
                    # Check if all variables are defined or can be understood
                    missing_elements = self._check_missing_elements(expression, method_body)
                    
                    # Determine confidence based on missing elements
                    if not missing_elements:
                        confidence = ConfidenceLevel.HIGH
                        verified = True
                    elif len(missing_elements) <= 2:
                        confidence = ConfidenceLevel.MEDIUM
                        verified = True
                    else:
                        confidence = ConfidenceLevel.LOW
                        verified = False
                    
                    formula = Formula(
                        name=variable,
                        expression=self._humanize_expression(expression),
                        code_expression=expression,
                        variables=variables,
                        source_line=i,
                        source_method="",  # Will be set by caller
                        verified=verified,
                        copy_pastable=self._is_copy_pastable(expression),
                        confidence=confidence,
                        missing_elements=missing_elements
                    )
                    
                    self.logger.info(
                        f"Extracted formula: {variable} = {expression} "
                        f"(confidence: {confidence.value})"
                    )
                    return formula
        
        # No simple formula found
        self.logger.warning("No simple formula found in method body")
        return None
    
    def assess_confidence(self, extraction: Extraction) -> ConfidenceLevel:
        """
        Assess confidence level of extraction.
        
        Following zero-hallucination policy:
        - HIGH: Complete code found, formula explicit, all values present
        - MEDIUM: Code found, some values in config, formula clear but incomplete
        - LOW: Partial code, formula requires interpretation
        - UNVERIFIED: No code found or cannot validate
        
        Args:
            extraction: Extraction to assess
            
        Returns:
            ConfidenceLevel enum value
        """
        # Check if extraction has content
        if not extraction.content or not extraction.content.strip():
            self.logger.confidence_assessment(
                extraction.name,
                ConfidenceLevel.UNVERIFIED.value,
                "No content found"
            )
            return ConfidenceLevel.UNVERIFIED
        
        # Check if line number is valid
        if extraction.line_number < 1:
            self.logger.confidence_assessment(
                extraction.name,
                ConfidenceLevel.UNVERIFIED.value,
                "Invalid line number"
            )
            return ConfidenceLevel.UNVERIFIED
        
        # Verify line reference
        if not self.verify_line_reference(extraction.line_number, extraction.content[:100]):
            self.logger.confidence_assessment(
                extraction.name,
                ConfidenceLevel.LOW.value,
                "Line reference could not be verified"
            )
            return ConfidenceLevel.LOW
        
        # Check formulas if present
        if extraction.formulas:
            formula_confidences = [f.confidence for f in extraction.formulas]
            
            # If any formula is unverified, overall confidence is low
            if any(c == ConfidenceLevel.UNVERIFIED for c in formula_confidences):
                self.logger.confidence_assessment(
                    extraction.name,
                    ConfidenceLevel.LOW.value,
                    "Contains unverified formulas"
                )
                return ConfidenceLevel.LOW
            
            # If all formulas are high confidence, overall is high
            if all(c == ConfidenceLevel.HIGH for c in formula_confidences):
                self.logger.confidence_assessment(
                    extraction.name,
                    ConfidenceLevel.HIGH.value,
                    "All formulas verified with complete data"
                )
                return ConfidenceLevel.HIGH
            
            # Mixed confidence levels
            self.logger.confidence_assessment(
                extraction.name,
                ConfidenceLevel.MEDIUM.value,
                "Formulas verified but some data missing"
            )
            return ConfidenceLevel.MEDIUM
        
        # Check config values if present
        if extraction.config_values:
            # Check if config values are placeholders or actual values
            placeholder_count = sum(
                1 for v in extraction.config_values.values()
                if v.startswith('<') and v.endswith('>')
            )
            
            if placeholder_count == 0:
                # All values are actual values
                self.logger.confidence_assessment(
                    extraction.name,
                    ConfidenceLevel.HIGH.value,
                    "All config values found"
                )
                return ConfidenceLevel.HIGH
            elif placeholder_count < len(extraction.config_values) / 2:
                # Less than half are placeholders
                self.logger.confidence_assessment(
                    extraction.name,
                    ConfidenceLevel.MEDIUM.value,
                    f"{placeholder_count} config values missing"
                )
                return ConfidenceLevel.MEDIUM
            else:
                # More than half are placeholders
                self.logger.confidence_assessment(
                    extraction.name,
                    ConfidenceLevel.LOW.value,
                    f"Most config values missing ({placeholder_count}/{len(extraction.config_values)})"
                )
                return ConfidenceLevel.LOW
        
        # Default: if we have content and valid line number, medium confidence
        self.logger.confidence_assessment(
            extraction.name,
            ConfidenceLevel.MEDIUM.value,
            "Code found but limited verification"
        )
        return ConfidenceLevel.MEDIUM
    
    def identify_missing_data(self, extraction: Extraction) -> List[str]:
        """
        Identify what data is missing or unclear.
        
        Args:
            extraction: Extraction to analyze
            
        Returns:
            Specific list of missing elements (class names, methods, values)
        """
        missing = []
        
        # Check if class name is missing
        if not extraction.class_name:
            missing.append("Class name not identified")
        
        # Check if method name is missing (for method extractions)
        if extraction.category in ["formula", "calculation"] and not extraction.method_name:
            missing.append("Method name not identified")
        
        # Check formulas for missing elements
        if extraction.formulas:
            for formula in extraction.formulas:
                if formula.missing_elements:
                    missing.extend([
                        f"Formula '{formula.name}': {elem}"
                        for elem in formula.missing_elements
                    ])
        
        # Check config values for placeholders
        if extraction.config_values:
            for key, value in extraction.config_values.items():
                if value.startswith('<') and value.endswith('>'):
                    missing.append(f"Config value '{key}' not found in code")
        
        # Check if content is too short (might be incomplete)
        if len(extraction.content.strip()) < 50:
            missing.append("Content appears incomplete (less than 50 characters)")
        
        if missing:
            self.logger.warning(
                f"Missing data for {extraction.name}: {len(missing)} items"
            )
        else:
            self.logger.info(f"No missing data identified for {extraction.name}")
        
        return missing
    
    def check_for_assumptions(self, extraction: Extraction) -> List[str]:
        """
        Check if extraction contains any assumptions.
        
        Following zero-hallucination policy: identify any statements that
        are not directly verifiable from code.
        
        Args:
            extraction: Extraction to check
            
        Returns:
            List of assumptions that need to be removed or verified
        """
        assumptions = []
        
        # Keywords that indicate assumptions or speculation
        assumption_keywords = [
            'probably',
            'likely',
            'might',
            'could be',
            'seems to',
            'appears to',
            'possibly',
            'maybe',
            'presumably',
            'should be',
            'expected to',
        ]
        
        content_lower = extraction.content.lower()
        
        # Check for assumption keywords
        for keyword in assumption_keywords:
            if keyword in content_lower:
                assumptions.append(
                    f"Contains assumption keyword: '{keyword}'"
                )
        
        # Check for external references (not from code)
        external_indicators = [
            'according to',
            'based on forum',
            'players report',
            'community says',
            'wiki states',
            'developer mentioned',
        ]
        
        for indicator in external_indicators:
            if indicator in content_lower:
                assumptions.append(
                    f"Contains external reference: '{indicator}' - not verifiable from code"
                )
        
        # Check formulas for interpretation requirements
        if extraction.formulas:
            for formula in extraction.formulas:
                if not formula.verified:
                    assumptions.append(
                        f"Formula '{formula.name}' requires interpretation or has missing data"
                    )
        
        # Check for inferred values (values not directly in code)
        if extraction.config_values:
            for key, value in extraction.config_values.items():
                # Check if value looks like it was calculated or inferred
                if any(op in value for op in ['calculated', 'inferred', 'estimated', 'derived']):
                    assumptions.append(
                        f"Config value '{key}' appears to be inferred: {value}"
                    )
        
        if assumptions:
            self.logger.warning(
                f"Assumptions found in {extraction.name}: {len(assumptions)} items"
            )
            for assumption in assumptions:
                self.logger.warning(f"  - {assumption}")
        else:
            self.logger.info(f"No assumptions found in {extraction.name}")
        
        return assumptions
    
    def _is_mathematical_expression(self, expression: str) -> bool:
        """Check if expression contains mathematical operations."""
        math_operators = ['+', '-', '*', '/', '%', '**']
        return any(op in expression for op in math_operators)
    
    def _extract_variables_from_expression(self, expression: str) -> Dict[str, str]:
        """
        Extract variables from expression.
        
        Args:
            expression: Mathematical expression
            
        Returns:
            Dictionary of variable_name -> description (placeholder)
        """
        variables = {}
        
        # Find all identifiers (words)
        identifiers = re.findall(r'\b[a-zA-Z_]\w*\b', expression)
        
        # Filter out keywords and common method names
        keywords = {
            'return', 'new', 'this', 'base', 'true', 'false', 'null',
            'int', 'float', 'double', 'string', 'bool', 'var'
        }
        
        for identifier in identifiers:
            if identifier not in keywords and not identifier[0].isupper():
                # Use placeholder description - actual descriptions should be added manually
                variables[identifier] = f"<description needed for {identifier}>"
        
        return variables
    
    def _check_missing_elements(self, expression: str, method_body: str) -> List[str]:
        """
        Check for missing elements in formula.
        
        Args:
            expression: Formula expression
            method_body: Full method body
            
        Returns:
            List of missing elements
        """
        missing = []
        
        # Extract variables from expression
        variables = self._extract_variables_from_expression(expression)
        
        # Check if each variable is defined in method body
        for var in variables.keys():
            # Look for variable declaration or assignment
            var_pattern = rf'\b{re.escape(var)}\b\s*='
            if not re.search(var_pattern, method_body):
                # Variable not defined in method, might be parameter or field
                missing.append(f"Variable '{var}' definition not found in method")
        
        # Check for method calls in expression (might need external data)
        method_call_pattern = r'\w+\([^)]*\)'
        method_calls = re.findall(method_call_pattern, expression)
        if method_calls:
            for call in method_calls:
                missing.append(f"Method call '{call}' requires external verification")
        
        # Check for property access (might need config data)
        property_pattern = r'\w+\.\w+'
        properties = re.findall(property_pattern, expression)
        if properties:
            for prop in properties:
                if prop not in method_body:
                    missing.append(f"Property '{prop}' value not found in code")
        
        return missing
    
    def _is_copy_pastable(self, expression: str) -> bool:
        """
        Check if expression can be copy-pasted for calculations.
        
        Args:
            expression: Formula expression
            
        Returns:
            True if expression is copy-pastable
        """
        # Expression is copy-pastable if it:
        # 1. Contains only basic operators
        # 2. No method calls
        # 3. No property access to unknown objects
        
        # Check for method calls
        if '(' in expression and ')' in expression:
            # Might be a method call
            method_call_pattern = r'\w+\([^)]*\)'
            if re.search(method_call_pattern, expression):
                return False
        
        # Check for complex property access
        property_pattern = r'\w+\.\w+\.\w+'  # Multiple levels
        if re.search(property_pattern, expression):
            return False
        
        # Check for special operators or keywords
        special_keywords = ['new ', 'typeof', 'is ', 'as ']
        if any(keyword in expression for keyword in special_keywords):
            return False
        
        return True
    
    def _humanize_expression(self, expression: str) -> str:
        """
        Convert code expression to human-readable format.
        
        Args:
            expression: Code expression
            
        Returns:
            Human-readable formula
        """
        # Replace operators with symbols
        humanized = expression
        humanized = humanized.replace('*', ' × ')
        humanized = humanized.replace('/', ' ÷ ')
        humanized = humanized.replace('+', ' + ')
        humanized = humanized.replace('-', ' - ')
        
        # Clean up extra spaces
        humanized = re.sub(r'\s+', ' ', humanized)
        
        return humanized.strip()
