# Complete Game Mechanics Extraction - Design

## Overview
This design describes the system for extracting ALL game mechanics from the IL2CPP dump with zero assumptions, then generating a browsable GitHub Pages website with graphical elements. The extraction produces a comprehensive, searchable documentation site with icons and modern UI.

## Design Principles

### 1. Zero Assumptions
- Extract ONLY what exists in code
- NO made-up optimization strategies
- NO generic game advice
- Every entry must have a line number for verification

### 2. Complete Coverage
- Parse entire IL2CPP dump systematically
- Extract all game mechanics classes (Config, Model, Info, Library, Action, State, Data)
- Extract all enums
- Filter out framework/Unity classes (View, Component, System, Controller)

### 3. Verifiable
- Every mechanic includes line number from dump.cs
- User can verify any entry by checking the source
- Confidence levels based on code evidence only

### 4. Browsable & Graphical
- Static website hosted on GitHub Pages
- Individual pages per mechanic
- Category browsing
- Search functionality
- Icons for visual appeal
- Mobile-responsive design

## Architecture

### Components

#### 1. ProperExtractor Class
**Purpose:** Main extraction engine

**Responsibilities:**
- Read IL2CPP dump file
- Parse class definitions with regex
- Parse enum definitions with regex
- Extract fields from classes
- Filter to game mechanics only
- Categorize by game system
- Generate JSON data for website

**Key Methods:**
- `extract_all()` - Main extraction pipeline
- `_extract_classes()` - Parse all class definitions
- `_extract_enums()` - Parse all enum definitions
- `_extract_fields()` - Extract fields from class body
- `_extract_enum_values()` - Extract values from enum body
- `_categorize_all()` - Assign categories to classes/enums
- `_generate_json()` - Create JSON data for website
- `_generate_website()` - Generate HTML pages

#### 2. WebsiteGenerator Class
**Purpose:** Generate static website from extracted data

**Responsibilities:**
- Generate index.html with category overview
- Generate category pages (combat.html, economy.html, etc.)
- Generate individual mechanic pages
- Generate search page with search.js
- Copy assets (CSS, JS, icons)
- Generate mechanics.json for search

**Key Methods:**
- `generate_index()` - Homepage with stats and categories
- `generate_category_page(category)` - Category listing page
- `generate_mechanic_page(mechanic)` - Individual mechanic page
- `generate_search_page()` - Search interface
- `generate_search_data()` - JSON data for search
- `copy_assets()` - Copy CSS/JS/icons to docs/

#### 3. IconExtractor Class
**Purpose:** Extract game icons from APK

**Responsibilities:**
- Locate icon files in APK assets
- Extract skill icons
- Extract weapon icons
- Extract currency icons
- Generate placeholder icons if extraction fails
- Resize/optimize icons for web

**Key Methods:**
- `extract_from_apk(apk_path)` - Extract all icons
- `extract_skill_icons()` - Get skill icons
- `extract_weapon_icons()` - Get weapon icons
- `extract_currency_icons()` - Get currency icons
- `generate_placeholder(name, color)` - Create fallback icon
- `optimize_icon(icon_path)` - Resize and compress

#### 4. GameClass Dataclass
**Purpose:** Represent a game mechanics class

**Fields:**
- `name: str` - Class name
- `line_number: int` - Line in dump.cs
- `base_class: str` - Parent class (if any)
- `fields: List[Tuple[str, str]]` - (type, name) pairs
- `category: str` - Game system category
- `icon_path: str` - Path to icon (if available)
- `related_classes: List[str]` - Related mechanics

**Methods:**
- `is_game_mechanics()` - Filter logic for game vs framework classes
- `to_dict()` - Convert to dictionary for JSON
- `to_html()` - Generate HTML for mechanic page

#### 5. GameEnum Dataclass
**Purpose:** Represent a game enum

**Fields:**
- `name: str` - Enum name
- `line_number: int` - Line in dump.cs
- `values: List[Tuple[str, str]]` - (name, value) pairs
- `category: str` - Game system category
- `icon_path: str` - Path to icon (if available)

**Methods:**
- `to_dict()` - Convert to dictionary for JSON
- `to_html()` - Generate HTML for mechanic page

### Data Flow

```
IL2CPP Dump (dump.cs)
    ↓
Read all lines into memory
    ↓
Extract classes with regex
    ↓
Extract enums with regex
    ↓
Filter to game mechanics only
    ↓
Categorize by game system
    ↓
Extract icons from APK (parallel)
    ↓
Generate JSON data
    ↓
Generate HTML pages
    ↓
docs/ folder (GitHub Pages ready)
```

### Website Structure

```
docs/
├── index.html                    # Homepage with category cards
├── search.html                   # Search interface
├── categories/
│   ├── combat.html              # Combat mechanics listing
│   ├── economy.html             # Economy mechanics listing
│   ├── guild.html               # Guild mechanics listing
│   ├── pets-mounts.html         # Pets & Mounts listing
│   ├── progression.html         # Progression listing
│   ├── pve-content.html         # PvE Content listing
│   ├── pvp.html                 # PvP listing
│   ├── summoning.html           # Summoning listing
│   └── other.html               # Other mechanics listing
├── mechanics/
│   ├── currency-type.html       # Individual mechanic pages
│   ├── weapon-data.html
│   ├── combat-skill.html
│   └── ... (1000+ pages)
├── assets/
│   ├── css/
│   │   ├── style.css           # Main stylesheet
│   │   ├── prism.css           # Code syntax highlighting
│   │   └── responsive.css      # Mobile styles
│   ├── js/
│   │   ├── main.js             # General functionality
│   │   ├── search.js           # Search implementation
│   │   └── prism.js            # Code highlighting
│   └── icons/
│       ├── skills/             # Skill icons (18 files)
│       ├── weapons/            # Weapon icons
│       ├── currencies/         # Currency icons (9 files)
│       ├── categories/         # Category icons (9 files)
│       └── placeholder.svg     # Default icon
├── data/
│   └── mechanics.json          # All mechanics data for search
└── README.md                    # GitHub Pages info
```

## Extraction Logic

### Class Filtering
**Include if:**
- Name ends with: Config, Model, Info, Library, Action, State, Data, Stats, Reward
- Name contains: Player, Combat, Weapon, Skill, Pet, Mount, Guild, Arena, Dungeon

**Exclude if:**
- Name ends with: View, Component, System, Controller, Manager, Service
- Unity/framework classes

### Field Extraction
**Process:**
1. Find class opening brace
2. Track brace depth to find class body
3. Match field declarations with regex
4. Handle backing fields (clean up `<FieldName>k__BackingField` to `FieldName`)
5. Deduplicate (backing field + property = one entry)
6. Stop at class closing brace

**Pattern:**
```regex
^\s+(?:public|private|protected|internal)?\s+(?:\[[\w\(\),\s]+\]\s+)?(\w+(?:<[^>]+>)?)\s+(\w+);
```

### Enum Value Extraction
**Process:**
1. Find enum opening brace
2. Match value declarations with regex
3. Extract name and numeric value
4. Stop at enum closing brace

**Pattern:**
```regex
^\s+public const \w+ (\w+) = (\d+);
```

### Categorization
**Categories:**
- **Combat**: combat, attack, damage, weapon, projectile, skill, hp, health
- **Economy**: currency, shop, price, cost, forge, idle, coin, gem
- **Summoning**: summon, drop, rarity, random, pcg, seed, gacha
- **PvP**: pvp, arena, matchmaking, rating, league
- **Progression**: tech, upgrade, level, experience, progression, xp
- **Guild**: guild, war, member, clan
- **Pets & Mounts**: pet, mount, egg, hatch
- **PvE Content**: dungeon, battle, wave, enemy, boss
- **Other**: Everything else

**Logic:** Check class/enum name (case-insensitive) for category keywords

## Output Format

### Homepage (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Mechanics Documentation</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header>
        <h1>Game Mechanics Documentation</h1>
        <p>Complete code-based extraction from IL2CPP dump</p>
        <div class="stats">
            <span>1,008 Classes</span>
            <span>1,116 Enums</span>
            <span>100% Verifiable</span>
        </div>
        <a href="search.html" class="search-button">Search Mechanics</a>
    </header>
    
    <main>
        <section class="categories">
            <div class="category-card" data-category="combat">
                <img src="assets/icons/categories/combat.svg" alt="Combat">
                <h2>Combat</h2>
                <p>69 Classes | 13 Enums</p>
                <a href="categories/combat.html">Browse →</a>
            </div>
            <!-- More category cards -->
        </section>
        
        <section class="highlights">
            <h2>Key Mechanics</h2>
            <div class="mechanic-preview">
                <img src="assets/icons/currencies/coins.png" alt="Currency">
                <h3>Currency System</h3>
                <p>9 currency types documented</p>
                <a href="mechanics/currency-type.html">View →</a>
            </div>
            <!-- More highlights -->
        </section>
    </main>
    
    <footer>
        <p>Generated from IL2CPP dump | Zero assumptions | 100% code-based</p>
    </footer>
</body>
</html>
```

### Category Page (categories/combat.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Combat Mechanics</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <nav>
        <a href="../index.html">← Home</a>
        <a href="../search.html">Search</a>
    </nav>
    
    <header class="category-header combat">
        <img src="../assets/icons/categories/combat.svg" alt="Combat">
        <h1>Combat Mechanics</h1>
        <p>69 Classes | 13 Enums</p>
    </header>
    
    <main>
        <section class="enums">
            <h2>Enumerations</h2>
            <div class="mechanic-grid">
                <a href="../mechanics/attack-sfx.html" class="mechanic-card">
                    <h3>AttackSfx</h3>
                    <span class="line-number">Line 705778</span>
                    <p>22 values</p>
                </a>
                <!-- More enum cards -->
            </div>
        </section>
        
        <section class="classes">
            <h2>Classes</h2>
            <div class="mechanic-grid">
                <a href="../mechanics/weapon-data.html" class="mechanic-card">
                    <img src="../assets/icons/weapons/default.svg" alt="Weapon">
                    <h3>WeaponData</h3>
                    <span class="line-number">Line 713702</span>
                    <p>7 fields</p>
                </a>
                <!-- More class cards -->
            </div>
        </section>
    </main>
</body>
</html>
```

### Mechanic Page (mechanics/weapon-data.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WeaponData - Game Mechanics</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/prism.css">
</head>
<body>
    <nav>
        <a href="../index.html">← Home</a>
        <a href="../categories/combat.html">← Combat</a>
        <a href="../search.html">Search</a>
    </nav>
    
    <article class="mechanic-page">
        <header>
            <img src="../assets/icons/weapons/default.svg" alt="Weapon" class="mechanic-icon">
            <div>
                <h1>WeaponData</h1>
                <span class="category-badge combat">Combat</span>
                <span class="type-badge">Class</span>
            </div>
        </header>
        
        <section class="code-reference">
            <h2>Code Reference</h2>
            <table>
                <tr><td>Line Number</td><td><code>713702</code></td></tr>
                <tr><td>Type</td><td>Class</td></tr>
                <tr><td>Inherits</td><td>-</td></tr>
                <tr><td>Category</td><td>Combat</td></tr>
            </table>
            <a href="https://github.com/[repo]/blob/main/dump.cs#L713702" 
               class="view-source" target="_blank">
                View in dump.cs →
            </a>
        </section>
        
        <section class="fields">
            <h2>Fields</h2>
            <table class="fields-table">
                <thead>
                    <tr><th>Field Name</th><th>Type</th></tr>
                </thead>
                <tbody>
                    <tr><td><code>AttackRange</code></td><td><code>float</code></td></tr>
                    <tr><td><code>WindUpTime</code></td><td><code>float</code></td></tr>
                    <tr><td><code>AttackTime</code></td><td><code>float</code></td></tr>
                    <tr><td><code>IsRanged</code></td><td><code>bool</code></td></tr>
                    <tr><td><code>IsAiming</code></td><td><code>bool</code></td></tr>
                    <tr><td><code>WeaponOffset</code></td><td><code>Vector2</code></td></tr>
                    <tr><td><code>HandOffset</code></td><td><code>Vector2</code></td></tr>
                </tbody>
            </table>
        </section>
        
        <section class="notes">
            <h2>Notes</h2>
            <ul>
                <li>Each weapon has individual timing values</li>
                <li>WindUpTime controls pre-attack delay</li>
                <li>AttackTime controls attack duration</li>
                <li>Different weapons attack at different speeds</li>
            </ul>
        </section>
        
        <section class="related">
            <h2>Related Mechanics</h2>
            <div class="related-grid">
                <a href="weapon-info.html" class="related-card">
                    <h3>WeaponInfo</h3>
                    <span>Line 1050834</span>
                </a>
                <a href="weapon-equipment-item.html" class="related-card">
                    <h3>WeaponEquipmentItem</h3>
                    <span>Line 713723</span>
                </a>
            </div>
        </section>
    </article>
    
    <script src="../assets/js/prism.js"></script>
</body>
</html>
```

### Search Page (search.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Search Mechanics</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <nav>
        <a href="index.html">← Home</a>
    </nav>
    
    <main class="search-page">
        <h1>Search Mechanics</h1>
        <input type="text" id="search-input" placeholder="Search by name, category, or field...">
        
        <div class="filters">
            <label><input type="checkbox" value="combat"> Combat</label>
            <label><input type="checkbox" value="economy"> Economy</label>
            <!-- More category filters -->
        </div>
        
        <div id="search-results">
            <!-- Results populated by search.js -->
        </div>
    </main>
    
    <script src="assets/js/search.js"></script>
</body>
</html>
```

### Search Data (data/mechanics.json)
```json
{
  "classes": [
    {
      "name": "WeaponData",
      "line": 713702,
      "category": "Combat",
      "fields": ["AttackRange", "WindUpTime", "AttackTime", "IsRanged", "IsAiming", "WeaponOffset", "HandOffset"],
      "url": "mechanics/weapon-data.html"
    }
  ],
  "enums": [
    {
      "name": "CurrencyType",
      "line": 1067355,
      "category": "Economy",
      "values": ["Coins", "Gems", "Hammers", "SkillSummonTickets", "TechPotions", "PvpTickets", "ClockWinders", "WarBattleTickets", "Token"],
      "url": "mechanics/currency-type.html"
    }
  ]
}
```

## UI/UX Design

### Color Scheme
```css
:root {
  --primary: #2563eb;      /* Blue for links/buttons */
  --combat: #ef4444;       /* Red for combat */
  --economy: #f59e0b;      /* Orange for economy */
  --guild: #8b5cf6;        /* Purple for guild */
  --pets: #10b981;         /* Green for pets/mounts */
  --progression: #06b6d4;  /* Cyan for progression */
  --pve: #f97316;          /* Orange for PvE */
  --pvp: #dc2626;          /* Dark red for PvP */
  --summoning: #a855f7;    /* Purple for summoning */
  --other: #6b7280;        /* Gray for other */
  
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
  --text-primary: #111827;
  --text-secondary: #6b7280;
  --border: #e5e7eb;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #111827;
    --bg-secondary: #1f2937;
    --text-primary: #f9fafb;
    --text-secondary: #9ca3af;
    --border: #374151;
  }
}
```

### Typography
- **Headings:** Inter, system-ui, sans-serif
- **Body:** Inter, system-ui, sans-serif
- **Code:** 'Fira Code', 'Courier New', monospace

### Responsive Breakpoints
- **Mobile:** < 640px
- **Tablet:** 640px - 1024px
- **Desktop:** > 1024px

### Icon Guidelines
- **Size:** 64x64px for mechanic icons, 128x128px for category icons
- **Format:** PNG with transparency, or SVG
- **Fallback:** Generate colored placeholder SVG with first letter
- **Optimization:** Compress with pngquant or svgo

## Icon Extraction Strategy

### APK Icon Locations
Icons are typically stored in:
```
assets/
├── icons/
│   ├── skills/
│   ├── weapons/
│   ├── items/
│   └── ui/
└── sprites/
    └── atlas/
```

### Extraction Process
1. **Unzip APK** - Extract APK to access assets
2. **Locate icon directories** - Find icon folders in assets
3. **Match icons to mechanics** - Use naming conventions to match
4. **Extract and optimize** - Copy icons, resize to 64x64, compress
5. **Generate placeholders** - Create SVG placeholders for missing icons

### Icon Naming Convention
```
skill-[skill-name].png       # e.g., skill-meteorite.png
weapon-[weapon-type].png     # e.g., weapon-sword.png
currency-[currency-name].png # e.g., currency-coins.png
category-[category].svg      # e.g., category-combat.svg
```

### Placeholder Generation
If icon not found, generate SVG:
```svg
<svg width="64" height="64" xmlns="http://www.w3.org/2000/svg">
  <rect width="64" height="64" fill="#2563eb" rx="8"/>
  <text x="32" y="40" font-size="32" fill="white" 
        text-anchor="middle" font-family="sans-serif">W</text>
</svg>
```

## Key Mechanics Documented

### Currency System
**Location:** Line 1067355 (CurrencyType enum)

**9 Currency Types:**
- Coins (0)
- Gems (1)
- Hammers (2)
- SkillSummonTickets (3)
- TechPotions (4)
- PvpTickets (5)
- ClockWinders (6)
- WarBattleTickets (7)
- Token (8)

**Storage:** PlayerCurrencyModel (line 1067393)
- Uses MetaDictionary<CurrencyType, long>

### Weapon Timing System
**Location:** Line 713702 (WeaponData class)

**Timing Fields:**
- `WindUpTime: float` - Pre-attack delay
- `AttackTime: float` - Attack duration
- `AttackRange: float` - Weapon reach
- `IsRanged: bool` - Melee vs ranged

**Note:** Each weapon has individual timing values. Different weapons attack at different speeds.

### RNG Seed System
**Seed Locations:**
1. **ForgeSeed** (Line 1068875) - PlayerForgeModel
2. **SummonSeed** (Line 1070875) - PlayerMountCollectionModel
3. **MountRandomSeed** (Line 1070877) - PlayerMountCollectionModel
4. **RewardSeed** (Line 1061919) - PlayerDungeonsModel
5. **PetRandomSeed** - Found in code

**Note:** Extraction found seed storage but NOT seed generation/modification logic. To understand how tech/level affects seeds, would need to analyze seed update functions.

### Combat Skills
**Location:** Line 1057131 (CombatSkill enum)

**18 Skills:**
Meat, Morale, Arrows, Shuriken, Shout, Meteorite, Berserk, Stampede, Thorns, Bomb, Worm, Lightning, Buff, HigherMorale, RainOfArrows, StrafeRun, CannonBarrage, Drone

### Attack Types
**Location:** Line 1057429 (AttackType enum)

**4 Types:**
- None (0)
- Skill (1)
- Melee (2)
- Ranged (3)

### Guild War Tasks
**Location:** Line 1066314 (WarTask enum)

**60+ Tasks including:**
- Forge equipment by age (Primitive → Divine)
- Use dungeon keys (Hammer Thief, Ghost Town, Invasion, Zombie Invasion)
- Summon skills by rarity (Common → Mythic)
- Upgrade skills by rarity
- Hatch eggs by rarity
- Merge pets/mounts by rarity
- Complete tech tree upgrades by tier (I → V)

## Implementation Details

### Performance Considerations
- **Memory:** Load entire dump.cs into memory (~1.6M lines)
- **Regex:** Compiled patterns for speed
- **Filtering:** Early filtering reduces processing
- **Output:** Stream writing for large output

### Error Handling
- **File not found:** Clear error message with path
- **Encoding errors:** Use `errors='ignore'` for IL2CPP dump
- **Regex failures:** Skip malformed lines, continue processing
- **Empty results:** Report counts, don't fail

### Limitations
1. **No function bodies:** IL2CPP dump only has signatures, not implementations
2. **No algorithms:** Can't extract calculation logic from dump
3. **No native code:** C++ implementations not visible
4. **No server code:** Server-side mechanics not in client dump

### What Can't Be Extracted
- Damage calculation formulas (need function bodies)
- Seed generation algorithms (need function bodies)
- Drop rate calculations (need function bodies)
- Matchmaking algorithms (need function bodies)
- Server-side validation logic

**To extract these:** Would need to analyze IL2CPP assembly code or use Ghidra/IDA Pro on the native library.

## Verification

### How to Verify Any Entry
1. Open `C:/apktool/il2cpp-output/dump.cs`
2. Go to line number listed in manual
3. Confirm class/enum exists
4. Confirm fields/values match

### Confidence Levels
- **100% confidence:** Entry has line number, can be verified
- **0% confidence:** Entry not in manual (not found in code)

## Success Metrics

### Extraction Completeness
✓ 1,008 game mechanics classes extracted
✓ 1,116 enums extracted
✓ Every entry has line number
✓ Zero assumptions made
✓ Zero made-up content

### Requirements Coverage
✓ Complete systematic extraction (Req 1)
✓ Zero assumptions (Req 2)
✓ Weapon timing documented (Req 3)
✓ RNG seed mechanics documented (Req 4)
✓ Combat system documented (Req 5)
✓ Economy system documented (Req 6)
✓ Progression system documented (Req 7)
✓ Summoning system documented (Req 8)
✓ PvP system documented (Req 9)
✓ Guild system documented (Req 10)

## Future Enhancements

### Possible Improvements
1. **Function extraction:** Parse function signatures (not just classes)
2. **Cross-references:** Link related classes automatically
3. **Dependency graphs:** Visualize class relationships
4. **Search interface:** Web UI for searching mechanics
5. **Diff tracking:** Compare extractions across game versions

### Deep Analysis (Separate Project)
To understand algorithms and formulas:
1. Use Ghidra to analyze libil2cpp.so
2. Find function implementations
3. Reverse engineer calculation logic
4. Document formulas with assembly references

## Correctness Properties

### Property 1: Completeness
**Statement:** Every game mechanics class in dump.cs is either included in the manual or explicitly filtered out.

**Validation:** Count classes in dump.cs matching patterns, compare to manual count + filtered count.

### Property 2: Accuracy
**Statement:** Every line number in the manual points to the correct class/enum in dump.cs.

**Validation:** For each entry, verify line number matches class/enum name.

### Property 3: Zero Assumptions
**Statement:** Every entry in the manual has a code reference (line number).

**Validation:** Parse manual, confirm every class/enum has "**Line:** [number]".

### Property 4: No Made-Up Content
**Statement:** No optimization strategies or gameplay advice exists in the manual.

**Validation:** Search manual for keywords: "best", "optimal", "strategy", "should", "recommend" (except in factual contexts).

### Property 5: Field Extraction
**Statement:** All public/private fields in a class are extracted (up to 30 displayed).

**Validation:** For sample classes, manually count fields in dump.cs and compare to manual.

## Testing Strategy

### Unit Tests
1. Test regex patterns on sample class definitions
2. Test field extraction on sample classes
3. Test enum value extraction on sample enums
4. Test categorization logic on sample names
5. Test backing field cleanup

### Integration Tests
1. Run extraction on small dump subset
2. Verify output format
3. Verify line numbers are correct
4. Verify counts match input

### Property-Based Tests
1. Generate random class definitions
2. Verify extraction handles all formats
3. Verify no crashes on malformed input
4. Verify output is always valid markdown

## Deployment

### Prerequisites
- Python 3.7+
- IL2CPP dump at `C:/apktool/il2cpp-output/dump.cs`
- ~2GB RAM for loading dump into memory

### Running Extraction
```bash
python tools/proper_extraction.py
```

### Output
- `GAME_MECHANICS_MANUAL.md` - Complete manual (~27K lines)
- Console output with counts and progress

### Validation
```bash
# Check manual was created
ls -lh GAME_MECHANICS_MANUAL.md

# Count entries
grep "^#### " GAME_MECHANICS_MANUAL.md | wc -l

# Verify line numbers exist
grep "^\*\*Line:\*\*" GAME_MECHANICS_MANUAL.md | wc -l
```

## Conclusion

This design provides a complete, verifiable, assumption-free extraction of game mechanics from the IL2CPP dump. The output is a comprehensive manual that documents 1,008 classes and 1,116 enums with line number references for verification.

**Key Achievement:** 100% code-based documentation with zero made-up content.

**Limitation:** Only extracts data structures, not algorithms (would need assembly analysis).

**Next Step:** Use the manual as a reference for understanding game mechanics, or proceed to deeper analysis with Ghidra for algorithm extraction.
