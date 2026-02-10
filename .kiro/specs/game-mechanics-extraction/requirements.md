# Requirements Document: Game Mechanics Extraction System

## Introduction

This system extracts and documents ALL game mechanics from a decompiled mobile game by cross-referencing IL2CPP dump metadata with Ghidra-decompiled ARM code. The goal is complete, accurate documentation of every game system with minimal human intervention.

## Glossary

- **IL2CPP_Dump**: C# metadata file containing class/method names and RVA addresses
- **Ghidra_Export**: Decompiled C code (~1.5GB) with ARM implementation but generic function names
- **RVA_Address**: Relative Virtual Address used to map IL2CPP methods to Ghidra functions
- **Mechanics_Manual**: Comprehensive markdown document containing all extracted game mechanics
- **Extraction_Tool**: Python script that automates mechanics extraction
- **Pattern_Finder**: Tool that searches for specific code patterns (RNG, drop tables, etc.)
- **Address_Mapper**: Tool that maps IL2CPP addresses to Ghidra function names
- **Confidence_Level**: Rating (High/Medium/Low) indicating verification status of extracted mechanics
- **Game_System**: Major category of mechanics (Combat, Summoning, PvP, Progression, Economy)
- **Config_Parser**: Tool that extracts numeric values from binary configuration files
- **Verification_Test**: Automated test that validates extracted mechanics against game behavior

## Requirements

### Requirement 1: IL2CPP to Ghidra Address Mapping

**User Story:** As a reverse engineer, I want to map IL2CPP method addresses to Ghidra functions, so that I can identify what each decompiled function does.

#### Acceptance Criteria

1. WHEN the Address_Mapper processes the IL2CPP_Dump, THE System SHALL extract all RVA addresses and associated method names
2. WHEN an RVA address is extracted, THE System SHALL convert it to the corresponding Ghidra function name format (FUN_XXXXXXXX)
3. WHEN searching for a Ghidra function, THE System SHALL locate the function definition and extract its complete implementation
4. WHEN a function cannot be found, THE System SHALL log the missing function and continue processing
5. THE Address_Mapper SHALL create a bidirectional mapping between IL2CPP names and Ghidra function names
6. THE System SHALL save the address mapping to a persistent file for reuse

### Requirement 2: Combat System Extraction

**User Story:** As a game analyst, I want to extract all combat mechanics, so that I can understand and document how combat works.

#### Acceptance Criteria

1. WHEN extracting attack speed mechanics, THE System SHALL identify the formula relating base attack time to attack speed multiplier
2. WHEN extracting damage calculation, THE System SHALL identify all damage modifiers (critical hits, double damage, blocks, dodges)
3. WHEN extracting combat stats, THE System SHALL document formulas for HP, damage, move speed, crit chance, crit multiplier, block, dodge, life steal, and health regen
4. WHEN extracting status effects, THE System SHALL identify all buff/debuff types and their application logic
5. THE System SHALL extract base attack times for all weapon types from configuration data
6. THE System SHALL verify extracted formulas by identifying the ARM code that implements them
7. THE System SHALL assign confidence levels based on verification completeness

### Requirement 3: Random Number Generation Extraction

**User Story:** As a game analyst, I want to understand the RNG system, so that I can document how randomness affects game outcomes.

#### Acceptance Criteria

1. WHEN searching for RNG algorithms, THE System SHALL check for PCG, Mersenne Twister, LCG, and Xorshift implementations
2. WHEN an RNG algorithm is found, THE System SHALL extract the seed initialization logic
3. WHEN an RNG algorithm is found, THE System SHALL extract the state update logic
4. WHEN an RNG algorithm is found, THE System SHALL extract the output generation logic
5. THE System SHALL identify all locations where random numbers are consumed
6. THE System SHALL document seed storage mechanisms (per-player, per-system)
7. IF no standard RNG is found, THE System SHALL document the custom RNG implementation

### Requirement 4: Summoning System Extraction

**User Story:** As a game analyst, I want to extract summoning mechanics, so that I can document drop rates and rarity determination.

#### Acceptance Criteria

1. WHEN extracting drop tables, THE System SHALL identify all rarity tiers and their percentage chances
2. WHEN extracting drop tables, THE System SHALL identify how drop chances scale with summon level
3. WHEN extracting rarity determination, THE System SHALL identify the algorithm that converts random numbers to rarity outcomes
4. WHEN extracting summon progression, THE System SHALL identify the thresholds for leveling up summon systems
5. THE System SHALL extract drop tables for mounts, pets, eggs, and any other summonable items
6. THE System SHALL verify drop table percentages sum to 100% (or identify pity systems)
7. THE System SHALL extract pity system mechanics if present

### Requirement 5: PvP System Extraction

**User Story:** As a game analyst, I want to extract PvP mechanics, so that I can document matchmaking, scoring, and stat modifications.

#### Acceptance Criteria

1. WHEN extracting PvP matchmaking, THE System SHALL identify the algorithm that pairs players
2. WHEN extracting PvP scoring, THE System SHALL identify how wins/losses affect ratings
3. WHEN extracting PvP stat modifiers, THE System SHALL identify all stat multipliers that differ from PvE
4. WHEN extracting guild war mechanics, THE System SHALL identify scoring, matchmaking, and reward distribution
5. THE System SHALL extract arena tier thresholds and rewards
6. THE System SHALL extract PvP-specific damage formulas if they differ from PvE

### Requirement 6: Progression System Extraction

**User Story:** As a game analyst, I want to extract progression mechanics, so that I can document tech trees, forge systems, and leveling.

#### Acceptance Criteria

1. WHEN extracting tech tree mechanics, THE System SHALL identify all nodes, prerequisites, costs, and bonuses
2. WHEN extracting forge mechanics, THE System SHALL identify upgrade costs, success rates, and stat improvements
3. WHEN extracting pet leveling, THE System SHALL identify experience formulas, level caps, and stat scaling
4. WHEN extracting mount leveling, THE System SHALL identify experience formulas, level caps, and stat scaling
5. WHEN extracting skill systems, THE System SHALL identify skill trees, unlock conditions, and effect formulas
6. THE System SHALL extract all resource costs for progression activities

### Requirement 7: Economy System Extraction

**User Story:** As a game analyst, I want to extract economy mechanics, so that I can document resource generation, costs, and shop pricing.

#### Acceptance Criteria

1. WHEN extracting resource generation, THE System SHALL identify all passive income sources and their rates
2. WHEN extracting shop pricing, THE System SHALL identify base prices and dynamic pricing algorithms
3. WHEN extracting currency conversion, THE System SHALL identify exchange rates between currency types
4. THE System SHALL extract all resource sinks (costs for actions)
5. THE System SHALL identify any inflation or deflation mechanics

### Requirement 8: Configuration Data Extraction

**User Story:** As a reverse engineer, I want to extract numeric values from configuration files, so that I can document exact game parameters.

#### Acceptance Criteria

1. WHEN the Config_Parser encounters a binary configuration file, THE System SHALL parse its structure
2. WHEN extracting numeric constants, THE System SHALL identify their data types (int, float, double)
3. WHEN extracting arrays, THE System SHALL preserve element order and count
4. THE System SHALL extract drop table percentages from configuration data
5. THE System SHALL extract base attack times from configuration data
6. THE System SHALL extract all stat scaling coefficients from configuration data
7. IF configuration parsing fails, THE System SHALL fall back to extracting hardcoded constants from ARM code

### Requirement 9: Pattern Recognition and Search

**User Story:** As a reverse engineer, I want to search for code patterns, so that I can locate specific mechanics in the decompiled code.

#### Acceptance Criteria

1. WHEN searching for division operations, THE Pattern_Finder SHALL identify all float/double divisions with surrounding context
2. WHEN searching for comparison chains, THE Pattern_Finder SHALL identify sequences of 4+ consecutive if statements
3. WHEN searching for array accesses, THE Pattern_Finder SHALL identify array indexing patterns that suggest lookup tables
4. WHEN searching for bit operations, THE Pattern_Finder SHALL identify shifts, XORs, and rotations that suggest RNG or hashing
5. THE Pattern_Finder SHALL support custom regex patterns for user-defined searches
6. THE Pattern_Finder SHALL limit results to prevent overwhelming output
7. THE Pattern_Finder SHALL provide configurable context lines around matches

### Requirement 10: Automated Verification

**User Story:** As a game analyst, I want to verify extracted mechanics, so that I can ensure documentation accuracy.

#### Acceptance Criteria

1. WHEN a formula is extracted, THE Verification_Test SHALL check if it produces expected outputs for known inputs
2. WHEN drop tables are extracted, THE Verification_Test SHALL verify percentages sum correctly
3. WHEN stat formulas are extracted, THE Verification_Test SHALL verify they match observed in-game values
4. THE System SHALL assign High confidence when ARM code is found and verified
5. THE System SHALL assign Medium confidence when IL2CPP structure is found but ARM code is not verified
6. THE System SHALL assign Low confidence when mechanics are inferred from patterns only
7. THE System SHALL flag contradictions between IL2CPP metadata and ARM implementation

### Requirement 11: Comprehensive Documentation Generation

**User Story:** As a game analyst, I want a complete mechanics manual, so that I have a single reference for all game systems.

#### Acceptance Criteria

1. WHEN generating the Mechanics_Manual, THE System SHALL organize content by game system categories
2. WHEN documenting a mechanic, THE System SHALL include the formula, data structures, ARM code evidence, and confidence level
3. WHEN documenting a mechanic, THE System SHALL include examples demonstrating the formula
4. THE Mechanics_Manual SHALL include a table of contents with links to all sections
5. THE Mechanics_Manual SHALL include a status section showing extraction progress for each game system
6. THE Mechanics_Manual SHALL include references to source code locations (line numbers, function names)
7. THE Mechanics_Manual SHALL be updated incrementally as new mechanics are extracted

### Requirement 12: Autonomous Extraction Pipeline

**User Story:** As a user, I want the system to run autonomously, so that I can walk away and return to complete documentation.

#### Acceptance Criteria

1. WHEN the Extraction_Tool is started, THE System SHALL process all game systems without user intervention
2. WHEN an error occurs, THE System SHALL log the error and continue with the next extraction task
3. WHEN extraction is complete, THE System SHALL generate a summary report of what was extracted
4. THE System SHALL save progress after each major extraction step
5. THE System SHALL support resuming from the last saved checkpoint
6. THE System SHALL estimate and display remaining processing time
7. THE System SHALL prioritize high-value mechanics (combat, summoning) before low-value mechanics (cosmetics)

### Requirement 13: Cross-Reference Validation

**User Story:** As a reverse engineer, I want to cross-reference IL2CPP and Ghidra data, so that I can validate extracted mechanics.

#### Acceptance Criteria

1. WHEN a mechanic is extracted from IL2CPP, THE System SHALL locate the corresponding ARM implementation in Ghidra
2. WHEN ARM code is found, THE System SHALL verify it matches the IL2CPP data structure
3. WHEN discrepancies are found, THE System SHALL flag them for manual review
4. THE System SHALL extract constants from both IL2CPP and ARM code and compare them
5. THE System SHALL verify function call graphs match between IL2CPP and ARM code

### Requirement 14: Incremental Extraction and Updates

**User Story:** As a game analyst, I want to extract mechanics incrementally, so that I can review and refine documentation as I go.

#### Acceptance Criteria

1. WHEN a game system is extracted, THE System SHALL update the Mechanics_Manual immediately
2. WHEN new patterns are discovered, THE System SHALL re-scan previously processed code
3. THE System SHALL support manual overrides for incorrectly extracted mechanics
4. THE System SHALL track which mechanics have been manually verified by the user
5. THE System SHALL support extracting a single game system without re-processing everything

### Requirement 15: Optimization Strategy Documentation

**User Story:** As a game player, I want optimization strategies documented, so that I can play more effectively.

#### Acceptance Criteria

1. WHEN combat mechanics are extracted, THE System SHALL generate optimization strategies for maximizing damage
2. WHEN summoning mechanics are extracted, THE System SHALL generate strategies for maximizing rare drops
3. WHEN progression mechanics are extracted, THE System SHALL generate strategies for efficient resource usage
4. THE System SHALL identify any exploits or unintended mechanics
5. THE System SHALL document optimal build paths based on stat scaling

### Requirement 16: Multi-Language Support

**User Story:** As a reverse engineer, I want to handle different programming languages, so that the system works with various game engines.

#### Acceptance Criteria

1. THE System SHALL support IL2CPP dumps from Unity games
2. THE System SHALL support Ghidra exports from ARM, x86, and x64 architectures
3. THE System SHALL support parsing C, C++, and pseudocode decompiler output
4. IF the decompiler output format is unknown, THE System SHALL attempt to infer the format

### Requirement 17: Error Handling and Robustness

**User Story:** As a user, I want the system to handle errors gracefully, so that extraction doesn't fail completely on edge cases.

#### Acceptance Criteria

1. WHEN a file cannot be read, THE System SHALL log the error and skip that file
2. WHEN a function cannot be parsed, THE System SHALL log the error and continue with the next function
3. WHEN memory limits are reached, THE System SHALL process the file in chunks
4. THE System SHALL validate all extracted data before writing to the Mechanics_Manual
5. THE System SHALL provide detailed error messages with context for debugging

### Requirement 18: Performance Optimization

**User Story:** As a user, I want extraction to complete in reasonable time, so that I don't wait days for results.

#### Acceptance Criteria

1. WHEN processing large files, THE System SHALL use memory-mapped file access
2. WHEN searching for patterns, THE System SHALL use optimized regex engines
3. THE System SHALL cache parsed IL2CPP data to avoid re-parsing
4. THE System SHALL process independent game systems in parallel
5. THE System SHALL skip already-extracted mechanics when resuming
6. THE System SHALL provide progress indicators showing percentage complete

### Requirement 19: Data Export and Integration

**User Story:** As a developer, I want to export extracted data, so that I can use it in other tools.

#### Acceptance Criteria

1. THE System SHALL export extracted mechanics to JSON format
2. THE System SHALL export extracted mechanics to CSV format for spreadsheet analysis
3. THE System SHALL export drop tables in a format suitable for simulation tools
4. THE System SHALL export stat formulas in a format suitable for calculator tools
5. THE System SHALL provide an API for programmatic access to extracted data

### Requirement 20: Visualization and Reporting

**User Story:** As a game analyst, I want visual representations of mechanics, so that I can understand complex systems more easily.

#### Acceptance Criteria

1. WHEN drop tables are extracted, THE System SHALL generate bar charts showing rarity distributions
2. WHEN stat scaling is extracted, THE System SHALL generate line graphs showing stat growth curves
3. WHEN tech trees are extracted, THE System SHALL generate node graphs showing dependencies
4. THE System SHALL generate a summary dashboard showing extraction completeness
5. THE System SHALL generate comparison charts for PvE vs PvP stat differences
