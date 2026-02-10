# Requirements Document

## Introduction

This feature enhances the existing GitHub Pages documentation (docs/index.html and docs/war-pvp.html) by adding missing game mechanics content that has been extracted from the IL2CPP dump but not yet documented on the website. The goal is to provide players with comprehensive, code-verified information about intricate game systems with real examples and clear explanations.

## Glossary

- **IL2CPP_Dump**: The dump.cs file containing decompiled game code from Unity IL2CPP
- **Documentation_System**: The GitHub Pages website (docs/index.html, docs/war-pvp.html)
- **Game_Mechanics**: Systems and formulas that govern gameplay behavior
- **Code_Reference**: Line number citation from dump.cs verifying a mechanic
- **Seeded_RNG**: Deterministic pseudo-random number generation using seed values
- **Drop_Table**: Configuration defining probability ranges for different item rarities
- **Matchmaking_System**: Algorithm for pairing players or guilds in competitive modes
- **Dungeon_Scaling**: System that modifies enemy stats and rewards based on dungeon level

## Requirements

### Requirement 1: Guild War Matchmaking Documentation

**User Story:** As a guild member, I want to understand how guild war matchmaking works, so that I can strategize and know what to expect each week.

#### Acceptance Criteria

1. THE Documentation_System SHALL extract guild war matchmaking logic from dump.cs with line number references
2. THE Documentation_System SHALL extract tier point thresholds from game configuration files with code references
3. THE Documentation_System SHALL extract war points calculation formulas from dump.cs with line number references
4. WHEN matchmaking logic is found in code, THE Documentation_System SHALL explain the algorithm with concrete examples
5. WHEN tier thresholds are found in code, THE Documentation_System SHALL document them with specific values
6. WHEN any aspect of matchmaking cannot be verified from code, THE Documentation_System SHALL mark it as unverified and explain what is missing
7. THE Documentation_System SHALL NOT include information about matchmaking cycles or patterns unless directly extractable from code

### Requirement 2: Dungeon Scaling Documentation

**User Story:** As a player, I want to understand how dungeon difficulty scales, so that I can choose the optimal dungeon level for my progression.

#### Acceptance Criteria

1. WHEN documenting dungeon scaling, THE Documentation_System SHALL extract enemy HP multiplier formulas from dump.cs with line number references
2. WHEN documenting dungeon scaling, THE Documentation_System SHALL extract enemy damage multiplier formulas from dump.cs with line number references
3. WHEN documenting dungeon scaling, THE Documentation_System SHALL extract reward scaling formulas from dump.cs with line number references
4. WHEN providing scaling examples, THE Documentation_System SHALL show concrete comparisons between Dungeon 10, Dungeon 20, and Dungeon 30
5. THE Documentation_System SHALL display actual multiplier values for each dungeon level example
6. WHEN explaining progression, THE Documentation_System SHALL show how rewards improve relative to difficulty increases

### Requirement 3: Egg Drop RNG Documentation

**User Story:** As a player, I want to understand how egg drops work with seeded RNG, so that I can understand why improving dungeon level gives better results.

#### Acceptance Criteria

1. WHEN explaining seeded RNG for egg drops, THE Documentation_System SHALL clarify that the seed stays constant while drop tables change
2. WHEN providing RNG examples, THE Documentation_System SHALL show the same seed value producing different results at different dungeon levels
3. THE Documentation_System SHALL extract dungeon-level-specific drop tables from dump.cs with line number references
4. WHEN demonstrating "improving odds", THE Documentation_System SHALL show concrete examples with specific random values and how they map to different rarities at different dungeon levels
5. THE Documentation_System SHALL include a comparison table showing at least 5 random values and their results across at least 3 dungeon levels
6. WHEN explaining the mechanism, THE Documentation_System SHALL make it crystal clear that players cannot change their seed but can change how it is interpreted

### Requirement 4: PvP League Matchmaking Documentation

**User Story:** As a PvP player, I want to understand the league system and matchmaking algorithm, so that I can understand my rank progression and opponent selection.

#### Acceptance Criteria

1. WHEN documenting the league system, THE Documentation_System SHALL extract promotion thresholds from dump.cs with line number references
2. WHEN documenting the league system, THE Documentation_System SHALL extract demotion thresholds from dump.cs with line number references
3. THE Documentation_System SHALL extract the matchmaking algorithm logic from dump.cs with line number references
4. WHEN providing league examples, THE Documentation_System SHALL show concrete rank thresholds for at least 3 different leagues
5. WHEN explaining matchmaking, THE Documentation_System SHALL describe how rating ranges work and how they expand over time
6. THE Documentation_System SHALL provide real examples showing which ranks promote, stay, and demote in a given league

### Requirement 5: Shop Seeding Investigation and Documentation

**User Story:** As a player, I want to know if shop items are seeded like eggs, so that I can understand shop refresh mechanics.

#### Acceptance Criteria

1. THE Documentation_System SHALL analyze ShopRefreshConfig in dump.cs to determine if shop items use seeded RNG
2. THE Documentation_System SHALL analyze PlayerShopModel in dump.cs to determine shop state management
3. WHEN shop seeding is confirmed, THE Documentation_System SHALL document the seeding mechanism with code references
4. WHEN shop seeding is not confirmed, THE Documentation_System SHALL document the actual refresh mechanism with code references
5. THE Documentation_System SHALL extract shop refresh costs and mechanics from dump.cs with line number references
6. WHEN documenting shop mechanics, THE Documentation_System SHALL provide clear examples of how shop refreshes work

### Requirement 6: Code Verification and References

**User Story:** As a documentation reader, I want every mechanic to be verified from game code, so that I can trust the information is accurate.

#### Acceptance Criteria

1. THE Documentation_System SHALL include line number references from dump.cs for every extracted mechanic
2. THE Documentation_System SHALL make zero assumptions about game mechanics not found in code
3. THE Documentation_System SHALL NOT include information from external sources (developer comments, screenshots, forums) unless directly verifiable in code
4. WHEN a mechanic cannot be fully verified from code, THE Documentation_System SHALL clearly mark it as "needs verification" or "TBD" with explanation of what is missing
5. WHEN confidence level is less than 100%, THE Documentation_System SHALL explicitly state why and what additional verification is needed
6. THE Documentation_System SHALL extract all formulas directly from code without modification
7. THE Documentation_System SHALL cite specific class names and method names when referencing code
8. WHEN providing examples, THE Documentation_System SHALL base all values on actual configuration data from dump.cs
9. THE Documentation_System SHALL remove or mark as unverified any existing content that cannot be validated from code

### Requirement 7: Documentation Quality and Presentation

**User Story:** As a website visitor, I want the documentation to be clear, well-organized, and visually appealing, so that I can easily find and understand information.

#### Acceptance Criteria

1. THE Documentation_System SHALL maintain the existing responsive design and CSS styling
2. WHEN adding new content, THE Documentation_System SHALL use consistent formatting with existing sections
3. THE Documentation_System SHALL organize information with clear headings and subsections
4. WHEN providing examples, THE Documentation_System SHALL use tables, comparison grids, or formatted code blocks for clarity
5. THE Documentation_System SHALL include visual indicators (✅, ❌, ⚠️, 💡) to highlight important information
6. THE Documentation_System SHALL ensure all new content is mobile-responsive and accessible

### Requirement 8: Content Integration

**User Story:** As a documentation maintainer, I want new content integrated into existing pages, so that the website structure remains coherent.

#### Acceptance Criteria

1. THE Documentation_System SHALL update docs/war-pvp.html with guild war, PvP, dungeon, and shop mechanics
2. THE Documentation_System SHALL not create new HTML pages unless explicitly required
3. WHEN updating existing sections, THE Documentation_System SHALL preserve existing content and enhance it with new details
4. THE Documentation_System SHALL maintain navigation links between pages
5. THE Documentation_System SHALL ensure footer information remains accurate
6. WHEN adding new sections, THE Documentation_System SHALL update navigation menus accordingly

### Requirement 9: Comprehensive Formula Documentation

**User Story:** As a player or developer, I want exact formulas for all game mechanics, so that I can calculate outcomes precisely and understand the math behind the game.

#### Acceptance Criteria

1. THE Documentation_System SHALL extract damage calculation formulas from dump.cs with line number references
2. THE Documentation_System SHALL extract attack speed calculation formulas from dump.cs with line number references
3. THE Documentation_System SHALL extract critical hit formulas from dump.cs with line number references
4. THE Documentation_System SHALL extract defensive stat formulas (dodge, block) from dump.cs with line number references
5. THE Documentation_System SHALL extract life steal formulas from dump.cs with line number references
6. WHEN presenting formulas, THE Documentation_System SHALL provide both human-readable format and exact code expression
7. WHEN presenting formulas, THE Documentation_System SHALL define all variables with descriptions
8. THE Documentation_System SHALL provide copy-pastable formula expressions that can be used in spreadsheets or calculators
9. WHEN a formula references other formulas, THE Documentation_System SHALL show the complete calculation chain
10. THE Documentation_System SHALL extract any multipliers, constants, or configuration values used in formulas with their sources

### Requirement 10: GitHub Pages Rendering Fix

**User Story:** As a website visitor, I want to see rendered HTML pages, so that I can read the documentation properly instead of seeing raw HTML code.

#### Acceptance Criteria

1. THE Documentation_System SHALL ensure GitHub Pages is configured to serve HTML files from the /docs folder
2. THE Documentation_System SHALL verify that index.html is the default landing page
3. WHEN GitHub Pages displays raw HTML code, THE Documentation_System SHALL investigate and fix the configuration issue
4. THE Documentation_System SHALL ensure proper MIME types are set for HTML files
5. THE Documentation_System SHALL verify the repository settings have Pages enabled with correct branch and folder
6. WHEN troubleshooting rendering issues, THE Documentation_System SHALL check for Jekyll configuration conflicts and add _config.yml if needed to disable Jekyll processing

### Requirement 11: Knowledge Gap Tracking

**User Story:** As a documentation maintainer, I want a comprehensive list of information we couldn't verify, so that I can pursue additional sources or testing to fill those gaps.

#### Acceptance Criteria

1. THE Documentation_System SHALL maintain a list of all information searched for but not found in code
2. THE Documentation_System SHALL document what search patterns were used for each gap
3. THE Documentation_System SHALL document where searches were performed (file paths, line ranges)
4. THE Documentation_System SHALL identify potential alternative sources for missing information
5. THE Documentation_System SHALL categorize gaps by priority (HIGH, MEDIUM, LOW) based on impact
6. THE Documentation_System SHALL export knowledge gaps to a KNOWLEDGE_GAPS.md file
7. WHEN a gap is identified, THE Documentation_System SHALL document what mechanics are affected by the missing information
8. THE Documentation_System SHALL provide a summary of search statistics (total searches, found vs not found)
9. THE Documentation_System SHALL suggest next steps for filling knowledge gaps
