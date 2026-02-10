# Knowledge Gaps Summary

Last Updated: 2026-02-10 23:54:47

## Overview

This document tracks all information we attempted to find but could not verify from code.

## Statistics

- **Total Gaps**: 2
- **High Priority**: 2
- **Medium Priority**: 0
- **Low Priority**: 0

### By Category

- **Guild War**: 2
- **Dungeon**: 0
- **Pvp**: 0
- **Shop**: 0
- **Combat**: 0
- **Rng**: 0

## High Priority Gaps

### Guild War: Guild War classes matching pattern: class.*War.*Match.*

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `class.*War.*Match.*`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for classes matching pattern 'class.*War.*Match.*' but found no matches. This information may be in server-side code, native ARM implementation, or using different naming conventions.

**Potential Sources**:

- Server-side code (not in client dump)
- Native ARM code in libil2cpp.so
- Configuration files (.mpa, .json)
- Different class naming convention

**Impact**: HIGH - Affects Guild War Matchmaking, Guild Tiers, War Points

**Notes**: Searched entire dump.cs file with pattern: class.*War.*Match.*

---

### Guild War: Guild War classes matching pattern: \bWarPoints\b

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `\bWarPoints\b`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for classes matching pattern '\bWarPoints\b' but found no matches. This information may be in server-side code, native ARM implementation, or using different naming conventions.

**Potential Sources**:

- Server-side code (not in client dump)
- Native ARM code in libil2cpp.so
- Configuration files (.mpa, .json)
- Different class naming convention

**Impact**: HIGH - Affects Guild War Matchmaking, Guild Tiers, War Points

**Notes**: Searched entire dump.cs file with pattern: \bWarPoints\b

---

## Search Summary

**Total Searches**: 8

**Found**: 6

**Not Found**: 2

**Partial Matches**: 0

**Success Rate**: 75.0%

## Most Common Missing Data

- **Server-side logic**: 2 instances

## Next Steps

1. **Analyze ARM code in libil2cpp.so** - May contain native implementations
2. **Decompile server code** - If accessible, may reveal server-side logic
3. **Test in-game** - Empirically determine missing values through gameplay testing
4. **Review game updates** - Check if newer versions expose more information
