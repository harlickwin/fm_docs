/**
 * Formula Configuration Types
 * Defines types for configurable game formulas
 */

export interface AttackSpeedTier {
  minPercent: number;
  maxPercent: number;
  attackInterval: number;
}

export interface DoubleAttackDelays {
  normal: number;
  highAttackSpeed: number;
}

export interface CriticalHitConfig {
  baseDamageMultiplier: number;
}

export interface StatCaps {
  attackSpeed: number;
  critChance: number;
  doubleChance: number;
}

export interface FormulaConfig {
  id: string;
  name: string;
  description: string;
  version: string;
  createdAt: number;
  
  attackSpeedTiers: AttackSpeedTier[];
  doubleAttackDelays: DoubleAttackDelays;
  criticalHit: CriticalHitConfig;
  meleeMovementDelay: number;
  caps: StatCaps;
}

export interface ValidationResult {
  valid: boolean;
  errors: string[];
  warnings: string[];
}
