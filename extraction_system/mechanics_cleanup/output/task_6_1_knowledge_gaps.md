# Knowledge Gaps Summary

Last Updated: 2026-02-11 04:23:47

## Overview

This document tracks all information we attempted to find but could not verify from code.

## Statistics

- **Total Gaps**: 2
- **High Priority**: 0
- **Medium Priority**: 2
- **Low Priority**: 0

### By Category

- **Guild War**: 0
- **Dungeon**: 0
- **Pvp**: 0
- **Shop**: 0
- **Combat**: 0
- **Rng**: 0

## Medium Priority Gaps

### Drop Chance: Drop chance classes matching pattern: RandomSeed

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `RandomSeed`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for drop chance/RNG classes matching pattern 'RandomSeed' but found no matches.

**Potential Sources**:

- Server-side RNG
- Native ARM code
- Different naming convention

**Impact**: MEDIUM - Affects Drop tables, Egg summoning, RNG mechanics

**Notes**: Searched entire dump.cs file with pattern: RandomSeed

---

### Drop Chance: Drop chance classes matching pattern: DungeonDrop

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `DungeonDrop`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for drop chance/RNG classes matching pattern 'DungeonDrop' but found no matches.

**Potential Sources**:

- Server-side RNG
- Native ARM code
- Different naming convention

**Impact**: MEDIUM - Affects Drop tables, Egg summoning, RNG mechanics

**Notes**: Searched entire dump.cs file with pattern: DungeonDrop

---

## Search Summary

**Total Searches**: 10

**Found**: 8

**Not Found**: 2

**Partial Matches**: 0

**Success Rate**: 80.0%

## Most Common Missing Data

- **Other**: 2 instances

## Next Steps

1. **Test in-game** - Empirically determine missing values through gameplay testing
2. **Review game updates** - Check if newer versions expose more information
