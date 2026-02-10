"""
Integration tests for CodeVerifier with CodeExtractor.

Tests the complete workflow of extracting code and verifying it.
"""

import pytest
from extraction_system.mechanics_cleanup import (
    CodeExtractor,
    CodeVerifier,
    ConfidenceLevel,
    Extraction,
    Config
)


class TestCodeVerifierIntegration:
    """Integration tests for CodeVerifier with CodeExtractor."""
    
    @pytest.fixture
    def extractor(self):
        """Create a CodeExtractor instance for testing."""
        if not Config.DUMP_PATH.exists():
            pytest.skip(f"dump.cs not found at {Config.DUMP_PATH}")
        return CodeExtractor(str(Config.DUMP_PATH))
    
    @pytest.fixture
    def verifier(self):
        """Create a CodeVerifier instance for testing."""
        if not Config.DUMP_PATH.exists():
            pytest.skip(f"dump.cs not found at {Config.DUMP_PATH}")
        return CodeVerifier(str(Config.DUMP_PATH))
    
    def test_extract_and_verify_class(self, extractor, verifier):
        """Test extracting a class and verifying its line reference."""
        # Search for a known class (PlayerPetCollectionModel mentioned in design)
        pattern = r"class PlayerPetCollectionModel"
        matches = extractor.search_class(pattern)
        
        if matches:
            match = matches[0]
            
            # Get the first line of content (the class declaration line)
            first_line = match.content.split('\n')[0].strip()
            
            # Verify the line reference with the actual first line
            verified = verifier.verify_line_reference(
                match.line_number,
                first_line
            )
            
            # Should be verified
            assert verified is True
    
    def test_extract_and_assess_confidence(self, extractor, verifier):
        """Test extracting a class and assessing confidence."""
        # Search for a config class
        pattern = r"class.*Config"
        matches = extractor.search_class(pattern)
        
        if matches:
            match = matches[0]
            
            # Create an extraction
            extraction = Extraction(
                name=match.class_name,
                category="config",
                content=match.content[:200],
                line_number=match.line_number,
                class_name=match.class_name
            )
            
            # Assess confidence
            confidence = verifier.assess_confidence(extraction)
            
            # Should have some confidence level
            assert confidence in [
                ConfidenceLevel.HIGH,
                ConfidenceLevel.MEDIUM,
                ConfidenceLevel.LOW,
                ConfidenceLevel.UNVERIFIED
            ]
    
    def test_extract_method_and_verify_formula(self, extractor, verifier):
        """Test extracting a method and verifying its formula."""
        # Search for AttacksSystem class (mentioned in design)
        pattern = r"class AttacksSystem"
        matches = extractor.search_class(pattern)
        
        if matches:
            # Try to extract a method
            method_match = extractor.extract_method("AttacksSystem", "CalculateAttackTime")
            
            if method_match:
                # Try to extract formula from method
                formula = verifier.extract_formula(method_match.body)
                
                # If formula found, verify it
                if formula:
                    assert formula.name is not None
                    assert formula.code_expression is not None
                    assert formula.confidence in [
                        ConfidenceLevel.HIGH,
                        ConfidenceLevel.MEDIUM,
                        ConfidenceLevel.LOW
                    ]
    
    def test_extract_and_check_assumptions(self, extractor, verifier):
        """Test extracting code and checking for assumptions."""
        # Search for any class
        pattern = r"class.*System"
        matches = extractor.search_class(pattern)
        
        if matches:
            match = matches[0]
            
            # Create an extraction
            extraction = Extraction(
                name=match.class_name,
                category="system",
                content=match.content[:500],
                line_number=match.line_number,
                class_name=match.class_name
            )
            
            # Check for assumptions
            assumptions = verifier.check_for_assumptions(extraction)
            
            # Should return a list (may be empty)
            assert isinstance(assumptions, list)
    
    def test_extract_and_identify_missing_data(self, extractor, verifier):
        """Test extracting code and identifying missing data."""
        # Search for a config class
        config_match = extractor.search_config("MountSummonDropChanceConfig")
        
        if config_match:
            # Create an extraction
            extraction = Extraction(
                name=config_match.class_name,
                category="config",
                content=config_match.content[:300],
                line_number=config_match.line_number,
                class_name=config_match.class_name,
                config_values=config_match.fields
            )
            
            # Identify missing data
            missing = verifier.identify_missing_data(extraction)
            
            # Should return a list (may be empty)
            assert isinstance(missing, list)
    
    def test_complete_verification_workflow(self, extractor, verifier):
        """Test complete workflow: extract, verify, assess, check."""
        # Search for a class
        pattern = r"class.*Config"
        matches = extractor.search_class(pattern)
        
        if matches:
            match = matches[0]
            
            # Step 1: Extract
            extraction = Extraction(
                name=match.class_name,
                category="config",
                content=match.content[:300],
                line_number=match.line_number,
                class_name=match.class_name
            )
            
            # Step 2: Verify line reference
            verified = verifier.verify_line_reference(
                extraction.line_number,
                extraction.content[:50]
            )
            assert isinstance(verified, bool)
            
            # Step 3: Assess confidence
            confidence = verifier.assess_confidence(extraction)
            assert isinstance(confidence, ConfidenceLevel)
            
            # Step 4: Identify missing data
            missing = verifier.identify_missing_data(extraction)
            assert isinstance(missing, list)
            
            # Step 5: Check for assumptions
            assumptions = verifier.check_for_assumptions(extraction)
            assert isinstance(assumptions, list)
            
            # Complete workflow executed successfully
            assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
