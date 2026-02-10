# Implementation Plan: Game Mechanics Extraction System

## Overview

This implementation plan creates a comprehensive, autonomous system for extracting and documenting all game mechanics from a decompiled mobile game. The system cross-references IL2CPP metadata with Ghidra-decompiled ARM code to produce complete, accurate documentation with minimal human intervention.

## Tasks

- [x] 1. Set up project structure and core infrastructure
  - Create directory structure for extraction system
  - Set up configuration management (YAML config file)
  - Create base classes and interfaces for all components
  - Set up logging system with progress indicators
  - Set up testing framework (pytest + hypothesis)
  - _Requirements: 12.1, 17.5, 18.6_

- [ ] 2. Implement IL2CPP Parser
  - [x] 2.1 Create IL2CPP parser class
    - Parse IL2CPP dump file to extract class definitions
    - Extract method signatures with RVA addresses
    - Extract field and property definitions with MetaMember offsets
    - Handle large files with memory-mapped access
    - _Requirements: 1.1, 18.1_
  
  - [ ]* 2.2 Write property test for IL2CPP parsing
    - **Property 1: Address Mapping Round Trip**
    - **Validates: Requirements 1.1, 1.2, 1.5**
  
  - [ ]* 2.3 Write unit tests for IL2CPP parser
    - Test parsing of known class structures
    - Test extraction of RVA addresses
    - Test handling of malformed input
    - _Requirements: 1.1_

- [ ] 3. Implement Address Mapper
  - [x] 3.1 Create address mapper class
    - Convert RVA addresses to Ghidra function names (0x5AF7094 -> FUN_05af7094)
    - Build bidirectional mapping (IL2CPP <-> Ghidra)
    - Implement mapping persistence (save/load to JSON)
    - _Requirements: 1.2, 1.5, 1.6_
  
  - [ ]* 3.2 Write property test for address mapping
    - **Property 1: Address Mapping Round Trip**
    - **Property 4: Mapping Persistence Round Trip**
    - **Validates: Requirements 1.2, 1.5, 1.6**
  
  - [ ]* 3.3 Write unit tests for address conversion
    - Test known address conversions
    - Test edge cases (short addresses, long addresses)
    - _Requirements: 1.2_

- [ ] 4. Implement Function Extractor
  - [x] 4.1 Create function extractor class
    - Locate function definitions in Ghidra export by name
    - Extract complete function implementation (handle nested braces)
    - Extract numeric constants from function code
    - Analyze code patterns (divisions, comparisons, bit ops, etc.)
    - Handle missing functions gracefully (log and continue)
    - _Requirements: 1.3, 1.4, 2.1_
  
  - [ ]* 4.2 Write property test for function extraction
    - **Property 2: Function Extraction Completeness**
    - **Property 3: Error Resilience**
    - **Validates: Requirements 1.3, 1.4**
  
  - [ ]* 4.3 Write unit tests for function extractor
    - Test extraction of known functions
    - Test handling of missing functions
    - Test constant extraction
    - _Requirements: 1.3, 1.4_

- [x] 5. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Implement Pattern Finder
  - [x] 6.1 Create pattern finder class
    - Implement PCG algorithm detection (constants, bit shifts)
    - Implement drop table detection (float arrays)
    - Implement division operation detection (attack speed)
    - Implement comparison chain detection (rarity determination)
    - Implement bit operation detection (RNG)
    - Implement array access detection (lookup tables)
    - Support custom regex patterns
    - Limit results to prevent overwhelming output
    - _Requirements: 3.1, 4.1, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7_
  
  - [ ]* 6.2 Write property test for pattern detection
    - **Property 5: Pattern Detection Completeness**
    - **Property 25: Pattern Search Customization**
    - **Property 26: Result Limiting**
    - **Validates: Requirements 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7**
  
  - [ ]* 6.3 Write unit tests for pattern finder
    - Test each pattern type with known examples
    - Test custom regex patterns
    - Test result limiting
    - _Requirements: 9.1, 9.2, 9.3, 9.4_

- [ ] 7. Implement Combat Analyzer
  - [x] 7.1 Create combat analyzer class
    - Extract attack speed formula from ARM code
    - Extract damage calculation with all modifiers
    - Extract formulas for all combat stats (HP, crit, dodge, etc.)
    - Extract status effect mechanics
    - Extract base attack times from config or ARM code
    - Cross-reference IL2CPP structures with ARM implementations
    - Assign confidence levels based on verification
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7_
  
  - [ ]* 7.2 Write property test for combat extraction
    - **Property 5: Pattern Detection Completeness**
    - **Property 6: Extraction Completeness**
    - **Property 7: Cross-Reference Validation**
    - **Property 8: Confidence Level Assignment**
    - **Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7**
  
  - [ ]* 7.3 Write unit tests for combat analyzer
    - Test attack speed extraction with known code
    - Test damage calculation extraction
    - Test stat formula extraction
    - _Requirements: 2.1, 2.2, 2.3_

- [ ] 8. Implement Summoning Analyzer
  - [x] 8.1 Create summoning analyzer class
    - Identify RNG algorithm type (PCG, Mersenne Twister, LCG, Xorshift, custom)
    - Extract RNG seed initialization, state update, and output generation
    - Extract drop tables for all summon levels
    - Extract rarity determination algorithm
    - Extract summon level progression thresholds
    - Identify and extract pity system mechanics if present
    - Verify drop table percentages sum to 100%
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7_
  
  - [ ]* 8.2 Write property test for summoning extraction
    - **Property 9: RNG Algorithm Extraction**
    - **Property 10: RNG Algorithm Detection**
    - **Property 13: Drop Table Validation**
    - **Property 14: Drop Table Extraction**
    - **Property 15: Rarity Algorithm Extraction**
    - **Property 16: Progression Threshold Extraction**
    - **Property 17: Pity System Detection**
    - **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4, 4.6, 4.7**
  
  - [ ]* 8.3 Write unit tests for summoning analyzer
    - Test RNG algorithm detection with known implementations
    - Test drop table extraction with known values
    - Test drop table percentage validation
    - _Requirements: 3.1, 4.1, 4.6_

- [ ] 9. Implement PvP Analyzer
  - [x] 9.1 Create PvP analyzer class
    - Extract matchmaking algorithm
    - Extract scoring formulas (win/loss rating changes)
    - Extract PvP stat multipliers (HP, damage, skill modifiers)
    - Extract guild war mechanics (scoring, matchmaking, rewards)
    - Extract arena tier thresholds and rewards
    - Extract PvP-specific damage formulas if different from PvE
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6_
  
  - [ ]* 9.2 Write property test for PvP extraction
    - **Property 18: PvP Mechanics Extraction**
    - **Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5, 5.6**
  
  - [ ]* 9.3 Write unit tests for PvP analyzer
    - Test matchmaking algorithm extraction
    - Test stat multiplier extraction
    - _Requirements: 5.1, 5.3_

- [ ] 10. Implement Progression Analyzer
  - [x] 10.1 Create progression analyzer class
    - Extract tech tree nodes, prerequisites, costs, and bonuses
    - Extract forge mechanics (upgrade costs, success rates, stat improvements)
    - Extract pet leveling (XP formulas, level caps, stat scaling)
    - Extract mount leveling (XP formulas, level caps, stat scaling)
    - Extract skill system (skill trees, unlock conditions, effect formulas)
    - Extract all resource costs for progression activities
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6_
  
  - [ ]* 10.2 Write property test for progression extraction
    - **Property 19: Progression Mechanics Extraction**
    - **Validates: Requirements 6.1, 6.2, 6.3, 6.4, 6.5, 6.6**
  
  - [ ]* 10.3 Write unit tests for progression analyzer
    - Test tech tree extraction
    - Test forge mechanics extraction
    - Test leveling formula extraction
    - _Requirements: 6.1, 6.2, 6.3_

- [ ] 11. Implement Economy Analyzer
  - [x] 11.1 Create economy analyzer class
    - Extract resource generation rates (passive income)
    - Extract shop pricing (base prices, dynamic pricing algorithms)
    - Extract currency conversion rates
    - Extract all resource sinks (action costs)
    - Identify inflation/deflation mechanics if present
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5_
  
  - [ ]* 11.2 Write property test for economy extraction
    - **Property 20: Economy Mechanics Extraction**
    - **Validates: Requirements 7.1, 7.2, 7.3, 7.5**
  
  - [ ]* 11.3 Write unit tests for economy analyzer
    - Test resource generation extraction
    - Test pricing algorithm extraction
    - _Requirements: 7.1, 7.2_

- [x] 12. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 13. Implement Configuration Parser
  - [x] 13.1 Create config parser class
    - Parse binary configuration files (SharedGameConfig.mpa)
    - Identify data types (int, float, double) for numeric constants
    - Preserve array element order and count
    - Extract drop table percentages from config
    - Extract base attack times from config
    - Extract stat scaling coefficients from config
    - Fall back to ARM code extraction if config parsing fails
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7_
  
  - [ ]* 13.2 Write property test for config parsing
    - **Property 21: Configuration Parsing Round Trip**
    - **Property 22: Data Type Preservation**
    - **Property 23: Array Extraction Invariant**
    - **Property 24: Configuration Extraction**
    - **Validates: Requirements 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7**
  
  - [ ]* 13.3 Write unit tests for config parser
    - Test binary file parsing
    - Test data type identification
    - Test fallback to ARM code
    - _Requirements: 8.1, 8.2, 8.7_

- [ ] 14. Implement Verification Engine
  - [x] 14.1 Create verification engine class
    - Verify formulas produce expected outputs for test cases
    - Verify drop table percentages sum to 100% (with tolerance)
    - Verify stat formulas match observed in-game values
    - Assign High confidence when ARM code is found and verified
    - Assign Medium confidence when IL2CPP structure exists but ARM not verified
    - Assign Low confidence when mechanics are inferred from patterns only
    - Flag contradictions between IL2CPP and ARM data
    - Compare constants from IL2CPP and ARM code
    - Verify function call graphs match between IL2CPP and ARM
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 13.2, 13.3, 13.4, 13.5_
  
  - [ ]* 14.2 Write property test for verification
    - **Property 27: Formula Verification**
    - **Property 28: Contradiction Detection**
    - **Property 37: Constant Comparison**
    - **Property 38: Call Graph Verification**
    - **Validates: Requirements 10.1, 10.3, 10.7, 13.2, 13.3, 13.4, 13.5**
  
  - [ ]* 14.3 Write unit tests for verification engine
    - Test formula verification with known test cases
    - Test drop table validation
    - Test confidence level assignment
    - _Requirements: 10.1, 10.2, 10.4, 10.5, 10.6_

- [ ] 15. Implement Documentation Generator
  - [x] 15.1 Create documentation generator class
    - Generate table of contents with links
    - Generate status section showing extraction progress
    - Organize content by game system categories
    - Include formula, data structures, ARM code evidence, confidence level for each mechanic
    - Include examples demonstrating formulas
    - Include source code references (line numbers, function names)
    - Support incremental updates (preserve existing content)
    - Generate optimization strategies based on extracted mechanics
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 15.1, 15.2, 15.3, 15.5_
  
  - [ ]* 15.2 Write property test for documentation generation
    - **Property 29: Documentation Structure**
    - **Property 30: Documentation Completeness**
    - **Property 31: Incremental Documentation Updates**
    - **Property 43: Optimization Strategy Generation**
    - **Validates: Requirements 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 15.1, 15.2, 15.3, 15.5**
  
  - [ ]* 15.3 Write unit tests for documentation generator
    - Test TOC generation
    - Test status section generation
    - Test incremental updates
    - _Requirements: 11.4, 11.5, 11.7_

- [ ] 16. Implement Extraction Pipeline Orchestrator
  - [x] 16.1 Create main extraction pipeline class
    - Orchestrate all components (parser, mapper, extractors, analyzers, verifier, generator)
    - Process all game systems without user intervention
    - Handle errors gracefully (log and continue)
    - Generate summary report after extraction
    - Save progress after each major step (checkpointing)
    - Support resuming from last checkpoint
    - Estimate and display remaining processing time
    - Prioritize high-value systems (combat, summoning) before low-value systems
    - Support parallel processing of independent systems
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 18.4_
  
  - [ ]* 16.2 Write property test for pipeline orchestration
    - **Property 32: Autonomous Execution**
    - **Property 33: Extraction Summary Generation**
    - **Property 34: Checkpoint Persistence**
    - **Property 35: Progress Indication**
    - **Property 36: Priority Ordering**
    - **Property 52: Parallel Processing**
    - **Validates: Requirements 12.1, 12.3, 12.4, 12.5, 12.6, 12.7, 18.4**
  
  - [ ]* 16.3 Write integration tests for full pipeline
    - Test end-to-end extraction with sample data
    - Test checkpoint and resume functionality
    - Test error recovery
    - _Requirements: 12.1, 12.2, 12.4, 12.5_

- [x] 17. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 18. Implement Advanced Features
  - [x] 18.1 Implement selective extraction
    - Support extracting single game system without re-processing everything
    - Support re-scanning with new patterns
    - Support manual overrides for incorrectly extracted mechanics
    - Track which mechanics have been manually verified
    - _Requirements: 14.1, 14.2, 14.3, 14.4, 14.5_
  
  - [x] 18.2 Implement exploit detection
    - Identify unusual patterns or unintended behaviors
    - Flag potential exploits for review
    - _Requirements: 15.4_
  
  - [x] 18.3 Implement multi-format support
    - Support IL2CPP dumps from Unity games
    - Support Ghidra exports from ARM, x86, x64 architectures
    - Support parsing C, C++, and pseudocode decompiler output
    - Attempt format inference for unknown formats
    - _Requirements: 16.1, 16.2, 16.3, 16.4_
  
  - [ ]* 18.4 Write property tests for advanced features
    - **Property 39: Pattern-Triggered Re-scanning**
    - **Property 40: Manual Override Persistence**
    - **Property 41: Verification Status Tracking**
    - **Property 42: Selective Extraction**
    - **Property 44: Exploit Detection**
    - **Property 45: Multi-Format Support**
    - **Property 46: Format Inference**
    - **Validates: Requirements 14.2, 14.3, 14.4, 14.5, 15.4, 16.1, 16.2, 16.3, 16.4**

- [ ] 19. Implement Performance Optimizations
  - [x] 19.1 Implement memory-mapped file access
    - Use memory-mapped files for files > 100MB
    - Implement chunked processing for large files
    - _Requirements: 17.3, 18.1_
  
  - [x] 19.2 Implement caching
    - Cache parsed IL2CPP data
    - Cache address mappings
    - Skip already-extracted mechanics when resuming
    - _Requirements: 18.3, 18.5_
  
  - [x] 19.3 Optimize regex performance
    - Compile regex patterns once and reuse
    - Use optimized regex engines
    - _Requirements: 18.2_
  
  - [ ]* 19.4 Write property tests for performance features
    - **Property 47: Chunked Processing**
    - **Property 50: Memory-Mapped File Access**
    - **Property 51: IL2CPP Caching**
    - **Validates: Requirements 17.3, 18.1, 18.3**

- [ ] 20. Implement Export and Visualization
  - [x] 20.1 Implement data export
    - Export to JSON format
    - Export to CSV format
    - Export drop tables in simulation-friendly format
    - Export stat formulas in calculator-friendly format
    - Provide programmatic API for data access
    - _Requirements: 19.1, 19.2, 19.3, 19.4, 19.5_
  
  - [x] 20.2 Implement visualization generation
    - Generate bar charts for drop table distributions
    - Generate line graphs for stat scaling curves
    - Generate node graphs for tech tree dependencies
    - Generate summary dashboard showing extraction completeness
    - Generate comparison charts for PvE vs PvP stats
    - _Requirements: 20.1, 20.2, 20.3, 20.4, 20.5_
  
  - [ ]* 20.3 Write property tests for export and visualization
    - **Property 53: Export Format Validity**
    - **Property 54: API Data Access**
    - **Property 55: Visualization Generation**
    - **Validates: Requirements 19.1, 19.2, 19.3, 19.4, 19.5, 20.1, 20.2, 20.3, 20.4, 20.5**

- [ ] 21. Implement Error Handling and Validation
  - [x] 21.1 Implement comprehensive error handling
    - Handle file access errors (missing, permission denied, corrupted)
    - Handle parse errors (invalid syntax, unexpected format)
    - Handle memory errors (out of memory, file too large)
    - Handle validation errors (invalid data, contradictions)
    - Provide detailed error messages with context
    - Validate all extracted data before writing to documentation
    - _Requirements: 17.1, 17.2, 17.3, 17.4, 17.5_
  
  - [ ]* 21.2 Write property tests for error handling
    - **Property 3: Error Resilience**
    - **Property 48: Data Validation**
    - **Property 49: Detailed Error Messages**
    - **Validates: Requirements 17.1, 17.2, 17.4, 17.5**

- [ ] 22. Create Command-Line Interface
  - [x] 22.1 Implement CLI with argparse
    - Support full extraction mode
    - Support single system extraction mode
    - Support resume from checkpoint mode
    - Support verify-only mode
    - Support visualization generation mode
    - Load configuration from YAML file
    - Display real-time progress updates
    - _Requirements: 12.1, 12.6, 14.5, 18.6_
  
  - [ ]* 22.2 Write integration tests for CLI
    - Test all CLI modes
    - Test configuration loading
    - Test progress display
    - _Requirements: 12.1, 12.6_

- [ ] 23. Create Documentation and Examples
  - [x] 23.1 Write user documentation
    - Installation instructions
    - Configuration file format
    - CLI usage examples
    - Troubleshooting guide
    - _Requirements: 12.1_
  
  - [x] 23.2 Create example configuration files
    - Sample config.yaml with all options
    - Example IL2CPP dump snippet
    - Example Ghidra export snippet
    - _Requirements: 12.1_
  
  - [x] 23.3 Write developer documentation
    - Architecture overview
    - Component interfaces
    - Extension guide (adding new analyzers, patterns, etc.)
    - _Requirements: 12.1_

- [ ] 24. Final Integration and Testing
  - [x] 24.1 Run full extraction on actual game data
    - Test with real IL2CPP dump and Ghidra export
    - Verify all game systems are extracted
    - Verify documentation quality
    - Verify confidence levels are accurate
    - _Requirements: 12.1, 12.3_
  
  - [x] 24.2 Performance testing
    - Measure extraction time for full run
    - Measure memory usage
    - Verify parallel processing works correctly
    - Verify caching improves performance
    - _Requirements: 18.1, 18.2, 18.3, 18.4_
  
  - [x] 24.3 Verify output quality
    - Review generated COMPLETE_GAME_MECHANICS_MANUAL.md
    - Verify all mechanics are documented
    - Verify formulas are correct
    - Verify code references are accurate
    - Verify optimization strategies are useful
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 15.1, 15.2, 15.3_

- [x] 25. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional property-based and unit tests that can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties across all inputs
- Unit tests validate specific examples and edge cases
- The system is designed for autonomous operation with minimal user intervention
- Python 3.9+ is used as the implementation language
- The extraction pipeline processes systems in priority order: Combat → Summoning → PvP → Progression → Economy
- All extracted mechanics include confidence levels (High/Medium/Low) based on verification completeness
