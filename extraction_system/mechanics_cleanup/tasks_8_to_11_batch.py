#!/usr/bin/env python3
"""
Tasks 8-11 Batch Execution:
- 8.1: Search for PvP classes
- 8.2: Extract league and matchmaking data
- 9.1: Search for shop classes
- 9.2: Analyze shop mechanics
- 10.1: Search for combat classes
- 10.2: Extract combat formulas
- 11: Checkpoint - Verify all extractions complete
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
    Config
)
import json

def task_8_1_pvp_search(extractor, gap_tracker, logger):
    """Task 8.1: Search for PvP classes"""
    logger.info("=" * 80)
    logger.info("TASK 8.1: Search for PvP classes")
    logger.info("=" * 80)
    
    patterns = [
        r"class Pvp.*Config",
        r"class.*League.*Config",
        r"PromotionEnd",
        r"DemotionStart",
        r"PvpMatchmaking",
    ]
    
    results = {}
    all_matches = []
    
    for pattern in patterns:
        logger.info(f"\nSearching for pattern: {pattern}")
        matches = extractor.search_class(pattern)
        
        if matches:
            logger.info(f"✓ Found {len(matches)} matches")
            for match in matches:
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                all_matches.append(match)
            results[pattern] = [{"class_name": m.class_name, "line": m.line_number} for m in matches]
        else:
            logger.info(f"✗ No matches for pattern: {pattern}")
            gap = KnowledgeGap(
                category="pvp",
                title=f"PvP classes matching pattern: {pattern}",
                description=f"Searched for PvP-related classes matching pattern '{pattern}' but found no matches.",
                searched_patterns=[pattern],
                searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
                potential_sources=["Server-side logic", "Native ARM code", "Different naming"],
                impact=GapPriority.MEDIUM,
                related_mechanics=["PvP leagues", "Matchmaking", "Promotion/demotion"],
                notes=f"Searched entire dump.cs with pattern: {pattern}"
            )
            gap_tracker.add_gap(gap)
            results[pattern] = []
    
    return {"task_8_1_pvp_search": results, "matches": all_matches}

def task_8_2_league_extraction(extractor, all_matches, logger):
    """Task 8.2: Extract league and matchmaking data"""
    logger.info("\n" + "=" * 80)
    logger.info("TASK 8.2: Extract league and matchmaking data")
    logger.info("=" * 80)
    
    league_data = {}
    
    # Analyze found PvP classes
    for match in all_matches:
        if "League" in match.class_name or "Pvp" in match.class_name:
            logger.info(f"\nAnalyzing {match.class_name} at line {match.line_number}")
            logger.info(f"Content preview (first 30 lines):")
            content_lines = match.content.split('\n')[:30]
            logger.info('\n'.join(content_lines))
            
            league_data[match.class_name] = {
                "line": match.line_number,
                "has_promotion": "Promotion" in match.content,
                "has_demotion": "Demotion" in match.content,
                "has_matchmaking": "Match" in match.content,
                "confidence": "MEDIUM",
                "notes": "Class structure found but specific threshold values may be in config files"
            }
    
    return {"task_8_2_league_extraction": league_data}

def task_9_1_shop_search(extractor, gap_tracker, logger):
    """Task 9.1: Search for shop classes"""
    logger.info("\n" + "=" * 80)
    logger.info("TASK 9.1: Search for shop classes")
    logger.info("=" * 80)
    
    patterns = [
        r"class ShopRefreshConfig",
        r"class PlayerShopModel",
        r"class ShopItem.*",
        r"ShopSeed",
    ]
    
    results = {}
    all_matches = []
    
    for pattern in patterns:
        logger.info(f"\nSearching for pattern: {pattern}")
        matches = extractor.search_class(pattern)
        
        if matches:
            logger.info(f"✓ Found {len(matches)} matches")
            for match in matches[:3]:  # Show first 3
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                all_matches.append(match)
            results[pattern] = [{"class_name": m.class_name, "line": m.line_number} for m in matches]
        else:
            logger.info(f"✗ No matches for pattern: {pattern}")
            results[pattern] = []
    
    return {"task_9_1_shop_search": results, "matches": all_matches}

def task_9_2_shop_mechanics(all_matches, logger):
    """Task 9.2: Analyze shop mechanics"""
    logger.info("\n" + "=" * 80)
    logger.info("TASK 9.2: Analyze shop mechanics")
    logger.info("=" * 80)
    
    shop_mechanics = {}
    
    for match in all_matches:
        logger.info(f"\nAnalyzing {match.class_name} at line {match.line_number}")
        
        has_seed = "Seed" in match.content or "seed" in match.content
        has_refresh = "Refresh" in match.content or "refresh" in match.content
        has_cost = "Cost" in match.content or "cost" in match.content
        
        logger.info(f"  Has seed reference: {has_seed}")
        logger.info(f"  Has refresh reference: {has_refresh}")
        logger.info(f"  Has cost reference: {has_cost}")
        
        shop_mechanics[match.class_name] = {
            "line": match.line_number,
            "has_seed": has_seed,
            "has_refresh": has_refresh,
            "has_cost": has_cost,
            "confidence": "MEDIUM" if (has_refresh or has_cost) else "LOW",
            "notes": "Class structure found. Seeding mechanism unclear from class alone."
        }
    
    return {"task_9_2_shop_mechanics": shop_mechanics}

def task_10_1_combat_search(extractor, logger):
    """Task 10.1: Search for combat classes"""
    logger.info("\n" + "=" * 80)
    logger.info("TASK 10.1: Search for combat classes")
    logger.info("=" * 80)
    
    patterns = [
        r"class AttacksSystem",
        r"class UnitEntity",
        r"class WeaponInfo",
        r"DamageCalculation",
    ]
    
    results = {}
    all_matches = []
    
    for pattern in patterns:
        logger.info(f"\nSearching for pattern: {pattern}")
        matches = extractor.search_class(pattern)
        
        if matches:
            logger.info(f"✓ Found {len(matches)} matches")
            for match in matches[:2]:  # Show first 2
                logger.info(f"  - {match.class_name} at line {match.line_number}")
                all_matches.append(match)
            results[pattern] = [{"class_name": m.class_name, "line": m.line_number} for m in matches]
        else:
            logger.info(f"✗ No matches for pattern: {pattern}")
            results[pattern] = []
    
    return {"task_10_1_combat_search": results, "matches": all_matches}

def task_10_2_combat_formulas(extractor, all_matches, logger):
    """Task 10.2: Extract combat formulas"""
    logger.info("\n" + "=" * 80)
    logger.info("TASK 10.2: Extract combat formulas")
    logger.info("=" * 80)
    
    formulas = {}
    
    # Try to extract specific methods from AttacksSystem
    logger.info("\nSearching for combat formula methods...")
    
    formula_methods = [
        ("AttacksSystem", "GetDamage"),
        ("AttacksSystem", "CalculateAttackTime"),
        ("CombatSystem", "CheckCritical"),
        ("CombatSystem", "CheckDodge"),
        ("CombatSystem", "CheckBlock"),
        ("CombatSystem", "CalculateLifeSteal"),
    ]
    
    for class_name, method_name in formula_methods:
        logger.info(f"\nSearching for {class_name}.{method_name}...")
        method_match = extractor.extract_method(class_name, method_name)
        
        if method_match:
            logger.info(f"✓ Found {method_name} at line {method_match.line_number}")
            logger.info(f"Signature: {method_match.signature}")
            
            formulas[f"{class_name}.{method_name}"] = {
                "class": class_name,
                "method": method_name,
                "line": method_match.line_number,
                "signature": method_match.signature,
                "confidence": "LOW",
                "confidence_reason": "Method found but body empty (IL2CPP limitation)",
                "notes": "Method signature visible but implementation not extractable from dump"
            }
        else:
            logger.info(f"✗ {method_name} not found in {class_name}")
    
    # Analyze found combat classes
    for match in all_matches:
        logger.info(f"\nAnalyzing {match.class_name} for formula hints...")
        content_preview = match.content[:500]
        logger.info(f"Content preview:\n{content_preview}")
    
    return {"task_10_2_combat_formulas": formulas}

def main():
    logger = get_logger()
    logger.info("=" * 80)
    logger.info("BATCH EXECUTION: Tasks 8.1 - 11")
    logger.info("=" * 80)
    
    if not Config.validate():
        logger.error("Configuration validation failed")
        return 1
    
    extractor = CodeExtractor(str(Config.DUMP_PATH))
    gap_tracker = get_tracker()
    
    all_results = {}
    
    # Task 8.1 & 8.2: PvP
    result_8_1 = task_8_1_pvp_search(extractor, gap_tracker, logger)
    all_results.update(result_8_1)
    
    result_8_2 = task_8_2_league_extraction(extractor, result_8_1.get("matches", []), logger)
    all_results.update(result_8_2)
    
    # Task 9.1 & 9.2: Shop
    result_9_1 = task_9_1_shop_search(extractor, gap_tracker, logger)
    all_results.update(result_9_1)
    
    result_9_2 = task_9_2_shop_mechanics(result_9_1.get("matches", []), logger)
    all_results.update(result_9_2)
    
    # Task 10.1 & 10.2: Combat
    result_10_1 = task_10_1_combat_search(extractor, logger)
    all_results.update(result_10_1)
    
    result_10_2 = task_10_2_combat_formulas(extractor, result_10_1.get("matches", []), logger)
    all_results.update(result_10_2)
    
    # Save all results (remove non-serializable matches)
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Remove matches from results before saving
    serializable_results = {}
    for key, value in all_results.items():
        if key != "matches":
            serializable_results[key] = value
    
    output_file = output_dir / "tasks_8_to_11_batch_results.json"
    with open(output_file, 'w') as f:
        json.dump(serializable_results, f, indent=2)
    
    logger.info(f"\n{'=' * 80}")
    logger.info("All results saved to {output_file}")
    logger.info(f"{'=' * 80}")
    
    # Export knowledge gaps
    if gap_tracker.gaps:
        gap_file = output_dir / "tasks_8_to_11_knowledge_gaps.md"
        gap_tracker.export_to_file(str(gap_file))
        logger.info(f"Knowledge gaps exported to {gap_file}")
    
    # Task 11: Checkpoint summary
    logger.info("\n" + "=" * 80)
    logger.info("TASK 11: Checkpoint - Verify all extractions complete")
    logger.info("=" * 80)
    
    logger.info("\nExtraction Summary:")
    logger.info(f"  PvP classes found: {len(result_8_1.get('matches', []))}")
    logger.info(f"  Shop classes found: {len(result_9_1.get('matches', []))}")
    logger.info(f"  Combat classes found: {len(result_10_1.get('matches', []))}")
    logger.info(f"  Total knowledge gaps: {len(gap_tracker.gaps)}")
    
    logger.info("\n" + "=" * 80)
    logger.info("BATCH EXECUTION COMPLETE")
    logger.info("=" * 80)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
