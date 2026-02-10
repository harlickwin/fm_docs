"""
Unit tests for DocumentationGenerator class.

Tests HTML generation, code reference formatting, confidence indicators,
and formula card generation.
"""

import pytest
from extraction_system.mechanics_cleanup.documentation_generator import (
    DocumentationGenerator,
    MechanicData,
    CodeReference,
    Example,
)
from extraction_system.mechanics_cleanup.code_verifier import (
    ConfidenceLevel,
    Formula,
)


class TestDocumentationGenerator:
    """Test suite for DocumentationGenerator."""
    
    @pytest.fixture
    def generator(self):
        """Create a DocumentationGenerator instance."""
        return DocumentationGenerator()
    
    @pytest.fixture
    def sample_formula(self):
        """Create a sample formula for testing."""
        return Formula(
            name="effectiveTime",
            expression="baseTime ÷ attackSpeedMulti",
            code_expression="baseTime / attackSpeedMulti",
            variables={
                "baseTime": "Base attack time in seconds",
                "attackSpeedMulti": "Attack speed multiplier"
            },
            source_line=1057705,
            source_method="AttacksSystem.CalculateAttackTime",
            verified=True,
            copy_pastable=True,
            confidence=ConfidenceLevel.HIGH,
            missing_elements=[]
        )
    
    @pytest.fixture
    def sample_code_reference(self):
        """Create a sample code reference."""
        return CodeReference(
            line_number=1057705,
            class_name="AttacksSystem",
            method_name="CalculateAttackTime",
            content="float effectiveTime = baseTime / attackSpeedMulti;",
            context="// Context around the code"
        )
    
    @pytest.fixture
    def sample_example(self):
        """Create a sample example."""
        return Example(
            scenario="Dungeon Level 10",
            inputs={"base_hp": 100, "multiplier": 1.5},
            outputs={"final_hp": 150},
            explanation="HP is multiplied by 1.5x at level 10",
            based_on_code=True
        )
    
    @pytest.fixture
    def sample_mechanic(self, sample_formula, sample_code_reference, sample_example):
        """Create a sample mechanic data."""
        return MechanicData(
            name="Attack Speed Calculation",
            category="combat",
            description="Calculates effective attack time based on speed multiplier",
            code_references=[sample_code_reference],
            formulas=[sample_formula],
            examples=[sample_example],
            confidence=ConfidenceLevel.HIGH,
            missing_data=[]
        )
    
    def test_initialization(self, generator):
        """Test DocumentationGenerator initialization."""
        assert generator is not None
        assert generator.template_path is None
    
    def test_format_code_reference_with_method(self, generator):
        """Test formatting code reference with method name."""
        result = generator.format_code_reference(
            line_number=1057705,
            class_name="AttacksSystem",
            method_name="CalculateAttackTime"
        )
        
        assert "AttacksSystem.CalculateAttackTime()" in result
        assert "dump.cs line 1057705" in result
        assert "code-ref" in result
        assert "<code>" in result
        assert "</code>" in result
    
    def test_format_code_reference_without_method(self, generator):
        """Test formatting code reference without method name."""
        result = generator.format_code_reference(
            line_number=1000,
            class_name="TestClass"
        )
        
        assert "TestClass" in result
        assert "dump.cs line 1000" in result
        assert "code-ref" in result
    
    def test_add_confidence_indicator_high(self, generator):
        """Test confidence indicator for HIGH confidence."""
        result = generator.add_confidence_indicator(
            ConfidenceLevel.HIGH,
            "All data verified"
        )
        
        assert "confidence-high" in result
        assert "CONFIDENCE: HIGH" in result.upper()
        assert "All data verified" in result
        assert "Fully verified from code" in result
    
    def test_add_confidence_indicator_medium(self, generator):
        """Test confidence indicator for MEDIUM confidence."""
        result = generator.add_confidence_indicator(
            ConfidenceLevel.MEDIUM,
            "Some values missing"
        )
        
        assert "confidence-medium" in result
        assert "CONFIDENCE: MEDIUM" in result.upper()
        assert "Some values missing" in result
    
    def test_add_confidence_indicator_low(self, generator):
        """Test confidence indicator for LOW confidence."""
        result = generator.add_confidence_indicator(
            ConfidenceLevel.LOW,
            "Limited evidence"
        )
        
        assert "confidence-low" in result
        assert "CONFIDENCE: LOW" in result.upper()
        assert "Limited evidence" in result
    
    def test_add_confidence_indicator_unverified(self, generator):
        """Test confidence indicator for UNVERIFIED."""
        result = generator.add_confidence_indicator(
            ConfidenceLevel.UNVERIFIED,
            "No code found"
        )
        
        assert "confidence-unverified" in result
        assert "CONFIDENCE: UNVERIFIED" in result.upper()
        assert "No code found" in result
    
    def test_generate_formula_card(self, generator, sample_formula):
        """Test formula card generation."""
        result = generator.generate_formula_card(sample_formula)
        
        # Check structure
        assert "formula-card" in result
        assert "effectiveTime" in result
        
        # Check human-readable format
        assert "formula-readable" in result
        assert "baseTime ÷ attackSpeedMulti" in result
        
        # Check code format
        assert "formula-code" in result
        assert "baseTime / attackSpeedMulti" in result
        assert "copy-btn" in result
        
        # Check variables
        assert "formula-variables" in result
        assert "baseTime" in result
        assert "Base attack time in seconds" in result
        assert "attackSpeedMulti" in result
        
        # Check source reference
        assert "dump.cs line 1057705" in result
        assert "AttacksSystem.CalculateAttackTime" in result
    
    def test_generate_formula_card_with_missing_elements(self, generator):
        """Test formula card with missing elements."""
        formula = Formula(
            name="testFormula",
            expression="a + b",
            code_expression="a + b",
            variables={"a": "Variable A", "b": "Variable B"},
            source_line=100,
            source_method="TestMethod",
            verified=False,
            copy_pastable=False,
            confidence=ConfidenceLevel.MEDIUM,
            missing_elements=["Variable 'a' not defined", "Variable 'b' not defined"]
        )
        
        result = generator.generate_formula_card(formula)
        
        # Check warning section
        assert "warning" in result
        assert "Missing Elements" in result
        assert "Variable 'a' not defined" in result
        assert "Variable 'b' not defined" in result
        
        # Check confidence indicator
        assert "confidence-medium" in result
    
    def test_generate_example_table(self, generator, sample_example):
        """Test example table generation."""
        examples = [sample_example]
        result = generator.generate_example_table(examples)
        
        # Check structure
        assert "examples-section" in result
        assert "comparison-table" in result
        assert "<table" in result
        assert "<thead>" in result
        assert "<tbody>" in result
        
        # Check headers
        assert "Scenario" in result
        assert "Base Hp" in result
        assert "Multiplier" in result
        assert "Final Hp" in result
        assert "Based on Code" in result
        
        # Check data
        assert "Dungeon Level 10" in result
        assert "100" in result
        assert "1.5" in result
        assert "150" in result
        assert "✅" in result  # Code-verified indicator
        
        # Check explanation
        assert "HP is multiplied by 1.5x at level 10" in result
    
    def test_generate_example_table_illustrative(self, generator):
        """Test example table with illustrative (non-code-based) example."""
        example = Example(
            scenario="Test Scenario",
            inputs={"value": 10},
            outputs={"result": 20},
            explanation="Test explanation",
            based_on_code=False
        )
        
        result = generator.generate_example_table([example])
        
        # Check illustrative indicator
        assert "💡" in result
        assert "Illustrative" in result
    
    def test_generate_example_table_multiple_examples(self, generator):
        """Test example table with multiple examples."""
        examples = [
            Example(
                scenario="Level 10",
                inputs={"level": 10},
                outputs={"multiplier": 1.5},
                explanation="",
                based_on_code=True
            ),
            Example(
                scenario="Level 20",
                inputs={"level": 20},
                outputs={"multiplier": 2.0},
                explanation="",
                based_on_code=True
            ),
            Example(
                scenario="Level 30",
                inputs={"level": 30},
                outputs={"multiplier": 2.5},
                explanation="",
                based_on_code=True
            ),
        ]
        
        result = generator.generate_example_table(examples)
        
        # Check all scenarios are present
        assert "Level 10" in result
        assert "Level 20" in result
        assert "Level 30" in result
        
        # Check all multipliers
        assert "1.5" in result
        assert "2.0" in result
        assert "2.5" in result
    
    def test_generate_section(self, generator, sample_mechanic):
        """Test complete section generation."""
        result = generator.generate_section(sample_mechanic)
        
        # Check structure
        assert "mechanic-card" in result
        assert "<h3>Attack Speed Calculation</h3>" in result
        
        # Check confidence indicator
        assert "confidence-high" in result
        
        # Check description
        assert "Calculates effective attack time" in result
        
        # Check formula
        assert "formula-card" in result
        assert "effectiveTime" in result
        
        # Check code references
        assert "code-references" in result
        assert "AttacksSystem.CalculateAttackTime()" in result
        
        # Check examples
        assert "examples-section" in result
        assert "Dungeon Level 10" in result
    
    def test_generate_section_with_missing_data(self, generator, sample_mechanic):
        """Test section generation with missing data."""
        sample_mechanic.missing_data = [
            "Config value 'multiplier' not found",
            "Method 'CalculateBonus' not found"
        ]
        sample_mechanic.confidence = ConfidenceLevel.MEDIUM
        
        result = generator.generate_section(sample_mechanic)
        
        # Check warning section
        assert "warning" in result
        assert "Missing Data" in result
        assert "Config value 'multiplier' not found" in result
        assert "Method 'CalculateBonus' not found" in result
        
        # Check confidence is medium
        assert "confidence-medium" in result
    
    def test_generate_section_no_formulas(self, generator, sample_mechanic):
        """Test section generation without formulas."""
        sample_mechanic.formulas = []
        
        result = generator.generate_section(sample_mechanic)
        
        # Should still generate valid HTML
        assert "mechanic-card" in result
        assert "<h3>Attack Speed Calculation</h3>" in result
        
        # Should not have formula card
        assert "formula-card" not in result
    
    def test_generate_section_no_examples(self, generator, sample_mechanic):
        """Test section generation without examples."""
        sample_mechanic.examples = []
        
        result = generator.generate_section(sample_mechanic)
        
        # Should still generate valid HTML
        assert "mechanic-card" in result
        
        # Should not have examples section
        assert "examples-section" not in result
    
    def test_format_value_float(self, generator):
        """Test value formatting for floats."""
        result = generator._format_value(1.5678)
        assert result == "1.57"
    
    def test_format_value_bool(self, generator):
        """Test value formatting for booleans."""
        assert generator._format_value(True) == "Yes"
        assert generator._format_value(False) == "No"
    
    def test_format_value_string(self, generator):
        """Test value formatting for strings."""
        result = generator._format_value("test")
        assert result == "test"
    
    def test_format_column_name(self, generator):
        """Test column name formatting."""
        assert generator._format_column_name("base_hp") == "Base Hp"
        assert generator._format_column_name("attack_speed") == "Attack Speed"
        assert generator._format_column_name("value") == "Value"
    
    def test_escape_html(self, generator):
        """Test HTML escaping."""
        result = generator._escape_html('<script>alert("test")</script>')
        assert "&lt;" in result
        assert "&gt;" in result
        assert "&quot;" in result
        assert "<script>" not in result
    
    def test_generate_section_empty_code_references(self, generator, sample_mechanic):
        """Test section generation with empty code references."""
        sample_mechanic.code_references = []
        
        result = generator.generate_section(sample_mechanic)
        
        # Should still generate valid HTML
        assert "mechanic-card" in result
        
        # Should not have code references section
        assert "code-references" not in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
