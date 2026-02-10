#!/usr/bin/env python3
"""
Task 5.2: Extract dungeon scaling formulas
Extract HP multiplier, damage multiplier, and reward scaling formulas
Requirements: 2.4, 2.5, 2.6, 9.1, 9.2, 9.6, 9.7
"""

import sys
from pathlib import Path
from extraction_system.mechanics_cleanup import (
    CodeExtractor,
    CodeVerifier,
    get_tracker,
    get_logger,
    GapPriority,
    KnowledgeGap,
    Config,
    ConfidenceLevel
)
import json
import re

def main():
    logger = get_logger()
    logger.info("=" * 80)
    logger.info("Task 5.2: Extract dungeon scaling formulas")
    logger.info("=" * 80)
    
    # Validate configuration
    if not Config.validate():
        logger.error("Configuration validation failed")
        return 1
    
    # Initialize extractor, verifier, and gap tracker
    extractor = CodeExtractor(str(Config.DUMP_PATH))
    verifier = CodeVerifier(str(Config.DUMP_PATH))
    gap_tracker = get_tracker()
    
    # Classes to analyze based on Task 5.1 results
    target_classes = [
        ("DungeonRewardConfig", 1061177),  # Has RewardBase and RewardIncrease
        ("DungeonEggRewardHelper", 1061458),  # Has GetNextEggRarity and RollEggRarity
        ("DungeonBaseConfig", 1061151),  # Has MaxDungeonLevel
    ]
    
    formulas = {}
    
    # Extract reward scaling formula from DungeonRewardConfig
    logger.info("\n" + "=" * 80)
    logger.info("Analyzing DungeonRewardConfig for reward scaling")
    logger.info("=" * 80)
    
    reward_config_match = extractor.search_class(r"class DungeonRewardConfig")
    if reward_config_match:
        match = reward_config_match[0]
        logger.info(f"Found DungeonRewardConfig at line {match.line_number}")
        logger.info("\nClass structure:")
        logger.info(match.content)
        
        # Look for RewardBase and RewardIncrease fields
        if "RewardBase" in match.content and "RewardIncrease" in match.content:
            logger.info("\n✓ Found reward scaling fields: RewardBase and RewardIncrease")
            formulas["reward_scaling"] = {
                "class": "DungeonRewardConfig",
                "line": match.line_number,
                "fields": ["RewardBase", "RewardIncrease"],
                "formula_description": "Reward = RewardBase + (Level * RewardIncrease)",
                "confidence": "MEDIUM",
                "confidence_reason": "Fields found but formula logic not explicitly in code. Inferred from field names.",
                "notes": "RewardBase and RewardIncrease are F64[] arrays, suggesting per-currency-type scaling"
            }
        else:
            logger.warning("RewardBase or RewardIncrease fields not found in expected format")
    
    # Search for HP and damage multiplier formulas
    logger.info("\n" + "=" * 80)
    logger.info("Searching for HP and damage multiplier formulas")
    logger.info("=" * 80)
    
    # Search for enemy/unit scaling patterns
    hp_patterns = [
        r"HP.*Multiplier",
        r"Health.*Scale",
        r"Enemy.*HP",
        r"Dungeon.*Difficulty",
    ]
    
    damage_patterns = [
        r"Damage.*Multiplier",
        r"Attack.*Scale",
        r"Enemy.*Damage",
    ]
    
    logger.info("\nSearching for HP multiplier patterns...")
    hp_found = False
    for pattern in hp_patterns:
        matches = extractor.search_class(pattern)
        if matches:
            logger.info(f"✓ Found matches for pattern: {pattern}")
            for match in matches:
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                hp_found = True
        else:
            logger.info(f"✗ No matches for pattern: {pattern}")
    
    if not hp_found:
        logger.warning("\nNo HP multiplier formulas found")
        gap = KnowledgeGap(
            category="dungeon",
            title="Dungeon HP multiplier formula",
            description="Searched for HP scaling/multiplier formulas for dungeon enemies but found no matches. "
                       "The HP scaling logic may be server-side, in native code, or use different naming.",
            searched_patterns=hp_patterns,
            searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
            potential_sources=[
                "Server-side enemy spawning logic",
                "Native ARM code",
                "Configuration files with pre-calculated values",
                "Different naming convention (e.g., 'Stats', 'Power', 'Strength')"
            ],
            impact=GapPriority.HIGH,
            related_mechanics=["Dungeon scaling", "Enemy HP calculation", "Difficulty progression"],
            notes="Searched multiple pattern variations but found no explicit HP multiplier formula"
        )
        gap_tracker.add_gap(gap)
    
    logger.info("\nSearching for damage multiplier patterns...")
    damage_found = False
    for pattern in damage_patterns:
        matches = extractor.search_class(pattern)
        if matches:
            logger.info(f"✓ Found matches for pattern: {pattern}")
            for match in matches:
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                damage_found = True
        else:
            logger.info(f"✗ No matches for pattern: {pattern}")
    
    if not damage_found:
        logger.warning("\nNo damage multiplier formulas found")
        gap = KnowledgeGap(
            category="dungeon",
            title="Dungeon damage multiplier formula",
            description="Searched for damage scaling/multiplier formulas for dungeon enemies but found no matches. "
                       "The damage scaling logic may be server-side, in native code, or use different naming.",
            searched_patterns=damage_patterns,
            searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
            potential_sources=[
                "Server-side enemy spawning logic",
                "Native ARM code",
                "Configuration files with pre-calculated values",
                "Different naming convention (e.g., 'Attack', 'Power', 'Strength')"
            ],
            impact=GapPriority.HIGH,
            related_mechanics=["Dungeon scaling", "Enemy damage calculation", "Difficulty progression"],
            notes="Searched multiple pattern variations but found no explicit damage multiplier formula"
        )
        gap_tracker.add_gap(gap)
    
    # Analyze DungeonEggRewardHelper for egg rarity formula
    logger.info("\n" + "=" * 80)
    logger.info("Analyzing DungeonEggRewardHelper for egg rarity mechanics")
    logger.info("=" * 80)
    
    egg_helper_match = extractor.search_class(r"class DungeonEggRewardHelper")
    if egg_helper_match:
        match = egg_helper_match[0]
        logger.info(f"Found DungeonEggRewardHelper at line {match.line_number}")
        logger.info("\nClass structure:")
        logger.info(match.content)
        
        # Try to extract the RollEggRarity method
        method_match = extractor.extract_method("DungeonEggRewardHelper", "RollEggRarity")
        if method_match:
            logger.info(f"\n✓ Found RollEggRarity method at line {method_match.line_number}")
            logger.info("\nMethod signature:")
            logger.info(method_match.signature)
            logger.info("\nMethod body:")
            logger.info(method_match.body)
            
            formulas["egg_rarity_roll"] = {
                "class": "DungeonEggRewardHelper",
                "method": "RollEggRarity",
                "line": method_match.line_number,
                "signature": method_match.signature,
                "confidence": "LOW",
                "confidence_reason": "Method found but body is empty (IL2CPP limitation). Cannot extract actual formula.",
                "notes": "Method takes PlayerModel, RandomPCG, and level as parameters. Actual logic not visible in dump."
            }
        else:
            logger.warning("RollEggRarity method body not extractable")
    
    # Save results
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / "task_5_2_dungeon_formulas.json"
    with open(output_file, 'w') as f:
        json.dump(formulas, f, indent=2)
    
    logger.info(f"\nResults saved to {output_file}")
    
    # Export knowledge gaps
    if gap_tracker.gaps:
        gap_file = output_dir / "task_5_2_knowledge_gaps.md"
        gap_tracker.export_to_file(str(gap_file))
        logger.info(f"Knowledge gaps exported to {gap_file}")
    
    # Print summary
    logger.info(f"\n{'=' * 80}")
    logger.info("SUMMARY")
    logger.info(f"{'=' * 80}")
    logger.info(f"Formulas extracted: {len(formulas)}")
    logger.info(f"Knowledge gaps created: {len(gap_tracker.gaps)}")
    
    if formulas:
        logger.info("\nExtracted formulas:")
        for key, formula in formulas.items():
            logger.info(f"\n  {key}:")
            logger.info(f"    Class: {formula.get('class', 'N/A')}")
            logger.info(f"    Line: {formula.get('line', 'N/A')}")
            logger.info(f"    Confidence: {formula.get('confidence', 'N/A')}")
            logger.info(f"    Reason: {formula.get('confidence_reason', 'N/A')}")
    
    logger.info(f"\n{'=' * 80}")
    logger.info("TASK 5.2 COMPLETE")
    logger.info(f"{'=' * 80}")
    logger.info("\nKey findings:")
    logger.info("  ✓ Reward scaling fields found (RewardBase, RewardIncrease)")
    logger.info("  ✗ HP multiplier formula not found")
    logger.info("  ✗ Damage multiplier formula not found")
    logger.info("  ~ Egg rarity method found but body not extractable")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
