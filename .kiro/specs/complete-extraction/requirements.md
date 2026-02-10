# Complete Game Mechanics Extraction - Requirements

## Overview
Extract ALL game mechanics from the IL2CPP dump with ZERO assumptions. Document only what exists in code with line number references.

## Core Principle
**EXTRACT EVERYTHING. ASSUME NOTHING.**

## User Requirements

### 1. Complete Systematic Extraction
**As a user**, I want every game mechanic extracted from the code so that nothing is missed.

**Acceptance Criteria:**
- Parse entire IL2CPP dump systematically
- Extract ALL classes (Config, Model, Info, Library, etc.)
- Extract ALL enums
- Extract ALL structs
- Group by game system (Combat, Economy, Progression, etc.)
- Provide line numbers for every item
- NO mechanics should be missed

### 1.1 GitHub Pages Website
**As a user**, I want a browsable website hosted on GitHub Pages so I can easily navigate mechanics.

**Acceptance Criteria:**
- Generate static HTML website from extracted data
- Host on GitHub Pages
- Browsable by category (Combat, Economy, etc.)
- Browsable by individual mechanic
- Search functionality
- Responsive design (mobile-friendly)
- Fast loading times

### 1.2 Graphical Interface
**As a user**, I want a graphical interface with icons so the documentation is visually appealing.

**Acceptance Criteria:**
- Extract game icons from APK if possible
- Use icons for skills, weapons, currencies, etc.
- Fallback to placeholder icons if extraction fails
- Clean, modern UI design
- Category icons/colors
- Syntax highlighting for code blocks

### 2. Zero Assumptions
**As a user**, I want only factual mechanics from code, with no made-up content.

**Acceptance Criteria:**
- NO "optimization strategies" unless they exist as code/algorithms
- NO assumed mechanics
- NO generic game advice
- Every mechanic must have a code reference (line number)
- If something isn't in the code, it's not in the manual

### 3. Weapon Timing Documentation
**As a user**, I want to know the exact timing values for different weapons.

**Acceptance Criteria:**
- Extract WeaponInfo class structure (line 1050834)
- Document that each weapon has individual WindupTime and AttackDuration
- Note that weapons are stored in GameConfigLibrary<ItemId, WeaponInfo>
- Explain that different weapon types have different values
- NO assumptions about which weapons are faster - just state the structure exists

### 4. RNG Seed Mechanics
**As a user**, I want to understand how RNG seeds work for summoning/crafting.

**Acceptance Criteria:**
- Extract all seed fields: ForgeSeed, SummonSeed, MountRandomSeed, RewardSeed, PetRandomSeed, SkinsRandomSeed
- Document seed types (ulong/uint64)
- Document where seeds are stored (which Model classes)
- Document seed initialization if found in code
- Document seed modification if found in code
- Only include what exists in code - no speculation

### 5. Complete Combat System
**As a user**, I want all combat mechanics documented.

**Acceptance Criteria:**
- All CombatStats fields
- All damage calculation steps (from AttacksSystem.GetDamage)
- All combat-related configs
- Weapon system
- Projectile system
- Skill system integration with combat
- Pet/Mount combat bonuses
- PvP modifications

### 6. Complete Economy System
**As a user**, I want all economy mechanics documented.

**Acceptance Criteria:**
- All 9 currency types (from CurrencyType enum)
- Shop system (ShopConfig, ShopItemConfig, etc.)
- Forge system (ForgeConfig, costs, timers)
- Idle/offline income (IdleConfig)
- Dungeon rewards (DungeonRewardConfig)
- All economy-related configs with line numbers

### 7. Complete Progression System
**As a user**, I want all progression mechanics documented.

**Acceptance Criteria:**
- Tech tree system (TechTreeConfig, nodes, costs, bonuses)
- Level system
- Experience system
- Skill progression
- Pet progression (PetUpgradeConfig)
- Mount progression (MountUpgradeConfig)
- Equipment progression (ForgeUpgradeLibrary)

### 8. Complete Summoning System
**As a user**, I want all summoning mechanics documented.

**Acceptance Criteria:**
- RNG algorithm (RandomPCG class)
- Drop tables (all *DropChanceConfig classes)
- Rarity determination
- Pity system (if it exists in code)
- Seed mechanics
- Summon costs
- Summon counts/levels

### 9. Complete PvP System
**As a user**, I want all PvP mechanics documented.

**Acceptance Criteria:**
- Matchmaking system
- Rating/ranking system
- PvP stat modifications (PvpBaseConfig multipliers)
- Arena system
- Guild war system
- Ticket system

### 10. Complete Guild System
**As a user**, I want all guild mechanics documented.

**Acceptance Criteria:**
- Guild creation (costs, limits)
- Guild roles and permissions
- Guild war system
- Guild progression
- Guild rewards

## Technical Requirements

### Extraction Process
1. Read entire IL2CPP dump (C:\apktool\il2cpp-output\dump.cs)
2. Parse all class definitions with line numbers
3. Parse all enum definitions with line numbers
4. Parse all struct definitions with line numbers
5. Group by naming patterns (*Config, *Model, *Info, *Library, etc.)
6. Cross-reference related classes
7. Generate documentation with line numbers

### Output Format

#### Website Structure
```
docs/
├── index.html                 # Homepage with category overview
├── search.html               # Search page
├── categories/
│   ├── combat.html          # Combat category page
│   ├── economy.html         # Economy category page
│   └── ...
├── mechanics/
│   ├── currency-type.html   # Individual mechanic pages
│   ├── weapon-data.html
│   └── ...
├── assets/
│   ├── css/
│   │   └── style.css        # Styling
│   ├── js/
│   │   ├── search.js        # Search functionality
│   │   └── main.js          # General scripts
│   └── icons/
│       ├── skills/          # Skill icons
│       ├── weapons/         # Weapon icons
│       ├── currencies/      # Currency icons
│       └── categories/      # Category icons
└── data/
    └── mechanics.json       # All mechanics data for search
```

#### Mechanic Page Format
```html
<div class="mechanic-page">
  <header>
    <img src="icon.png" alt="Icon" class="mechanic-icon">
    <h1>[Mechanic Name]</h1>
    <span class="category-badge">[Category]</span>
  </header>
  
  <section class="code-reference">
    <h2>Code Reference</h2>
    <p>Line: <a href="dump.cs#L[line]">[line_number]</a></p>
    <p>Type: [Class/Enum]</p>
    <p>Inherits: [BaseClass]</p>
  </section>
  
  <section class="fields">
    <h2>Fields/Values</h2>
    <table>
      <tr><td>Field1</td><td>Type1</td></tr>
      ...
    </table>
  </section>
  
  <section class="related">
    <h2>Related Mechanics</h2>
    <ul>
      <li><a href="related1.html">RelatedMechanic1</a></li>
    </ul>
  </section>
</div>
```

### Confidence Levels
- **HIGH**: Class/enum/struct found with line number
- **MEDIUM**: Inferred from multiple related classes
- **LOW**: Partial information, incomplete
- **NONE**: Remove from manual (not in code)

## Success Criteria
1. Every class in IL2CPP dump is categorized
2. Every mechanic has line number reference
3. Zero made-up content
4. Zero optimization strategies (unless algorithms exist in code)
5. Weapon timing structure documented
6. RNG seed system documented
7. All 9 currency types documented
8. Manual is 100% code-based
9. GitHub Pages website is live and browsable
10. Website has search functionality
11. Website includes icons (extracted or placeholder)
12. Website is mobile-responsive

## Out of Scope
- Gameplay advice
- Optimization strategies
- "Best practices"
- Assumptions about mechanics
- Speculation about missing features
