"""
Task 4.1: Search for guild war classes

This script searches for guild war related classes in dump.cs and documents
the results in the knowledge gap tracker.

Search patterns:
- GuildWar.*Config
- GuildTier.*
- .*War.*Match.*
- WarPoints

Requirements: 1.1, 1.2, 1.3
"""

import sys
from pathlib import Path
from extraction_system.mechanics_cleanup import (
    CodeExtractor,
    get_tracker,
    GapPriority,
    KnowledgeGap,
    Config,
    get_logger
)


def main():
    """Execute Task 4.1: Search for guild war classes."""
    
    # Initialize
    logger = get_logger()
    logger.info("=" * 80)
    logger.info("Task 4.1: Search for guild war classes")
    logger.info("=" * 80)
    
    # Validate configuration
    if not Config.validate():
        logger.error("Configuration validation failed")
        return 1
    
    # Initialize extractor
    extractor = CodeExtractor(str(Config.DUMP_PATH))
    tracker = get_tracker()
    
    # Define search patterns for guild war
    search_patterns = [
        r"class GuildWar.*Config",
        r"class GuildTier.*",
        r"class.*War.*Match.*",
        r"\bWarPoints\b",
    ]
    
    logger.info(f"Searching for guild war classes with {len(search_patterns)} patterns")
    
    # Store all results
    all_matches = []
    
    # Execute searches
    for pattern in search_patterns:
        logger.info(f"\nSearching pattern: {pattern}")
        matches = extractor.search_class(pattern)
        
        if matches:
            logger.info(f"Found {len(matches)} matches for pattern: {pattern}")
            for match in matches:
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                all_matches.append(match)
        else:
            logger.info(f"No matches found for pattern: {pattern}")
    
    # Document results
    logger.info("\n" + "=" * 80)
    logger.info("SEARCH RESULTS SUMMARY")
    logger.info("=" * 80)
    
    if all_matches:
        logger.info(f"\nTotal matches found: {len(all_matches)}")
        logger.info("\nDetailed results:")
        
        for match in all_matches:
            logger.info(f"\n{'=' * 60}")
            logger.info(f"Class: {match.class_name}")
            logger.info(f"Line: {match.line_number}")
            logger.info(f"{'=' * 60}")
            logger.info("\nContext:")
            logger.info(match.context)
            logger.info("\nClass content preview (first 20 lines):")
            content_lines = match.content.split('\n')[:20]
            logger.info('\n'.join(content_lines))
            if len(match.content.split('\n')) > 20:
                logger.info(f"\n... ({len(match.content.split('\n')) - 20} more lines)")
    else:
        logger.info("\nNo guild war classes found in dump.cs")
        logger.info("This indicates that guild war mechanics may be:")
        logger.info("  - Implemented server-side")
        logger.info("  - Using different naming conventions")
        logger.info("  - Located in native ARM code")
    
    # Create knowledge gaps for patterns that didn't match
    # Track which patterns found matches
    patterns_with_matches = set()
    for match in all_matches:
        # Determine which pattern(s) matched this class
        for pattern in search_patterns:
            try:
                import re
                if re.search(pattern, f"class {match.class_name}", re.IGNORECASE):
                    patterns_with_matches.add(pattern)
            except:
                pass
    
    patterns_without_matches = [p for p in search_patterns if p not in patterns_with_matches]
    
    if patterns_without_matches:
        logger.info("\n" + "=" * 80)
        logger.info("KNOWLEDGE GAPS")
        logger.info("=" * 80)
        
        for pattern in patterns_without_matches:
            logger.info(f"\nPattern with no matches: {pattern}")
            
            # Create knowledge gap entry
            gap = KnowledgeGap(
                category="guild_war",
                title=f"Guild War classes matching pattern: {pattern}",
                description=f"Searched for classes matching pattern '{pattern}' but found no matches. "
                           f"This information may be in server-side code, native ARM implementation, "
                           f"or using different naming conventions.",
                searched_patterns=[pattern],
                searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
                potential_sources=[
                    "Server-side code (not in client dump)",
                    "Native ARM code in libil2cpp.so",
                    "Configuration files (.mpa, .json)",
                    "Different class naming convention"
                ],
                impact=GapPriority.HIGH,
                related_mechanics=["Guild War Matchmaking", "Guild Tiers", "War Points"],
                notes=f"Searched entire dump.cs file with pattern: {pattern}"
            )
            tracker.add_gap(gap)
    
    # Export results to output directory
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save search results
    results_file = output_dir / "task_4_1_guild_war_search_results.txt"
    with open(results_file, 'w', encoding='utf-8') as f:
        f.write("Task 4.1: Guild War Class Search Results\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Search Date: {tracker.gaps[0].timestamp if tracker.gaps else 'N/A'}\n")
        f.write(f"Total Patterns Searched: {len(search_patterns)}\n")
        f.write(f"Total Matches Found: {len(all_matches)}\n\n")
        
        f.write("Search Patterns:\n")
        for pattern in search_patterns:
            f.write(f"  - {pattern}\n")
        f.write("\n")
        
        if all_matches:
            f.write("Matches Found:\n")
            f.write("-" * 80 + "\n\n")
            
            for match in all_matches:
                f.write(f"Class: {match.class_name}\n")
                f.write(f"Line: {match.line_number}\n")
                f.write(f"File: {Config.DUMP_PATH}\n")
                f.write("\nContext:\n")
                f.write(match.context + "\n")
                f.write("\nClass Content:\n")
                f.write(match.content + "\n")
                f.write("\n" + "=" * 80 + "\n\n")
        else:
            f.write("No matches found.\n\n")
            f.write("Possible reasons:\n")
            f.write("  - Guild war logic is implemented server-side\n")
            f.write("  - Different naming conventions are used\n")
            f.write("  - Logic is in native ARM code\n")
            f.write("  - Classes exist but don't match search patterns\n")
    
    logger.info(f"\nResults saved to: {results_file}")
    
    # Export knowledge gaps
    if tracker.gaps:
        gaps_file = output_dir / "task_4_1_knowledge_gaps.md"
        tracker.export_to_file(str(gaps_file))
        logger.info(f"Knowledge gaps saved to: {gaps_file}")
    
    # Print summary
    logger.info("\n" + "=" * 80)
    logger.info("TASK 4.1 COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Patterns searched: {len(search_patterns)}")
    logger.info(f"Matches found: {len(all_matches)}")
    logger.info(f"Knowledge gaps created: {len(tracker.gaps)}")
    logger.info(f"Results saved to: {output_dir}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
