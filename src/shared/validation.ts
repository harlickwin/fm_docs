/**
 * Configuration Validation Utilities
 */

import { TournamentConfig, ValidationError } from './types';

/**
 * Validate tournament configuration
 * Returns array of validation errors (empty if valid)
 */
export function validateConfig(config: TournamentConfig): ValidationError[] {
  const errors: ValidationError[] = [];

  // At least one substat must be selected
  const hasSubstat = Object.values(config.substats).some(v => v);
  if (!hasSubstat) {
    errors.push({
      field: 'substats',
      message: 'At least one substat must be selected',
      severity: 'error',
    });
  }

  // At least one weapon type must be selected
  if (!config.weaponTypes.ranged && !config.weaponTypes.melee) {
    errors.push({
      field: 'weaponTypes',
      message: 'At least one weapon type must be selected',
      severity: 'error',
    });
  }

  // Substat multiplier validation
  if (config.substatMultiplier < 0.01 || config.substatMultiplier > 1.0) {
    errors.push({
      field: 'substatMultiplier',
      message: 'Substat multiplier must be between 1% and 100%',
      severity: 'error',
    });
  }

  // Target builds validation
  if (config.targetBuilds <= 0) {
    errors.push({
      field: 'targetBuilds',
      message: 'Target builds must be greater than 0',
      severity: 'error',
    });
  } else if (config.targetBuilds < 100) {
    errors.push({
      field: 'targetBuilds',
      message: 'Target builds below 100 may not produce meaningful results',
      severity: 'warning',
    });
  } else if (config.targetBuilds > 100000) {
    errors.push({
      field: 'targetBuilds',
      message: 'Target builds above 100,000 will take a very long time',
      severity: 'warning',
    });
  }

  // Output directory validation
  if (!config.outputDirectory || config.outputDirectory.trim() === '') {
    errors.push({
      field: 'outputDirectory',
      message: 'Output directory must be selected',
      severity: 'error',
    });
  }

  // Max workers validation
  if (config.maxWorkers < 1) {
    errors.push({
      field: 'maxWorkers',
      message: 'At least 1 worker is required',
      severity: 'error',
    });
  } else if (config.maxWorkers > 32) {
    errors.push({
      field: 'maxWorkers',
      message: 'More than 32 workers may cause performance issues',
      severity: 'warning',
    });
  }

  // Checkpoint interval validation
  if (config.checkpointInterval < 60) {
    errors.push({
      field: 'checkpointInterval',
      message: 'Checkpoint interval should be at least 60 seconds',
      severity: 'warning',
    });
  } else if (config.checkpointInterval > 3600) {
    errors.push({
      field: 'checkpointInterval',
      message: 'Checkpoint interval above 1 hour may risk data loss',
      severity: 'warning',
    });
  }

  // Weapon type and substat consistency
  if (config.weaponTypes.ranged && !config.weaponTypes.melee) {
    if (config.substats.meleeDamage && !config.substats.rangedDamage) {
      errors.push({
        field: 'substats',
        message: 'Ranged weapons selected but only melee damage substat enabled',
        severity: 'warning',
      });
    }
  }

  if (config.weaponTypes.melee && !config.weaponTypes.ranged) {
    if (config.substats.rangedDamage && !config.substats.meleeDamage) {
      errors.push({
        field: 'substats',
        message: 'Melee weapons selected but only ranged damage substat enabled',
        severity: 'warning',
      });
    }
  }

  return errors;
}

/**
 * Check if configuration has any errors (not warnings)
 */
export function hasErrors(errors: ValidationError[]): boolean {
  return errors.some(e => e.severity === 'error');
}

/**
 * Get error messages by severity
 */
export function getErrorsBySeverity(errors: ValidationError[]): {
  errors: ValidationError[];
  warnings: ValidationError[];
} {
  return {
    errors: errors.filter(e => e.severity === 'error'),
    warnings: errors.filter(e => e.severity === 'warning'),
  };
}
