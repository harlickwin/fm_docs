# Knowledge Gaps Summary

Last Updated: 2026-02-11 04:22:02

## Overview

This document tracks all information we attempted to find but could not verify from code.

## Statistics

- **Total Gaps**: 2
- **High Priority**: 0
- **Medium Priority**: 2
- **Low Priority**: 0

### By Category

- **Guild War**: 0
- **Dungeon**: 2
- **Pvp**: 0
- **Shop**: 0
- **Combat**: 0
- **Rng**: 0

## Medium Priority Gaps

### Dungeon: Dungeon classes matching pattern: DifficultyMultiplier

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `DifficultyMultiplier`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for dungeon-related classes matching pattern 'DifficultyMultiplier' but found no matches. This information may be in server-side code, native ARM implementation, or using different naming conventions.

**Potential Sources**:

- SharedGameConfig.mpa
- Native ARM code in libil2cpp.so
- Server-side configuration
- Different class naming convention

**Impact**: MEDIUM - Affects Dungeon scaling, Difficulty multipliers, Reward calculations

**Notes**: Searched entire dump.cs file with pattern: DifficultyMultiplier

---

### Dungeon: Dungeon classes matching pattern: DungeonLevel

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `DungeonLevel`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for dungeon-related classes matching pattern 'DungeonLevel' but found no matches. This information may be in server-side code, native ARM implementation, or using different naming conventions.

**Potential Sources**:

- SharedGameConfig.mpa
- Native ARM code in libil2cpp.so
- Server-side configuration
- Different class naming convention

**Impact**: MEDIUM - Affects Dungeon scaling, Difficulty multipliers, Reward calculations

**Notes**: Searched entire dump.cs file with pattern: DungeonLevel

---

## Search Summary

**Total Searches**: 15

**Found**: 13

**Not Found**: 2

**Partial Matches**: 0

**Success Rate**: 86.7%

## Most Common Missing Data

- **Server-side logic**: 2 instances

## Next Steps

1. **Analyze ARM code in libil2cpp.so** - May contain native implementations
2. **Decompile server code** - If accessible, may reveal server-side logic
3. **Test in-game** - Empirically determine missing values through gameplay testing
4. **Review game updates** - Check if newer versions expose more information
