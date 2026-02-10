# CodeVerifier Implementation

## Overview

The `CodeVerifier` class validates extracted code and assesses confidence levels following the **zero-hallucination policy**: verify everything, assume nothing, hallucinate nothing.

## Implementation Status

✅ **COMPLETE** - Task 2.3: Implement CodeVerifier class

### Implemented Methods

1. ✅ `verify_line_reference()` - Exact line matching with partial match support
2. ✅ `extract_formula()` - Formula extraction with no-interpretation policy
3. ✅ `assess_confidence()` - Strict confidence level assessment
4. ✅ `identify_missing_data()` - Missing element identification
5. ✅ `check_for_assumptions()` - Assumption detection and flagging

## Core Features

### 1. Line Reference Verification

Verifies that a line number points to expected content with exact or partial matching:

```python
from extraction_system.mechanics_cleanup import CodeVerifier

verifier = CodeVerifier("C:/apktool/il2cpp-output/dump.cs")

# Exact match verification
verified = verifier.verify_line_reference(
    line_number=1072106,
    expected_content="private sealed class PlayerPetCollectionModel"
)

print(f"Verified: {verified}")  # True if exact or partial match
```

**Rules:**
- Returns `True` only for exact match or if expected content is substring
- Returns `False` for no match or invalid line numbers
- Logs verification results with details

### 2. Formula Extraction

Extracts mathematical formulas from method bodies with strict interpretation rules:

```python
method_body = """
{
    int baseValue = 100;
    int multiplier = 2;
    int result = baseValue * multiplier;
    return result;
}
"""

formula = verifier.extract_formula(method_body)

if formula:
    print(f"Formula: {formula.name} = {formula.expression}")
    print(f"Code: {formula.code_expression}")
    print(f"Confidence: {formula.confidence.value}")
    print(f"Copy-pastable: {formula.copy_pastable}")
else:
    print("No simple formula found (complex logic detected)")
```

**Rules:**
- Returns `None` if method contains conditionals, loops, or complex logic
- Only extracts explicit, simple mathematical expressions
- Identifies missing variables and dependencies
- Assesses confidence based on completeness

### 3. Confidence Assessment

Assesses confidence level of extractions with strict criteria:

```python
from extraction_system.mechanics_cleanup import Extraction, ConfidenceLevel

extraction = Extraction(
    name="DamageCalculation",
    category="combat",
    content="public int CalculateDamage() { return baseDamage * multiplier; }",
    line_number=12345,
    class_name="CombatSystem",
    method_name="CalculateDamage"
)

confidence = verifier.assess_confidence(extraction)

print(f"Confidence: {confidence.value}")
print(f"Description: {confidence.get_description()}")
```

**Confidence Levels:**

- **HIGH**: Complete code found, formula explicit, all values present
- **MEDIUM**: Code found, some values in config, formula clear but incomplete
- **LOW**: Partial code, formula requires interpretation
- **UNVERIFIED**: No code found or cannot validate

### 4. Missing Data Identification

Identifies specific missing elements in extractions:

```python
missing = verifier.identify_missing_data(extraction)

for item in missing:
    print(f"Missing: {item}")

# Example output:
# Missing: Class name not identified
# Missing: Config value 'multiplier' not found in code
# Missing: Formula 'damage': Variable 'baseDamage' definition not found in method
```

**Checks:**
- Missing class names
- Missing method names (for formula extractions)
- Missing formula elements (variables, values)
- Placeholder config values
- Incomplete content (< 50 characters)

### 5. Assumption Detection

Checks for assumptions and unverifiable claims:

```python
extraction.content = "This probably works and might be correct according to forum posts."

assumptions = verifier.check_for_assumptions(extraction)

for assumption in assumptions:
    print(f"Assumption: {assumption}")

# Example output:
# Assumption: Contains assumption keyword: 'probably'
# Assumption: Contains assumption keyword: 'might'
# Assumption: Contains external reference: 'according to' - not verifiable from code
```

**Detects:**
- Assumption keywords (probably, likely, might, could be, etc.)
- External references (forums, wikis, developer comments)
- Unverified formulas
- Inferred or calculated values

## Usage Examples

### Complete Verification Workflow

```python
from extraction_system.mechanics_cleanup import (
    CodeExtractor,
    CodeVerifier,
    Extraction,
    ConfidenceLevel
)

# Initialize
extractor = CodeExtractor("C:/apktool/il2cpp-output/dump.cs")
verifier = CodeVerifier("C:/apktool/il2cpp-output/dump.cs")

# Step 1: Extract code
matches = extractor.search_class(r"class AttacksSystem")
if matches:
    match = matches[0]
    
    # Step 2: Create extraction
    extraction = Extraction(
        name=match.class_name,
        category="combat",
        content=match.content[:500],
        line_number=match.line_number,
        class_name=match.class_name
    )
    
    # Step 3: Verify line reference
    verified = verifier.verify_line_reference(
        extraction.line_number,
        match.content.split('\n')[0]
    )
    print(f"Line verified: {verified}")
    
    # Step 4: Assess confidence
    confidence = verifier.assess_confidence(extraction)
    print(f"Confidence: {confidence.value}")
    
    # Step 5: Identify missing data
    missing = verifier.identify_missing_data(extraction)
    if missing:
        print(f"Missing data: {len(missing)} items")
        for item in missing:
            print(f"  - {item}")
    
    # Step 6: Check for assumptions
    assumptions = verifier.check_for_assumptions(extraction)
    if assumptions:
        print(f"Assumptions found: {len(assumptions)}")
        for assumption in assumptions:
            print(f"  - {assumption}")
    else:
        print("No assumptions - clean extraction!")
```

### Formula Verification Example

```python
# Extract a method
method_match = extractor.extract_method("AttacksSystem", "CalculateAttackTime")

if method_match:
    # Try to extract formula
    formula = verifier.extract_formula(method_match.body)
    
    if formula:
        print(f"Formula found: {formula.name}")
        print(f"Expression: {formula.expression}")
        print(f"Code: {formula.code_expression}")
        print(f"Confidence: {formula.confidence.value}")
        
        # Check variables
        print(f"\nVariables:")
        for var, desc in formula.variables.items():
            print(f"  {var}: {desc}")
        
        # Check missing elements
        if formula.missing_elements:
            print(f"\nMissing elements:")
            for elem in formula.missing_elements:
                print(f"  - {elem}")
        
        # Check if copy-pastable
        if formula.copy_pastable:
            print(f"\n✅ Formula is copy-pastable for calculations")
        else:
            print(f"\n⚠️ Formula requires interpretation")
    else:
        print("No simple formula found - method contains complex logic")
```

## Testing

### Unit Tests

Run unit tests with:

```bash
python -m pytest extraction_system/mechanics_cleanup/test_code_verifier.py -v
```

**Test Coverage:**
- ✅ 33 unit tests
- ✅ Initialization with valid/invalid paths
- ✅ Line reference verification (exact, partial, no match, invalid)
- ✅ Formula extraction (simple, complex, loops, no math)
- ✅ Confidence assessment (all levels)
- ✅ Missing data identification
- ✅ Assumption detection
- ✅ Helper methods (mathematical expression, copy-pastable, humanize)

### Integration Tests

Run integration tests with:

```bash
python -m pytest extraction_system/mechanics_cleanup/test_integration_verifier.py -v
```

**Test Coverage:**
- ✅ 6 integration tests
- ✅ Extract and verify class
- ✅ Extract and assess confidence
- ✅ Extract method and verify formula
- ✅ Extract and check assumptions
- ✅ Extract and identify missing data
- ✅ Complete verification workflow

### All Tests

Run all tests together:

```bash
python -m pytest extraction_system/mechanics_cleanup/test_code_verifier.py extraction_system/mechanics_cleanup/test_integration_verifier.py -v
```

**Result:** ✅ 39/39 tests passing

## Design Principles

### Zero-Hallucination Policy

The CodeVerifier strictly follows the zero-hallucination policy:

1. **Exact Matching**: Line references must match exactly or contain expected content
2. **No Interpretation**: Complex formulas return `None` rather than simplified versions
3. **No Inference**: Missing values are flagged, not inferred from patterns
4. **No Extrapolation**: If data exists for X but not Y, don't assume Y follows X
5. **No External Sources**: Only code from dump.cs is valid

### Confidence Level Rules

**HIGH Confidence:**
- Complete code found
- Formula explicit and simple
- All values present
- No missing elements
- No assumptions

**MEDIUM Confidence:**
- Code found
- Formula clear but some values missing
- Logic verified but incomplete data
- Minor gaps that don't affect understanding

**LOW Confidence:**
- Partial code found
- Formula requires interpretation
- Significant gaps in understanding
- Multiple missing elements

**UNVERIFIED:**
- No code found
- Cannot validate claim
- Invalid line references
- Empty or missing content

## Requirements Validation

This implementation validates the following requirements:

- ✅ **Requirement 6.1**: Line number references for every extracted mechanic
- ✅ **Requirement 6.2**: Zero assumptions about game mechanics not found in code
- ✅ **Requirement 6.4**: Clear marking of mechanics that cannot be fully verified
- ✅ **Requirement 6.5**: Explicit confidence levels with explanations
- ✅ **Requirement 6.6**: Extract formulas directly from code without modification

## Next Steps

After completing Task 2.3, the next tasks are:

1. **Task 2.4**: Write property test for CodeVerifier
   - Property 2: Zero Unverified Claims
   - Property 3: Formula Extraction Accuracy

2. **Task 3**: Checkpoint - Verify extraction modules work
   - Test extraction on known classes
   - Verify confidence assessment
   - Ensure all tests pass

## Files Created

- ✅ `code_verifier.py` - Main implementation (500+ lines)
- ✅ `test_code_verifier.py` - Unit tests (33 tests)
- ✅ `test_integration_verifier.py` - Integration tests (6 tests)
- ✅ `CODE_VERIFIER_IMPLEMENTATION.md` - This documentation

## Summary

The CodeVerifier class is fully implemented and tested with:

- **5 core methods** implementing strict verification rules
- **39 passing tests** (33 unit + 6 integration)
- **Zero-hallucination policy** enforced throughout
- **Complete documentation** with usage examples
- **Requirements validation** for 6.1, 6.2, 6.4, 6.5, 6.6

The implementation is ready for use in the mechanics cleanup extraction pipeline.
