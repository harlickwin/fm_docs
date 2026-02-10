#!/usr/bin/env python3
"""
Task 5.1: Search for dungeon classes
Search patterns: Dungeon.*Config, DifficultyMultiplier, DungeonLevel, .*Dungeon.*Reward
Requirements: 2.1, 2.2, 2.3
"""

import sys
from pathlib import Path
from extraction_system.mechanics_cleanup import (
    CodeExtractor,
    get_tracker,
    get_logger,
    GapPriority,
    KnowledgeGap,
    Config
)
import json

def main():
    logger = get_logger()
    logger.info("=" * 80)
    logger.info("Task 5.1: Search for dungeon classes")
    logger.info("=" * 80)
    
    # Validate configuration
    if not Config.validate():
        logger.error("Configuration validation failed")
        return 1
    
    # Initialize extractor and gap tracker
    extractor = CodeExtractor(str(Config.DUMP_PATH))
    gap_tracker = get_tracker()
    
    # Define search patterns
    patterns = [
        r"class Dungeon.*Config",
        r"DifficultyMultiplier",
        r"DungeonLevel",
        r"class.*Dungeon.*Reward",
    ]
    
    logger.info(f"Searching for dungeon classes with {len(patterns)} patterns")
    
    results = {}
    all_matches = []
    
    # Search for each pattern
    for pattern in patterns:
        logger.info(f"\nSearching for pattern: {pattern}")
        matches = extractor.search_class(pattern)
        
        if matches:
            logger.info(f"Found {len(matches)} matches for pattern: {pattern}")
            for match in matches:
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                all_matches.append(match)
            results[pattern] = [
                {
                    "class_name": match.class_name,
                    "line_number": match.line_number,
                    "content_preview": match.content[:200] if match.content else ""
                }
                for match in matches
            ]
        else:
            logger.warning(f"No matches found for pattern: {pattern}")
            gap = KnowledgeGap(
                category="dungeon",
                title=f"Dungeon classes matching pattern: {pattern}",
                description=f"Searched for dungeon-related classes matching pattern '{pattern}' but found no matches. "
                           f"This information may be in server-side code, native ARM implementation, or using different naming conventions.",
                searched_patterns=[pattern],
                searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
                potential_sources=["SharedGameConfig.mpa", "Native ARM code in libil2cpp.so", "Server-side configuration", "Different class naming convention"],
                impact=GapPriority.MEDIUM,
                related_mechanics=["Dungeon scaling", "Difficulty multipliers", "Reward calculations"],
                notes=f"Searched entire dump.cs file with pattern: {pattern}"
            )
            gap_tracker.add_gap(gap)
            results[pattern] = []
    
    # Save results
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / "task_5_1_dungeon_search_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    logger.info(f"Results saved to {output_file}")
    
    # Export knowledge gaps
    if gap_tracker.gaps:
        gap_file = output_dir / "task_5_1_knowledge_gaps.md"
        gap_tracker.export_to_file(str(gap_file))
        logger.info(f"Knowledge gaps exported to {gap_file}")
    
    # Print summary
    logger.info(f"\n{'=' * 80}")
    logger.info(f"SUMMARY")
    logger.info(f"{'=' * 80}")
    logger.info(f"Total patterns searched: {len(patterns)}")
    logger.info(f"Total matches found: {len(all_matches)}")
    logger.info(f"Patterns with matches: {sum(1 for matches in results.values() if matches)}")
    logger.info(f"Patterns without matches: {sum(1 for matches in results.values() if not matches)}")
    logger.info(f"Knowledge gaps created: {len(gap_tracker.gaps)}")
    
    # Print detailed results
    if all_matches:
        logger.info(f"\n{'=' * 80}")
        logger.info("DETAILED RESULTS")
        logger.info(f"{'=' * 80}")
        for match in all_matches:
            logger.info(f"\n{'-' * 60}")
            logger.info(f"Class: {match.class_name}")
            logger.info(f"Line: {match.line_number}")
            logger.info(f"{'-' * 60}")
            logger.info("\nContext:")
            logger.info(match.context)
            logger.info("\nClass content preview (first 20 lines):")
            content_lines = match.content.split('\n')[:20]
            logger.info('\n'.join(content_lines))
            if len(match.content.split('\n')) > 20:
                logger.info(f"\n... ({len(match.content.split('\n')) - 20} more lines)")
    
    logger.info(f"\n{'=' * 80}")
    logger.info("TASK 5.1 COMPLETE")
    logger.info(f"{'=' * 80}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
