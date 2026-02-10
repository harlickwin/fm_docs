# Knowledge Gaps Summary

Last Updated: 2026-02-11 04:18:19

## Overview

This document tracks all information we attempted to find but could not verify from code.

## Statistics

- **Total Gaps**: 8
- **High Priority**: 7
- **Medium Priority**: 1
- **Low Priority**: 0

### By Category

- **Guild War**: 8
- **Dungeon**: 0
- **Pvp**: 0
- **Shop**: 0
- **Combat**: 0
- **Rng**: 0

## High Priority Gaps

### Guild War: Guild War matchmaking: FindOpponent

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `FindOpponent`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for matchmaking logic matching pattern 'FindOpponent' but found no matches. Matchmaking algorithm may be implemented server-side or in native code.

**Potential Sources**:

- Server-side matchmaking service (not in client dump)
- Native ARM code in libil2cpp.so
- Metaplay framework server code
- Division/League system on server

**Impact**: HIGH - Affects Guild War Matchmaking, Division Assignment, Opponent Selection

**Notes**: Client code shows LeagueClient<GuildWarDivisionModel> but actual matchmaking logic not found

---

### Guild War: Guild War matchmaking: SelectOpponent

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `SelectOpponent`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for matchmaking logic matching pattern 'SelectOpponent' but found no matches. Matchmaking algorithm may be implemented server-side or in native code.

**Potential Sources**:

- Server-side matchmaking service (not in client dump)
- Native ARM code in libil2cpp.so
- Metaplay framework server code
- Division/League system on server

**Impact**: HIGH - Affects Guild War Matchmaking, Division Assignment, Opponent Selection

**Notes**: Client code shows LeagueClient<GuildWarDivisionModel> but actual matchmaking logic not found

---

### Guild War: Guild War matchmaking: MatchGuild

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `MatchGuild`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Searched for matchmaking logic matching pattern 'MatchGuild' but found no matches. Matchmaking algorithm may be implemented server-side or in native code.

**Potential Sources**:

- Server-side matchmaking service (not in client dump)
- Native ARM code in libil2cpp.so
- Metaplay framework server code
- Division/League system on server

**Impact**: HIGH - Affects Guild War Matchmaking, Division Assignment, Opponent Selection

**Notes**: Client code shows LeagueClient<GuildWarDivisionModel> but actual matchmaking logic not found

---

### Guild War: Tier threshold values (RequiredPoints per tier)

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `GuildWar.*`
- Pattern: `GuildTier.*`
- Pattern: `Division.*`
- Pattern: `League.*`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

GuildTierConfig structure found but actual values not in IL2CPP dump

**Potential Sources**:

- SharedGameConfig.mpa file or server configuration

**Impact**: HIGH - Affects Guild War Matchmaking, Tier System, War Points

**Notes**: Client code shows data structures but not actual values or server-side logic

---

### Guild War: Tier point change values (TierPointsOnWin/TierPointsOnLose)

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `GuildWar.*`
- Pattern: `GuildTier.*`
- Pattern: `Division.*`
- Pattern: `League.*`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

Fields exist in GuildTierConfig but values not in IL2CPP dump

**Potential Sources**:

- SharedGameConfig.mpa file or server configuration

**Impact**: HIGH - Affects Guild War Matchmaking, Tier System, War Points

**Notes**: Client code shows data structures but not actual values or server-side logic

---

### Guild War: Matchmaking algorithm (opponent selection)

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `GuildWar.*`
- Pattern: `GuildTier.*`
- Pattern: `Division.*`
- Pattern: `League.*`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

No client-side matchmaking logic found, likely server-side

**Potential Sources**:

- Server-side division/league matchmaking service

**Impact**: HIGH - Affects Guild War Matchmaking, Tier System, War Points

**Notes**: Client code shows data structures but not actual values or server-side logic

---

### Guild War: Division assignment logic

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `GuildWar.*`
- Pattern: `GuildTier.*`
- Pattern: `Division.*`
- Pattern: `League.*`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

LeagueClient reference found but division creation/assignment logic not in client

**Potential Sources**:

- Server-side league management system

**Impact**: HIGH - Affects Guild War Matchmaking, Tier System, War Points

**Notes**: Client code shows data structures but not actual values or server-side logic

---

## Medium Priority Gaps

### Guild War: War points calculation formula

**Status**: UNVERIFIED

**Searched For**:

- Pattern: `GuildWar.*`
- Pattern: `GuildTier.*`
- Pattern: `Division.*`
- Pattern: `League.*`
- Location: C:\apktool\il2cpp-output\dump.cs (all lines)

**What's Missing**:

MaxPointsForAttackingOpponentGuildMember field exists but calculation logic not found

**Potential Sources**:

- Server-side battle resolution code

**Impact**: MEDIUM - Affects Guild War Matchmaking, Tier System, War Points

**Notes**: Client code shows data structures but not actual values or server-side logic

---

## Search Summary

**Total Searches**: 37

**Found**: 34

**Not Found**: 8

**Partial Matches**: 0

**Success Rate**: 91.9%

## Most Common Missing Data

- **Server-side logic**: 4 instances
- **Configuration values**: 2 instances
- **Formula details**: 1 instances
- **Other**: 1 instances

## Next Steps

1. **Analyze .mpa config files** - May contain missing configuration values
2. **Analyze ARM code in libil2cpp.so** - May contain native implementations
3. **Decompile server code** - If accessible, may reveal server-side logic
4. **Test in-game** - Empirically determine missing values through gameplay testing
5. **Review game updates** - Check if newer versions expose more information
