# Implementation Plan: Mechanics Cleanup

## Overview

This implementation plan extracts missing game mechanics from the IL2CPP dump (C:\apktool\il2cpp-output\dump.cs) and updates the GitHub Pages documentation with code-verified information. The approach follows a strict zero-hallucination policy: verify everything, assume nothing, and explicitly track knowledge gaps.

## Tasks

- [x] 1. Set up extraction infrastructure
  - Create Python extraction scripts directory structure
  - Set up logging and error handling
  - Initialize knowledge gap tracker
  - _Requirements: 11.1, 11.2, 11.3_

- [ ] 2. Implement core extraction modules
  - [x] 2.1 Implement CodeExtractor class
    - Create search_class() method with regex patterns
    - Create search_config() method for configuration classes
    - Create extract_method() method for specific methods
    - Create extract_formula() method for formula extraction
    - Create get_context() method for code context
    - _Requirements: 1.1, 2.1, 3.3, 4.3, 5.1, 9.1-9.5_
  
  - [ ]* 2.2 Write property test for CodeExtractor
    - **Property 1: Code Reference Validity**
    - **Validates: Requirements 6.1, 6.7**
  
  - [x] 2.3 Implement CodeVerifier class
    - Create verify_line_reference() method with exact matching
    - Create extract_formula() method with no-interpretation policy
    - Create assess_confidence() method with strict rules
    - Create identify_missing_data() method
    - Create check_for_assumptions() method
    - _Requirements: 6.1, 6.2, 6.4, 6.5, 6.6_
  
  - [ ]* 2.4 Write property test for CodeVerifier
    - **Property 2: Zero Unverified Claims**
    - **Property 3: Formula Extraction Accuracy**
    - **Validates: Requirements 6.2, 6.3, 6.4, 6.5, 6.6**

- [x] 3. Checkpoint - Verify extraction modules work
  - Test extraction on known classes (PlayerPetCollectionModel line 1070882)
  - Verify confidence assessment is working correctly
  - Ensure all tests pass, ask the user if questions arise

- [ ] 4. Implement guild war mechanics extraction
  - [x] 4.1 Search for guild war classes
    - Search patterns: GuildWar.*Config, GuildTier.*, .*War.*Match.*, WarPoints
    - Extract all matches with line numbers
    - Document search results in knowledge gap tracker
    - _Requirements: 1.1, 1.2, 1.3_
  
  - [x] 4.2 Extract guild war matchmaking logic
    - Extract matchmaking methods if found
    - Assess confidence level
    - Identify missing data (tier thresholds, point calculations)
    - Create knowledge gap entries for missing information
    - _Requirements: 1.4, 1.5, 1.6, 1.7, 11.1-11.5_
  
  - [ ]* 4.3 Write unit tests for guild war extraction
    - Test search pattern matching
    - Test confidence assessment for partial data
    - Test knowledge gap creation
    - _Requirements: 1.1-1.7_

- [ ] 5. Implement dungeon scaling extraction
  - [x] 5.1 Search for dungeon classes
    - Search patterns: Dungeon.*Config, DifficultyMultiplier, DungeonLevel, .*Dungeon.*Reward
    - Extract all matches with line numbers
    - Document search results
    - _Requirements: 2.1, 2.2, 2.3_
  
  - [x] 5.2 Extract dungeon scaling formulas
    - Extract HP multiplier formula
    - Extract damage multiplier formula
    - Extract reward scaling formula
    - Identify missing config values
    - Create knowledge gap entries
    - _Requirements: 2.4, 2.5, 2.6, 9.1, 9.2, 9.6, 9.7_
  
  - [ ]* 5.3 Write property test for dungeon formulas
    - **Property 3: Formula Extraction Accuracy**
    - **Property 9: Formula Completeness**
    - **Validates: Requirements 2.1-2.6, 9.7**

- [ ] 6. Implement egg drop RNG extraction
  - [x] 6.1 Search for drop chance classes
    - Search patterns: .*DropChance.*Config, .*Summon.*Config, RandomSeed, DungeonDrop
    - Extract MountSummonDropChanceConfig and related classes
    - Document findings
    - _Requirements: 3.3_
  
  - [x] 6.2 Extract drop table data
    - Extract drop chance tables by level
    - Verify seeded RNG mechanism
    - Create examples showing same seed, different drop tables
    - _Requirements: 3.1, 3.2, 3.4, 3.5, 3.6_
  
  - [ ]* 6.3 Write unit tests for RNG extraction
    - Test drop table extraction
    - Test example generation
    - _Requirements: 3.1-3.6_

- [x] 7. Checkpoint - Verify mechanics extraction
  - Review extracted mechanics for accuracy
  - Check confidence levels are appropriate
  - Review knowledge gaps list
  - Ensure all tests pass, ask the user if questions arise

- [ ] 8. Implement PvP league extraction
  - [x] 8.1 Search for PvP classes
    - Search patterns: Pvp.*Config, .*League.*Config, PromotionEnd, DemotionStart, PvpMatchmaking
    - Extract all matches
    - Document findings
    - _Requirements: 4.1, 4.2, 4.3_
  
  - [x] 8.2 Extract league and matchmaking data
    - Extract promotion/demotion thresholds
    - Extract matchmaking algorithm
    - Create examples with concrete rank thresholds
    - Identify missing data
    - _Requirements: 4.4, 4.5, 4.6_
  
  - [ ]* 8.3 Write unit tests for PvP extraction
    - Test threshold extraction
    - Test example generation
    - _Requirements: 4.1-4.6_

- [ ] 9. Implement shop seeding investigation
  - [x] 9.1 Search for shop classes
    - Search patterns: ShopRefreshConfig, PlayerShopModel, ShopItem.*, ShopSeed
    - Extract all matches
    - Document findings
    - _Requirements: 5.1, 5.2_
  
  - [x] 9.2 Analyze shop mechanics
    - Determine if shop uses seeded RNG
    - Extract refresh mechanics
    - Extract refresh costs
    - Create knowledge gap if seeding unclear
    - _Requirements: 5.3, 5.4, 5.5, 5.6_
  
  - [ ]* 9.3 Write unit tests for shop extraction
    - Test shop class extraction
    - Test seeding detection
    - _Requirements: 5.1-5.6_

- [ ] 10. Implement combat formula extraction
  - [x] 10.1 Search for combat classes
    - Search patterns: AttacksSystem, UnitEntity, WeaponInfo, DamageCalculation
    - Extract AttacksSystem.GetDamage() method
    - Extract attack speed calculation methods
    - _Requirements: 9.1, 9.2_
  
  - [x] 10.2 Extract combat formulas
    - Extract damage calculation formula with complete chain
    - Extract attack speed formula
    - Extract critical hit formula
    - Extract dodge/block formulas
    - Extract life steal formula
    - Define all variables with descriptions
    - _Requirements: 9.3, 9.4, 9.5, 9.6, 9.7, 9.9, 9.10_
  
  - [ ]* 10.3 Write property test for formula completeness
    - **Property 9: Formula Completeness**
    - **Property 10: Formula Copy-Pastability**
    - **Property 11: Formula Chain Completeness**
    - **Validates: Requirements 9.7, 9.8, 9.9**

- [x] 11. Checkpoint - Verify all extractions complete
  - Review all extracted mechanics
  - Verify all formulas are complete
  - Check knowledge gaps are documented
  - Ensure all tests pass, ask the user if questions arise

- [ ] 12. Implement documentation generator
  - [x] 12.1 Create DocumentationGenerator class
    - Implement generate_section() for mechanic sections
    - Implement format_code_reference() for line number links
    - Implement generate_example_table() for comparison tables
    - Implement add_confidence_indicator() for confidence badges
    - Implement generate_formula_card() for formula presentation
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 9.6, 9.7, 9.8_
  
  - [ ]* 12.2 Write unit tests for documentation generator
    - Test HTML generation
    - Test code reference formatting
    - Test confidence indicator rendering
    - Test formula card generation
    - _Requirements: 7.1-7.6, 9.6-9.8_

- [ ] 13. Implement HTML updater
  - [x] 13.1 Create HTMLUpdater class
    - Implement find_section() using BeautifulSoup
    - Implement update_section() preserving structure
    - Implement remove_unverified_content() with logging
    - Implement preserve_styling() to maintain CSS classes
    - _Requirements: 7.1, 7.2, 8.1, 8.3, 8.4, 8.5_
  
  - [ ]* 13.2 Write property test for HTML preservation
    - **Property 6: HTML Structure Preservation**
    - **Validates: Requirements 7.1, 7.2, 7.5**

- [ ] 14. Update docs/war-pvp.html
  - [x] 14.1 Update guild war section
    - Replace "Dev Confirmed" content with code-verified content
    - Add confidence indicators
    - Add code references
    - Remove unverified claims
    - _Requirements: 1.1-1.7, 6.3, 6.9, 8.1, 8.3_
  
  - [x] 14.2 Update dungeon section
    - Add dungeon scaling formulas
    - Add scaling examples with real multipliers (if found)
    - Add confidence indicators
    - Add code references
    - _Requirements: 2.1-2.6, 8.1, 8.3_
  
  - [x] 14.3 Update egg drop section
    - Enhance RNG explanation with code references
    - Add drop table comparison
    - Add confidence indicators
    - _Requirements: 3.1-3.6, 8.1, 8.3_
  
  - [x] 14.4 Update PvP section
    - Add league system details
    - Add matchmaking algorithm
    - Add confidence indicators
    - Add code references
    - _Requirements: 4.1-4.6, 8.1, 8.3_
  
  - [x] 14.5 Update shop section
    - Add shop seeding findings
    - Add refresh mechanics
    - Add confidence indicators
    - _Requirements: 5.1-5.6, 8.1, 8.3_

- [ ] 15. Update docs/index.html
  - [x] 15.1 Update combat section with formulas
    - Add comprehensive damage calculation formula
    - Add attack speed formula
    - Add critical hit formula
    - Add defensive stat formulas
    - Add life steal formula
    - Add formula cards with copy buttons
    - Add code references
    - _Requirements: 9.1-9.10, 8.1, 8.3_
  
  - [ ]* 15.2 Write integration tests for HTML updates
    - Test that all sections are updated
    - Test that styling is preserved
    - Test that navigation works
    - _Requirements: 7.1-7.6, 8.1-8.6_

- [x] 16. Checkpoint - Verify HTML updates
  - Open docs/index.html in browser locally
  - Open docs/war-pvp.html in browser locally
  - Verify all sections render correctly
  - Verify confidence indicators display properly
  - Verify formulas are readable
  - Ensure all tests pass, ask the user if questions arise

- [ ] 17. Add CSS for new elements
  - [x] 17.1 Add confidence badge styles
    - Add .confidence-badge base styles
    - Add .confidence-high, .confidence-medium, .confidence-low, .confidence-unverified
    - Add .confidence-reason styles
    - _Requirements: 7.1, 7.2, 7.5_
  
  - [x] 17.2 Add formula card styles
    - Add .formula-card styles
    - Add .formula-readable, .formula-code, .formula-spreadsheet styles
    - Add .formula-variables, .formula-example styles
    - Add .copy-btn styles
    - _Requirements: 9.6, 9.7, 9.8, 7.1, 7.5_

- [x] 18. Add JavaScript for copy functionality
  - Create docs/assets/js/formulas.js
  - Implement copy-to-clipboard for formula code
  - Add visual feedback on copy
  - _Requirements: 9.8_

- [ ] 19. Fix GitHub Pages rendering
  - [x] 19.1 Create .nojekyll file
    - Create empty .nojekyll file in docs/ folder
    - Commit to repository
    - _Requirements: 10.1, 10.3, 10.6_
  
  - [x] 19.2 Verify GitHub Pages configuration
    - Check repository settings
    - Verify branch is set to main
    - Verify folder is set to /docs
    - Verify index.html is default page
    - _Requirements: 10.1, 10.2, 10.4, 10.5_

- [ ] 20. Generate knowledge gaps document
  - [x] 20.1 Export KNOWLEDGE_GAPS.md
    - Generate markdown file from knowledge gap tracker
    - Include all gaps with search details
    - Include priority levels and affected mechanics
    - Include search statistics
    - Include next steps suggestions
    - _Requirements: 11.1-11.9_
  
  - [ ]* 20.2 Write unit tests for knowledge gap export
    - Test markdown generation
    - Test gap categorization
    - Test statistics calculation
    - _Requirements: 11.1-11.9_

- [x] 21. Final checkpoint - Complete verification
  - Review all generated documentation
  - Verify all code references are valid
  - Verify all confidence levels are appropriate
  - Review KNOWLEDGE_GAPS.md for completeness
  - Test website locally
  - Ensure all tests pass, ask the user if questions arise

- [x] 22. Deployment preparation
  - Commit all changes to git
  - Push to GitHub
  - Verify GitHub Pages deployment
  - Test live website
  - Verify HTML renders correctly (not as raw code)
  - _Requirements: 10.1-10.6_

## Notes

- Tasks marked with `*` are optional property-based and unit tests
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation and user feedback
- Zero-hallucination policy applies to all extraction tasks
- Knowledge gap tracking is mandatory for all failed searches
- All formulas must be code-verified with line number references

## Testing Strategy

### Property-Based Tests
- Use `hypothesis` library for Python
- Minimum 100 iterations per test
- Each test tagged with property number from design

### Unit Tests
- Use `pytest` framework
- Focus on specific examples and edge cases
- Test error handling and confidence assessment
- Test HTML generation and preservation

### Integration Tests
- Test complete extraction pipeline
- Test HTML update workflow
- Test knowledge gap generation

### Manual Verification
- Visual inspection of generated HTML
- Spot-check 10 random code references
- Verify 5 random formulas against dump.cs
- Test responsive design on multiple devices
- Verify GitHub Pages deployment
