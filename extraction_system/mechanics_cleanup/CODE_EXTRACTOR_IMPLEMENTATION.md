# CodeExtractor Implementation Summary

## Overview

Successfully implemented the `CodeExtractor` class for Task 2.1 of the mechanics-cleanup spec. This class provides robust code extraction capabilities from the IL2CPP dump file (dump.cs) following a strict zero-hallucination policy.

## Implementation Details

### File Location
- **Main Implementation**: `extraction_system/mechanics_cleanup/code_extractor.py`
- **Unit Tests**: `extraction_system/mechanics_cleanup/test_code_extractor.py`

### Core Features Implemented

#### 1. Class Search (`search_class()`)
- Searches for classes matching regex patterns
- Returns list of `ClassMatch` objects with:
  - Class name
  - Line number
  - Full class content
  - Context around the match
- Handles multiple matches appropriately
- Logs all search attempts

#### 2. Configuration Search (`search_config()`)
- Searches for configuration classes by name
- Extracts field declarations and values
- Returns `ConfigMatch` object with:
  - Class name
  - Line number
  - Dictionary of fields and values
  - Full class content
- Handles multiple matches with error reporting

#### 3. Method Extraction (`extract_method()`)
- Extracts specific methods from classes
- Returns `MethodMatch` object with:
  - Class and method names
  - Line number
  - Method signature
  - Method body
  - Full method content
- Uses brace matching to extract complete method bodies

#### 4. Formula Extraction (`extract_formula()`)
- Extracts mathematical formulas from method bodies
- Returns list of `FormulaExtraction` objects with:
  - Formula name (variable being assigned)
  - Human-readable expression
  - Exact code expression
  - Dictionary of variables
  - Line number
  - Complexity indicator (simple vs complex)
- Identifies mathematical operations (+, -, *, /, %)
- Distinguishes simple formulas from complex logic

#### 5. Context Retrieval (`get_context()`)
- Retrieves code context around any line number
- Configurable lines before and after
- Returns formatted text with line numbers
- Marks target line with ">>>" indicator

### Data Models

#### ClassMatch
```python
@dataclass
class ClassMatch:
    class_name: str
    line_number: int
    content: str
    context: str
```

#### ConfigMatch
```python
@dataclass
class ConfigMatch:
    class_name: str
    line_number: int
    fields: Dict[str, str]
    content: str
```

#### MethodMatch
```python
@dataclass
class MethodMatch:
    class_name: str
    method_name: str
    line_number: int
    signature: str
    body: str
    full_content: str
```

#### FormulaExtraction
```python
@dataclass
class FormulaExtraction:
    formula_name: str
    expression: str
    code_expression: str
    variables: Dict[str, str]
    line_number: int
    method_name: str
    is_simple: bool
```

### Integration with Infrastructure

The CodeExtractor integrates seamlessly with existing infrastructure:

1. **Logger Integration**: Uses `MechanicsCleanupLogger` for structured logging
   - Logs search patterns and results
   - Logs matches found with line numbers
   - Logs knowledge gaps

2. **Error Handler Integration**: Uses `ErrorHandler` for error management
   - Handles file not found errors
   - Handles multiple matches
   - Handles partial matches
   - Handles missing data

3. **Knowledge Gap Tracker Integration**: Creates gap entries for missing information
   - Records failed searches
   - Documents search patterns used
   - Categorizes gaps by priority
   - Tracks related mechanics

### Helper Methods

The implementation includes several private helper methods:

- `_load_content()`: Loads and caches dump.cs content
- `_extract_class_name()`: Extracts class name from declaration line
- `_extract_class_content()`: Extracts complete class body using brace matching
- `_extract_config_fields()`: Parses field declarations from class content
- `_extract_method_body()`: Extracts method body using brace matching
- `_is_mathematical_expression()`: Detects mathematical operations
- `_is_simple_formula()`: Determines formula complexity
- `_extract_variables()`: Extracts variable names from expressions
- `_humanize_expression()`: Converts code to human-readable format

### Zero-Hallucination Policy Compliance

The implementation strictly follows the zero-hallucination policy:

1. **Exact Matching**: Only returns exact matches, no assumptions
2. **No Interpretation**: Complex formulas are marked as such, not simplified
3. **Missing Data Tracking**: All failed searches create knowledge gap entries
4. **Confidence Assessment**: Provides data for confidence level determination
5. **Full Context**: Always provides surrounding code for verification

## Testing

### Test Coverage

Created comprehensive test suite with 23 tests covering:

1. **Initialization Tests**
   - Valid path initialization
   - Invalid path error handling

2. **Class Search Tests**
   - Known class search (PlayerPetCollectionModel)
   - Non-existent class search
   - Multiple match handling
   - Pattern matching

3. **Config Search Tests**
   - Known config class extraction
   - Field parsing

4. **Method Extraction Tests**
   - Known method extraction
   - Non-existent class handling
   - Non-existent method handling

5. **Formula Extraction Tests**
   - Simple mathematical expressions
   - Complex expressions with conditionals
   - Non-mathematical code filtering

6. **Context Retrieval Tests**
   - Valid line number context
   - Edge cases (start/end of file)

7. **Knowledge Gap Tests**
   - Gap creation and tracking

8. **Helper Method Tests**
   - Mathematical expression detection
   - Formula complexity detection
   - Expression humanization
   - Variable extraction
   - Class name extraction

9. **Integration Tests**
   - AttacksSystem class search
   - Combat-related class search
   - Config class search

### Test Results

All 23 tests pass successfully:
```
======================== 23 passed in 5.66s =========================
```

### Test Execution

Run tests with:
```bash
python -m pytest extraction_system/mechanics_cleanup/test_code_extractor.py -v
```

## Usage Examples

### Example 1: Search for a Class
```python
from extraction_system.mechanics_cleanup.code_extractor import CodeExtractor

extractor = CodeExtractor(r"C:\apktool\il2cpp-output\dump.cs")
matches = extractor.search_class(r"class AttacksSystem")

for match in matches:
    print(f"Found {match.class_name} at line {match.line_number}")
```

### Example 2: Extract a Configuration Class
```python
config = extractor.search_config("MountSummonDropChanceConfig")
if config:
    print(f"Config: {config.class_name}")
    for field, value in config.fields.items():
        print(f"  {field} = {value}")
```

### Example 3: Extract a Method
```python
method = extractor.extract_method("AttacksSystem", "GetDamage")
if method:
    print(f"Method: {method.signature}")
    print(f"Body:\n{method.body}")
```

### Example 4: Extract Formulas
```python
method = extractor.extract_method("AttacksSystem", "CalculateAttackTime")
if method:
    formulas = extractor.extract_formula(method.body)
    for formula in formulas:
        print(f"Formula: {formula.formula_name} = {formula.expression}")
        print(f"Variables: {formula.variables}")
```

### Example 5: Get Code Context
```python
context = extractor.get_context(1057705, lines_before=5, lines_after=5)
print(context)
```

### Example 6: Create Knowledge Gap
```python
extractor.create_knowledge_gap(
    category="combat",
    title="Missing damage multiplier values",
    description="Found formula structure but multiplier values not in dump.cs",
    searched_patterns=["DamageMultiplier", "CombatConfig"],
    priority=GapPriority.MEDIUM,
    related_mechanics=["damage_calculation"],
    notes="May be in config files"
)
```

## Requirements Validation

This implementation satisfies the following requirements:

- **Requirement 1.1**: Guild war matchmaking logic extraction capability
- **Requirement 2.1**: Dungeon scaling formula extraction capability
- **Requirement 3.3**: Drop table extraction capability
- **Requirement 4.3**: PvP matchmaking algorithm extraction capability
- **Requirement 5.1**: Shop mechanics extraction capability
- **Requirement 9.1-9.5**: Combat formula extraction capabilities
- **Requirement 6.1**: Line number reference capability
- **Requirement 6.7**: Class and method name citation capability

## Next Steps

With the CodeExtractor implemented and tested, the next tasks are:

1. **Task 2.2**: Write property test for CodeExtractor (optional)
2. **Task 2.3**: Implement CodeVerifier class
3. **Task 2.4**: Write property test for CodeVerifier (optional)

The CodeExtractor provides the foundation for all subsequent extraction tasks in the mechanics-cleanup spec.

## Files Created

1. `extraction_system/mechanics_cleanup/code_extractor.py` (520 lines)
2. `extraction_system/mechanics_cleanup/test_code_extractor.py` (350 lines)
3. `extraction_system/mechanics_cleanup/CODE_EXTRACTOR_IMPLEMENTATION.md` (this file)

## Dependencies

- Python 3.7+
- pathlib (standard library)
- re (standard library)
- dataclasses (standard library)
- pytest (for testing)

## Performance Notes

- **Caching**: File content is cached after first load to avoid repeated disk reads
- **Memory**: Entire dump.cs (~1.2M lines) is loaded into memory for fast searching
- **Search Speed**: Regex searches are efficient, typically completing in seconds
- **Context Extraction**: Fast due to in-memory content access

## Conclusion

The CodeExtractor class is fully implemented, thoroughly tested, and ready for use in the mechanics extraction pipeline. It provides robust, reliable code extraction capabilities while maintaining strict adherence to the zero-hallucination policy.
