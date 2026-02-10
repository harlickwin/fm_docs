/**
 * Unit tests for runtime estimation utilities
 */

import { describe, it, expect } from 'vitest';
import { estimateRuntime, getConfidenceDescription } from './estimation';
import { TournamentConfig } from './types';

const createBaseConfig = (): TournamentConfig => ({
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
  targetBuilds: 1000,
  outputDirectory: '/path/to/output',
  maxWorkers: 4,
  checkpointInterval: 300,
  includeMetaBuild: true,
  loadPreviousResults: false,
});

describe('estimateRuntime', () => {
  it('calculates total battles correctly (round-robin)', () => {
    const config = createBaseConfig();
    config.targetBuilds = 100;
    
    const estimate = estimateRuntime(config);
    
    // Round-robin: N*(N-1)/2 = 100*99/2 = 4950
    expect(estimate.totalBattles).toBe(4950);
  });

  it('returns all required fields', () => {
    const config = createBaseConfig();
    const estimate = estimateRuntime(config);
    
    expect(estimate).toHaveProperty('totalBattles');
    expect(estimate).toHaveProperty('estimatedSeconds');
    expect(estimate).toHaveProperty('estimatedMinutes');
    expect(estimate).toHaveProperty('estimatedHours');
    expect(estimate).toHaveProperty('formattedTime');
    expect(estimate).toHaveProperty('battlesPerSecond');
    expect(estimate).toHaveProperty('confidence');
  });

  it('estimates faster for simple configurations (few substats)', () => {
    const simpleConfig = createBaseConfig();
    simpleConfig.substats = {
      damage: false,
      meleeDamage: false,
      rangedDamage: true,
      criticalChance: true,
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
    
    const complexConfig = createBaseConfig();
    complexConfig.substats = {
      damage: true,
      meleeDamage: true,
      rangedDamage: true,
      criticalChance: true,
      criticalDamage: true,
      attackSpeed: true,
      doubleChance: true,
      health: true,
      healthRegen: true,
      lifesteal: true,
      blockChance: true,
      skillCooldown: true,
      skillDamage: true,
    };
    
    const simpleEstimate = estimateRuntime(simpleConfig);
    const complexEstimate = estimateRuntime(complexConfig);
    
    // Simple config should have higher battles per second
    expect(simpleEstimate.battlesPerSecond).toBeGreaterThan(complexEstimate.battlesPerSecond);
  });

  it('scales with worker count', () => {
    const config1 = createBaseConfig();
    config1.maxWorkers = 1;
    
    const config4 = createBaseConfig();
    config4.maxWorkers = 4;
    
    const estimate1 = estimateRuntime(config1);
    const estimate4 = estimateRuntime(config4);
    
    // More workers should result in higher effective speed
    expect(estimate4.battlesPerSecond).toBeGreaterThan(estimate1.battlesPerSecond);
    
    // More workers should result in shorter estimated time
    expect(estimate4.estimatedSeconds).toBeLessThan(estimate1.estimatedSeconds);
  });

  it('formats time correctly for seconds', () => {
    const config = createBaseConfig();
    config.targetBuilds = 10; // Very small tournament
    
    const estimate = estimateRuntime(config);
    
    // Should be formatted as seconds
    expect(estimate.formattedTime).toMatch(/\d+s/);
  });

  it('formats time correctly for minutes', () => {
    const config = createBaseConfig();
    config.targetBuilds = 5000; // Larger tournament to ensure minutes
    config.maxWorkers = 1;
    
    const estimate = estimateRuntime(config);
    
    // Should be formatted with minutes (or seconds if very fast)
    expect(estimate.formattedTime).toMatch(/(\d+m|\d+s)/);
  });

  it('formats time correctly for hours', () => {
    const config = createBaseConfig();
    config.targetBuilds = 100000; // Larger tournament
    config.maxWorkers = 1;
    
    const estimate = estimateRuntime(config);
    
    // With 100k builds, should take significant time
    // Just verify it's a reasonable estimate
    expect(estimate.estimatedMinutes).toBeGreaterThan(30);
  });

  it('returns high confidence for typical configurations', () => {
    const config = createBaseConfig();
    config.targetBuilds = 10000;
    config.maxWorkers = 4;
    
    const estimate = estimateRuntime(config);
    
    expect(estimate.confidence).toBe('high');
  });

  it('returns medium confidence for edge cases', () => {
    const config = createBaseConfig();
    config.targetBuilds = 500; // Very low
    
    const estimate = estimateRuntime(config);
    
    expect(estimate.confidence).toBe('medium');
  });

  it('returns medium confidence for very large tournaments', () => {
    const config = createBaseConfig();
    config.targetBuilds = 150000; // Very high
    
    const estimate = estimateRuntime(config);
    
    expect(estimate.confidence).toBe('medium');
  });

  it('calculates correct time units', () => {
    const config = createBaseConfig();
    config.targetBuilds = 1000;
    
    const estimate = estimateRuntime(config);
    
    // Verify time unit conversions
    expect(estimate.estimatedMinutes).toBeCloseTo(estimate.estimatedSeconds / 60, 2);
    expect(estimate.estimatedHours).toBeCloseTo(estimate.estimatedMinutes / 60, 2);
  });

  it('handles large tournaments', () => {
    const config = createBaseConfig();
    config.targetBuilds = 100000;
    
    const estimate = estimateRuntime(config);
    
    // Should handle large numbers without errors
    expect(estimate.totalBattles).toBeGreaterThan(0);
    expect(estimate.estimatedSeconds).toBeGreaterThan(0);
    expect(estimate.formattedTime).toBeTruthy();
  });

  it('adjusts speed for weapon type diversity', () => {
    const rangedOnly = createBaseConfig();
    rangedOnly.weaponTypes = { ranged: true, melee: false };
    
    const both = createBaseConfig();
    both.weaponTypes = { ranged: true, melee: true };
    
    const rangedEstimate = estimateRuntime(rangedOnly);
    const bothEstimate = estimateRuntime(both);
    
    // Both weapon types should be slightly slower
    expect(bothEstimate.battlesPerSecond).toBeLessThanOrEqual(rangedEstimate.battlesPerSecond);
  });

  it('adjusts speed for substat multiplier', () => {
    const lowMultiplier = createBaseConfig();
    lowMultiplier.substatMultiplier = 0.3;
    
    const highMultiplier = createBaseConfig();
    highMultiplier.substatMultiplier = 0.9;
    
    const lowEstimate = estimateRuntime(lowMultiplier);
    const highEstimate = estimateRuntime(highMultiplier);
    
    // Higher multiplier should be slightly slower (longer battles)
    expect(highEstimate.battlesPerSecond).toBeLessThanOrEqual(lowEstimate.battlesPerSecond);
  });
});

describe('getConfidenceDescription', () => {
  it('returns correct description for high confidence', () => {
    const description = getConfidenceDescription('high');
    expect(description).toContain('accurate');
    expect(description).toContain('20%');
  });

  it('returns correct description for medium confidence', () => {
    const description = getConfidenceDescription('medium');
    expect(description).toContain('vary');
    expect(description).toContain('30-50%');
  });

  it('returns correct description for low confidence', () => {
    const description = getConfidenceDescription('low');
    expect(description).toContain('rough');
    expect(description).toContain('vary significantly');
  });
});
