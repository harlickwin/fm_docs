"""
Documentation Generator for mechanics cleanup extraction.

Generates HTML content with code references, confidence indicators,
and formatted examples following the design specifications.
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from pathlib import Path

from extraction_system.mechanics_cleanup.logger import get_logger
from extraction_system.mechanics_cleanup.code_verifier import ConfidenceLevel, Formula


@dataclass
class MechanicData:
    """Represents a game mechanic to be documented."""
    name: str
    category: str  # "guild_war", "dungeon", "pvp", "shop", "rng"
    description: str
    code_references: List['CodeReference']
    formulas: List[Formula]
    examples: List['Example']
    confidence: ConfidenceLevel
    missing_data: List[str]


@dataclass
class CodeReference:
    """Represents a code reference with line number."""
    line_number: int
    class_name: str
    method_name: Optional[str]
    content: str
    context: str  # Surrounding code for clarity


@dataclass
class Example:
    """Represents an example for documentation."""
    scenario: str
    inputs: Dict[str, Any]
    outputs: Dict[str, Any]
    explanation: str
    based_on_code: bool  # True if values from config, False if illustrative


class DocumentationGenerator:
    """Generates HTML documentation with code references and confidence indicators."""
    
    def __init__(self, template_path: Optional[str] = None):
        """
        Initialize with optional HTML template.
        
        Args:
            template_path: Path to HTML template file (optional)
        """
        self.logger = get_logger()
        self.template_path = Path(template_path) if template_path else None
        
        if self.template_path and not self.template_path.exists():
            self.logger.warning(f"Template not found: {self.template_path}")
            self.template_path = None
        
        self.logger.info("DocumentationGenerator initialized")
    
    def generate_section(self, mechanic: MechanicData) -> str:
        """
        Generate HTML section for a mechanic.
        
        Args:
            mechanic: MechanicData instance with all mechanic information
            
        Returns:
            HTML string with proper formatting
        """
        self.logger.info(f"Generating section for mechanic: {mechanic.name}")
        
        html_parts = []
        
        # Start mechanic card
        html_parts.append('<div class="mechanic-card">')
        
        # Add heading
        html_parts.append(f'    <h3>{mechanic.name}</h3>')
        
        # Add confidence indicator
        confidence_html = self.add_confidence_indicator(
            mechanic.confidence,
            self._get_confidence_reason(mechanic)
        )
        html_parts.append(f'    {confidence_html}')
        
        # Add description
        html_parts.append(f'    <p>{mechanic.description}</p>')
        
        # Add formulas if present
        if mechanic.formulas:
            for formula in mechanic.formulas:
                formula_html = self.generate_formula_card(formula)
                html_parts.append(f'    {formula_html}')
        
        # Add code references
        if mechanic.code_references:
            html_parts.append('    <div class="code-references">')
            html_parts.append('        <h4>Code References</h4>')
            html_parts.append('        <ul>')
            for ref in mechanic.code_references:
                ref_html = self.format_code_reference(
                    ref.line_number,
                    ref.class_name,
                    ref.method_name
                )
                html_parts.append(f'            <li>{ref_html}</li>')
            html_parts.append('        </ul>')
            html_parts.append('    </div>')
        
        # Add examples if present
        if mechanic.examples:
            examples_html = self.generate_example_table(mechanic.examples)
            html_parts.append(f'    {examples_html}')
        
        # Add missing data warning if applicable
        if mechanic.missing_data:
            html_parts.append('    <div class="warning">')
            html_parts.append('        ⚠️ <strong>Missing Data:</strong>')
            html_parts.append('        <ul>')
            for missing in mechanic.missing_data:
                html_parts.append(f'            <li>{missing}</li>')
            html_parts.append('        </ul>')
            html_parts.append('    </div>')
        
        # Close mechanic card
        html_parts.append('</div>')
        
        html = '\n'.join(html_parts)
        self.logger.info(f"Generated {len(html)} characters of HTML for {mechanic.name}")
        
        return html
    
    def format_code_reference(
        self,
        line_number: int,
        class_name: str,
        method_name: Optional[str] = None
    ) -> str:
        """
        Format code reference link.
        
        Args:
            line_number: Line number in dump.cs
            class_name: Name of the class
            method_name: Optional method name
            
        Returns:
            HTML link to line in dump.cs
        """
        # Format the reference text
        if method_name:
            ref_text = f"{class_name}.{method_name}()"
        else:
            ref_text = class_name
        
        # Create link (using anchor to line number)
        link = f'<a href="#line-{line_number}" class="code-ref">dump.cs line {line_number}</a>'
        
        # Combine reference text and link
        html = f'<code>{ref_text}</code> - {link}'
        
        return html
    
    def generate_example_table(self, examples: List[Example]) -> str:
        """
        Generate comparison table for examples.
        
        Args:
            examples: List of Example instances
            
        Returns:
            HTML table element
        """
        if not examples:
            return ""
        
        self.logger.info(f"Generating example table with {len(examples)} examples")
        
        html_parts = []
        
        # Start table
        html_parts.append('<div class="examples-section">')
        html_parts.append('    <h4>Examples</h4>')
        html_parts.append('    <table class="comparison-table">')
        
        # Determine columns from first example
        first_example = examples[0]
        input_keys = list(first_example.inputs.keys())
        output_keys = list(first_example.outputs.keys())
        
        # Table header
        html_parts.append('        <thead>')
        html_parts.append('            <tr>')
        html_parts.append('                <th>Scenario</th>')
        for key in input_keys:
            html_parts.append(f'                <th>{self._format_column_name(key)}</th>')
        for key in output_keys:
            html_parts.append(f'                <th>{self._format_column_name(key)}</th>')
        html_parts.append('                <th>Based on Code</th>')
        html_parts.append('            </tr>')
        html_parts.append('        </thead>')
        
        # Table body
        html_parts.append('        <tbody>')
        for example in examples:
            html_parts.append('            <tr>')
            
            # Scenario
            html_parts.append(f'                <td>{example.scenario}</td>')
            
            # Inputs
            for key in input_keys:
                value = example.inputs.get(key, 'N/A')
                html_parts.append(f'                <td>{self._format_value(value)}</td>')
            
            # Outputs
            for key in output_keys:
                value = example.outputs.get(key, 'N/A')
                html_parts.append(f'                <td><strong>{self._format_value(value)}</strong></td>')
            
            # Based on code indicator
            indicator = '✅' if example.based_on_code else '💡'
            tooltip = 'Code-verified' if example.based_on_code else 'Illustrative'
            html_parts.append(f'                <td title="{tooltip}">{indicator}</td>')
            
            html_parts.append('            </tr>')
            
            # Add explanation row if present
            if example.explanation:
                colspan = len(input_keys) + len(output_keys) + 2
                html_parts.append('            <tr class="explanation-row">')
                html_parts.append(f'                <td colspan="{colspan}">')
                html_parts.append(f'                    <em>{example.explanation}</em>')
                html_parts.append('                </td>')
                html_parts.append('            </tr>')
        
        html_parts.append('        </tbody>')
        html_parts.append('    </table>')
        html_parts.append('</div>')
        
        return '\n'.join(html_parts)
    
    def add_confidence_indicator(
        self,
        confidence: ConfidenceLevel,
        reason: str
    ) -> str:
        """
        Add visual confidence indicator.
        
        Args:
            confidence: ConfidenceLevel enum value
            reason: Explanation for the confidence level
            
        Returns:
            HTML element showing confidence level
        """
        # Map confidence level to CSS class
        css_class = f"confidence-{confidence.value}"
        
        # Get confidence description
        description = confidence.get_description()
        
        # Build HTML
        html_parts = []
        html_parts.append(f'<div class="confidence-badge {css_class}">')
        html_parts.append(f'    <span class="confidence-level">Confidence: {confidence.value.upper()}</span>')
        html_parts.append(f'    <span class="confidence-description">{description}</span>')
        if reason:
            html_parts.append(f'    <span class="confidence-reason">{reason}</span>')
        html_parts.append('</div>')
        
        return '\n'.join(html_parts)
    
    def generate_formula_card(self, formula: Formula) -> str:
        """
        Generate formula card with multiple formats.
        
        Args:
            formula: Formula instance
            
        Returns:
            HTML element with formula presentation
        """
        self.logger.info(f"Generating formula card for: {formula.name}")
        
        html_parts = []
        
        # Start formula card
        html_parts.append('<div class="formula-card">')
        html_parts.append(f'    <h4>{formula.name}</h4>')
        
        # Human-readable format
        html_parts.append('    <div class="formula-readable">')
        html_parts.append('        <strong>Formula:</strong>')
        html_parts.append(f'        <code>{formula.expression}</code>')
        html_parts.append('    </div>')
        
        # Code format with copy button
        html_parts.append('    <div class="formula-code">')
        html_parts.append('        <strong>Code:</strong>')
        html_parts.append('        <div class="code-block-wrapper">')
        html_parts.append(f'            <pre><code>{formula.code_expression}</code></pre>')
        html_parts.append(f'            <button class="copy-btn" data-copy="{self._escape_html(formula.code_expression)}">Copy</button>')
        html_parts.append('        </div>')
        html_parts.append('    </div>')
        
        # Spreadsheet format (if copy-pastable)
        if formula.copy_pastable:
            spreadsheet_formula = self._convert_to_spreadsheet(formula.code_expression)
            html_parts.append('    <div class="formula-spreadsheet">')
            html_parts.append('        <strong>Spreadsheet:</strong>')
            html_parts.append(f'        <code>{spreadsheet_formula}</code>')
            html_parts.append('        <span class="hint">(Adjust cell references as needed)</span>')
            html_parts.append('    </div>')
        
        # Variables
        if formula.variables:
            html_parts.append('    <div class="formula-variables">')
            html_parts.append('        <strong>Variables:</strong>')
            html_parts.append('        <ul>')
            for var_name, var_desc in formula.variables.items():
                html_parts.append(f'            <li><code>{var_name}</code>: {var_desc}</li>')
            html_parts.append('        </ul>')
            html_parts.append('    </div>')
        
        # Source reference
        html_parts.append('    <div class="code-ref">')
        html_parts.append('        <strong>Source:</strong>')
        html_parts.append(f'        <a href="#line-{formula.source_line}">dump.cs line {formula.source_line}</a>')
        if formula.source_method:
            html_parts.append(f', {formula.source_method}')
        html_parts.append('    </div>')
        
        # Confidence indicator for formula
        if formula.confidence != ConfidenceLevel.HIGH:
            confidence_html = self.add_confidence_indicator(
                formula.confidence,
                f"Formula has {len(formula.missing_elements)} missing elements" if formula.missing_elements else ""
            )
            html_parts.append(f'    {confidence_html}')
        
        # Missing elements warning
        if formula.missing_elements:
            html_parts.append('    <div class="warning">')
            html_parts.append('        ⚠️ <strong>Missing Elements:</strong>')
            html_parts.append('        <ul>')
            for missing in formula.missing_elements:
                html_parts.append(f'            <li>{missing}</li>')
            html_parts.append('        </ul>')
            html_parts.append('    </div>')
        
        # Close formula card
        html_parts.append('</div>')
        
        return '\n'.join(html_parts)
    
    def _get_confidence_reason(self, mechanic: MechanicData) -> str:
        """
        Get reason for confidence level.
        
        Args:
            mechanic: MechanicData instance
            
        Returns:
            Reason string
        """
        if mechanic.confidence == ConfidenceLevel.HIGH:
            return "All data verified from code"
        elif mechanic.confidence == ConfidenceLevel.MEDIUM:
            if mechanic.missing_data:
                return f"{len(mechanic.missing_data)} data elements missing"
            return "Some configuration values not found"
        elif mechanic.confidence == ConfidenceLevel.LOW:
            return "Limited code evidence, significant gaps"
        else:  # UNVERIFIED
            return "No code evidence found"
    
    def _format_column_name(self, key: str) -> str:
        """
        Format column name for display.
        
        Args:
            key: Column key
            
        Returns:
            Formatted column name
        """
        # Convert snake_case to Title Case
        return key.replace('_', ' ').title()
    
    def _format_value(self, value: Any) -> str:
        """
        Format value for display in table.
        
        Args:
            value: Value to format
            
        Returns:
            Formatted string
        """
        if isinstance(value, float):
            # Format floats with 2 decimal places
            return f"{value:.2f}"
        elif isinstance(value, bool):
            # Format booleans as Yes/No
            return "Yes" if value else "No"
        else:
            return str(value)
    
    def _escape_html(self, text: str) -> str:
        """
        Escape HTML special characters.
        
        Args:
            text: Text to escape
            
        Returns:
            Escaped text
        """
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))
    
    def _convert_to_spreadsheet(self, code_expression: str) -> str:
        """
        Convert code expression to spreadsheet formula format.
        
        Args:
            code_expression: Code expression
            
        Returns:
            Spreadsheet formula (e.g., =A2*B2/C2)
        """
        # Simple conversion: replace variable names with cell references
        # This is a basic implementation - more sophisticated conversion
        # would require parsing the expression
        
        # Start with equals sign
        formula = "=" + code_expression
        
        # Replace common operators
        formula = formula.replace('*', '*')
        formula = formula.replace('/', '/')
        
        # Note: Actual cell references would need to be determined
        # based on the specific variables and their positions
        # For now, we'll add a note that this needs adjustment
        
        return formula + " (adjust cell references)"
