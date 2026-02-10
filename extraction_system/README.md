# Game Mechanics Extraction System

A comprehensive, autonomous system for extracting and documenting all game mechanics from decompiled mobile games.

## Features

- **Autonomous Extraction**: Walk away and return to complete documentation
- **Cross-Reference Analysis**: Maps IL2CPP metadata to Ghidra ARM code
- **Confidence Levels**: High/Medium/Low ratings based on verification
- **Comprehensive Coverage**: Combat, Summoning, RNG, PvP, Progression, Economy
- **Pattern Recognition**: Finds RNG algorithms, drop tables, formulas
- **Checkpointing**: Resume from last saved progress
- **Parallel Processing**: Extract multiple systems simultaneously

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```bash
# Run full extraction
python run_extraction.py

# Extract single system
python run_extraction.py --mode single --system Combat

# Use custom config
python run_extraction.py --config my_config.yaml

# Verbose output
python run_extraction.py --verbose
```

## Configuration

Edit `extraction_system/config.yaml` to configure:

- Input file paths (IL2CPP dump, Ghidra export)
- Output paths
- Processing options (caching, parallel processing)
- Verification settings
- Priority systems

## Output

The system generates:

- **COMPLETE_GAME_MECHANICS_MANUAL.md**: Comprehensive documentation
- **Checkpoints**: Progress saved after each system
- **Logs**: Detailed extraction logs
- **Cache**: Parsed data for faster re-runs

## Architecture

```
extraction_system/
├── core/           # Base classes, config, logging
├── parsers/        # IL2CPP parser
├── mappers/        # Address mapping
├── extractors/     # Function and pattern extraction
├── analyzers/      # System-specific analyzers
├── verification/   # Verification engine
├── documentation/  # Documentation generator
└── pipeline/       # Main orchestrator
```

## Confidence Levels

- **High**: ARM code found and verified
- **Medium**: IL2CPP structure found, ARM not verified
- **Low**: Inferred from patterns only

## Systems Analyzed

1. **Combat**: Attack speed, damage, stats, status effects
2. **Summoning**: RNG algorithms, drop tables, rarity determination
3. **PvP**: Matchmaking, scoring, stat modifiers
4. **Progression**: Tech tree, forge, leveling
5. **Economy**: Resource generation, pricing, currency conversion
