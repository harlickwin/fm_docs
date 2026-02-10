# Mechanics Cleanup Extraction System

This module extracts missing game mechanics from the IL2CPP dump (dump.cs) and updates the GitHub Pages documentation with code-verified information.

## Core Principle

**VERIFY EVERYTHING. ASSUME NOTHING. HALLUCINATE NOTHING.**

Every statement must be verifiable from code, with explicit confidence levels and gap identification when information is incomplete or missing.

## Directory Structure

```
extraction_system/mechanics_cleanup/
├── __init__.py                    # Module initialization
├── README.md                      # This file
├── config.py                      # Configuration settings
├── logger.py                      # Logging infrastructure
├── error_handler.py               # Error handling with zero-hallucination policy
├── knowledge_gap_tracker.py       # Tracks missing information
└── output/                        # Generated output files
```

## Components

### Logger (`logger.py`)

Provides structured logging for extraction operations:
- File logging with detailed information
- Console logging for important messages
- Specialized methods for extraction events, confidence assessment, and knowledge gaps

**Usage:**
```python
from extraction_system.mechanics_cleanup.logger import get_logger

logger = get_logger()
logger.extraction_start("guild_war")
logger.match_found("GuildWarConfig", 12345, "GuildWarConfig")
logger.confidence_assessment("matchmaking", "MEDIUM", "Logic found but values missing")
```

### Error Handler (`error_handler.py`)

Handles errors following the zero-hallucination policy:
- Custom exceptions for different error types
- Error severity levels (LOW, MEDIUM, HIGH, CRITICAL)
- Specific handlers for common scenarios (class not found, multiple matches, etc.)
- Suggested actions for each error type

**Usage:**
```python
from extraction_system.mechanics_cleanup.error_handler import ErrorHandler

handler = ErrorHandler()
error = handler.handle_class_not_found(
    "GuildWarConfig",
    "dump.cs",
    ["class GuildWar.*Config"]
)
```

### Knowledge Gap Tracker (`knowledge_gap_tracker.py`)

Maintains a comprehensive list of information we couldn't verify:
- Tracks what was searched for and where
- Categorizes gaps by priority (HIGH, MEDIUM, LOW)
- Identifies potential alternative sources
- Generates markdown summary with statistics
- Exports to KNOWLEDGE_GAPS.md

**Usage:**
```python
from extraction_system.mechanics_cleanup.knowledge_gap_tracker import (
    get_tracker, KnowledgeGap, GapPriority
)

tracker = get_tracker()
gap = KnowledgeGap(
    category="guild_war",
    title="Two-Week Matchmaking Cycle",
    description="Weekly cycle logic not found in client code",
    searched_patterns=["GuildWar.*Week", "War.*Cycle"],
    searched_locations=["dump.cs lines 1-1,200,000"],
    potential_sources=["Server-side code", "Native ARM code"],
    impact=GapPriority.HIGH,
    related_mechanics=["Guild matchmaking", "Tier progression"],
    notes="External sources claim two-week cycle exists"
)
tracker.add_gap(gap)
tracker.export_to_file("KNOWLEDGE_GAPS.md")
```

### Configuration (`config.py`)

Defines paths, search patterns, and extraction settings:
- File paths for dump.cs and documentation
- Search patterns for each mechanic category
- Confidence level definitions
- Extraction settings

**Usage:**
```python
from extraction_system.mechanics_cleanup.config import Config

# Validate configuration
if Config.validate():
    # Get search patterns for a category
    patterns = Config.get_search_patterns("guild_war")
    
    # Access paths
    dump_path = Config.DUMP_PATH
    docs_path = Config.DOCS_PATH
```

## Zero-Hallucination Policy

This system follows a strict zero-hallucination policy:

1. **Exact Match Only**: Line numbers must point to exact code, not "similar" code
2. **No Interpretation**: If formula requires interpretation, mark as LOW confidence
3. **No Inference**: If value not in code, mark as MISSING, don't infer
4. **No Extrapolation**: If pattern exists for X but not Y, don't assume Y follows same pattern
5. **No External Sources**: Developer comments, forums, screenshots are NOT valid sources

### Confidence Levels

- **HIGH**: Complete code verification, no assumptions
- **MEDIUM**: Partial verification, some config values missing but logic clear
- **LOW**: Limited code evidence, requires interpretation
- **UNVERIFIED**: No code evidence, cannot validate

## Error Handling Scenarios

### Class Not Found
```
❌ Not Found: GuildWarConfig not found in IL2CPP dump (searched lines 1-1,200,000).
This mechanic may not exist, may use different naming, or may be in native ARM code.
```

### Multiple Matches
```
⚠️ Multiple Matches: Found 3 classes matching pattern. Manual review required.
Line numbers: 12345, 23456, 34567
```

### Partial Match
```
⚠️ Partial Match: Found SimilarClass at line 12345, but expected ExactClass.
May be related but cannot confirm.
```

### Complex Formula
```
⚠️ Complex Logic: Method contains branching/loops. Full code shown below.
Cannot extract simple formula without making assumptions.
```

### Missing Config Value
```
⚠️ Missing Config: Formula uses ConfigClass.ValueName (not found in dump.cs).
Actual value unknown. Formula structure verified but cannot calculate without this value.
```

## Logging Levels

- **DEBUG**: Detailed search patterns and operations
- **INFO**: Successful matches, extraction progress, confidence assessments
- **WARNING**: No matches, knowledge gaps, unverified content
- **ERROR**: Extraction failures, verification errors
- **CRITICAL**: System-level failures, missing files

## Output Files

### KNOWLEDGE_GAPS.md
Comprehensive markdown file documenting all missing information:
- Overview and statistics
- High/Medium/Low priority gaps
- Search patterns used
- Potential sources for missing data
- Next steps suggestions

## Requirements

- Python 3.7+
- Access to dump.cs at C:\apktool\il2cpp-output\dump.cs
- Write access to docs/ directory
- Write access to extraction_system/logs/ directory

## Next Steps

After setting up this infrastructure, the next tasks are:
1. Implement CodeExtractor class for searching and extracting code
2. Implement CodeVerifier class for verification and confidence assessment
3. Implement DocumentationGenerator for HTML generation
4. Implement HTMLUpdater for updating existing HTML files
5. Extract mechanics for each category (guild war, dungeon, PvP, shop, RNG, combat)
6. Generate and export knowledge gaps document

## References

- Spec: `.kiro/specs/mechanics-cleanup/`
- Requirements: Requirements 11.1, 11.2, 11.3
- Design: See design.md for complete architecture
