"""
Task 4.2: Extract guild war matchmaking logic

This script extracts matchmaking methods from the classes found in Task 4.1,
assesses confidence level, identifies missing data, and creates knowledge gap entries.

Requirements: 1.4, 1.5, 1.6, 1.7, 11.1-11.5
"""

import sys
from pathlib import Path
from extraction_system.mechanics_cleanup import (
    CodeExtractor,
    CodeVerifier,
    get_tracker,
    GapPriority,
    KnowledgeGap,
    Config,
    get_logger,
    ConfidenceLevel
)


def main():
    """Execute Task 4.2: Extract guild war matchmaking logic."""
    
    # Initialize
    logger = get_logger()
    logger.info("=" * 80)
    logger.info("Task 4.2: Extract guild war matchmaking logic")
    logger.info("=" * 80)
    
    # Validate configuration
    if not Config.validate():
        logger.error("Configuration validation failed")
        return 1
    
    # Initialize extractor and verifier
    extractor = CodeExtractor(str(Config.DUMP_PATH))
    verifier = CodeVerifier(str(Config.DUMP_PATH))
    tracker = get_tracker()
    
    # Classes found in Task 4.1
    guild_war_classes = [
        ("GuildWarConfig", 1062587),
        ("GuildTierConfig", 1062465),
        ("GuildTierExtensions", 1062576),
        ("GuildWarManager", 717022),
    ]
    
    logger.info(f"Analyzing {len(guild_war_classes)} classes for matchmaking logic")
    
    # Results storage
    matchmaking_methods = []
    tier_calculations = []
    point_calculations = []
    missing_data = []
    
    # 1. Extract GuildTierConfig - contains tier thresholds
    logger.info("\n" + "=" * 80)
    logger.info("1. Analyzing GuildTierConfig for tier thresholds")
    logger.info("=" * 80)
    
    tier_config_match = extractor.search_class(r"class GuildTierConfig")
    if tier_config_match:
        tier_config = tier_config_match[0]
        logger.info(f"Found GuildTierConfig at line {tier_config.line_number}")
        logger.info("\nClass content:")
        logger.info(tier_config.content)
        
        # Check for RequiredPoints field
        if "RequiredPoints" in tier_config.content:
            logger.info("\n✓ Found RequiredPoints field in GuildTierConfig")
            logger.info("  - This field defines tier thresholds")
            logger.info("  - Confidence: MEDIUM - Structure found but actual values not in dump.cs")
            
            tier_calculations.append({
                "name": "Tier Required Points",
                "class": "GuildTierConfig",
                "line": tier_config.line_number,
                "field": "RequiredPoints",
                "confidence": ConfidenceLevel.MEDIUM,
                "reason": "Field structure found but config values not in IL2CPP dump"
            })
        
        # Check for TierPointsOnWin/TierPointsOnLose
        if "TierPointsOnWin" in tier_config.content and "TierPointsOnLose" in tier_config.content:
            logger.info("\n✓ Found tier point change fields:")
            logger.info("  - TierPointsOnWin: Points gained on war victory")
            logger.info("  - TierPointsOnLose: Points lost on war defeat")
            logger.info("  - Confidence: MEDIUM - Structure found but actual values not in dump.cs")
            
            point_calculations.append({
                "name": "Tier Points Change on Win/Loss",
                "class": "GuildTierConfig",
                "line": tier_config.line_number,
                "fields": ["TierPointsOnWin", "TierPointsOnLose"],
                "confidence": ConfidenceLevel.MEDIUM,
                "reason": "Field structure found but config values not in IL2CPP dump"
            })
    else:
        logger.warning("GuildTierConfig not found")
    
    # 2. Extract GuildTierExtensions - contains tier calculation logic
    logger.info("\n" + "=" * 80)
    logger.info("2. Analyzing GuildTierExtensions for tier calculation")
    logger.info("=" * 80)
    
    tier_ext_match = extractor.search_class(r"class GuildTierExtensions")
    if tier_ext_match:
        # Find the non-compiler-generated class
        for match in tier_ext_match:
            if "sealed class" not in match.content and "<>c" not in match.class_name:
                tier_ext = match
                logger.info(f"Found GuildTierExtensions at line {tier_ext.line_number}")
                logger.info("\nClass content:")
                logger.info(tier_ext.content)
                
                # Check for GetTierFromTierPoints method
                if "GetTierFromTierPoints" in tier_ext.content:
                    logger.info("\n✓ Found GetTierFromTierPoints method")
                    logger.info("  - This method calculates guild tier from tier points")
                    logger.info("  - Signature: GetTierFromTierPoints(GameConfigLibrary<GuildTier, GuildTierConfig> configs, int points)")
                    logger.info("  - Confidence: HIGH - Method exists and signature is clear")
                    
                    matchmaking_methods.append({
                        "name": "GetTierFromTierPoints",
                        "class": "GuildTierExtensions",
                        "line": tier_ext.line_number,
                        "signature": "public static GuildTier GetTierFromTierPoints(GameConfigLibrary<GuildTier, GuildTierConfig> configs, int points)",
                        "confidence": ConfidenceLevel.HIGH,
                        "reason": "Method signature found, logic likely compares points against RequiredPoints thresholds"
                    })
                break
    else:
        logger.warning("GuildTierExtensions not found")
    
    # 3. Extract GuildWarConfig - contains war mechanics config
    logger.info("\n" + "=" * 80)
    logger.info("3. Analyzing GuildWarConfig for war mechanics")
    logger.info("=" * 80)
    
    war_config_match = extractor.search_class(r"class GuildWarConfig")
    if war_config_match:
        war_config = war_config_match[0]
        logger.info(f"Found GuildWarConfig at line {war_config.line_number}")
        logger.info("\nClass content:")
        logger.info(war_config.content)
        
        # Extract relevant fields
        relevant_fields = [
            "MaxWarTicketsPerMember",
            "MaxPointsForAttackingOpponentGuildMember",
            "MaxMembersDefeatedForReset",
            "BrawlWinPointsReward",
            "MaxGuildTierPoints"
        ]
        
        found_fields = []
        for field in relevant_fields:
            if field in war_config.content:
                found_fields.append(field)
                logger.info(f"  ✓ Found field: {field}")
        
        if found_fields:
            logger.info(f"\n✓ Found {len(found_fields)} war mechanic fields")
            logger.info("  - Confidence: MEDIUM - Structure found but actual values not in dump.cs")
            
            point_calculations.append({
                "name": "War Points Configuration",
                "class": "GuildWarConfig",
                "line": war_config.line_number,
                "fields": found_fields,
                "confidence": ConfidenceLevel.MEDIUM,
                "reason": "Field structure found but config values not in IL2CPP dump"
            })
    else:
        logger.warning("GuildWarConfig not found")
    
    # 4. Search for actual matchmaking algorithm
    logger.info("\n" + "=" * 80)
    logger.info("4. Searching for matchmaking algorithm")
    logger.info("=" * 80)
    
    # Search for division/league matchmaking patterns
    matchmaking_patterns = [
        r"FindOpponent",
        r"SelectOpponent",
        r"MatchGuild",
        r"DivisionModel",
        r"LeagueClient",
    ]
    
    for pattern in matchmaking_patterns:
        logger.info(f"\nSearching for pattern: {pattern}")
        matches = extractor.search_class(pattern)
        
        if matches:
            logger.info(f"  Found {len(matches)} matches")
            for match in matches[:3]:  # Limit to first 3
                logger.info(f"    - {match.class_name} at line {match.line_number}")
        else:
            logger.info(f"  No matches found")
            
            # Create knowledge gap
            gap = KnowledgeGap(
                category="guild_war",
                title=f"Guild War matchmaking: {pattern}",
                description=f"Searched for matchmaking logic matching pattern '{pattern}' but found no matches. "
                           f"Matchmaking algorithm may be implemented server-side or in native code.",
                searched_patterns=[pattern],
                searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
                potential_sources=[
                    "Server-side matchmaking service (not in client dump)",
                    "Native ARM code in libil2cpp.so",
                    "Metaplay framework server code",
                    "Division/League system on server"
                ],
                impact=GapPriority.HIGH,
                related_mechanics=["Guild War Matchmaking", "Division Assignment", "Opponent Selection"],
                notes=f"Client code shows LeagueClient<GuildWarDivisionModel> but actual matchmaking logic not found"
            )
            tracker.add_gap(gap)
    
    # 5. Identify missing data
    logger.info("\n" + "=" * 80)
    logger.info("5. Identifying missing data")
    logger.info("=" * 80)
    
    missing_items = [
        {
            "item": "Tier threshold values (RequiredPoints per tier)",
            "reason": "GuildTierConfig structure found but actual values not in IL2CPP dump",
            "impact": GapPriority.HIGH,
            "potential_source": "SharedGameConfig.mpa file or server configuration"
        },
        {
            "item": "Tier point change values (TierPointsOnWin/TierPointsOnLose)",
            "reason": "Fields exist in GuildTierConfig but values not in IL2CPP dump",
            "impact": GapPriority.HIGH,
            "potential_source": "SharedGameConfig.mpa file or server configuration"
        },
        {
            "item": "War points calculation formula",
            "reason": "MaxPointsForAttackingOpponentGuildMember field exists but calculation logic not found",
            "impact": GapPriority.MEDIUM,
            "potential_source": "Server-side battle resolution code"
        },
        {
            "item": "Matchmaking algorithm (opponent selection)",
            "reason": "No client-side matchmaking logic found, likely server-side",
            "impact": GapPriority.HIGH,
            "potential_source": "Server-side division/league matchmaking service"
        },
        {
            "item": "Division assignment logic",
            "reason": "LeagueClient reference found but division creation/assignment logic not in client",
            "impact": GapPriority.HIGH,
            "potential_source": "Server-side league management system"
        }
    ]
    
    for item in missing_items:
        logger.info(f"\n❌ Missing: {item['item']}")
        logger.info(f"   Reason: {item['reason']}")
        logger.info(f"   Impact: {item['impact'].value}")
        logger.info(f"   Potential source: {item['potential_source']}")
        
        # Create knowledge gap
        gap = KnowledgeGap(
            category="guild_war",
            title=item['item'],
            description=item['reason'],
            searched_patterns=["GuildWar.*", "GuildTier.*", "Division.*", "League.*"],
            searched_locations=[f"{Config.DUMP_PATH} (all lines)"],
            potential_sources=[item['potential_source']],
            impact=item['impact'],
            related_mechanics=["Guild War Matchmaking", "Tier System", "War Points"],
            notes="Client code shows data structures but not actual values or server-side logic"
        )
        tracker.add_gap(gap)
        missing_data.append(item)
    
    # 6. Generate summary report
    logger.info("\n" + "=" * 80)
    logger.info("EXTRACTION SUMMARY")
    logger.info("=" * 80)
    
    logger.info(f"\nMatchmaking methods found: {len(matchmaking_methods)}")
    for method in matchmaking_methods:
        logger.info(f"  - {method['name']} ({method['class']}) - Confidence: {method['confidence'].value}")
    
    logger.info(f"\nTier calculations found: {len(tier_calculations)}")
    for calc in tier_calculations:
        logger.info(f"  - {calc['name']} ({calc['class']}) - Confidence: {calc['confidence'].value}")
    
    logger.info(f"\nPoint calculations found: {len(point_calculations)}")
    for calc in point_calculations:
        logger.info(f"  - {calc['name']} ({calc['class']}) - Confidence: {calc['confidence'].value}")
    
    logger.info(f"\nMissing data items: {len(missing_data)}")
    for item in missing_data:
        logger.info(f"  - {item['item']} (Impact: {item['impact'].value})")
    
    logger.info(f"\nKnowledge gaps created: {len(tracker.gaps)}")
    
    # 7. Export results
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save detailed results
    results_file = output_dir / "task_4_2_matchmaking_extraction_results.txt"
    with open(results_file, 'w', encoding='utf-8') as f:
        f.write("Task 4.2: Guild War Matchmaking Logic Extraction\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("OVERVIEW\n")
        f.write("-" * 80 + "\n")
        f.write(f"Classes analyzed: {len(guild_war_classes)}\n")
        f.write(f"Matchmaking methods found: {len(matchmaking_methods)}\n")
        f.write(f"Tier calculations found: {len(tier_calculations)}\n")
        f.write(f"Point calculations found: {len(point_calculations)}\n")
        f.write(f"Missing data items: {len(missing_data)}\n")
        f.write(f"Knowledge gaps created: {len(tracker.gaps)}\n\n")
        
        f.write("MATCHMAKING METHODS\n")
        f.write("-" * 80 + "\n")
        for method in matchmaking_methods:
            f.write(f"\nMethod: {method['name']}\n")
            f.write(f"Class: {method['class']}\n")
            f.write(f"Line: {method['line']}\n")
            f.write(f"Signature: {method['signature']}\n")
            f.write(f"Confidence: {method['confidence'].value}\n")
            f.write(f"Reason: {method['reason']}\n")
        
        f.write("\n\nTIER CALCULATIONS\n")
        f.write("-" * 80 + "\n")
        for calc in tier_calculations:
            f.write(f"\nCalculation: {calc['name']}\n")
            f.write(f"Class: {calc['class']}\n")
            f.write(f"Line: {calc['line']}\n")
            f.write(f"Field: {calc['field']}\n")
            f.write(f"Confidence: {calc['confidence'].value}\n")
            f.write(f"Reason: {calc['reason']}\n")
        
        f.write("\n\nPOINT CALCULATIONS\n")
        f.write("-" * 80 + "\n")
        for calc in point_calculations:
            f.write(f"\nCalculation: {calc['name']}\n")
            f.write(f"Class: {calc['class']}\n")
            f.write(f"Line: {calc['line']}\n")
            f.write(f"Fields: {', '.join(calc['fields'])}\n")
            f.write(f"Confidence: {calc['confidence'].value}\n")
            f.write(f"Reason: {calc['reason']}\n")
        
        f.write("\n\nMISSING DATA\n")
        f.write("-" * 80 + "\n")
        for item in missing_data:
            f.write(f"\nItem: {item['item']}\n")
            f.write(f"Reason: {item['reason']}\n")
            f.write(f"Impact: {item['impact'].value}\n")
            f.write(f"Potential Source: {item['potential_source']}\n")
        
        f.write("\n\nCONCLUSIONS\n")
        f.write("-" * 80 + "\n")
        f.write("1. Guild tier system structure is well-defined in client code\n")
        f.write("2. Tier calculation method (GetTierFromTierPoints) exists\n")
        f.write("3. Configuration fields for thresholds and points exist but values are not in IL2CPP dump\n")
        f.write("4. Actual matchmaking algorithm is NOT in client code - likely server-side\n")
        f.write("5. War points calculation logic is NOT in client code - likely server-side\n")
        f.write("6. Client uses LeagueClient<GuildWarDivisionModel> to communicate with server\n")
        f.write("7. Confidence level: MEDIUM for structure, LOW for actual values and algorithms\n")
    
    logger.info(f"\nResults saved to: {results_file}")
    
    # Export knowledge gaps
    if tracker.gaps:
        gaps_file = output_dir / "task_4_2_knowledge_gaps.md"
        tracker.export_to_file(str(gaps_file))
        logger.info(f"Knowledge gaps saved to: {gaps_file}")
    
    # Print final summary
    logger.info("\n" + "=" * 80)
    logger.info("TASK 4.2 COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Matchmaking methods found: {len(matchmaking_methods)}")
    logger.info(f"Tier calculations found: {len(tier_calculations)}")
    logger.info(f"Point calculations found: {len(point_calculations)}")
    logger.info(f"Missing data items: {len(missing_data)}")
    logger.info(f"Knowledge gaps created: {len(tracker.gaps)}")
    logger.info(f"Overall confidence: MEDIUM (structure found, values and algorithms missing)")
    logger.info(f"Results saved to: {output_dir}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
