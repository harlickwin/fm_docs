# Tournament Pro - User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Quick Start](#quick-start)
3. [Configuration Guide](#configuration-guide)
4. [Running Tournaments](#running-tournaments)
5. [Understanding Results](#understanding-results)
6. [Advanced Features](#advanced-features)
7. [Troubleshooting](#troubleshooting)
8. [FAQ](#faq)

## Introduction

Tournament Pro is a desktop application for running PvP build tournaments. It simulates battles between different character builds to determine which combinations of stats and equipment are most effective in player-versus-player combat.

### Key Features

- **Multi-threaded Execution**: Uses multiple CPU cores for fast tournament completion
- **Automatic Checkpoints**: Saves progress every 5 minutes to prevent data loss
- **User-Friendly Interface**: No coding required - configure everything through the GUI
- **Detailed Results**: Export results in HTML, JSON, or text format
- **Flexible Configuration**: Customize substats, weapon types, and multipliers
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Quick Start

### First Run

When you launch Tournament Pro for the first time, you'll see a setup wizard that guides you through:

1. **Welcome Screen**: Overview of Tournament Pro features
2. **CPU Configuration**: Automatic detection of your CPU cores with recommended settings
3. **Output Directory**: Choose where tournament results will be saved
4. **Quick Guide**: Step-by-step instructions for running your first tournament

### Running Your First Tournament

1. **Configure Tournament Settings**:
   - Select which substats to include (damage, crit chance, attack speed, etc.)
   - Choose weapon types (melee, ranged, or both)
   - Set substat multiplier (1-100%)
   - Specify number of builds to generate

2. **Start Tournament**:
   - Click "Start Tournament" button
   - Monitor real-time progress
   - View per-worker status

3. **Review Results**:
   - See top 10 builds
   - Export results in your preferred format
   - Open results folder to view detailed reports

## Configuration Guide

### Substats

Substats are the character attributes that will be varied across different builds:

- **Damage**: Base damage output
- **Melee Damage**: Additional damage for melee weapons
- **Ranged Damage**: Additional damage for ranged weapons
- **Critical Chance**: Probability of landing critical hits
- **Critical Damage**: Damage multiplier for critical hits
- **Attack Speed**: How quickly attacks are performed
- **Double Chance**: Probability of double attacks
- **Health**: Maximum hit points
- **Health Regen**: HP regeneration per second
- **Lifesteal**: Percentage of damage converted to healing
- **Block Chance**: Probability of blocking attacks
- **Skill Cooldown**: Reduction in skill cooldown times
- **Skill Damage**: Additional damage for skills

**Tip**: Start with core combat stats (damage, crit chance, attack speed, health) for faster tournaments.

### Weapon Types

- **Melee**: Close-range weapons with movement delay
- **Ranged**: Long-range weapons without movement delay
- **Both**: Test both weapon types in the same tournament

### Substat Multiplier

Controls the strength of substats relative to base stats:

- **100%**: Full substat values (realistic gameplay)
- **50%**: Half substat values (faster tournaments, less variation)
- **25%**: Quarter substat values (very fast tournaments)

Lower multipliers result in faster tournaments but less diverse builds.

### Target Builds

Number of unique builds to generate and test:

- **100-500**: Quick test (minutes)
- **1,000-5,000**: Standard tournament (30-60 minutes)
- **10,000+**: Comprehensive tournament (hours)

**Formula**: Total battles = (N × (N-1)) / 2, where N is the number of builds

### Worker Threads

Number of CPU cores to use:

- **Recommended**: Total cores - 1 (leaves one core for your system)
- **Maximum**: All available cores (may slow down other applications)
- **Minimum**: 1 core (slowest but safest)

### Checkpoint Interval

How often to save progress (in seconds):

- **Default**: 300 seconds (5 minutes)
- **Frequent**: 60-120 seconds (more safety, slight performance impact)
- **Infrequent**: 600+ seconds (better performance, less safety)

## Running Tournaments

### Starting a Tournament

1. Configure all settings in the Configuration Screen
2. Review the estimated runtime
3. Click "Start Tournament"
4. The application switches to Execution Screen

### Monitoring Progress

The Execution Screen shows:

- **Progress Bar**: Overall completion percentage
- **Statistics**:
  - Completed battles vs. total battles
  - Current speed (battles per second)
  - Elapsed time
  - Estimated time remaining
- **Worker Status**: Individual status of each worker thread
- **Configuration Summary**: Your tournament settings

### Pausing and Resuming

- **Pause**: Click "Pause" button to temporarily stop the tournament
- **Resume**: Click "Resume" to continue from where you left off
- **Cancel**: Click "Cancel Tournament" to stop and save a checkpoint

### Checkpoint Recovery

If the application crashes or is closed during a tournament:

1. Restart Tournament Pro
2. A dialog will appear showing the checkpoint details
3. Choose "Resume Tournament" to continue from the checkpoint
4. Or choose "Start Fresh" to discard the checkpoint

## Understanding Results

### Results Summary

When a tournament completes, you'll see:

- **Total Builds**: Number of builds tested
- **Total Battles**: Number of battles simulated
- **Total Time**: Tournament duration
- **Average Speed**: Battles per second

### Top Builds

The top 10 builds are displayed with:

- **Rank**: Position (🥇🥈🥉 for top 3)
- **Description**: Build characteristics
- **Weapon Type**: Melee or ranged
- **DPS**: Damage per second
- **HP**: Maximum health
- **Win Rate**: Percentage of battles won
- **Record**: Wins-Losses-Draws

### Exporting Results

Three export formats are available:

#### HTML Export
- Human-readable report
- Styled tables and charts
- Best for sharing with others
- Open in any web browser

#### JSON Export
- Machine-readable format
- Complete tournament data
- Best for further analysis
- Can be imported into other tools

#### TXT Export
- Plain text format
- Simple and lightweight
- Best for quick review
- Easy to read in any text editor

### Results Files

Results are saved in timestamped subdirectories:

```
Documents/TournamentPro/Results/
  └── 2024-01-15_14-30-00/
      ├── results.html
      ├── results.json
      ├── results.txt
      └── checkpoint.json (if applicable)
```

## Advanced Features

### Configuration Presets

Save frequently used configurations:

1. Configure your tournament settings
2. Click "Save as Preset"
3. Enter a name and description
4. Load the preset anytime from the dropdown

**Built-in Presets**:
- **Quick Test**: Fast tournament for testing (100 builds)
- **Balanced**: Standard tournament (1,000 builds)
- **Comprehensive**: Thorough analysis (5,000 builds)

### Meta Build Inclusion

Enable "Include Meta Build" to add a reference build based on current game meta. This helps compare generated builds against known strong builds.

### Loading Previous Results

Enable "Load Previous Results" to continue a tournament with additional builds. This is useful for expanding an existing tournament without starting over.

### Formula Configuration

Advanced users can customize game formulas:

- Attack speed tiers
- Double attack delays
- Critical damage multipliers
- Melee movement delays
- Stat caps

Access via the Formula Editor (coming soon).

## Troubleshooting

### Tournament Won't Start

**Problem**: "Start Tournament" button doesn't work

**Solutions**:
- Check that at least one substat is selected
- Verify output directory exists and is writable
- Ensure target builds is greater than 0
- Check validation errors at the bottom of the screen

### Application Crashes During Tournament

**Problem**: Application closes unexpectedly

**Solutions**:
- Restart the application - checkpoint recovery will activate
- Reduce number of worker threads
- Increase checkpoint interval
- Check available disk space
- Update to the latest version

### Slow Performance

**Problem**: Tournament is running slower than expected

**Solutions**:
- Reduce number of target builds
- Lower substat multiplier
- Disable unused substats
- Close other applications
- Increase worker threads (if CPU usage is low)

### Checkpoint Not Found

**Problem**: Checkpoint recovery doesn't appear after crash

**Solutions**:
- Check the output directory for .checkpoint.json files
- Verify the output directory path is correct
- Checkpoint may have been corrupted - start a new tournament
- Check that checkpoints weren't manually deleted

### Results Not Exporting

**Problem**: Export buttons don't create files

**Solutions**:
- Verify output directory is writable
- Check available disk space
- Try a different export format
- Check file permissions
- Restart the application

### High Memory Usage

**Problem**: Application uses too much RAM

**Solutions**:
- Reduce number of target builds
- Reduce number of worker threads
- Close other applications
- Restart the application periodically for long tournaments

## FAQ

### How long does a tournament take?

It depends on:
- Number of builds (more builds = longer time)
- Number of substats (more substats = longer time)
- CPU cores (more cores = faster)
- Substat multiplier (lower = faster)

**Estimates**:
- 100 builds: 1-5 minutes
- 1,000 builds: 30-60 minutes
- 5,000 builds: 2-4 hours
- 10,000 builds: 8-12 hours

### Can I use my computer while a tournament runs?

Yes! Tournament Pro runs in the background. However:
- Performance may be slower if you use CPU-intensive applications
- Consider reducing worker threads to leave more CPU for other tasks
- The application window can be minimized

### What happens if I close the application?

Tournament Pro automatically saves checkpoints every 5 minutes. When you restart:
- You'll be prompted to resume from the checkpoint
- Progress is preserved
- Only in-progress battles need to be rerun

### Can I run multiple tournaments simultaneously?

No, Tournament Pro runs one tournament at a time. However:
- You can queue tournaments by running them sequentially
- Each tournament saves to a separate timestamped directory
- Previous results remain accessible

### How much disk space do I need?

Disk space requirements:
- Application: ~200 MB
- Per tournament: 1-50 MB (depends on number of builds)
- Checkpoints: 1-20 MB each

**Recommendation**: Keep at least 1 GB free for comfortable operation.

### Can I edit results after export?

Yes:
- HTML files can be edited in any text editor
- JSON files can be processed with scripts or tools
- TXT files are plain text and easily editable

### How accurate are the simulations?

Simulations use the same combat formulas as the game:
- Attack speed tiers
- Critical hit mechanics
- Double attack system
- Health regeneration
- Lifesteal calculations

Results are deterministic and reproducible.

### Can I share tournaments with others?

Yes! Share the entire results directory:
- Contains all export formats
- Includes configuration details
- Others can view without Tournament Pro
- HTML format is best for sharing

### What if I find a bug?

Please report bugs with:
- Description of the problem
- Steps to reproduce
- Tournament configuration used
- System information (OS, CPU)
- Error messages (if any)

### How do I update Tournament Pro?

Updates are distributed as new executables:
1. Download the latest version
2. Close the current application
3. Replace the old executable
4. Your settings and results are preserved

---

## Support

For additional help:
- Check the in-app Help menu
- Review the README.md file
- Check for updates
- Contact support with detailed bug reports

**Version**: 1.0.0  
**Last Updated**: 2024
