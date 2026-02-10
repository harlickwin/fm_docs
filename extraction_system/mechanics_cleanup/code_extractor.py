"""
Code Extractor for mechanics cleanup extraction.

Searches and extracts relevant code sections from dump.cs following the
zero-hallucination policy: extract only what exists, mark everything else
as unverified.
"""

import re
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass

from extraction_system.mechanics_cleanup.logger import get_logger
from extraction_system.mechanics_cleanup.error_handler import (
    ErrorHandler,
    CodeExtractionException
)
from extraction_system.mechanics_cleanup.knowledge_gap_tracker import (
    get_tracker,
    KnowledgeGap,
    GapPriority
)


@dataclass
class ClassMatch:
    """Represents a class found in dump.cs."""
    class_name: str
    line_number: int
    content: str
    context: str  # Surrounding code for clarity


@dataclass
class ConfigMatch:
    """Represents a configuration class with fields and values."""
    class_name: str
    line_number: int
    fields: Dict[str, str]  # field_name -> value
    content: str


@dataclass
class MethodMatch:
    """Represents a method extracted from a class."""
    class_name: str
    method_name: str
    line_number: int
    signature: str
    body: str
    full_content: str


@dataclass
class FormulaExtraction:
    """Represents a mathematical formula extracted from code."""
    formula_name: str
    expression: str  # Human-readable formula
    code_expression: str  # Exact code from dump.cs
    variables: Dict[str, str]  # variable_name -> description
    line_number: int
    method_name: str
    is_simple: bool  # True if formula is straightforward, False if complex


class CodeExtractor:
    """Extracts code sections from dump.cs with strict verification."""
    
    def __init__(self, dump_path: str):
        """
        Initialize with path to dump.cs.
        
        Args:
            dump_path: Path to the IL2CPP dump file
            
        Raises:
            CodeExtractionException: If dump file doesn't exist
        """
        self.dump_path = Path(dump_path)
        self.logger = get_logger()
        self.error_handler = ErrorHandler()
        self.gap_tracker = get_tracker()
        
        if not self.dump_path.exists():
            error = self.error_handler.handle_file_not_found(
                str(self.dump_path),
                "CodeExtractor initialization"
            )
            raise CodeExtractionException(
                f"Dump file not found: {self.dump_path}",
                error
            )
        
        self.logger.info(f"CodeExtractor initialized with dump: {self.dump_path}")
        
        # Cache for file content to avoid repeated reads
        self._content_cache: Optional[List[str]] = None
    
    def _load_content(self) -> List[str]:
        """
        Load dump.cs content into memory.
        
        Returns:
            List of lines from dump.cs
        """
        if self._content_cache is None:
            self.logger.info("Loading dump.cs into memory...")
            with open(self.dump_path, 'r', encoding='utf-8', errors='ignore') as f:
                self._content_cache = f.readlines()
            self.logger.info(f"Loaded {len(self._content_cache)} lines from dump.cs")
        return self._content_cache
    
    def search_class(self, pattern: str) -> List[ClassMatch]:
        """
        Search for classes matching pattern.
        
        Args:
            pattern: Regex pattern to search for
            
        Returns:
            List of ClassMatch instances
        """
        self.logger.search_pattern(pattern, str(self.dump_path))
        
        content = self._load_content()
        matches: List[ClassMatch] = []
        
        try:
            regex = re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            self.logger.error(f"Invalid regex pattern: {pattern} - {e}")
            return matches
        
        for line_num, line in enumerate(content, start=1):
            if regex.search(line):
                # Extract class name from the line
                class_name = self._extract_class_name(line)
                if class_name:
                    # Get context around the match
                    context = self.get_context(line_num, lines_before=5, lines_after=10)
                    
                    # Extract class content (until next class or end of namespace)
                    class_content = self._extract_class_content(content, line_num)
                    
                    match = ClassMatch(
                        class_name=class_name,
                        line_number=line_num,
                        content=class_content,
                        context=context
                    )
                    matches.append(match)
                    
                    self.logger.match_found(pattern, line_num, class_name)
                    self.gap_tracker.record_search(found=True)
        
        if not matches:
            self.logger.no_match(pattern, str(self.dump_path))
            self.gap_tracker.record_search(found=False)
        
        return matches
    
    def search_config(self, config_name: str) -> Optional[ConfigMatch]:
        """
        Search for configuration class and extract fields.
        
        Args:
            config_name: Name of the configuration class
            
        Returns:
            ConfigMatch with fields and values, or None if not found
        """
        self.logger.search_pattern(config_name, str(self.dump_path))
        
        # Search for the class
        pattern = rf"class\s+{re.escape(config_name)}\b"
        matches = self.search_class(pattern)
        
        if not matches:
            self.logger.no_match(config_name, str(self.dump_path))
            return None
        
        if len(matches) > 1:
            self.error_handler.handle_multiple_matches(
                config_name,
                [(m.class_name, m.line_number) for m in matches],
                str(self.dump_path)
            )
        
        # Use the first match
        match = matches[0]
        
        # Extract fields from the class content
        fields = self._extract_config_fields(match.content)
        
        config_match = ConfigMatch(
            class_name=match.class_name,
            line_number=match.line_number,
            fields=fields,
            content=match.content
        )
        
        self.logger.info(f"Extracted config {config_name} with {len(fields)} fields")
        return config_match
    
    def extract_method(self, class_name: str, method_name: str) -> Optional[MethodMatch]:
        """
        Extract specific method from class.
        
        Args:
            class_name: Name of the class containing the method
            method_name: Name of the method to extract
            
        Returns:
            MethodMatch with signature and body, or None if not found
        """
        self.logger.search_pattern(
            f"{class_name}.{method_name}",
            str(self.dump_path)
        )
        
        # First find the class
        class_pattern = rf"class\s+{re.escape(class_name)}\b"
        class_matches = self.search_class(class_pattern)
        
        if not class_matches:
            self.logger.no_match(class_name, str(self.dump_path))
            return None
        
        # Search for the method in the class content
        class_match = class_matches[0]
        content_lines = class_match.content.split('\n')
        
        # Look for method signature
        method_pattern = rf"(public|private|protected|internal)?\s*(static)?\s*\w+\s+{re.escape(method_name)}\s*\("
        
        for i, line in enumerate(content_lines):
            if re.search(method_pattern, line):
                # Found the method, extract it
                method_start_line = class_match.line_number + i
                
                # Extract method body (find matching braces)
                method_body = self._extract_method_body(content_lines, i)
                
                # Extract signature (first line)
                signature = line.strip()
                
                method_match = MethodMatch(
                    class_name=class_name,
                    method_name=method_name,
                    line_number=method_start_line,
                    signature=signature,
                    body=method_body,
                    full_content=signature + "\n" + method_body
                )
                
                self.logger.match_found(
                    f"{class_name}.{method_name}",
                    method_start_line,
                    method_name
                )
                self.gap_tracker.record_search(found=True)
                return method_match
        
        self.logger.no_match(f"{class_name}.{method_name}", str(self.dump_path))
        self.gap_tracker.record_search(found=False)
        return None
    
    def extract_formula(self, method_body: str) -> List[FormulaExtraction]:
        """
        Extract mathematical formulas from method body.
        
        Following zero-hallucination policy: extract only explicit formulas,
        mark complex logic as requiring interpretation.
        
        Args:
            method_body: Method body text
            
        Returns:
            List of FormulaExtraction instances
        """
        formulas: List[FormulaExtraction] = []
        
        # Look for assignment statements with mathematical operations
        # Pattern: variable = expression with math operators
        assignment_pattern = r'(\w+)\s*=\s*([^;]+);'
        
        lines = method_body.split('\n')
        for i, line in enumerate(lines, start=1):
            # Skip comments and empty lines
            if line.strip().startswith('//') or not line.strip():
                continue
            
            matches = re.finditer(assignment_pattern, line)
            for match in matches:
                variable = match.group(1)
                expression = match.group(2).strip()
                
                # Check if expression contains mathematical operations
                if self._is_mathematical_expression(expression):
                    # Determine if formula is simple or complex
                    is_simple = self._is_simple_formula(expression)
                    
                    # Extract variables from expression
                    variables = self._extract_variables(expression)
                    
                    formula = FormulaExtraction(
                        formula_name=variable,
                        expression=self._humanize_expression(expression),
                        code_expression=expression,
                        variables=variables,
                        line_number=i,
                        method_name="",  # Will be set by caller
                        is_simple=is_simple
                    )
                    formulas.append(formula)
        
        return formulas
    
    def get_context(self, line_number: int, lines_before: int = 5, lines_after: int = 5) -> str:
        """
        Get code context around a line number.
        
        Args:
            line_number: Target line number (1-indexed)
            lines_before: Number of lines before to include
            lines_after: Number of lines after to include
            
        Returns:
            Context string with line numbers
        """
        content = self._load_content()
        
        # Calculate range (convert to 0-indexed)
        start = max(0, line_number - lines_before - 1)
        end = min(len(content), line_number + lines_after)
        
        # Build context with line numbers
        context_lines = []
        for i in range(start, end):
            line_num = i + 1
            marker = ">>>" if line_num == line_number else "   "
            context_lines.append(f"{marker} {line_num:6d}: {content[i].rstrip()}")
        
        return '\n'.join(context_lines)
    
    def _extract_class_name(self, line: str) -> Optional[str]:
        """Extract class name from a class declaration line."""
        # Pattern: class ClassName or class ClassName : BaseClass
        match = re.search(r'class\s+(\w+)', line)
        if match:
            return match.group(1)
        return None
    
    def _extract_class_content(self, content: List[str], start_line: int, max_lines: int = 500) -> str:
        """
        Extract class content from start line until end of class.
        
        Args:
            content: Full file content as list of lines
            start_line: Line number where class starts (1-indexed)
            max_lines: Maximum number of lines to extract
            
        Returns:
            Class content as string
        """
        lines = []
        brace_count = 0
        started = False
        
        for i in range(start_line - 1, min(len(content), start_line + max_lines)):
            line = content[i]
            lines.append(line.rstrip())
            
            # Count braces to find end of class
            for char in line:
                if char == '{':
                    brace_count += 1
                    started = True
                elif char == '}':
                    brace_count -= 1
                    
                    # End of class
                    if started and brace_count == 0:
                        return '\n'.join(lines)
        
        return '\n'.join(lines)
    
    def _extract_config_fields(self, class_content: str) -> Dict[str, str]:
        """
        Extract field declarations from config class.
        
        Args:
            class_content: Class content as string
            
        Returns:
            Dictionary of field_name -> value/type
        """
        fields = {}
        
        # Pattern for field declarations
        # public int fieldName = value;
        # public string fieldName;
        field_pattern = r'(public|private|protected)?\s*(static)?\s*(\w+)\s+(\w+)\s*(=\s*([^;]+))?;'
        
        for line in class_content.split('\n'):
            match = re.search(field_pattern, line)
            if match:
                field_type = match.group(3)
                field_name = match.group(4)
                field_value = match.group(6) if match.group(6) else f"<{field_type}>"
                
                fields[field_name] = field_value.strip()
        
        return fields
    
    def _extract_method_body(self, content_lines: List[str], start_index: int) -> str:
        """
        Extract method body from content lines.
        
        Args:
            content_lines: Lines of content
            start_index: Index where method starts
            
        Returns:
            Method body as string
        """
        body_lines = []
        brace_count = 0
        started = False
        
        for i in range(start_index, len(content_lines)):
            line = content_lines[i]
            
            # Count braces
            for char in line:
                if char == '{':
                    brace_count += 1
                    started = True
                elif char == '}':
                    brace_count -= 1
            
            if started:
                body_lines.append(line)
                
                # End of method
                if brace_count == 0:
                    break
        
        return '\n'.join(body_lines)
    
    def _is_mathematical_expression(self, expression: str) -> bool:
        """Check if expression contains mathematical operations."""
        math_operators = ['+', '-', '*', '/', '%', '**']
        return any(op in expression for op in math_operators)
    
    def _is_simple_formula(self, expression: str) -> bool:
        """
        Determine if formula is simple or complex.
        
        Simple: Single line, no conditionals, no method calls
        Complex: Multiple operations, conditionals, method calls
        """
        # Check for complexity indicators
        complexity_indicators = [
            '?',  # Ternary operator
            'if',  # Conditional
            'for',  # Loop
            'while',  # Loop
            '(',  # Method call (might be)
        ]
        
        # Count operators
        operator_count = sum(1 for op in ['+', '-', '*', '/', '%'] if op in expression)
        
        # Simple if: few operators, no complexity indicators
        has_complexity = any(indicator in expression for indicator in complexity_indicators)
        
        return operator_count <= 3 and not has_complexity
    
    def _extract_variables(self, expression: str) -> Dict[str, str]:
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
        keywords = {'return', 'new', 'this', 'base', 'true', 'false', 'null'}
        
        for identifier in identifiers:
            if identifier not in keywords and not identifier[0].isupper():
                # Use placeholder description - actual descriptions should be added manually
                variables[identifier] = f"<description needed for {identifier}>"
        
        return variables
    
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
        humanized = humanized.replace('*', '×')
        humanized = humanized.replace('/', '÷')
        
        return humanized
    
    def create_knowledge_gap(
        self,
        category: str,
        title: str,
        description: str,
        searched_patterns: List[str],
        priority: GapPriority = GapPriority.MEDIUM,
        related_mechanics: Optional[List[str]] = None,
        notes: str = ""
    ) -> None:
        """
        Create a knowledge gap entry for information not found.
        
        Args:
            category: Category of the gap
            title: Short title
            description: Detailed description
            searched_patterns: Patterns that were searched
            priority: Priority level
            related_mechanics: List of affected mechanics
            notes: Additional notes
        """
        gap = KnowledgeGap(
            category=category,
            title=title,
            description=description,
            searched_patterns=searched_patterns,
            searched_locations=[f"{self.dump_path} (lines 1-{len(self._load_content())})"],
            potential_sources=[
                "Server-side code (not in client dump)",
                "Native ARM code in libil2cpp.so",
                "Configuration files (.mpa, .json)",
            ],
            impact=priority,
            related_mechanics=related_mechanics or [],
            notes=notes
        )
        
        self.gap_tracker.add_gap(gap)
        self.logger.knowledge_gap(category, title, priority.value)
