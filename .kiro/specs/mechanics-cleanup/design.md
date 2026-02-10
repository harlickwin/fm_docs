# Design Document: Mechanics Cleanup

## Overview

This feature enhances the existing GitHub Pages documentation by extracting missing game mechanics from the IL2CPP dump (C:\apktool\il2cpp-output\dump.cs) and adding them to docs/index.html and docs/war-pvp.html. The design follows an **absolute zero-hallucination policy**: every single statement must be verifiable from code, with explicit confidence levels and gap identification when information is incomplete or missing.

**Core Principle**: VERIFY EVERYTHING. ASSUME NOTHING. HALLUCINATE NOTHING.

The system will:
1. Extract ONLY what exists in dump.cs (IL2CPP) or ARM code
2. Mark confidence level for every extraction
3. Explicitly call out gaps, missing data, and uncertainties
4. Remove or mark as unverified any existing content that cannot be validated
5. Never infer, assume, or extrapolate beyond what code explicitly shows

## Architecture

### High-Level Flow

```
┌─────────────────────┐
│  IL2CPP Dump        │
│  (dump.cs)          │
│  1.2M lines         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Code Extraction    │
│  - Search patterns  │
│  - Line tracking    │
│  - Context capture  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Verification       │
│  - Validate refs    │
│  - Check formulas   │
│  - Assess confidence│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  HTML Generation    │
│  - Format content   │
│  - Add code refs    │
│  - Maintain styling │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Updated Docs       │
│  - index.html       │
│  - war-pvp.html     │
└─────────────────────┘
```

### Component Architecture

```
┌──────────────────────────────────────────────────┐
│              Extraction Layer                     │
│  ┌──────────────┐  ┌──────────────┐             │
│  │ Guild War    │  │ Dungeon      │             │
│  │ Extractor    │  │ Extractor    │             │
│  └──────────────┘  └──────────────┘             │
│  ┌──────────────┐  ┌──────────────┐             │
│  │ PvP League   │  │ Shop         │             │
│  │ Extractor    │  │ Extractor    │             │
│  └──────────────┘  └──────────────┘             │
│  ┌──────────────┐                                │
│  │ RNG/Drop     │                                │
│  │ Extractor    │                                │
│  └──────────────┘                                │
└──────────────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────┐
│           Verification Layer                      │
│  - Line number validation                         │
│  - Formula extraction                             │
│  - Confidence assessment                          │
│  - Missing data identification                    │
└──────────────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────┐
│           Documentation Layer                     │
│  - HTML template rendering                        │
│  - Code reference formatting                      │
│  - Example generation                             │
│  - Style preservation                             │
└──────────────────────────────────────────────────┘
```

## Components and Interfaces

### 1. Code Extraction Module

**Purpose**: Search and extract relevant code sections from dump.cs

**Interface**:
```python
class CodeExtractor:
    def __init__(self, dump_path: str):
        """Initialize with path to dump.cs"""
        
    def search_class(self, pattern: str) -> List[ClassMatch]:
        """Search for classes matching pattern
        Returns: List of (class_name, line_number, content)
        """
        
    def search_config(self, config_name: str) -> Optional[ConfigMatch]:
        """Search for configuration class
        Returns: ConfigMatch with fields and values
        """
        
    def extract_method(self, class_name: str, method_name: str) -> Optional[MethodMatch]:
        """Extract specific method from class
        Returns: MethodMatch with signature and body
        """
        
    def extract_formula(self, method_body: str) -> List[FormulaExtraction]:
        """Extract mathematical formulas from method body
        Returns: List of formulas with variables and operations
        """
        
    def get_context(self, line_number: int, lines_before: int, lines_after: int) -> str:
        """Get code context around a line number"""
```

**Key Classes to Extract**:
- Guild war: `GuildWarConfig`, `GuildTierConfig`, `GuildWarMatchmaking`
- Dungeons: `DungeonConfig`, `DungeonLevelConfig`, `DungeonRewardConfig`
- PvP: `PvpLeagueConfig`, `PvpMatchmaking`, `PvpBaseConfig`
- Shop: `ShopRefreshConfig`, `PlayerShopModel`, `ShopItemConfig`
- RNG: `MountSummonDropChanceConfig`, `DungeonDropConfig`
- Combat: `AttacksSystem`, `UnitEntity`, `WeaponInfo`, `DamageCalculation`
- Stats: `AttackSpeedMulti`, `CriticalHit`, `Dodge`, `Block`, `LifeSteal`

### 2. Verification Module

**Purpose**: Validate extracted code and assess confidence with ZERO tolerance for assumptions

**Interface**:
```python
class CodeVerifier:
    def verify_line_reference(self, line_number: int, expected_content: str) -> bool:
        """Verify line number points to expected content
        Returns: True only if exact match found
        """
        
    def extract_formula(self, method_body: str) -> Optional[Formula]:
        """Extract mathematical formula from method
        Returns: Formula object ONLY if formula is explicit and clear
        Returns: None if formula requires interpretation or assumption
        """
        
    def assess_confidence(self, extraction: Extraction) -> ConfidenceLevel:
        """Assess confidence level of extraction
        HIGH: Complete code found, formula explicit, all values present
        MEDIUM: Code found, some values in config, formula clear but incomplete
        LOW: Partial code, formula requires interpretation
        UNVERIFIED: No code found or cannot validate
        """
        
    def identify_missing_data(self, extraction: Extraction) -> List[str]:
        """Identify what data is missing or unclear
        Returns: Specific list of missing elements (class names, methods, values)
        """
        
    def check_for_assumptions(self, extraction: Extraction) -> List[str]:
        """Check if extraction contains any assumptions
        Returns: List of assumptions that need to be removed or verified
        """
```

**Verification Rules**:
1. **Exact Match Only**: Line numbers must point to exact code, not "similar" code
2. **No Interpretation**: If formula requires interpretation, mark as LOW confidence
3. **No Inference**: If value not in code, mark as MISSING, don't infer
4. **No Extrapolation**: If pattern exists for X but not Y, don't assume Y follows same pattern
5. **No External Sources**: Developer comments, forums, screenshots are NOT valid sources

### 3. Documentation Generator

**Purpose**: Generate HTML content with code references

**Interface**:
```python
class DocumentationGenerator:
    def __init__(self, template_path: str):
        """Initialize with HTML template"""
        
    def generate_section(self, mechanic: MechanicData) -> str:
        """Generate HTML section for a mechanic
        Returns: HTML string with proper formatting
        """
        
    def format_code_reference(self, line_number: int, class_name: str) -> str:
        """Format code reference link
        Returns: HTML link to line in dump.cs
        """
        
    def generate_example_table(self, examples: List[Example]) -> str:
        """Generate comparison table for examples
        Returns: HTML table element
        """
        
    def add_confidence_indicator(self, confidence: ConfidenceLevel, reason: str) -> str:
        """Add visual confidence indicator
        Returns: HTML element showing confidence level
        """
```

### 4. HTML Updater

**Purpose**: Update existing HTML files while preserving structure

**Interface**:
```python
class HTMLUpdater:
    def __init__(self, html_path: str):
        """Initialize with path to HTML file"""
        
    def find_section(self, section_id: str) -> Optional[Element]:
        """Find section by ID or heading"""
        
    def update_section(self, section_id: str, new_content: str) -> None:
        """Update section content"""
        
    def remove_unverified_content(self, section_id: str) -> List[str]:
        """Remove content that cannot be verified
        Returns: List of removed content for review
        """
        
    def preserve_styling(self) -> None:
        """Ensure CSS classes and structure are maintained"""
        
    def save(self, output_path: str) -> None:
        """Save updated HTML"""
```

### 5. GitHub Pages Configuration

**Purpose**: Fix rendering issues and ensure proper deployment

**Interface**:
```python
class GitHubPagesConfig:
    def create_nojekyll(self, docs_path: str) -> None:
        """Create .nojekyll file to disable Jekyll processing"""
        
    def verify_index(self, docs_path: str) -> bool:
        """Verify index.html exists and is valid"""
        
    def check_mime_types(self, docs_path: str) -> Dict[str, str]:
        """Check file extensions and expected MIME types"""
        
    def generate_config_yml(self, docs_path: str) -> None:
        """Generate _config.yml if needed"""
```

### 6. Knowledge Gap Tracker

**Purpose**: Maintain a comprehensive list of unknowns and missing information

**Interface**:
```python
class KnowledgeGapTracker:
    def __init__(self):
        """Initialize gap tracker"""
        self.gaps: List[KnowledgeGap] = []
        
    def add_gap(self, gap: KnowledgeGap) -> None:
        """Add a knowledge gap"""
        
    def get_gaps_by_category(self, category: str) -> List[KnowledgeGap]:
        """Get all gaps for a specific category"""
        
    def generate_summary(self) -> str:
        """Generate markdown summary of all gaps"""
        
    def export_to_file(self, output_path: str) -> None:
        """Export gaps to KNOWLEDGE_GAPS.md file"""
```

**KnowledgeGap Data Model**:
```python
@dataclass
class KnowledgeGap:
    category: str  # "guild_war", "dungeon", "pvp", "shop", "combat"
    title: str  # Short description
    description: str  # Detailed explanation of what's missing
    searched_patterns: List[str]  # What we searched for
    searched_locations: List[str]  # Where we searched (dump.cs lines, etc)
    potential_sources: List[str]  # Where this info might exist
    impact: str  # HIGH, MEDIUM, LOW - how important is this gap
    related_mechanics: List[str]  # What mechanics are affected
    notes: str  # Additional context
```

**Output Format** (KNOWLEDGE_GAPS.md):
```markdown
# Knowledge Gaps Summary

Last Updated: [timestamp]

## Overview
This document tracks all information we attempted to find but could not verify from code.

## High Priority Gaps

### Guild War: Two-Week Matchmaking Cycle
**Status**: UNVERIFIED
**Searched For**: 
- Pattern: `GuildWar.*Week`, `War.*Cycle`, `*TwoWeek*`, `*WeeklyMatch*`
- Locations: dump.cs lines 1-1,200,000
- Classes: GuildWarSystem, GuildWarConfig, MatchmakingSystem

**What's Missing**:
- Weekly cycle logic (Week 1 vs Week 2 behavior)
- Matchmaking algorithm differences between weeks
- Cycle reset timing

**Potential Sources**:
- Server-side code (not in client dump)
- Native ARM code in libil2cpp.so
- Configuration files (.mpa, .json) not yet analyzed

**Impact**: HIGH - Affects guild war strategy documentation

**Related Mechanics**: Guild matchmaking, tier progression

**Notes**: External sources claim two-week cycle exists, but no client-side code evidence found.

---

### Dungeon: Difficulty Multiplier Values
**Status**: PARTIAL
**Searched For**:
- Pattern: `DifficultyMultiplier`, `DungeonLevel.*Config`
- Locations: dump.cs lines 1-1,200,000
- Classes: DungeonConfig, DungeonLevelConfig

**What's Missing**:
- Actual multiplier values per dungeon level
- Formula found: `enemyHP = baseHP * difficultyMultiplier`
- But `difficultyMultiplier` values not in dump.cs

**Potential Sources**:
- SharedGameConfig.mpa file
- DungeonLevelConfig entries (class exists but values not in dump)
- Server-side configuration

**Impact**: MEDIUM - Can document formula but not calculate specific values

**Related Mechanics**: Dungeon scaling, reward calculations

**Notes**: Formula structure verified, only missing config values.

---

## Medium Priority Gaps

[Continue with more gaps...]

## Low Priority Gaps

[Continue with more gaps...]

## Search Summary

**Total Searches**: 47
**Classes Found**: 23
**Classes Not Found**: 15
**Partial Matches**: 9

**Most Common Missing Data**:
1. Configuration values (12 instances)
2. Server-side logic (8 instances)
3. Native code implementations (5 instances)

## Next Steps

1. **Analyze .mpa config files** - May contain missing configuration values
2. **Analyze ARM code in libil2cpp.so** - May contain native implementations
3. **Test in-game** - Empirically determine missing values
4. **Decompile server code** - If accessible, may reveal server-side logic
```

## Data Models

### MechanicData
```python
@dataclass
class MechanicData:
    name: str
    category: str  # "guild_war", "dungeon", "pvp", "shop", "rng"
    description: str
    code_references: List[CodeReference]
    formulas: List[Formula]
    examples: List[Example]
    confidence: ConfidenceLevel
    missing_data: List[str]
```

### CodeReference
```python
@dataclass
class CodeReference:
    line_number: int
    class_name: str
    method_name: Optional[str]
    content: str
    context: str  # Surrounding code for clarity
```

### Formula
```python
@dataclass
class Formula:
    name: str
    expression: str  # Human-readable formula
    code_expression: str  # Exact code from dump.cs
    variables: Dict[str, str]  # variable_name -> description
    source_line: int
    source_method: str
    verified: bool
    copy_pastable: bool  # True if can be used directly in calculations
```

### Example
```python
@dataclass
class Example:
    scenario: str
    inputs: Dict[str, Any]
    outputs: Dict[str, Any]
    explanation: str
    based_on_code: bool  # True if values from config, False if illustrative
```

### ConfidenceLevel
```python
class ConfidenceLevel(Enum):
    HIGH = "high"  # Complete code verification, no assumptions
    MEDIUM = "medium"  # Partial verification, some config values missing but logic clear
    LOW = "low"  # Limited code evidence, requires interpretation
    UNVERIFIED = "unverified"  # No code evidence, cannot validate
    
    def get_description(self) -> str:
        """Get human-readable description of confidence level"""
        descriptions = {
            "high": "Fully verified from code with all values present",
            "medium": "Logic verified but some config values not found",
            "low": "Partial code found, significant gaps in understanding",
            "unverified": "No code evidence found, cannot validate claim"
        }
        return descriptions[self.value]
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Code Reference Validity
*For any* mechanic documented in the HTML files, the line number reference should point to valid code in dump.cs that supports the documented behavior.

**Validates: Requirements 6.1, 6.7**

### Property 2: Zero Unverified Claims
*For any* statement in the documentation, it should either have a code reference or be explicitly marked as unverified with explanation.

**Validates: Requirements 6.2, 6.3, 6.4, 6.5**

### Property 3: Formula Extraction Accuracy
*For any* formula documented, it should be directly extractable from the referenced code without modification or interpretation.

**Validates: Requirements 6.6**

### Property 4: Example Value Traceability
*For any* example with specific numeric values, those values should be traceable to configuration data in dump.cs or clearly marked as illustrative.

**Validates: Requirements 6.8, 6.9**

### Property 5: Confidence Level Consistency
*For any* mechanic with confidence level less than HIGH, there should be an explicit explanation of what is missing or uncertain.

**Validates: Requirements 6.5**

### Property 6: HTML Structure Preservation
*For any* update to existing HTML files, the CSS classes, navigation structure, and responsive design should remain intact.

**Validates: Requirements 7.1, 7.2, 7.5**

### Property 7: Section Content Completeness
*For any* mechanic category (guild war, dungeon, PvP, shop, RNG), if code is found, it should be documented; if code is not found, the section should state what is missing.

**Validates: Requirements 1.6, 1.7, 2.6, 3.6, 4.6, 5.4**

### Property 8: GitHub Pages Rendering
*For any* HTML file in the docs folder, it should render as HTML in a browser, not display as raw code.

**Validates: Requirements 10.1, 10.2, 10.3, 10.4, 10.5, 10.6**

### Property 9: Formula Completeness
*For any* formula documented, all variables used in the formula should be defined with descriptions.

**Validates: Requirements 9.7**

### Property 10: Formula Copy-Pastability
*For any* formula marked as copy-pastable, it should be in a format that can be directly used in calculations without modification.

**Validates: Requirements 9.8**

### Property 11: Formula Chain Completeness
*For any* formula that references other formulas, the complete calculation chain should be documented.

**Validates: Requirements 9.9**

### Property 12: Formula Source Verification
*For any* formula, the source line number should point to the actual calculation method in dump.cs.

**Validates: Requirements 9.1, 9.2, 9.3, 9.4, 9.5, 9.10**

### Property 13: Knowledge Gap Completeness
*For any* search that returns no results, a knowledge gap entry should be created documenting the search.

**Validates: Requirements 11.1, 11.2, 11.3**

### Property 14: Knowledge Gap Categorization
*For any* knowledge gap, it should have a priority level and list of affected mechanics.

**Validates: Requirements 11.5, 11.7**

## Error Handling

### Zero-Hallucination Policy

**CRITICAL RULE**: When in doubt, mark as unverified. Never guess, infer, or assume.

### Code Extraction Errors

**Scenario**: Class or method not found in dump.cs
- **Action**: Mark mechanic as UNVERIFIED
- **Documentation**: "❌ **Not Found**: [ClassName] not found in IL2CPP dump (searched lines 1-1,200,000). This mechanic may not exist, may use different naming, or may be in native ARM code."
- **User Impact**: Clear that information is unavailable, no false claims

**Scenario**: Multiple matches for search pattern
- **Action**: Extract all matches, DO NOT choose one arbitrarily
- **Documentation**: "⚠️ **Multiple Matches**: Found [N] classes matching pattern. Manual review required. Line numbers: [list]"
- **User Impact**: Transparency about ambiguity

**Scenario**: Similar but not exact match found
- **Action**: Mark as LOW confidence, explain difference
- **Documentation**: "⚠️ **Partial Match**: Found [SimilarClass] at line [N], but expected [ExactClass]. May be related but cannot confirm."
- **User Impact**: User knows what was found vs what was expected

### Formula Extraction Errors

**Scenario**: Method body contains complex logic, formula not obvious
- **Action**: Extract entire method, mark confidence as LOW, DO NOT simplify
- **Documentation**: "⚠️ **Complex Logic**: Method contains branching/loops. Full code shown below. Cannot extract simple formula without making assumptions."
- **Code Block**: Show actual method body
- **User Impact**: User sees reality, can interpret themselves

**Scenario**: Formula references config values not in dump.cs
- **Action**: Mark missing values explicitly, set confidence to MEDIUM
- **Documentation**: "⚠️ **Missing Config**: Formula uses `ConfigClass.ValueName` (not found in dump.cs). Actual value unknown. Formula structure verified but cannot calculate without this value."
- **User Impact**: Clear about what's known vs unknown

**Scenario**: Formula requires interpretation (e.g., implicit conversions, unclear operations)
- **Action**: Mark as LOW confidence, show exact code, explain ambiguity
- **Documentation**: "⚠️ **Interpretation Required**: Code shows `value1 op value2` but operation type unclear. Exact code: [show code]. Cannot confirm without testing or ARM analysis."
- **User Impact**: Honesty about limitations

**Scenario**: External source claims formula but code doesn't match
- **Action**: IGNORE external source, document only what code shows
- **Documentation**: "❌ **Cannot Verify**: External sources claim [X], but code shows [Y]. Documenting only code-verified behavior: [Y]."
- **User Impact**: Code truth over external claims

### HTML Update Errors

**Scenario**: Existing content conflicts with extracted code
- **Action**: Replace with code-verified content, log old content with reason for removal
- **Documentation**: Add HTML comment: `<!-- REMOVED: [old content]. Reason: Cannot verify from code. Replaced with code-verified content. -->`
- **User Impact**: Audit trail, transparency

**Scenario**: Existing content has no code reference
- **Action**: Mark as unverified or remove
- **Documentation**: Add warning: "⚠️ **Unverified**: This information lacks code reference and cannot be validated. Treat as speculation."
- **User Impact**: Clear distinction between verified and unverified

**Scenario**: Section to update not found in HTML
- **Action**: Create new section with appropriate heading
- **Documentation**: Add to end of relevant page with clear heading
- **User Impact**: Content is added, structure maintained

### GitHub Pages Rendering Errors

**Scenario**: HTML displays as raw code
- **Action**: Create .nojekyll file in docs folder
- **Rationale**: GitHub Pages uses Jekyll by default, which can interfere with HTML rendering
- **User Impact**: Pages render correctly

**Scenario**: Files not found (404 errors)
- **Action**: Verify repository settings, check branch and folder configuration
- **Documentation**: Add troubleshooting section to README
- **User Impact**: Clear path to resolution

### Confidence Assessment Examples

**HIGH Confidence Example**:
```
✅ Attack Speed Formula
Formula: effectiveTime = baseTime / attackSpeedMulti
Source: dump.cs line 1057705, AttacksSystem.CalculateAttackTime()
Code: [exact code shown]
All variables defined in same class
Confidence: HIGH - Complete code verification, no assumptions
```

**MEDIUM Confidence Example**:
```
⚠️ Dungeon Scaling Formula
Formula: enemyHP = baseHP * difficultyMultiplier
Source: dump.cs line [N], DungeonSystem.CalculateEnemyHP()
Code: [exact code shown]
Missing: difficultyMultiplier values per level (referenced as DungeonConfig.DifficultyMultiplier but config not found)
Confidence: MEDIUM - Logic verified but multiplier values unknown
```

**LOW Confidence Example**:
```
⚠️ Guild War Matchmaking
Found: GuildWarSystem.FindOpponent() at line [N]
Code contains complex logic with multiple conditions
Cannot extract simple algorithm without interpretation
Missing: Tier threshold values, matchmaking weight calculations
Confidence: LOW - Partial code found, significant gaps
```

**UNVERIFIED Example**:
```
❌ Two-Week War Cycle
Claim: Wars alternate between random tier and war points matchmaking
Code Search: No evidence found in dump.cs for weekly cycle logic
Searched: GuildWar*, War*Match*, *WeeklyCycle*, *TwoWeek*
Confidence: UNVERIFIED - Cannot validate from code
Note: May exist in server-side code not present in client dump
```

## Testing Strategy

### Dual Testing Approach

This feature requires both unit tests and property-based tests:

**Unit Tests**: Focus on specific examples and edge cases
- Test extraction of known classes (e.g., MountSummonDropChanceConfig)
- Test HTML parsing and updating with sample files
- Test confidence level assignment for various scenarios
- Test .nojekyll file creation
- Test code reference formatting

**Property Tests**: Verify universal properties across all inputs
- Test that all documented mechanics have code references (Property 1)
- Test that all formulas are extractable from referenced code (Property 3)
- Test that HTML structure is preserved after updates (Property 6)
- Test that confidence levels are consistent with available data (Property 5)

### Property-Based Testing Configuration

**Library**: Use `hypothesis` for Python (property-based testing library)

**Configuration**: Minimum 100 iterations per property test

**Test Tagging**: Each property test must reference its design document property
- Format: `# Feature: mechanics-cleanup, Property {number}: {property_text}`

### Unit Testing Focus

Unit tests should cover:
1. **Specific extraction examples**: Known classes like `PlayerPetCollectionModel` (line 1070882)
2. **Edge cases**: Empty search results, malformed HTML, missing sections
3. **Error conditions**: File not found, invalid line numbers, parsing errors
4. **Integration points**: HTML updater with documentation generator

### Test Coverage Goals

- **Code extraction**: 90%+ coverage of extraction logic
- **Verification**: 100% coverage of confidence assessment
- **HTML generation**: 85%+ coverage of template rendering
- **Error handling**: 100% coverage of error scenarios

### Manual Verification Steps

1. **Visual inspection**: Review generated HTML in browser
2. **Code reference validation**: Spot-check 10 random line numbers
3. **Formula accuracy**: Verify 5 random formulas against dump.cs
4. **Responsive design**: Test on mobile, tablet, desktop
5. **GitHub Pages deployment**: Verify live site renders correctly

## Implementation Notes

### Formula Extraction and Presentation

**Goal**: Provide comprehensive, copy-pastable formulas for all game mechanics

**Extraction Strategy**:

1. **Identify calculation methods** in dump.cs:
   - `AttacksSystem.GetDamage()` - Damage calculation
   - `AttacksSystem.CalculateAttackTime()` - Attack speed
   - `CombatSystem.CheckCritical()` - Critical hits
   - `CombatSystem.CheckDodge()` - Dodge mechanics
   - `CombatSystem.CheckBlock()` - Block mechanics
   - `CombatSystem.CalculateLifeSteal()` - Life steal

2. **Extract complete formula chain**:
   ```
   Final Damage = BaseDamage × CritMultiplier × DoubleDamageMultiplier
   Where:
     BaseDamage = WeaponDamage + BonusDamage
     CritMultiplier = IsCrit ? CriticalMultiplier : 1.0
     DoubleDamageMultiplier = IsDoubleDamage ? 2.0 : 1.0
   ```

3. **Provide multiple formats**:
   - **Human-readable**: `Effective Attack Time = Base Attack Time / Attack Speed Multiplier`
   - **Code format**: `effectiveTime = baseTime / attackSpeedMulti`
   - **Spreadsheet format**: `=B2/C2` (with cell references explained)
   - **Mathematical notation**: `t_eff = t_base / m_speed`

4. **Document all variables**:
   ```
   Variables:
   - Base Attack Time (t_base): Weapon's base attack interval in seconds
   - Attack Speed Multiplier (m_speed): Combined multiplier from all sources
   - Effective Attack Time (t_eff): Actual time between attacks
   
   Source: dump.cs line 1057705, AttacksSystem.CalculateAttackTime()
   ```

**Formula Template**:

```html
<div class="formula-card">
    <h4>Formula Name</h4>
    
    <!-- Human-readable -->
    <div class="formula-readable">
        <strong>Formula:</strong>
        <code>Result = Input1 × Input2 / Input3</code>
    </div>
    
    <!-- Code format -->
    <div class="formula-code">
        <strong>Code:</strong>
        <pre>result = input1 * input2 / input3;</pre>
        <button class="copy-btn" data-copy="result = input1 * input2 / input3;">Copy</button>
    </div>
    
    <!-- Spreadsheet format -->
    <div class="formula-spreadsheet">
        <strong>Spreadsheet:</strong>
        <code>=A2*B2/C2</code>
        <span class="hint">(A2=Input1, B2=Input2, C2=Input3)</span>
    </div>
    
    <!-- Variables -->
    <div class="formula-variables">
        <strong>Variables:</strong>
        <ul>
            <li><code>Input1</code>: Description (typical range: X-Y)</li>
            <li><code>Input2</code>: Description (typical range: X-Y)</li>
            <li><code>Input3</code>: Description (typical range: X-Y)</li>
        </ul>
    </div>
    
    <!-- Source -->
    <div class="code-ref">
        <strong>Source:</strong> 
        <a href="#line-12345">dump.cs line 12345</a>, 
        ClassName.MethodName()
    </div>
    
    <!-- Example calculation -->
    <div class="formula-example">
        <strong>Example:</strong>
        <p>Input1 = 100, Input2 = 1.5, Input3 = 2.0</p>
        <p>Result = 100 × 1.5 / 2.0 = <strong>75</strong></p>
    </div>
</div>
```

**CSS for Formula Cards**:

```css
.formula-card {
    background: #f8f9fa;
    border-left: 4px solid var(--primary);
    padding: 16px;
    margin: 16px 0;
    border-radius: 4px;
}

.formula-readable,
.formula-code,
.formula-spreadsheet,
.formula-variables,
.formula-example {
    margin: 12px 0;
}

.formula-code pre {
    background: #2d2d2d;
    color: #f8f8f2;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    position: relative;
}

.copy-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    background: var(--primary);
    color: white;
    border: none;
    padding: 4px 8px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.85em;
}

.copy-btn:hover {
    background: var(--primary-dark);
}

.formula-variables ul {
    list-style: none;
    padding-left: 0;
}

.formula-variables li {
    padding: 4px 0;
    border-bottom: 1px solid #e0e0e0;
}

.formula-variables li:last-child {
    border-bottom: none;
}

.hint {
    font-size: 0.85em;
    color: #666;
    font-style: italic;
}
```

**JavaScript for Copy Functionality**:

```javascript
// Add to docs/assets/js/formulas.js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.copy-btn').forEach(button => {
        button.addEventListener('click', function() {
            const text = this.getAttribute('data-copy');
            navigator.clipboard.writeText(text).then(() => {
                const originalText = this.textContent;
                this.textContent = 'Copied!';
                setTimeout(() => {
                    this.textContent = originalText;
                }, 2000);
            });
        });
    });
});
```

### Search Patterns for dump.cs

**Guild War**:
```python
patterns = [
    r"class GuildWar.*Config",
    r"class GuildTier.*",
    r"class.*War.*Match.*",
    r"WarPoints",
    r"GuildTier\s*{",
]
```

**Dungeons**:
```python
patterns = [
    r"class Dungeon.*Config",
    r"DifficultyMultiplier",
    r"DungeonLevel",
    r"class.*Dungeon.*Reward",
]
```

**PvP**:
```python
patterns = [
    r"class Pvp.*Config",
    r"class.*League.*Config",
    r"PromotionEnd",
    r"DemotionStart",
    r"PvpMatchmaking",
]
```

**Shop**:
```python
patterns = [
    r"class ShopRefreshConfig",
    r"class PlayerShopModel",
    r"class ShopItem.*",
    r"ShopSeed",
]
```

**RNG/Drops**:
```python
patterns = [
    r"class.*DropChance.*Config",
    r"class.*Summon.*Config",
    r"RandomSeed",
    r"DungeonDrop",
]
```

### HTML Template Structure

Each mechanic section should follow this structure:

```html
<div class="mechanic-card">
    <h3>Mechanic Name</h3>
    
    <!-- Confidence indicator -->
    <div class="confidence-badge confidence-{level}">
        <span>Confidence: {level}</span>
        <span class="confidence-reason">{reason}</span>
    </div>
    
    <!-- Main content -->
    <p>{description}</p>
    
    <!-- Formula if applicable -->
    <div class="formula-box">
        <code>{formula}</code>
        <div class="code-ref">
            Source: <a href="#{line_number}">dump.cs line {line_number}</a>
        </div>
    </div>
    
    <!-- Examples -->
    <table class="comparison-table">
        <!-- example rows -->
    </table>
    
    <!-- Missing data warning if applicable -->
    <div class="warning">
        ⚠️ <strong>Missing:</strong> {missing_data_description}
    </div>
</div>
```

### CSS for Confidence Indicators

```css
.confidence-badge {
    display: inline-block;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.85em;
    margin-bottom: 8px;
}

.confidence-high {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.confidence-medium {
    background-color: #fff3cd;
    color: #856404;
    border: 1px solid #ffeaa7;
}

.confidence-low {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.confidence-unverified {
    background-color: #e2e3e5;
    color: #383d41;
    border: 1px solid #d6d8db;
}

.confidence-reason {
    display: block;
    font-size: 0.9em;
    margin-top: 4px;
    font-style: italic;
}
```

### GitHub Pages Fix

Create `.nojekyll` file in docs folder:
```python
def fix_github_pages_rendering(docs_path: str):
    """Create .nojekyll to disable Jekyll processing"""
    nojekyll_path = os.path.join(docs_path, '.nojekyll')
    with open(nojekyll_path, 'w') as f:
        f.write('')  # Empty file
    print(f"Created {nojekyll_path}")
```

This tells GitHub Pages to serve files as-is without Jekyll processing, which can cause HTML to display as raw code.

## Dependencies

- **Python 3.7+**: For extraction scripts
- **BeautifulSoup4**: For HTML parsing and updating
- **Hypothesis**: For property-based testing
- **pytest**: For unit testing
- **Access to dump.cs**: At C:\apktool\il2cpp-output\dump.cs

## Success Criteria

1. All five mechanic areas have documentation sections
2. Every documented mechanic has code references or is marked unverified
3. Confidence levels are assigned and explained
4. HTML files render correctly on GitHub Pages
5. Existing styling and navigation preserved
6. All property tests pass (100 iterations each)
7. Unit test coverage >85%
8. Manual verification confirms accuracy
