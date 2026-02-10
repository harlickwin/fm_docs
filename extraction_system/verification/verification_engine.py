"""Verification engine for validating extracted mechanics."""

from typing import List, Dict, Any
from dataclasses import dataclass
from extraction_system.core.base import ConfidenceLevel, GameMechanic
from extraction_system.core.logger import ProgressLogger


@dataclass
class VerificationResult:
    """Result of verification."""
    passed: bool
    details: str
    evidence: List[str]


class VerificationEngine:
    """Validates extracted mechanics and assigns confidence levels."""
    
    def __init__(self, logger: ProgressLogger = None):
        self.logger = logger or ProgressLogger("VerificationEngine")
    
    def verify_mechanic(self, mechanic: GameMechanic) -> VerificationResult:
        """Verify a game mechanic."""
        evidence = []
        
        # Check if ARM code location is found
        if mechanic.arm_code_location and mechanic.arm_code_location != "Not found":
            evidence.append(f"ARM code found at: {mechanic.arm_code_location}")
        
        # Check if formula exists
        if mechanic.formula:
            evidence.append(f"Formula defined: {mechanic.formula}")
        
        # Check if data structures are identified
        if mechanic.data_structures:
            evidence.append(f"Data structures: {', '.join(mechanic.data_structures)}")
        
        passed = len(evidence) >= 2
        details = "Verification passed" if passed else "Insufficient evidence"
        
        return VerificationResult(passed=passed, details=details, evidence=evidence)
    
    def assign_confidence(self, mechanic: GameMechanic, verification: VerificationResult) -> ConfidenceLevel:
        """Assign confidence level based on verification."""
        # High: ARM code found and verified
        if mechanic.arm_code_location and "Not found" not in mechanic.arm_code_location:
            if mechanic.formula and verification.passed:
                return ConfidenceLevel.HIGH
        
        # Medium: IL2CPP structure found but ARM not verified
        if mechanic.data_structures and len(mechanic.data_structures) > 0:
            return ConfidenceLevel.MEDIUM
        
        # Low: Inferred from patterns only
        return ConfidenceLevel.LOW
    
    def verify_all_mechanics(self, mechanics: Dict[str, GameMechanic]) -> Dict[str, VerificationResult]:
        """Verify all mechanics."""
        self.logger.section("Verifying Extracted Mechanics")
        
        results = {}
        for name, mechanic in mechanics.items():
            result = self.verify_mechanic(mechanic)
            confidence = self.assign_confidence(mechanic, result)
            mechanic.confidence = confidence
            results[name] = result
            
            self.logger.info(f"{mechanic.name}: {confidence.value}")
        
        return results
