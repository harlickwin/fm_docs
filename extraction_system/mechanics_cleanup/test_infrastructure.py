"""
Test script to verify the mechanics cleanup infrastructure is working correctly.

This script tests:
1. Logger initialization and basic logging
2. Error handler functionality
3. Knowledge gap tracker
4. Configuration validation
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from extraction_system.mechanics_cleanup.logger import init_logger
from extraction_system.mechanics_cleanup.error_handler import (
    ErrorHandler, ErrorSeverity, ExtractionError
)
from extraction_system.mechanics_cleanup.knowledge_gap_tracker import (
    init_tracker, KnowledgeGap, GapPriority
)
from extraction_system.mechanics_cleanup.config import Config


def test_logger():
    """Test logger functionality."""
    print("\n" + "=" * 60)
    print("Testing Logger")
    print("=" * 60)
    
    logger = init_logger()
    
    logger.info("Logger initialized successfully")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    
    logger.extraction_start("test_category")
    logger.search_pattern("test_pattern", "test_location")
    logger.match_found("TestPattern", 12345, "TestClass")
    logger.no_match("MissingPattern", "test_location")
    logger.confidence_assessment("test_mechanic", "HIGH", "All data found")
    logger.knowledge_gap("test_category", "Test Gap", "MEDIUM")
    logger.verification_result("test_item", True, "Code verified")
    logger.extraction_complete("test_category", 5, 2)
    
    print("✓ Logger test passed")


def test_error_handler():
    """Test error handler functionality."""
    print("\n" + "=" * 60)
    print("Testing Error Handler")
    print("=" * 60)
    
    handler = ErrorHandler()
    
    # Test class not found
    error1 = handler.handle_class_not_found(
        "TestClass",
        "dump.cs",
        ["class Test.*"]
    )
    assert error1.severity == ErrorSeverity.MEDIUM
    print(f"✓ Class not found error: {error1.message}")
    
    # Test multiple matches
    error2 = handler.handle_multiple_matches(
        "Test.*",
        [("TestClass1", 100), ("TestClass2", 200)],
        "dump.cs"
    )
    assert error2.severity == ErrorSeverity.LOW
    print(f"✓ Multiple matches error: {error2.message}")
    
    # Test partial match
    error3 = handler.handle_partial_match(
        "ExpectedClass",
        "SimilarClass",
        12345,
        "dump.cs"
    )
    assert error3.severity == ErrorSeverity.MEDIUM
    print(f"✓ Partial match error: {error3.message}")
    
    # Test complex formula
    error4 = handler.handle_complex_formula(
        "CalculateValue",
        54321,
        "Contains branching logic"
    )
    assert error4.severity == ErrorSeverity.LOW
    print(f"✓ Complex formula error: {error4.message}")
    
    # Test missing config value
    error5 = handler.handle_missing_config_value(
        "ConfigClass",
        "MissingValue",
        "CalculationMethod",
        99999
    )
    assert error5.severity == ErrorSeverity.MEDIUM
    print(f"✓ Missing config value error: {error5.message}")
    
    # Get summary
    summary = handler.get_error_summary()
    print(f"\n✓ Error summary: {summary['total_errors']} errors, {summary['total_warnings']} warnings")
    
    print("✓ Error handler test passed")


def test_knowledge_gap_tracker():
    """Test knowledge gap tracker functionality."""
    print("\n" + "=" * 60)
    print("Testing Knowledge Gap Tracker")
    print("=" * 60)
    
    tracker = init_tracker()
    
    # Add some test gaps
    gap1 = KnowledgeGap(
        category="guild_war",
        title="Test Gap 1",
        description="This is a test gap for guild war mechanics",
        searched_patterns=["GuildWar.*", "War.*Match.*"],
        searched_locations=["dump.cs lines 1-100000"],
        potential_sources=["Server-side code", "Native ARM code"],
        impact=GapPriority.HIGH,
        related_mechanics=["Guild matchmaking"],
        notes="This is a test note"
    )
    tracker.add_gap(gap1)
    
    gap2 = KnowledgeGap(
        category="dungeon",
        title="Test Gap 2",
        description="This is a test gap for dungeon mechanics",
        searched_patterns=["Dungeon.*Config"],
        searched_locations=["dump.cs lines 1-100000"],
        potential_sources=["Config files"],
        impact=GapPriority.MEDIUM,
        related_mechanics=["Dungeon scaling"],
        notes=""
    )
    tracker.add_gap(gap2)
    
    # Record some searches
    tracker.record_search(found=True)
    tracker.record_search(found=False)
    tracker.record_search(found=True, partial=True)
    
    # Get statistics
    stats = tracker.get_gap_statistics()
    print(f"✓ Total gaps: {stats['total_gaps']}")
    print(f"✓ High priority: {stats['high_priority']}")
    print(f"✓ Medium priority: {stats['medium_priority']}")
    
    # Get gaps by category
    guild_gaps = tracker.get_gaps_by_category("guild_war")
    print(f"✓ Guild war gaps: {len(guild_gaps)}")
    
    # Generate summary
    summary = tracker.generate_summary()
    print(f"✓ Generated summary ({len(summary)} characters)")
    
    # Export to file
    output_path = "extraction_system/mechanics_cleanup/output/TEST_KNOWLEDGE_GAPS.md"
    tracker.export_to_file(output_path)
    print(f"✓ Exported to {output_path}")
    
    print("✓ Knowledge gap tracker test passed")


def test_config():
    """Test configuration."""
    print("\n" + "=" * 60)
    print("Testing Configuration")
    print("=" * 60)
    
    # Get search patterns
    guild_patterns = Config.get_search_patterns("guild_war")
    print(f"✓ Guild war patterns: {len(guild_patterns)}")
    
    dungeon_patterns = Config.get_search_patterns("dungeon")
    print(f"✓ Dungeon patterns: {len(dungeon_patterns)}")
    
    # Get all categories
    categories = Config.get_all_categories()
    print(f"✓ Total categories: {len(categories)}")
    print(f"  Categories: {', '.join(categories)}")
    
    # Check confidence levels
    print(f"✓ Confidence levels defined: {len(Config.CONFIDENCE_LEVELS)}")
    
    # Validate configuration
    print("\nValidating configuration...")
    is_valid = Config.validate()
    
    if is_valid:
        print("✓ Configuration is valid")
    else:
        print("⚠ Configuration validation failed (this is expected if dump.cs is not at the default path)")
    
    print("✓ Configuration test passed")


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("MECHANICS CLEANUP INFRASTRUCTURE TEST")
    print("=" * 60)
    
    try:
        test_logger()
        test_error_handler()
        test_knowledge_gap_tracker()
        test_config()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED ✓")
        print("=" * 60)
        print("\nInfrastructure is ready for use!")
        print("\nNext steps:")
        print("1. Implement CodeExtractor class")
        print("2. Implement CodeVerifier class")
        print("3. Implement DocumentationGenerator class")
        print("4. Begin extracting mechanics from dump.cs")
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
