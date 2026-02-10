# Design Document: Game Mechanics Extraction System

## Overview

This system provides a comprehensive, autonomous solution for extracting and documenting all game mechanics from a decompiled mobile game. It cross-references IL2CPP metadata (class/method names with RVA addresses) with Ghidra-decompiled ARM code (implementation without names) to produce complete, accurate documentation.

The system is designed for minimal human intervention - users can start the extraction process and walk away, returning to find complete documentation with confidence levels indicating verification status.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Extraction Pipeline                          │
│                                                                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   IL2CPP     │───►│   Address    │───►│   Function   │      │
│  │   Parser     │    │   Mapper     │    │  Extractor   │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│         │                    │                    │              │
│         │                    │                    ▼              │
│         │                    │            ┌──────────────┐      │
│         │                    │            │   Pattern    │      │
│         │                    │            │   Finder     │      │
│         │                    │            └──────────────┘      │
│         │                    │                    │              │
│         ▼                    ▼                    ▼              │
│  ┌──────────────────────────────────────────────────────┐      │
│  │           Mechanics Analyzer                          │      │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │      │
│  │  │ Combat   │ │Summoning │ │   PvP    │ │  Prog.  │ │      │
│  │  │ Analyzer │ │ Analyzer │ │ Analyzer │ │Analyzer │ │      │
│  │  └──────────┘ └──────────┘ └──────────┘ └─────────┘ │      │
│  └──────────────────────────────────────────────────────┘      │
│         │                    │                    │              │
│         └────────────────────┴────────────────────┘              │
│                              │                                   │
│                              ▼                                   │
│                    ┌──────────────────┐                         │
│                    │   Verification   │                         │
│                    │     Engine       │                         │
│                    └──────────────────┘                         │
│                              │                                   │
│                              ▼                                   │
│                    ┌──────────────────┐                         │
│                    │  Documentation   │                         │
│                    │   Generator      │                         │
│                    └──────────────────┘                         │
│                              │                                   │
│                              ▼                                   │
│                    COMPLETE_GAME_MECHANICS_MANUAL.md            │
└─────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

1. **IL2CPP Parser**: Extracts class/method names and RVA addresses from IL2CPP dump
2. **Address Mapper**: Converts RVA addresses to Ghidra function names (FUN_XXXXXXXX)
3. **Function Extractor**: Locates and extracts complete function implementations from Ghidra
4. **Pattern Finder**: Searches for specific code patterns (RNG, divisions, comparisons, etc.)
5. **Mechanics Analyzers**: Specialized analyzers for each game system
6. **Verification Engine**: Validates extracted mechanics and assigns confidence levels
7. **Documentation Generator**: Produces comprehensive markdown documentation

## Components and Interfaces

### 1. IL2CPP Parser

**Purpose**: Extract structured metadata from IL2CPP dump

**Input**: IL2CPP dump file (dump.cs)

**Output**: Structured data containing:
- Class definitions with methods
- RVA addresses for each method
- Data structures (fields, properties)
- Type information

**Interface**:
```python
class IL2CPPParser:
    def __init__(self, dump_file_path: str):
        self.dump_file = dump_file_path
        self.classes = {}
        self.methods = {}
        self.addresses = {}
    
    def parse(self) -> Dict[str, ClassInfo]:
        """Parse IL2CPP dump and extract all metadata"""
        pass
    
    def get_methods_with_addresses(self) -> Dict[str, str]:
        """Return mapping of method_name -> RVA_address"""
        pass
    
    def get_class_structure(self, class_name: str) -> ClassInfo:
        """Get complete structure for a specific class"""
        pass
    
    def find_methods_by_pattern(self, pattern: str) -> List[MethodInfo]:
        """Find methods matching a name pattern"""
        pass
```

**Data Structures**:
```python
@dataclass
class MethodInfo:
    name: str
    class_name: str
    rva_address: str  # e.g., "0x5AF7094"
    return_type: str
    parameters: List[Parameter]
    attributes: List[str]  # MetaMember annotations

@dataclass
class ClassInfo:
    name: str
    base_class: str
    methods: List[MethodInfo]
    fields: List[FieldInfo]
    properties: List[PropertyInfo]

@dataclass
class FieldInfo:
    name: str
    type: str
    offset: int  # From MetaMember attribute
```

### 2. Address Mapper

**Purpose**: Map IL2CPP RVA addresses to Ghidra function names

**Input**: 
- RVA addresses from IL2CPP
- Ghidra export file

**Output**: Bidirectional mapping between IL2CPP names and Ghidra functions

**Interface**:
```python
class AddressMapper:
    def __init__(self, il2cpp_parser: IL2CPPParser, ghidra_file: str):
        self.il2cpp = il2cpp_parser
        self.ghidra_file = ghidra_file
        self.address_map = {}  # RVA -> Ghidra function name
        self.reverse_map = {}  # Ghidra function name -> IL2CPP method
    
    def build_mapping(self) -> Dict[str, str]:
        """Build complete address mapping"""
        pass
    
    def rva_to_ghidra_name(self, rva: str) -> str:
        """Convert RVA address to Ghidra function name
        Example: 0x5AF7094 -> FUN_05af7094
        """
        pass
    
    def get_il2cpp_name(self, ghidra_func: str) -> Optional[str]:
        """Get IL2CPP method name for Ghidra function"""
        pass
    
    def save_mapping(self, output_file: str):
        """Save mapping to file for reuse"""
        pass
    
    def load_mapping(self, input_file: str):
        """Load previously saved mapping"""
        pass
```

**Address Conversion Logic**:
```python
def rva_to_ghidra_name(rva: str) -> str:
    # Remove 0x prefix
    hex_addr = rva.replace('0x', '').lower()
    
    # Pad to 8 characters
    hex_addr = hex_addr.zfill(8)
    
    # Format as Ghidra function name
    return f"FUN_{hex_addr}"

# Example: 0x5AF7094 -> FUN_05af7094
```

### 3. Function Extractor

**Purpose**: Extract complete function implementations from Ghidra export

**Input**:
- Ghidra function name
- Ghidra export file

**Output**: Complete function code with context

**Interface**:
```python
class FunctionExtractor:
    def __init__(self, ghidra_file: str):
        self.ghidra_file = ghidra_file
        self.function_cache = {}  # Cache extracted functions
    
    def extract_function(self, func_name: str) -> Optional[FunctionCode]:
        """Extract complete function implementation"""
        pass
    
    def extract_with_context(self, func_name: str, 
                            context_lines: int = 10) -> FunctionCode:
        """Extract function with surrounding context"""
        pass
    
    def extract_constants(self, func_code: str) -> Constants:
        """Extract numeric constants from function"""
        pass
    
    def analyze_patterns(self, func_code: str) -> PatternAnalysis:
        """Identify code patterns in function"""
        pass
```

**Data Structures**:
```python
@dataclass
class FunctionCode:
    name: str
    line_number: int
    code: str
    signature: str
    constants: Constants
    patterns: PatternAnalysis

@dataclass
class Constants:
    integers: List[int]
    floats: List[float]
    hex_values: List[str]
    large_numbers: List[int]  # Potential seeds/multipliers

@dataclass
class PatternAnalysis:
    has_division: bool
    has_multiplication: bool
    has_modulo: bool
    has_random: bool
    has_comparison_chain: bool
    has_bit_shift: bool
    has_array_access: bool
    has_loop: bool
    has_float_ops: bool
    has_large_constants: bool
```

### 4. Pattern Finder

**Purpose**: Search for specific code patterns in Ghidra export

**Input**:
- Search patterns (regex, keywords)
- Ghidra export file

**Output**: Matches with context

**Interface**:
```python
class PatternFinder:
    def __init__(self, ghidra_file: str):
        self.ghidra_file = ghidra_file
    
    def find_pcg_algorithm(self) -> List[Match]:
        """Find PCG RNG implementation"""
        pass
    
    def find_drop_tables(self) -> List[Match]:
        """Find drop chance tables (arrays of floats)"""
        pass
    
    def find_division_operations(self) -> List[Match]:
        """Find division operations (stat calculations)"""
        pass
    
    def find_comparison_chains(self) -> List[Match]:
        """Find chains of if statements (rarity determination)"""
        pass
    
    def find_custom_pattern(self, regex: str, 
                           context_lines: int = 10) -> List[Match]:
        """Search for custom regex pattern"""
        pass
    
    def find_constants(self, min_value: int = 1000) -> List[Match]:
        """Find large numeric constants"""
        pass
```

**Pattern Definitions**:
```python
PATTERNS = {
    'pcg_multiplier': r'6364136223846793005|0x5851f42d4c957f2d',
    'pcg_increment': r'1442695040888963407|0x14057b7ef767814f',
    'pcg_shifts': r'>>\s*18.*\^.*>>\s*27|>>\s*59',
    'drop_table': r'float.*\[\s*[567]\s*\]',
    'division': r'[a-zA-Z_][a-zA-Z0-9_]*\s*/\s*[a-zA-Z_][a-zA-Z0-9_]*',
    'comparison_chain': r'(if\s*\([^)]+\)\s*{[^}]*}){4,}',
}
```

### 5. Combat Analyzer

**Purpose**: Extract all combat-related mechanics

**Input**:
- IL2CPP combat classes
- Ghidra combat functions
- Pattern matches

**Output**: Complete combat mechanics documentation

**Interface**:
```python
class CombatAnalyzer:
    def __init__(self, il2cpp: IL2CPPParser, 
                 mapper: AddressMapper,
                 extractor: FunctionExtractor):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
    
    def analyze_attack_speed(self) -> AttackSpeedMechanics:
        """Extract attack speed formula and base times"""
        pass
    
    def analyze_damage_calculation(self) -> DamageMechanics:
        """Extract damage formula with all modifiers"""
        pass
    
    def analyze_combat_stats(self) -> Dict[str, StatMechanics]:
        """Extract formulas for all combat stats"""
        pass
    
    def analyze_status_effects(self) -> List[StatusEffect]:
        """Extract status effect mechanics"""
        pass
    
    def generate_documentation(self) -> str:
        """Generate markdown documentation for combat system"""
        pass
```

**Data Structures**:
```python
@dataclass
class AttackSpeedMechanics:
    formula: str  # "effective_time = base_time / attack_speed_multi"
    base_times: Dict[str, float]  # weapon_type -> base_time
    sources: List[str]  # Where attack speed bonuses come from
    arm_code_location: str  # Line number in Ghidra
    confidence: ConfidenceLevel

@dataclass
class DamageMechanics:
    base_formula: str
    crit_formula: str
    modifiers: List[DamageModifier]
    proc_checks: List[ProcCheck]
    arm_code_location: str
    confidence: ConfidenceLevel

@dataclass
class StatMechanics:
    stat_name: str
    formula: str
    base_value: float
    scaling: str
    sources: List[str]
    caps: Optional[Tuple[float, float]]  # (min, max)
    confidence: ConfidenceLevel
```

### 6. Summoning Analyzer

**Purpose**: Extract summoning system mechanics

**Input**:
- IL2CPP summoning classes
- Ghidra RNG and drop table functions
- Pattern matches

**Output**: Complete summoning mechanics documentation

**Interface**:
```python
class SummoningAnalyzer:
    def __init__(self, il2cpp: IL2CPPParser,
                 mapper: AddressMapper,
                 extractor: FunctionExtractor,
                 pattern_finder: PatternFinder):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
        self.patterns = pattern_finder
    
    def analyze_rng_algorithm(self) -> RNGMechanics:
        """Identify and extract RNG algorithm"""
        pass
    
    def analyze_drop_tables(self) -> Dict[int, DropTable]:
        """Extract drop chance tables for all levels"""
        pass
    
    def analyze_rarity_determination(self) -> RarityAlgorithm:
        """Extract rarity determination logic"""
        pass
    
    def analyze_summon_progression(self) -> ProgressionTable:
        """Extract summon level thresholds"""
        pass
    
    def analyze_pity_system(self) -> Optional[PityMechanics]:
        """Extract pity system if present"""
        pass
    
    def generate_documentation(self) -> str:
        """Generate markdown documentation for summoning"""
        pass
```

**Data Structures**:
```python
@dataclass
class RNGMechanics:
    algorithm_type: str  # "PCG", "Mersenne Twister", "LCG", etc.
    seed_storage: Dict[str, str]  # system -> storage_location
    state_update_formula: str
    output_generation_formula: str
    arm_code_location: str
    confidence: ConfidenceLevel

@dataclass
class DropTable:
    level: int
    rarities: Dict[str, float]  # rarity_name -> percentage
    total_percentage: float  # Should be 100.0
    arm_code_location: str
    confidence: ConfidenceLevel

@dataclass
class RarityAlgorithm:
    algorithm: str  # Description of how random value maps to rarity
    pseudocode: str
    arm_code_location: str
    confidence: ConfidenceLevel
```

### 7. PvP Analyzer

**Purpose**: Extract PvP system mechanics

**Interface**:
```python
class PvPAnalyzer:
    def __init__(self, il2cpp: IL2CPPParser,
                 mapper: AddressMapper,
                 extractor: FunctionExtractor):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
    
    def analyze_matchmaking(self) -> MatchmakingMechanics:
        """Extract matchmaking algorithm"""
        pass
    
    def analyze_scoring(self) -> ScoringMechanics:
        """Extract PvP scoring system"""
        pass
    
    def analyze_stat_modifiers(self) -> Dict[str, float]:
        """Extract PvP stat multipliers"""
        pass
    
    def analyze_guild_war(self) -> GuildWarMechanics:
        """Extract guild war mechanics"""
        pass
    
    def generate_documentation(self) -> str:
        """Generate markdown documentation for PvP"""
        pass
```

### 8. Progression Analyzer

**Purpose**: Extract progression system mechanics

**Interface**:
```python
class ProgressionAnalyzer:
    def __init__(self, il2cpp: IL2CPPParser,
                 mapper: AddressMapper,
                 extractor: FunctionExtractor):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
    
    def analyze_tech_tree(self) -> TechTreeMechanics:
        """Extract tech tree mechanics"""
        pass
    
    def analyze_forge_system(self) -> ForgeMechanics:
        """Extract forge/crafting mechanics"""
        pass
    
    def analyze_pet_leveling(self) -> LevelingMechanics:
        """Extract pet leveling formulas"""
        pass
    
    def analyze_mount_leveling(self) -> LevelingMechanics:
        """Extract mount leveling formulas"""
        pass
    
    def analyze_skill_system(self) -> SkillMechanics:
        """Extract skill system mechanics"""
        pass
    
    def generate_documentation(self) -> str:
        """Generate markdown documentation for progression"""
        pass
```

### 9. Economy Analyzer

**Purpose**: Extract economy system mechanics

**Interface**:
```python
class EconomyAnalyzer:
    def __init__(self, il2cpp: IL2CPPParser,
                 mapper: AddressMapper,
                 extractor: FunctionExtractor):
        self.il2cpp = il2cpp
        self.mapper = mapper
        self.extractor = extractor
    
    def analyze_resource_generation(self) -> Dict[str, ResourceGeneration]:
        """Extract resource generation rates"""
        pass
    
    def analyze_shop_pricing(self) -> PricingMechanics:
        """Extract shop pricing algorithms"""
        pass
    
    def analyze_currency_conversion(self) -> Dict[Tuple[str, str], float]:
        """Extract currency exchange rates"""
        pass
    
    def generate_documentation(self) -> str:
        """Generate markdown documentation for economy"""
        pass
```

### 10. Verification Engine

**Purpose**: Validate extracted mechanics and assign confidence levels

**Input**: Extracted mechanics from all analyzers

**Output**: Verified mechanics with confidence levels

**Interface**:
```python
class VerificationEngine:
    def __init__(self):
        self.verification_rules = []
    
    def verify_formula(self, formula: str, 
                      test_cases: List[TestCase]) -> VerificationResult:
        """Verify formula produces expected outputs"""
        pass
    
    def verify_drop_table(self, drop_table: DropTable) -> VerificationResult:
        """Verify drop table percentages sum correctly"""
        pass
    
    def verify_cross_reference(self, il2cpp_data: Any,
                               arm_data: Any) -> VerificationResult:
        """Verify IL2CPP and ARM data match"""
        pass
    
    def assign_confidence(self, mechanic: Any,
                         verification: VerificationResult) -> ConfidenceLevel:
        """Assign confidence level based on verification"""
        pass
```

**Confidence Levels**:
```python
class ConfidenceLevel(Enum):
    HIGH = "High"      # ARM code found and verified
    MEDIUM = "Medium"  # IL2CPP structure found, ARM not verified
    LOW = "Low"        # Inferred from patterns only
    UNKNOWN = "Unknown"  # Not yet analyzed

@dataclass
class VerificationResult:
    passed: bool
    details: str
    evidence: List[str]  # Code locations, test results, etc.
```

### 11. Documentation Generator

**Purpose**: Generate comprehensive markdown documentation

**Input**: Verified mechanics from all analyzers

**Output**: Complete game mechanics manual

**Interface**:
```python
class DocumentationGenerator:
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.sections = []
    
    def add_section(self, title: str, content: str, 
                   confidence: ConfidenceLevel):
        """Add a section to the documentation"""
        pass
    
    def generate_table_of_contents(self) -> str:
        """Generate TOC with links"""
        pass
    
    def generate_status_section(self) -> str:
        """Generate extraction progress status"""
        pass
    
    def format_formula(self, formula: str, examples: List[Example]) -> str:
        """Format formula with examples"""
        pass
    
    def format_code_evidence(self, code: str, location: str) -> str:
        """Format ARM code evidence"""
        pass
    
    def generate_optimization_strategies(self, 
                                        mechanics: Dict[str, Any]) -> str:
        """Generate optimization strategies based on mechanics"""
        pass
    
    def write_documentation(self):
        """Write complete documentation to file"""
        pass
    
    def update_section(self, section_name: str, new_content: str):
        """Update existing section incrementally"""
        pass
```

## Data Models

### Core Data Models

```python
@dataclass
class GameMechanic:
    """Base class for all game mechanics"""
    name: str
    category: str  # Combat, Summoning, PvP, Progression, Economy
    description: str
    formula: Optional[str]
    data_structures: List[str]  # IL2CPP class/struct names
    arm_code_location: Optional[str]
    confidence: ConfidenceLevel
    examples: List[Example]
    notes: List[str]

@dataclass
class Example:
    """Example demonstrating a mechanic"""
    description: str
    inputs: Dict[str, Any]
    expected_output: Any
    actual_output: Optional[Any]

@dataclass
class TestCase:
    """Test case for verification"""
    inputs: Dict[str, Any]
    expected_output: Any
    tolerance: float = 0.001  # For float comparisons
```

### Configuration Models

```python
@dataclass
class ExtractionConfig:
    """Configuration for extraction pipeline"""
    il2cpp_dump_path: str
    ghidra_export_path: str
    output_manual_path: str
    config_file_path: Optional[str]
    
    # Processing options
    use_cache: bool = True
    parallel_processing: bool = True
    max_workers: int = 4
    
    # Pattern search options
    context_lines: int = 10
    max_matches_per_pattern: int = 100
    
    # Verification options
    run_verification: bool = True
    verification_strictness: str = "medium"  # low, medium, high
    
    # Output options
    include_code_evidence: bool = True
    include_optimization_strategies: bool = True
    generate_json_export: bool = True
    generate_csv_export: bool = True
    
    # Priority systems (extract these first)
    priority_systems: List[str] = field(default_factory=lambda: [
        "Combat", "Summoning", "PvP", "Progression", "Economy"
    ])
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*


### Property 1: Address Mapping Round Trip
*For any* IL2CPP method with an RVA address, mapping to Ghidra function name and back should preserve the original IL2CPP method name.
**Validates: Requirements 1.1, 1.2, 1.5**

### Property 2: Function Extraction Completeness
*For any* Ghidra function that exists in the file, the extractor should locate and extract its complete implementation including all code between opening and closing braces.
**Validates: Requirements 1.3**

### Property 3: Error Resilience
*For any* error condition (missing file, missing function, parse failure), the system should log the error and continue processing remaining items without crashing.
**Validates: Requirements 1.4, 12.2, 17.1, 17.2**

### Property 4: Mapping Persistence Round Trip
*For any* address mapping, saving to file then loading should produce an equivalent mapping.
**Validates: Requirements 1.6**

### Property 5: Pattern Detection Completeness
*For any* code file containing a specific pattern (division, comparison chain, bit operation, array access), the pattern finder should identify all occurrences of that pattern.
**Validates: Requirements 2.1, 2.2, 9.1, 9.2, 9.3, 9.4**

### Property 6: Extraction Completeness
*For any* game system category (combat stats, summonable types, resource costs), all items in that category should be extracted and documented.
**Validates: Requirements 2.3, 2.4, 2.5, 4.5, 6.6, 7.4**

### Property 7: Cross-Reference Validation
*For any* mechanic extracted from IL2CPP, there should be a corresponding ARM code location identified, or the mechanic should be flagged as unverified.
**Validates: Requirements 2.6, 13.1, 13.2**

### Property 8: Confidence Level Assignment
*For any* extracted mechanic, the confidence level should be High if ARM code is verified, Medium if only IL2CPP structure exists, and Low if inferred from patterns only.
**Validates: Requirements 2.7, 10.4, 10.5, 10.6**

### Property 9: RNG Algorithm Extraction
*For any* RNG algorithm found in code, the system should extract all three components: seed initialization, state update, and output generation logic.
**Validates: Requirements 3.2, 3.3, 3.4**

### Property 10: RNG Algorithm Detection
*For any* code file, the system should identify which RNG algorithm type is present (PCG, Mersenne Twister, LCG, Xorshift, or custom).
**Validates: Requirements 3.1, 3.7**

### Property 11: RNG Usage Tracking
*For any* RNG function, all call sites where random numbers are consumed should be identified and documented.
**Validates: Requirements 3.5**

### Property 12: Seed Storage Documentation
*For any* game system using RNG, the seed storage mechanism (location, scope, persistence) should be documented.
**Validates: Requirements 3.6**

### Property 13: Drop Table Validation
*For any* extracted drop table, the sum of all rarity percentages should equal 100% (within a tolerance of 0.1%), or a pity system should be identified.
**Validates: Requirements 4.6, 10.2**

### Property 14: Drop Table Extraction
*For any* summon level, the system should extract the complete drop table with all rarity tiers and their percentages.
**Validates: Requirements 4.1, 4.2**

### Property 15: Rarity Algorithm Extraction
*For any* summoning system, the algorithm that converts random values to rarity outcomes should be extracted and documented.
**Validates: Requirements 4.3**

### Property 16: Progression Threshold Extraction
*For any* progression system (summon levels, tech tree, leveling), all thresholds and requirements should be extracted.
**Validates: Requirements 4.4, 6.1**

### Property 17: Pity System Detection
*For any* summoning system, if a pity mechanism exists (guaranteed drops after X attempts), it should be identified and documented.
**Validates: Requirements 4.7**

### Property 18: PvP Mechanics Extraction
*For any* PvP system component (matchmaking, scoring, stat modifiers), the algorithm or formula should be extracted and documented.
**Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5, 5.6**

### Property 19: Progression Mechanics Extraction
*For any* progression system (tech tree, forge, pet/mount leveling, skills), all parameters (costs, rates, formulas, caps) should be extracted.
**Validates: Requirements 6.1, 6.2, 6.3, 6.4, 6.5**

### Property 20: Economy Mechanics Extraction
*For any* economy system (resource generation, shop pricing, currency conversion), all rates and formulas should be extracted.
**Validates: Requirements 7.1, 7.2, 7.3, 7.5**

### Property 21: Configuration Parsing Round Trip
*For any* binary configuration file, parsing then serializing should produce equivalent data (within floating-point tolerance).
**Validates: Requirements 8.1**

### Property 22: Data Type Preservation
*For any* numeric constant extracted from configuration or code, its data type (int, float, double) should be correctly identified and preserved.
**Validates: Requirements 8.2**

### Property 23: Array Extraction Invariant
*For any* array extracted from configuration or code, the element count and order should be preserved exactly.
**Validates: Requirements 8.3**

### Property 24: Configuration Extraction
*For any* configuration value (drop table percentage, base attack time, stat coefficient), it should be extracted from config files if present, otherwise from ARM code.
**Validates: Requirements 8.4, 8.5, 8.6, 8.7**

### Property 25: Pattern Search Customization
*For any* custom regex pattern provided by the user, the pattern finder should search for and return matches with the specified context lines.
**Validates: Requirements 9.5, 9.7**

### Property 26: Result Limiting
*For any* pattern search, the number of results should not exceed the configured maximum to prevent overwhelming output.
**Validates: Requirements 9.6**

### Property 27: Formula Verification
*For any* extracted formula with test cases, applying the formula to test inputs should produce outputs matching expected values (within tolerance).
**Validates: Requirements 10.1, 10.3**

### Property 28: Contradiction Detection
*For any* mechanic with both IL2CPP and ARM data, contradictions between the two sources should be flagged for review.
**Validates: Requirements 10.7, 13.3**

### Property 29: Documentation Structure
*For any* generated mechanics manual, it should contain a table of contents, status section, and sections organized by game system category.
**Validates: Requirements 11.1, 11.4, 11.5**

### Property 30: Documentation Completeness
*For any* documented mechanic, the documentation should include formula, data structures, ARM code evidence, confidence level, examples, and source code references.
**Validates: Requirements 11.2, 11.3, 11.6**

### Property 31: Incremental Documentation Updates
*For any* documentation update, existing content should be preserved and only the updated section should be modified.
**Validates: Requirements 11.7, 14.1**

### Property 32: Autonomous Execution
*For any* extraction run, the system should process all configured game systems from start to finish without requiring user input.
**Validates: Requirements 12.1**

### Property 33: Extraction Summary Generation
*For any* completed extraction run, a summary report should be generated listing all extracted mechanics and their confidence levels.
**Validates: Requirements 12.3**

### Property 34: Checkpoint Persistence
*For any* extraction checkpoint, saving then resuming should continue processing from the correct state without repeating completed work.
**Validates: Requirements 12.4, 12.5, 18.5**

### Property 35: Progress Indication
*For any* extraction run, progress indicators (percentage complete, time remaining) should be displayed and updated regularly.
**Validates: Requirements 12.6, 18.6**

### Property 36: Priority Ordering
*For any* extraction run, high-priority game systems (combat, summoning) should be processed before low-priority systems.
**Validates: Requirements 12.7**

### Property 37: Constant Comparison
*For any* mechanic with constants in both IL2CPP and ARM code, the constants should be extracted from both sources and compared for consistency.
**Validates: Requirements 13.4**

### Property 38: Call Graph Verification
*For any* function with calls to other functions, the call graph should match between IL2CPP metadata and ARM implementation.
**Validates: Requirements 13.5**

### Property 39: Pattern-Triggered Re-scanning
*For any* newly discovered pattern, previously processed code should be re-scanned to find instances of the new pattern.
**Validates: Requirements 14.2**

### Property 40: Manual Override Persistence
*For any* mechanic with a manual override, the override should be preserved across extraction runs and take precedence over automated extraction.
**Validates: Requirements 14.3**

### Property 41: Verification Status Tracking
*For any* mechanic, the system should track whether it has been manually verified by the user and display this status.
**Validates: Requirements 14.4**

### Property 42: Selective Extraction
*For any* single game system, it should be possible to extract only that system without re-processing other systems.
**Validates: Requirements 14.5**

### Property 43: Optimization Strategy Generation
*For any* extracted game system (combat, summoning, progression), optimization strategies should be generated based on the mechanics.
**Validates: Requirements 15.1, 15.2, 15.3, 15.5**

### Property 44: Exploit Detection
*For any* extracted mechanic, unusual patterns or unintended behaviors should be flagged as potential exploits.
**Validates: Requirements 15.4**

### Property 45: Multi-Format Support
*For any* IL2CPP dump from Unity or Ghidra export from ARM/x86/x64, the system should correctly parse the format.
**Validates: Requirements 16.1, 16.2, 16.3**

### Property 46: Format Inference
*For any* decompiler output with unknown format, the system should attempt to infer the format and parse accordingly, or fail gracefully.
**Validates: Requirements 16.4**

### Property 47: Chunked Processing
*For any* file exceeding memory limits, the system should process it in chunks without loading the entire file into memory.
**Validates: Requirements 17.3**

### Property 48: Data Validation
*For any* extracted data, it should be validated before being written to documentation, and invalid data should be rejected with an error message.
**Validates: Requirements 17.4**

### Property 49: Detailed Error Messages
*For any* error, the error message should include context (file name, line number, operation being performed) to aid debugging.
**Validates: Requirements 17.5**

### Property 50: Memory-Mapped File Access
*For any* file larger than a threshold (e.g., 100MB), memory-mapped file access should be used instead of loading the entire file.
**Validates: Requirements 18.1**

### Property 51: IL2CPP Caching
*For any* IL2CPP dump, after initial parsing, the parsed data should be cached and reused for subsequent operations.
**Validates: Requirements 18.3**

### Property 52: Parallel Processing
*For any* set of independent game systems, they should be processed in parallel using multiple workers.
**Validates: Requirements 18.4**

### Property 53: Export Format Validity
*For any* exported data (JSON, CSV, simulation format, calculator format), the output should be valid according to the format specification.
**Validates: Requirements 19.1, 19.2, 19.3, 19.4**

### Property 54: API Data Access
*For any* extracted mechanic, it should be accessible via the programmatic API with correct data types and values.
**Validates: Requirements 19.5**

### Property 55: Visualization Generation
*For any* extracted data suitable for visualization (drop tables, stat scaling, tech trees, stat comparisons), appropriate charts or graphs should be generated.
**Validates: Requirements 20.1, 20.2, 20.3, 20.4, 20.5**

## Error Handling

### Error Categories

1. **File Access Errors**
   - Missing files
   - Permission denied
   - Corrupted files
   - **Handling**: Log error, skip file, continue processing

2. **Parse Errors**
   - Invalid syntax
   - Unexpected format
   - Incomplete data
   - **Handling**: Log error, skip item, continue processing

3. **Memory Errors**
   - Out of memory
   - File too large
   - **Handling**: Switch to chunked processing, reduce cache size

4. **Validation Errors**
   - Invalid data
   - Contradictions
   - Missing required fields
   - **Handling**: Flag for review, assign low confidence, continue

5. **Configuration Errors**
   - Invalid config file
   - Missing required settings
   - **Handling**: Use defaults, log warning, continue

### Error Recovery Strategies

```python
class ErrorRecovery:
    @staticmethod
    def handle_file_error(error: FileError, context: Context) -> RecoveryAction:
        """Determine recovery action for file errors"""
        if error.type == FileErrorType.NOT_FOUND:
            return RecoveryAction.SKIP_FILE
        elif error.type == FileErrorType.PERMISSION_DENIED:
            return RecoveryAction.SKIP_FILE
        elif error.type == FileErrorType.CORRUPTED:
            return RecoveryAction.TRY_PARTIAL_READ
        else:
            return RecoveryAction.ABORT
    
    @staticmethod
    def handle_parse_error(error: ParseError, context: Context) -> RecoveryAction:
        """Determine recovery action for parse errors"""
        if error.severity == Severity.LOW:
            return RecoveryAction.USE_PARTIAL_DATA
        elif error.severity == Severity.MEDIUM:
            return RecoveryAction.SKIP_ITEM
        else:
            return RecoveryAction.SKIP_FILE
    
    @staticmethod
    def handle_memory_error(error: MemoryError, context: Context) -> RecoveryAction:
        """Determine recovery action for memory errors"""
        return RecoveryAction.SWITCH_TO_CHUNKED_PROCESSING
```

## Testing Strategy

### Dual Testing Approach

The system requires both unit tests and property-based tests for comprehensive coverage:

**Unit Tests**: Verify specific examples, edge cases, and error conditions
- Test address conversion with known examples
- Test pattern matching with specific code snippets
- Test error handling with simulated failures
- Test configuration parsing with sample files

**Property Tests**: Verify universal properties across all inputs
- Test round-trip properties (mapping, serialization)
- Test completeness properties (all items extracted)
- Test invariant properties (order preserved, percentages sum to 100%)
- Test error resilience (system doesn't crash)

### Property-Based Testing Configuration

- **Library**: Use `hypothesis` for Python (or equivalent for other languages)
- **Iterations**: Minimum 100 iterations per property test
- **Test Tags**: Each property test must reference its design document property
- **Tag Format**: `# Feature: game-mechanics-extraction, Property N: [property text]`

### Unit Testing Balance

- Focus unit tests on:
  - Specific examples demonstrating correct behavior
  - Integration points between components
  - Edge cases (empty files, malformed data, boundary values)
  - Error conditions (missing files, parse failures)

- Avoid writing too many unit tests for cases covered by property tests
- Property tests handle comprehensive input coverage through randomization

### Test Organization

```
tests/
├── unit/
│   ├── test_il2cpp_parser.py
│   ├── test_address_mapper.py
│   ├── test_function_extractor.py
│   ├── test_pattern_finder.py
│   ├── test_combat_analyzer.py
│   ├── test_summoning_analyzer.py
│   ├── test_pvp_analyzer.py
│   ├── test_progression_analyzer.py
│   ├── test_economy_analyzer.py
│   ├── test_verification_engine.py
│   └── test_documentation_generator.py
├── property/
│   ├── test_properties_address_mapping.py
│   ├── test_properties_extraction.py
│   ├── test_properties_verification.py
│   ├── test_properties_documentation.py
│   └── test_properties_error_handling.py
├── integration/
│   ├── test_full_pipeline.py
│   ├── test_combat_extraction_e2e.py
│   └── test_summoning_extraction_e2e.py
└── fixtures/
    ├── sample_il2cpp_dump.cs
    ├── sample_ghidra_export.c
    ├── sample_config.mpa
    └── expected_outputs/
```

### Example Property Test

```python
from hypothesis import given, strategies as st
import pytest

# Feature: game-mechanics-extraction, Property 1: Address Mapping Round Trip
@given(st.text(min_size=8, max_size=8, alphabet='0123456789abcdef'))
def test_address_mapping_round_trip(hex_address):
    """For any RVA address, mapping to Ghidra and back preserves the address"""
    rva = f"0x{hex_address}"
    il2cpp_name = f"TestClass.TestMethod"
    
    mapper = AddressMapper(mock_il2cpp_parser, mock_ghidra_file)
    
    # Map IL2CPP -> Ghidra
    ghidra_name = mapper.rva_to_ghidra_name(rva)
    
    # Store mapping
    mapper.address_map[rva] = il2cpp_name
    mapper.reverse_map[ghidra_name] = il2cpp_name
    
    # Map Ghidra -> IL2CPP
    recovered_name = mapper.get_il2cpp_name(ghidra_name)
    
    # Should recover original name
    assert recovered_name == il2cpp_name

# Feature: game-mechanics-extraction, Property 13: Drop Table Validation
@given(st.lists(st.floats(min_value=0.0, max_value=100.0), min_size=5, max_size=7))
def test_drop_table_percentages_sum_to_100(percentages):
    """For any drop table, percentages should sum to 100% (within tolerance)"""
    # Normalize to sum to 100
    total = sum(percentages)
    if total > 0:
        normalized = [p / total * 100.0 for p in percentages]
    else:
        normalized = [100.0 / len(percentages)] * len(percentages)
    
    drop_table = DropTable(
        level=1,
        rarities={f"rarity_{i}": p for i, p in enumerate(normalized)}
    )
    
    verification = VerificationEngine().verify_drop_table(drop_table)
    
    assert verification.passed
    assert abs(sum(normalized) - 100.0) < 0.1  # Tolerance
```

### Example Unit Test

```python
def test_address_conversion_known_example():
    """Test address conversion with known example"""
    mapper = AddressMapper(mock_il2cpp_parser, mock_ghidra_file)
    
    # Known example from documentation
    rva = "0x5AF7094"
    expected_ghidra = "FUN_05af7094"
    
    actual_ghidra = mapper.rva_to_ghidra_name(rva)
    
    assert actual_ghidra == expected_ghidra

def test_pattern_finder_empty_file():
    """Test pattern finder handles empty file gracefully"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("")
        temp_file = f.name
    
    try:
        finder = PatternFinder(temp_file)
        matches = finder.find_division_operations()
        
        assert matches == []  # Should return empty list, not crash
    finally:
        os.unlink(temp_file)

def test_error_handling_missing_file():
    """Test system handles missing file gracefully"""
    extractor = FunctionExtractor("nonexistent_file.c")
    
    result = extractor.extract_function("FUN_12345678")
    
    assert result is None  # Should return None, not crash
    # Check that error was logged (would need to capture logs)
```

## Implementation Notes

### Performance Considerations

1. **Large File Handling**
   - Use memory-mapped files for files > 100MB
   - Process in chunks to avoid loading entire file
   - Use streaming parsers where possible

2. **Caching Strategy**
   - Cache parsed IL2CPP data (can be reused across runs)
   - Cache address mappings (expensive to compute)
   - Don't cache Ghidra function extractions (too much memory)

3. **Parallel Processing**
   - Process independent game systems in parallel
   - Use process pool (not thread pool) to avoid GIL
   - Limit workers to CPU count to avoid thrashing

4. **Regex Optimization**
   - Compile regex patterns once and reuse
   - Use non-capturing groups where possible
   - Limit backtracking with atomic groups

### Security Considerations

1. **File Access**
   - Validate all file paths to prevent directory traversal
   - Check file sizes before loading
   - Set timeouts for file operations

2. **Code Execution**
   - Never execute extracted code
   - Sanitize all strings before writing to documentation
   - Validate all user inputs

3. **Resource Limits**
   - Set maximum file size limits
   - Set maximum memory usage limits
   - Set maximum processing time limits

### Extensibility

The system is designed to be extensible:

1. **New Game Systems**: Add new analyzer classes inheriting from base analyzer
2. **New Patterns**: Add new pattern definitions to PatternFinder
3. **New Verification Rules**: Add new rules to VerificationEngine
4. **New Export Formats**: Add new exporters to DocumentationGenerator

### Dependencies

- **Python 3.9+**: Core language
- **regex**: Advanced regex features
- **hypothesis**: Property-based testing
- **pytest**: Unit testing framework
- **mmap**: Memory-mapped file access
- **multiprocessing**: Parallel processing
- **json**: JSON export
- **csv**: CSV export
- **matplotlib**: Visualization generation (optional)
- **networkx**: Graph generation for tech trees (optional)

## Deployment and Usage

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run extraction
python extract_mechanics.py --config config.yaml
```

### Configuration File

```yaml
# config.yaml
input:
  il2cpp_dump: "path/to/dump.cs"
  ghidra_export: "path/to/libil2cpp.so.c"
  config_file: "path/to/SharedGameConfig.mpa"  # optional

output:
  manual: "COMPLETE_GAME_MECHANICS_MANUAL.md"
  json_export: "mechanics.json"
  csv_export: "mechanics.csv"

processing:
  use_cache: true
  parallel: true
  max_workers: 4

patterns:
  context_lines: 10
  max_matches: 100

verification:
  enabled: true
  strictness: "medium"

systems:
  priority:
    - Combat
    - Summoning
    - PvP
    - Progression
    - Economy
```

### Command-Line Interface

```bash
# Full extraction
python extract_mechanics.py --config config.yaml

# Extract single system
python extract_mechanics.py --config config.yaml --system Combat

# Resume from checkpoint
python extract_mechanics.py --config config.yaml --resume

# Verify only (no extraction)
python extract_mechanics.py --config config.yaml --verify-only

# Generate visualizations
python extract_mechanics.py --config config.yaml --visualize
```

### Progress Monitoring

The system provides real-time progress updates:

```
[2024-02-10 14:30:00] Starting extraction pipeline
[2024-02-10 14:30:01] Parsing IL2CPP dump... (1.2M lines)
[2024-02-10 14:30:15] IL2CPP parsing complete (14s)
[2024-02-10 14:30:15] Building address mapping...
[2024-02-10 14:30:20] Address mapping complete (5s, 1,234 functions mapped)
[2024-02-10 14:30:20] Extracting Combat system... [Priority 1/5]
[2024-02-10 14:30:25] ├─ Attack speed mechanics... ✓ (High confidence)
[2024-02-10 14:30:30] ├─ Damage calculation... ✓ (High confidence)
[2024-02-10 14:30:35] ├─ Combat stats... ✓ (Medium confidence)
[2024-02-10 14:30:40] └─ Status effects... ✓ (Medium confidence)
[2024-02-10 14:30:40] Combat system complete (20s)
[2024-02-10 14:30:40] Extracting Summoning system... [Priority 2/5]
[2024-02-10 14:30:45] ├─ RNG algorithm... ⚠ (Low confidence - PCG not found)
[2024-02-10 14:30:50] ├─ Drop tables... ✓ (High confidence)
[2024-02-10 14:30:55] ├─ Rarity determination... ✓ (High confidence)
[2024-02-10 14:31:00] └─ Summon progression... ✓ (Medium confidence)
[2024-02-10 14:31:00] Summoning system complete (20s)
...
[2024-02-10 14:35:00] Extraction complete! (5m 0s)
[2024-02-10 14:35:00] Summary:
[2024-02-10 14:35:00]   - Combat: 15 mechanics extracted (12 High, 3 Medium)
[2024-02-10 14:35:00]   - Summoning: 8 mechanics extracted (6 High, 1 Medium, 1 Low)
[2024-02-10 14:35:00]   - PvP: 6 mechanics extracted (4 High, 2 Medium)
[2024-02-10 14:35:00]   - Progression: 12 mechanics extracted (8 High, 4 Medium)
[2024-02-10 14:35:00]   - Economy: 5 mechanics extracted (3 High, 2 Medium)
[2024-02-10 14:35:00] Documentation written to: COMPLETE_GAME_MECHANICS_MANUAL.md
```

## Future Enhancements

1. **Machine Learning Integration**
   - Train models to recognize common patterns
   - Improve confidence level assignment
   - Suggest likely formulas based on similar games

2. **Interactive Mode**
   - Allow user to review and correct extractions in real-time
   - Provide suggestions for ambiguous cases
   - Enable manual annotation of complex mechanics

3. **Diff Analysis**
   - Compare mechanics across game versions
   - Identify balance changes
   - Track formula evolution

4. **Community Database**
   - Share extracted mechanics across users
   - Crowdsource verification
   - Build pattern library

5. **Web Interface**
   - Browse extracted mechanics in web UI
   - Visualize relationships between systems
   - Export custom reports

---

**This design provides a comprehensive, autonomous system for extracting and documenting all game mechanics with minimal human intervention and maximum accuracy.**
