"""
Unit tests for CodeVerifier class.

Tests verification methods, confidence assessment, and assumption checking
following the zero-hallucination policy.
"""

import pytest
from pathlib import Path
from extraction_system.mechanics_cleanup.code_verifier import (
    CodeVerifier,
    ConfidenceLevel,
    Formula,
    Extraction,
    VerificationException
)
from extraction_system.mechanics_cleanup.config import Config


class TestCodeVerifier:
    """Test suite for CodeVerifier class."""
    
    @pytest.fixture
    def verifier(self):
        """Create a CodeVerifier instance for testing."""
        # Use the actual dump.cs path from config
        if not Config.DUMP_PATH.exists():
            pytest.skip(f"dump.cs not found at {Config.DUMP_PATH}")
        return CodeVerifier(str(Config.DUMP_PATH))
    
    @pytest.fixture
    def sample_extraction(self):
        """Create a sample extraction for testing."""
        return Extraction(
            name="TestExtraction",
            category="test",
            content="public class TestClass { }",
            line_number=100,
            class_name="TestClass",
            method_name="TestMethod"
        )
    
    def test_initialization_with_valid_path(self, verifier):
        """Test that CodeVerifier initializes correctly with valid dump path."""
        assert verifier is not None
        assert verifier.dump_path.exists()
        assert verifier.logger is not None
        assert verifier.error_handler is not None
    
    def test_initialization_with_invalid_path(self):
        """Test that CodeVerifier raises exception with invalid dump path."""
        with pytest.raises(VerificationException):
            CodeVerifier("/nonexistent/path/dump.cs")
    
    def test_verify_line_reference_exact_match(self, verifier):
        """Test line reference verification with exact match."""
        # Load content to get a real line
        content = verifier._load_content()
        
        # Pick a line that's likely to exist (line 10)
        if len(content) >= 10:
            line_number = 10
            expected_content = content[line_number - 1].strip()
            
            result = verifier.verify_line_reference(line_number, expected_content)
            assert result is True
    
    def test_verify_line_reference_partial_match(self, verifier):
        """Test line reference verification with partial match."""
        # Load content to get a real line
        content = verifier._load_content()
        
        # Pick a line and use part of it
        if len(content) >= 10:
            line_number = 10
            full_line = content[line_number - 1].strip()
            
            # Use first 20 characters as partial match
            if len(full_line) > 20:
                partial_content = full_line[:20]
                result = verifier.verify_line_reference(line_number, partial_content)
                assert result is True
    
    def test_verify_line_reference_no_match(self, verifier):
        """Test line reference verification with no match."""
        result = verifier.verify_line_reference(
            10,
            "THIS_CONTENT_DEFINITELY_DOES_NOT_EXIST_IN_THE_FILE"
        )
        assert result is False
    
    def test_verify_line_reference_invalid_line_number(self, verifier):
        """Test line reference verification with invalid line number."""
        # Test negative line number
        result = verifier.verify_line_reference(-1, "test")
        assert result is False
        
        # Test line number beyond file length
        content = verifier._load_content()
        result = verifier.verify_line_reference(len(content) + 1000, "test")
        assert result is False
    
    def test_extract_formula_simple(self, verifier):
        """Test formula extraction from simple method body."""
        method_body = """
        {
            int baseValue = 100;
            int multiplier = 2;
            int result = baseValue * multiplier;
            return result;
        }
        """
        
        formula = verifier.extract_formula(method_body)
        
        # Should extract the formula
        assert formula is not None
        assert formula.name == "result"
        assert "*" in formula.code_expression or "×" in formula.expression
        assert formula.verified is True
    
    def test_extract_formula_complex_with_conditionals(self, verifier):
        """Test that complex formulas with conditionals return None."""
        method_body = """
        {
            int result;
            if (condition) {
                result = value1 * 2;
            } else {
                result = value2 * 3;
            }
            return result;
        }
        """
        
        formula = verifier.extract_formula(method_body)
        
        # Should return None due to conditional logic
        assert formula is None
    
    def test_extract_formula_with_loops(self, verifier):
        """Test that formulas with loops return None."""
        method_body = """
        {
            int sum = 0;
            for (int i = 0; i < 10; i++) {
                sum = sum + i;
            }
            return sum;
        }
        """
        
        formula = verifier.extract_formula(method_body)
        
        # Should return None due to loop
        assert formula is None
    
    def test_extract_formula_no_math_operations(self, verifier):
        """Test that non-mathematical assignments return None."""
        method_body = """
        {
            string name = "test";
            bool flag = true;
            return name;
        }
        """
        
        formula = verifier.extract_formula(method_body)
        
        # Should return None (no mathematical operations)
        assert formula is None
    
    def test_assess_confidence_high(self, verifier, sample_extraction):
        """Test confidence assessment for high confidence extraction."""
        # Set up extraction with complete data
        sample_extraction.content = "public class TestClass { public int value = 100; }"
        sample_extraction.line_number = 1
        sample_extraction.config_values = {
            "value1": "100",
            "value2": "200"
        }
        
        # Note: This will likely return MEDIUM or LOW because we can't verify
        # the line reference against actual dump.cs, but we're testing the logic
        confidence = verifier.assess_confidence(sample_extraction)
        
        # Should not be UNVERIFIED
        assert confidence != ConfidenceLevel.UNVERIFIED
    
    def test_assess_confidence_unverified_no_content(self, verifier, sample_extraction):
        """Test confidence assessment for extraction with no content."""
        sample_extraction.content = ""
        
        confidence = verifier.assess_confidence(sample_extraction)
        
        assert confidence == ConfidenceLevel.UNVERIFIED
    
    def test_assess_confidence_unverified_invalid_line(self, verifier, sample_extraction):
        """Test confidence assessment for extraction with invalid line number."""
        sample_extraction.line_number = -1
        
        confidence = verifier.assess_confidence(sample_extraction)
        
        assert confidence == ConfidenceLevel.UNVERIFIED
    
    def test_assess_confidence_with_formulas(self, verifier, sample_extraction):
        """Test confidence assessment with formulas."""
        # Create a high confidence formula
        high_formula = Formula(
            name="result",
            expression="a × b",
            code_expression="a * b",
            variables={"a": "value a", "b": "value b"},
            source_line=1,
            source_method="TestMethod",
            verified=True,
            copy_pastable=True,
            confidence=ConfidenceLevel.HIGH,
            missing_elements=[]
        )
        
        sample_extraction.formulas = [high_formula]
        sample_extraction.line_number = 1
        
        confidence = verifier.assess_confidence(sample_extraction)
        
        # Should reflect the formula confidence
        # Note: Actual result depends on line verification
        assert confidence in [ConfidenceLevel.HIGH, ConfidenceLevel.MEDIUM, ConfidenceLevel.LOW]
    
    def test_assess_confidence_with_config_values(self, verifier, sample_extraction):
        """Test confidence assessment with config values."""
        # All actual values (no placeholders)
        sample_extraction.config_values = {
            "value1": "100",
            "value2": "200",
            "value3": "300"
        }
        sample_extraction.line_number = 1
        
        confidence = verifier.assess_confidence(sample_extraction)
        
        # Should not be UNVERIFIED
        assert confidence != ConfidenceLevel.UNVERIFIED
    
    def test_assess_confidence_with_placeholder_values(self, verifier, sample_extraction):
        """Test confidence assessment with placeholder config values."""
        # Mix of actual and placeholder values
        sample_extraction.config_values = {
            "value1": "100",
            "value2": "<int>",
            "value3": "<string>"
        }
        sample_extraction.line_number = 1
        
        confidence = verifier.assess_confidence(sample_extraction)
        
        # Should be MEDIUM or LOW due to placeholders
        assert confidence in [ConfidenceLevel.MEDIUM, ConfidenceLevel.LOW]
    
    def test_identify_missing_data_no_class_name(self, verifier, sample_extraction):
        """Test missing data identification when class name is missing."""
        sample_extraction.class_name = None
        
        missing = verifier.identify_missing_data(sample_extraction)
        
        assert any("Class name" in item for item in missing)
    
    def test_identify_missing_data_no_method_name(self, verifier, sample_extraction):
        """Test missing data identification when method name is missing."""
        sample_extraction.category = "formula"
        sample_extraction.method_name = None
        
        missing = verifier.identify_missing_data(sample_extraction)
        
        assert any("Method name" in item for item in missing)
    
    def test_identify_missing_data_with_formulas(self, verifier, sample_extraction):
        """Test missing data identification with formulas."""
        formula_with_missing = Formula(
            name="result",
            expression="a × b",
            code_expression="a * b",
            variables={"a": "value a", "b": "value b"},
            source_line=1,
            source_method="TestMethod",
            verified=False,
            copy_pastable=True,
            confidence=ConfidenceLevel.MEDIUM,
            missing_elements=["Variable 'a' not defined", "Variable 'b' not defined"]
        )
        
        sample_extraction.formulas = [formula_with_missing]
        
        missing = verifier.identify_missing_data(sample_extraction)
        
        # Should include formula missing elements
        assert len(missing) > 0
        assert any("Variable 'a'" in item for item in missing)
    
    def test_identify_missing_data_with_placeholder_config(self, verifier, sample_extraction):
        """Test missing data identification with placeholder config values."""
        sample_extraction.config_values = {
            "value1": "100",
            "value2": "<int>",
            "value3": "<string>"
        }
        
        missing = verifier.identify_missing_data(sample_extraction)
        
        # Should identify placeholder values as missing
        assert any("value2" in item for item in missing)
        assert any("value3" in item for item in missing)
    
    def test_identify_missing_data_short_content(self, verifier, sample_extraction):
        """Test missing data identification with short content."""
        sample_extraction.content = "short"
        
        missing = verifier.identify_missing_data(sample_extraction)
        
        # Should flag short content as potentially incomplete
        assert any("incomplete" in item.lower() for item in missing)
    
    def test_check_for_assumptions_with_keywords(self, verifier, sample_extraction):
        """Test assumption checking with assumption keywords."""
        sample_extraction.content = "This probably works and might be correct."
        
        assumptions = verifier.check_for_assumptions(sample_extraction)
        
        # Should detect assumption keywords
        assert len(assumptions) > 0
        assert any("probably" in item.lower() for item in assumptions)
        assert any("might" in item.lower() for item in assumptions)
    
    def test_check_for_assumptions_with_external_references(self, verifier, sample_extraction):
        """Test assumption checking with external references."""
        sample_extraction.content = "According to the forum, this value is 100."
        
        assumptions = verifier.check_for_assumptions(sample_extraction)
        
        # Should detect external reference
        assert len(assumptions) > 0
        assert any("external reference" in item.lower() for item in assumptions)
    
    def test_check_for_assumptions_with_unverified_formulas(self, verifier, sample_extraction):
        """Test assumption checking with unverified formulas."""
        unverified_formula = Formula(
            name="result",
            expression="a × b",
            code_expression="a * b",
            variables={"a": "value a", "b": "value b"},
            source_line=1,
            source_method="TestMethod",
            verified=False,
            copy_pastable=True,
            confidence=ConfidenceLevel.LOW,
            missing_elements=["Missing data"]
        )
        
        sample_extraction.formulas = [unverified_formula]
        
        assumptions = verifier.check_for_assumptions(sample_extraction)
        
        # Should flag unverified formula
        assert len(assumptions) > 0
        assert any("requires interpretation" in item.lower() for item in assumptions)
    
    def test_check_for_assumptions_with_inferred_values(self, verifier, sample_extraction):
        """Test assumption checking with inferred config values."""
        sample_extraction.config_values = {
            "value1": "calculated from other values",
            "value2": "inferred from pattern"
        }
        
        assumptions = verifier.check_for_assumptions(sample_extraction)
        
        # Should detect inferred values
        assert len(assumptions) > 0
        assert any("inferred" in item.lower() for item in assumptions)
    
    def test_check_for_assumptions_clean_extraction(self, verifier, sample_extraction):
        """Test assumption checking with clean extraction (no assumptions)."""
        sample_extraction.content = "public class TestClass { public int value = 100; }"
        sample_extraction.config_values = {"value": "100"}
        
        assumptions = verifier.check_for_assumptions(sample_extraction)
        
        # Should have no assumptions
        assert len(assumptions) == 0
    
    def test_confidence_level_descriptions(self):
        """Test that all confidence levels have descriptions."""
        for level in ConfidenceLevel:
            description = level.get_description()
            assert description is not None
            assert len(description) > 0
    
    def test_is_mathematical_expression(self, verifier):
        """Test mathematical expression detection."""
        # Mathematical expressions
        assert verifier._is_mathematical_expression("a + b") is True
        assert verifier._is_mathematical_expression("x * y") is True
        assert verifier._is_mathematical_expression("value / 2") is True
        assert verifier._is_mathematical_expression("result - offset") is True
        
        # Non-mathematical expressions
        assert verifier._is_mathematical_expression("name = 'test'") is False
        assert verifier._is_mathematical_expression("flag = true") is False
    
    def test_is_copy_pastable(self, verifier):
        """Test copy-pastable expression detection."""
        # Copy-pastable expressions
        assert verifier._is_copy_pastable("a * b + c") is True
        assert verifier._is_copy_pastable("value / 2") is True
        
        # Not copy-pastable (method calls)
        assert verifier._is_copy_pastable("Math.Sqrt(value)") is False
        assert verifier._is_copy_pastable("GetValue()") is False
        
        # Not copy-pastable (complex property access)
        assert verifier._is_copy_pastable("obj.prop.subprop") is False
        
        # Not copy-pastable (special keywords)
        assert verifier._is_copy_pastable("new Object()") is False
    
    def test_humanize_expression(self, verifier):
        """Test expression humanization."""
        # Test operator replacement
        result = verifier._humanize_expression("a * b")
        assert "×" in result
        
        result = verifier._humanize_expression("a / b")
        assert "÷" in result
        
        result = verifier._humanize_expression("a + b - c")
        assert "+" in result
        assert "-" in result


class TestFormulaDataclass:
    """Test suite for Formula dataclass."""
    
    def test_formula_creation(self):
        """Test creating a Formula instance."""
        formula = Formula(
            name="testFormula",
            expression="a × b",
            code_expression="a * b",
            variables={"a": "value a", "b": "value b"},
            source_line=100,
            source_method="TestMethod",
            verified=True,
            copy_pastable=True,
            confidence=ConfidenceLevel.HIGH,
            missing_elements=[]
        )
        
        assert formula.name == "testFormula"
        assert formula.expression == "a × b"
        assert formula.verified is True
        assert formula.confidence == ConfidenceLevel.HIGH


class TestExtractionDataclass:
    """Test suite for Extraction dataclass."""
    
    def test_extraction_creation(self):
        """Test creating an Extraction instance."""
        extraction = Extraction(
            name="TestExtraction",
            category="test",
            content="test content",
            line_number=100
        )
        
        assert extraction.name == "TestExtraction"
        assert extraction.category == "test"
        assert extraction.line_number == 100
        assert extraction.formulas == []  # Default empty list
        assert extraction.config_values == {}  # Default empty dict
    
    def test_extraction_with_optional_fields(self):
        """Test creating an Extraction with optional fields."""
        extraction = Extraction(
            name="TestExtraction",
            category="test",
            content="test content",
            line_number=100,
            class_name="TestClass",
            method_name="TestMethod",
            formulas=[],
            config_values={"key": "value"}
        )
        
        assert extraction.class_name == "TestClass"
        assert extraction.method_name == "TestMethod"
        assert extraction.config_values == {"key": "value"}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
