#!/usr/bin/env python3
"""
Task 6.1: Search for drop chance classes
Search patterns: .*DropChance.*Config, .*Summon.*Config, RandomSeed, DungeonDrop
Requirements: 3.3
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
    logger.info("Task 6.1: Search for drop chance classes")
    logger.info("=" * 80)
    
    if not Config.validate():
        logger.error("Configuration validation failed")
        return 1
    
    extractor = CodeExtractor(str(Config.DUMP_PATH))
    gap_tracker = get_tracker()
    
    patterns = [
        r"class.*DropChance.*Config",
        r"class.*Summon.*Config",
        r"RandomSeed",
        r"DungeonDrop",
    ]
    
    logger.info(f"Searching for drop chance classes with {len(patterns)} patterns")
    
    results = {}
    all_matches = []
    
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
                category="drop_chance",
                title=f"Drop chance classes matching pattern: {pattern}",
                description=f"Searched for drop chance/RNG classes matching pattern '{pattern}' but found no matches.",
                searched_patterns=[pattern],
                searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
                potential_sources=["Server-side RNG", "Native ARM code", "Different naming convention"],
                impact=GapPriority.MEDIUM,
                related_mechanics=["Drop tables", "Egg summoning", "RNG mechanics"],
                notes=f"Searched entire dump.cs file with pattern: {pattern}"
            )
            gap_tracker.add_gap(gap)
            results[pattern] = []
    
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / "task_6_1_drop_chance_search_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    logger.info(f"\nResults saved to {output_file}")
    
    if gap_tracker.gaps:
        gap_file = output_dir / "task_6_1_knowledge_gaps.md"
        gap_tracker.export_to_file(str(gap_file))
        logger.info(f"Knowledge gaps exported to {gap_file}")
    
    logger.info(f"\n{'=' * 80}")
    logger.info("SUMMARY")
    logger.info(f"{'=' * 80}")
    logger.info(f"Total patterns searched: {len(patterns)}")
    logger.info(f"Total matches found: {len(all_matches)}")
    logger.info(f"Knowledge gaps created: {len(gap_tracker.gaps)}")
    
    if all_matches:
        logger.info(f"\n{'=' * 80}")
        logger.info("DETAILED RESULTS")
        logger.info(f"{'=' * 80}")
        for match in all_matches[:5]:  # Show first 5 for brevity
            logger.info(f"\n{'-' * 60}")
            logger.info(f"Class: {match.class_name}")
            logger.info(f"Line: {match.line_number}")
            logger.info(f"{'-' * 60}")
            logger.info("\nContext:")
            logger.info(match.context)
            content_lines = match.content.split('\n')[:15]
            logger.info('\n'.join(content_lines))
            if len(match.content.split('\n')) > 15:
                logger.info(f"\n... ({len(match.content.split('\n')) - 15} more lines)")
        
        if len(all_matches) > 5:
            logger.info(f"\n... and {len(all_matches) - 5} more matches (see JSON file for full results)")
    
    logger.info(f"\n{'=' * 80}")
    logger.info("TASK 6.1 COMPLETE")
    logger.info(f"{'=' * 80}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
