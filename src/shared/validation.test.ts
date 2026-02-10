/**
 * Unit tests for validation utilities
 */

import { describe, it, expect } from 'vitest';
import { validateConfig, hasErrors, getErrorsBySeverity } from './validation';
import { TournamentConfig } from './types';

const createValidConfig = (): TournamentConfig => ({
  substats: {
    damage: false,
    meleeDamage: false,
    rangedDamage: true,
    criticalChance: true,
    criticalDamage: true,
    attackSpeed: true,
    doubleChance: true,
    health: true,
    healthRegen: true,
    lifesteal: true,
    blockChance: false,
    skillCooldown: false,
    skillDamage: false,
  },
  weaponTypes: {
    ranged: true,
    melee: false,
  },
  substatMultiplier: 0.75,
  targetBuilds: 10000,
  outputDirectory: '/path/to/output',
  maxWorkers: 4,
  checkpointInterval: 300,
  includeMetaBuild: true,
  loadPreviousResults: false,
});

describe('validateConfig', () => {
  it('returns no errors for valid configuration', () => {
    const config = createValidConfig();
    const errors = validateConfig(config);
    expect(errors).toHaveLength(0);
  });

  it('returns error when no substats are selected', () => {
    const config = createValidConfig();
    config.substats = {
      damage: false,
      meleeDamage: false,
      rangedDamage: false,
      criticalChance: false,
      criticalDamage: false,
      attackSpeed: false,
      doubleChance: false,
      health: false,
      healthRegen: false,
      lifesteal: false,
      blockChance: false,
      skillCooldown: false,
      skillDamage: false,
    };
    
    const errors = validateConfig(config);
    expect(errors.length).toBeGreaterThan(0);
    expect(errors.some(e => e.field === 'substats' && e.severity === 'error')).toBe(true);
  });

  it('returns error when no weapon types are selected', () => {
    const config = createValidConfig();
    config.weaponTypes = { ranged: false, melee: false };
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'weaponTypes' && e.severity === 'error')).toBe(true);
  });

  it('returns error when substat multiplier is out of range', () => {
    const config = createValidConfig();
    config.substatMultiplier = 1.5;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'substatMultiplier' && e.severity === 'error')).toBe(true);
  });

  it('returns error when target builds is zero or negative', () => {
    const config = createValidConfig();
    config.targetBuilds = 0;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'targetBuilds' && e.severity === 'error')).toBe(true);
  });

  it('returns warning when target builds is very low', () => {
    const config = createValidConfig();
    config.targetBuilds = 50;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'targetBuilds' && e.severity === 'warning')).toBe(true);
  });

  it('returns warning when target builds is very high', () => {
    const config = createValidConfig();
    config.targetBuilds = 150000;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'targetBuilds' && e.severity === 'warning')).toBe(true);
  });

  it('returns error when output directory is empty', () => {
    const config = createValidConfig();
    config.outputDirectory = '';
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'outputDirectory' && e.severity === 'error')).toBe(true);
  });

  it('returns error when max workers is less than 1', () => {
    const config = createValidConfig();
    config.maxWorkers = 0;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'maxWorkers' && e.severity === 'error')).toBe(true);
  });

  it('returns warning when max workers is very high', () => {
    const config = createValidConfig();
    config.maxWorkers = 64;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'maxWorkers' && e.severity === 'warning')).toBe(true);
  });

  it('returns warning when checkpoint interval is too short', () => {
    const config = createValidConfig();
    config.checkpointInterval = 30;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'checkpointInterval' && e.severity === 'warning')).toBe(true);
  });

  it('returns warning when checkpoint interval is too long', () => {
    const config = createValidConfig();
    config.checkpointInterval = 7200;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'checkpointInterval' && e.severity === 'warning')).toBe(true);
  });

  it('returns warning for weapon type and substat mismatch (ranged only with melee damage)', () => {
    const config = createValidConfig();
    config.weaponTypes = { ranged: true, melee: false };
    config.substats.rangedDamage = false;
    config.substats.meleeDamage = true;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'substats' && e.severity === 'warning')).toBe(true);
  });

  it('returns warning for weapon type and substat mismatch (melee only with ranged damage)', () => {
    const config = createValidConfig();
    config.weaponTypes = { ranged: false, melee: true };
    config.substats.rangedDamage = true;
    config.substats.meleeDamage = false;
    
    const errors = validateConfig(config);
    expect(errors.some(e => e.field === 'substats' && e.severity === 'warning')).toBe(true);
  });
});

describe('hasErrors', () => {
  it('returns true when there are errors', () => {
    const errors = [
      { field: 'test', message: 'Error', severity: 'error' as const },
      { field: 'test2', message: 'Warning', severity: 'warning' as const },
    ];
    expect(hasErrors(errors)).toBe(true);
  });

  it('returns false when there are only warnings', () => {
    const errors = [
      { field: 'test', message: 'Warning', severity: 'warning' as const },
    ];
    expect(hasErrors(errors)).toBe(false);
  });

  it('returns false when there are no errors', () => {
    expect(hasErrors([])).toBe(false);
  });
});

describe('getErrorsBySeverity', () => {
  it('separates errors and warnings correctly', () => {
    const errors = [
      { field: 'test1', message: 'Error 1', severity: 'error' as const },
      { field: 'test2', message: 'Warning 1', severity: 'warning' as const },
      { field: 'test3', message: 'Error 2', severity: 'error' as const },
      { field: 'test4', message: 'Warning 2', severity: 'warning' as const },
    ];
    
    const result = getErrorsBySeverity(errors);
    expect(result.errors).toHaveLength(2);
    expect(result.warnings).toHaveLength(2);
    expect(result.errors.every(e => e.severity === 'error')).toBe(true);
    expect(result.warnings.every(e => e.severity === 'warning')).toBe(true);
  });

  it('handles empty array', () => {
    const result = getErrorsBySeverity([]);
    expect(result.errors).toHaveLength(0);
    expect(result.warnings).toHaveLength(0);
  });
});
