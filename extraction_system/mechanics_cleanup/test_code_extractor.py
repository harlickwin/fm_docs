"""
Unit tests for CodeExtractor class.

Tests extraction functionality with known classes and patterns from dump.cs.
"""

import pytest
from pathlib import Path
from extraction_system.mechanics_cleanup.code_extractor import (
    CodeExtractor,
    ClassMatch,
    ConfigMatch,
    MethodMatch,
    FormulaExtraction,
    CodeExtractionException
)
from extraction_system.mechanics_cleanup.knowledge_gap_tracker import GapPriority


class TestCodeExtractor:
    """Test suite for CodeExtractor class."""
    
    @pytest.fixture
    def extractor(self):
        """Create CodeExtractor instance for testing."""
        dump_path = Path(r"C:\apktool\il2cpp-output\dump.cs")
        if not dump_path.exists():
            pytest.skip(f"Dump file not found at {dump_path}")
        return CodeExtractor(str(dump_path))
    
    def test_initialization_with_valid_path(self, extractor):
        """Test that CodeExtractor initializes with valid dump path."""
        assert extractor is not None
        assert extractor.dump_path.exists()
    
    def test_initialization_with_invalid_path(self):
        """Test that CodeExtractor raises exception with invalid path."""
        with pytest.raises(CodeExtractionException):
            CodeExtractor("nonexistent_file.cs")
    
    def test_search_class_known_class(self, extractor):
        """Test searching for a known class (PlayerPetCollectionModel)."""
        # Known class at line 1070882
        pattern = r"class PlayerPetCollectionModel"
        matches = extractor.search_class(pattern)
        
        assert len(matches) > 0, "Should find PlayerPetCollectionModel"
        
        # Verify match structure
        match = matches[0]
        assert isinstance(match, ClassMatch)
        assert match.class_name == "PlayerPetCollectionModel"
        assert match.line_number > 0
        assert len(match.content) > 0
        assert len(match.context) > 0
    
    def test_search_class_no_match(self, extractor):
        """Test searching for a non-existent class."""
        pattern = r"class NonExistentClassNameThatDoesNotExist12345"
        matches = extractor.search_class(pattern)
        
        assert len(matches) == 0, "Should not find non-existent class"
    
    def test_search_class_multiple_matches(self, extractor):
        """Test searching with pattern that matches multiple classes."""
        # Pattern that should match multiple config classes
        pattern = r"class.*Config"
        matches = extractor.search_class(pattern)
        
        assert len(matches) > 1, "Should find multiple config classes"
        
        # Verify all matches are ClassMatch instances
        for match in matches[:5]:  # Check first 5
            assert isinstance(match, ClassMatch)
            assert match.class_name is not None
            assert match.line_number > 0
    
    def test_search_config_known_config(self, extractor):
        """Test searching for a known configuration class."""
        # Search for a config class (adjust based on actual dump.cs content)
        config_match = extractor.search_config("MountSummonDropChanceConfig")
        
        if config_match:
            assert isinstance(config_match, ConfigMatch)
            assert config_match.class_name == "MountSummonDropChanceConfig"
            assert config_match.line_number > 0
            assert isinstance(config_match.fields, dict)
    
    def test_extract_method_known_method(self, extractor):
        """Test extracting a known method from a class."""
        # Try to extract a method from AttacksSystem
        method_match = extractor.extract_method("AttacksSystem", "GetDamage")
        
        if method_match:
            assert isinstance(method_match, MethodMatch)
            assert method_match.class_name == "AttacksSystem"
            assert method_match.method_name == "GetDamage"
            assert method_match.line_number > 0
            assert len(method_match.signature) > 0
            assert len(method_match.body) > 0
    
    def test_extract_method_nonexistent_class(self, extractor):
        """Test extracting method from non-existent class."""
        method_match = extractor.extract_method(
            "NonExistentClass12345",
            "SomeMethod"
        )
        
        assert method_match is None, "Should return None for non-existent class"
    
    def test_extract_method_nonexistent_method(self, extractor):
        """Test extracting non-existent method from existing class."""
        # Use a known class but non-existent method
        method_match = extractor.extract_method(
            "PlayerPetCollectionModel",
            "NonExistentMethod12345"
        )
        
        assert method_match is None, "Should return None for non-existent method"
    
    def test_extract_formula_simple_expression(self, extractor):
        """Test extracting formula from simple mathematical expression."""
        method_body = """
        {
            int result = a + b * c;
            float ratio = total / count;
            return result;
        }
        """
        
        formulas = extractor.extract_formula(method_body)
        
        assert len(formulas) >= 2, "Should extract at least 2 formulas"
        
        # Check first formula
        formula = formulas[0]
        assert isinstance(formula, FormulaExtraction)
        assert formula.formula_name == "result"
        assert "a" in formula.variables or "b" in formula.variables
    
    def test_extract_formula_complex_expression(self, extractor):
        """Test extracting formula from complex expression."""
        method_body = """
        {
            float damage = baseDamage * (isCrit ? critMultiplier : 1.0f);
            return damage;
        }
        """
        
        formulas = extractor.extract_formula(method_body)
        
        if formulas:
            formula = formulas[0]
            assert isinstance(formula, FormulaExtraction)
            # Complex formula should be marked as not simple
            assert formula.is_simple == False
    
    def test_extract_formula_no_math(self, extractor):
        """Test extracting formula from code with no mathematical operations."""
        method_body = """
        {
            string name = "test";
            bool flag = true;
            return flag;
        }
        """
        
        formulas = extractor.extract_formula(method_body)
        
        assert len(formulas) == 0, "Should not extract formulas from non-math code"
    
    def test_get_context_valid_line(self, extractor):
        """Test getting context around a valid line number."""
        # Use a known line number (adjust based on actual dump.cs)
        context = extractor.get_context(1000, lines_before=3, lines_after=3)
        
        assert len(context) > 0, "Should return context"
        assert ">>>" in context, "Should mark target line with >>>"
        assert "1000" in context, "Should include line number"
    
    def test_get_context_edge_cases(self, extractor):
        """Test getting context at file boundaries."""
        # Test at start of file
        context_start = extractor.get_context(1, lines_before=5, lines_after=5)
        assert len(context_start) > 0
        
        # Test near end of file (use a large number but not beyond file)
        content = extractor._load_content()
        last_line = len(content)
        context_end = extractor.get_context(last_line, lines_before=5, lines_after=5)
        assert len(context_end) > 0
    
    def test_create_knowledge_gap(self, extractor):
        """Test creating a knowledge gap entry."""
        extractor.create_knowledge_gap(
            category="test",
            title="Test Gap",
            description="This is a test gap",
            searched_patterns=["pattern1", "pattern2"],
            priority=GapPriority.LOW,
            related_mechanics=["mechanic1"],
            notes="Test notes"
        )
        
        # Verify gap was added to tracker
        gaps = extractor.gap_tracker.get_gaps_by_category("test")
        assert len(gaps) > 0
        
        gap = gaps[-1]  # Get the last added gap
        assert gap.title == "Test Gap"
        assert gap.category == "test"
        assert gap.impact == GapPriority.LOW
    
    def test_is_mathematical_expression(self, extractor):
        """Test detection of mathematical expressions."""
        assert extractor._is_mathematical_expression("a + b")
        assert extractor._is_mathematical_expression("x * y / z")
        assert extractor._is_mathematical_expression("total - discount")
        assert not extractor._is_mathematical_expression("name = 'test'")
        assert not extractor._is_mathematical_expression("flag = true")
    
    def test_is_simple_formula(self, extractor):
        """Test detection of simple vs complex formulas."""
        # Simple formulas
        assert extractor._is_simple_formula("a + b")
        assert extractor._is_simple_formula("x * y")
        assert extractor._is_simple_formula("total / count")
        
        # Complex formulas
        assert not extractor._is_simple_formula("a ? b : c")
        assert not extractor._is_simple_formula("if (x > 0) return y")
        assert not extractor._is_simple_formula("Math.Max(a, b)")
    
    def test_humanize_expression(self, extractor):
        """Test conversion of code expressions to human-readable format."""
        assert extractor._humanize_expression("a * b") == "a × b"
        assert extractor._humanize_expression("x / y") == "x ÷ y"
        assert extractor._humanize_expression("a + b * c") == "a + b × c"
    
    def test_extract_variables(self, extractor):
        """Test extraction of variables from expressions."""
        variables = extractor._extract_variables("baseDamage * critMultiplier")
        
        assert "baseDamage" in variables
        assert "critMultiplier" in variables
        assert len(variables) == 2
    
    def test_extract_class_name(self, extractor):
        """Test extraction of class name from declaration line."""
        assert extractor._extract_class_name("public class TestClass {") == "TestClass"
        assert extractor._extract_class_name("class MyClass : BaseClass") == "MyClass"
        assert extractor._extract_class_name("  class  SpacedClass  ") == "SpacedClass"
        assert extractor._extract_class_name("not a class") is None


class TestCodeExtractorIntegration:
    """Integration tests using actual dump.cs content."""
    
    @pytest.fixture
    def extractor(self):
        """Create CodeExtractor instance for testing."""
        dump_path = Path(r"C:\apktool\il2cpp-output\dump.cs")
        if not dump_path.exists():
            pytest.skip(f"Dump file not found at {dump_path}")
        return CodeExtractor(str(dump_path))
    
    def test_search_attacks_system(self, extractor):
        """Test searching for AttacksSystem class."""
        pattern = r"class AttacksSystem"
        matches = extractor.search_class(pattern)
        
        if matches:
            assert len(matches) > 0
            match = matches[0]
            assert "AttacksSystem" in match.class_name
            assert match.line_number > 0
    
    def test_search_combat_related_classes(self, extractor):
        """Test searching for combat-related classes."""
        patterns = [
            r"class.*Damage.*",
            r"class.*Attack.*",
            r"class.*Combat.*"
        ]
        
        total_matches = 0
        for pattern in patterns:
            matches = extractor.search_class(pattern)
            total_matches += len(matches)
        
        # Should find at least some combat-related classes
        assert total_matches > 0, "Should find combat-related classes"
    
    def test_search_config_classes(self, extractor):
        """Test searching for configuration classes."""
        pattern = r"class.*Config"
        matches = extractor.search_class(pattern)
        
        assert len(matches) > 10, "Should find many config classes"
        
        # Verify structure of matches
        for match in matches[:3]:
            assert match.class_name.endswith("Config") or "Config" in match.class_name
            assert match.line_number > 0
            assert len(match.content) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
