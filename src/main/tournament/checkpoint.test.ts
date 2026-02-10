/**
 * Tests for Checkpoint Manager
 * Validates checkpoint save/load and recovery functionality
 */

import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { CheckpointManager } from './checkpoint';
import { TournamentState, TournamentConfig } from '../../shared/types';
import * as fs from 'fs';
import * as path from 'path';

describe('CheckpointManager', () => {
  let checkpointManager: CheckpointManager;
  let testOutputDir: string;
  let mockState: TournamentState;

  beforeEach(() => {
    testOutputDir = path.join(process.cwd(), 'test-checkpoints');
    
    // Create test directory
    if (!fs.existsSync(testOutputDir)) {
      fs.mkdirSync(testOutputDir, { recursive: true });
    }

    checkpointManager = new CheckpointManager(testOutputDir);

    // Mock tournament state
    mockState = {
      version: '1.0.0',
      timestamp: Date.now(),
      config: {
        substats: {
          damage: true,
          meleeDamage: false,
          rangedDamage: false,
          criticalChance: true,
          criticalDamage: true,
          attackSpeed: true,
          doubleChance: false,
          health: true,
          healthRegen: false,
          lifesteal: false,
          blockChance: false,
          skillCooldown: false,
          skillDamage: false,
        },
        weaponTypes: { ranged: true, melee: true },
        substatMultiplier: 1.0,
        targetBuilds: 100,
        outputDirectory: testOutputDir,
        maxWorkers: 2,
        checkpointInterval: 300,
        includeMetaBuild: false,
        loadPreviousResults: false,
      },
      builds: [],
      completedBattles: [],
      results: {},
      nextBattleIndex: 0,
      totalBattles: 4950,
    };
  });

  afterEach(() => {
    // Clean up test directory
    if (fs.existsSync(testOutputDir)) {
      const files = fs.readdirSync(testOutputDir);
      files.forEach(file => {
        fs.unlinkSync(path.join(testOutputDir, file));
      });
      fs.rmdirSync(testOutputDir);
    }
  });

  describe('Checkpoint Save', () => {
    it('should save checkpoint successfully', async () => {
      await checkpointManager.save(mockState);
      
      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      expect(fs.existsSync(checkpointPath)).toBe(true);
    });

    it('should save valid JSON', async () => {
      await checkpointManager.save(mockState);
      
      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      const content = fs.readFileSync(checkpointPath, 'utf-8');
      
      expect(() => JSON.parse(content)).not.toThrow();
    });

    it('should include all required fields', async () => {
      await checkpointManager.save(mockState);
      
      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      const content = fs.readFileSync(checkpointPath, 'utf-8');
      const saved = JSON.parse(content);

      expect(saved).toHaveProperty('version');
      expect(saved).toHaveProperty('timestamp');
      expect(saved).toHaveProperty('config');
      expect(saved).toHaveProperty('builds');
      expect(saved).toHaveProperty('completedBattles');
      expect(saved).toHaveProperty('results');
      expect(saved).toHaveProperty('nextBattleIndex');
      expect(saved).toHaveProperty('totalBattles');
    });

    it('should update timestamp on each save', async () => {
      await checkpointManager.save(mockState);
      const firstTimestamp = mockState.timestamp;

      // Wait a bit and save again
      await new Promise(resolve => setTimeout(resolve, 10));
      mockState.timestamp = Date.now();
      await checkpointManager.save(mockState);

      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      const content = fs.readFileSync(checkpointPath, 'utf-8');
      const saved = JSON.parse(content);

      expect(saved.timestamp).toBeGreaterThan(firstTimestamp);
    });

    it('should handle large state objects', async () => {
      // Add many builds and battles
      mockState.builds = Array.from({ length: 1000 }, (_, i) => ({
        substats: { damage: i },
        dps: i * 10,
        hps: 10,
        maxHP: 1000,
        weaponType: 'melee' as const,
        description: `Build ${i}`,
        slotAllocation: 'test',
      }));

      mockState.completedBattles = Array.from({ length: 10000 }, (_, i) => ({
        build1Index: i % 1000,
        build2Index: (i + 1) % 1000,
        winner: 'build1' as const,
      }));

      await checkpointManager.save(mockState);
      
      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      expect(fs.existsSync(checkpointPath)).toBe(true);
      
      const stats = fs.statSync(checkpointPath);
      expect(stats.size).toBeGreaterThan(0);
    });
  });

  describe('Checkpoint Load', () => {
    it('should load checkpoint successfully', async () => {
      await checkpointManager.save(mockState);
      const loaded = await checkpointManager.load();

      expect(loaded).not.toBeNull();
      expect(loaded?.version).toBe(mockState.version);
      expect(loaded?.totalBattles).toBe(mockState.totalBattles);
    });

    it('should return null if checkpoint does not exist', async () => {
      const loaded = await checkpointManager.load();
      expect(loaded).toBeNull();
    });

    it('should preserve all data fields', async () => {
      mockState.nextBattleIndex = 1000;
      mockState.completedBattles = [
        { build1Index: 0, build2Index: 1, winner: 'build1' },
        { build1Index: 0, build2Index: 2, winner: 'build2' },
      ];

      await checkpointManager.save(mockState);
      const loaded = await checkpointManager.load();

      expect(loaded?.nextBattleIndex).toBe(1000);
      expect(loaded?.completedBattles).toHaveLength(2);
    });

    it('should handle corrupted JSON gracefully', async () => {
      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      fs.writeFileSync(checkpointPath, 'invalid json {{{', 'utf-8');

      const loaded = await checkpointManager.load();
      expect(loaded).toBeNull();
    });
  });

  describe('Checkpoint Validation', () => {
    it('should validate correct checkpoint', () => {
      const isValid = checkpointManager.validate(mockState);
      expect(isValid).toBe(true);
    });

    it('should reject checkpoint without version', () => {
      const invalid = { ...mockState, version: undefined };
      const isValid = checkpointManager.validate(invalid as any);
      expect(isValid).toBe(false);
    });

    it('should reject checkpoint without config', () => {
      const invalid = { ...mockState, config: undefined };
      const isValid = checkpointManager.validate(invalid as any);
      expect(isValid).toBe(false);
    });

    it('should reject checkpoint with invalid structure', () => {
      const invalid = { random: 'data' };
      const isValid = checkpointManager.validate(invalid as any);
      expect(isValid).toBe(false);
    });

    it('should validate checkpoint with empty arrays', () => {
      mockState.builds = [];
      mockState.completedBattles = [];
      
      const isValid = checkpointManager.validate(mockState);
      expect(isValid).toBe(true);
    });
  });

  describe('Checkpoint Existence', () => {
    it('should detect existing checkpoint', async () => {
      await checkpointManager.save(mockState);
      const exists = await checkpointManager.exists();
      expect(exists).toBe(true);
    });

    it('should return false when no checkpoint exists', async () => {
      const exists = await checkpointManager.exists();
      expect(exists).toBe(false);
    });
  });

  describe('Checkpoint Cleanup', () => {
    it('should delete checkpoint file', async () => {
      await checkpointManager.save(mockState);
      await checkpointManager.cleanup();

      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      expect(fs.existsSync(checkpointPath)).toBe(false);
    });

    it('should not throw if checkpoint does not exist', async () => {
      await expect(checkpointManager.cleanup()).resolves.not.toThrow();
    });
  });

  describe('Checkpoint Info', () => {
    it('should get checkpoint info', async () => {
      mockState.nextBattleIndex = 2000;
      await checkpointManager.save(mockState);

      const info = await checkpointManager.getInfo();

      expect(info).not.toBeNull();
      expect(info?.timestamp).toBe(mockState.timestamp);
      expect(info?.progress).toBeCloseTo((2000 / 4950) * 100, 1);
    });

    it('should return null if no checkpoint exists', async () => {
      const info = await checkpointManager.getInfo();
      expect(info).toBeNull();
    });

    it('should calculate progress correctly', async () => {
      mockState.nextBattleIndex = 2475; // 50% of 4950
      await checkpointManager.save(mockState);

      const info = await checkpointManager.getInfo();
      expect(info?.progress).toBeCloseTo(50, 1);
    });
  });

  describe('Old Checkpoint Cleanup', () => {
    it('should identify old checkpoints', async () => {
      // Create old checkpoint
      const oldState = { ...mockState };
      oldState.timestamp = Date.now() - (8 * 24 * 60 * 60 * 1000); // 8 days ago
      
      await checkpointManager.save(oldState);

      // Check if it's considered old (7 days threshold)
      const info = await checkpointManager.getInfo();
      const ageInDays = (Date.now() - info!.timestamp) / (24 * 60 * 60 * 1000);
      
      expect(ageInDays).toBeGreaterThan(7);
    });

    it('should clean up old checkpoints', async () => {
      // Create old checkpoint
      const oldState = { ...mockState };
      oldState.timestamp = Date.now() - (8 * 24 * 60 * 60 * 1000);
      
      await checkpointManager.save(oldState);

      // Clean up checkpoints older than 7 days
      await checkpointManager.cleanupOldCheckpoints(7);

      const exists = await checkpointManager.exists();
      expect(exists).toBe(false);
    });

    it('should not delete recent checkpoints', async () => {
      await checkpointManager.save(mockState);

      // Clean up checkpoints older than 7 days
      await checkpointManager.cleanupOldCheckpoints(7);

      const exists = await checkpointManager.exists();
      expect(exists).toBe(true);
    });
  });

  describe('Recovery Scenarios', () => {
    it('should recover from 50% completion', async () => {
      mockState.nextBattleIndex = 2475; // 50%
      mockState.completedBattles = Array.from({ length: 2475 }, (_, i) => ({
        build1Index: i % 100,
        build2Index: (i + 1) % 100,
        winner: 'build1' as const,
      }));

      await checkpointManager.save(mockState);
      const loaded = await checkpointManager.load();

      expect(loaded?.nextBattleIndex).toBe(2475);
      expect(loaded?.completedBattles).toHaveLength(2475);
    });

    it('should recover from near completion', async () => {
      mockState.nextBattleIndex = 4900; // 99%
      await checkpointManager.save(mockState);
      
      const loaded = await checkpointManager.load();
      const progress = (loaded!.nextBattleIndex / loaded!.totalBattles) * 100;

      expect(progress).toBeGreaterThan(98);
    });

    it('should recover from early stage', async () => {
      mockState.nextBattleIndex = 100; // ~2%
      await checkpointManager.save(mockState);
      
      const loaded = await checkpointManager.load();
      expect(loaded?.nextBattleIndex).toBe(100);
    });
  });

  describe('Atomic Writes', () => {
    it('should use atomic write pattern', async () => {
      // Checkpoint should be written to temp file first, then renamed
      // This prevents corruption if write is interrupted
      
      await checkpointManager.save(mockState);
      
      const checkpointPath = path.join(testOutputDir, '.checkpoint.json');
      const tempPath = path.join(testOutputDir, '.checkpoint.json.tmp');
      
      // Temp file should not exist after successful write
      expect(fs.existsSync(checkpointPath)).toBe(true);
      expect(fs.existsSync(tempPath)).toBe(false);
    });
  });

  describe('Performance', () => {
    it('should save checkpoint quickly', async () => {
      const startTime = Date.now();
      await checkpointManager.save(mockState);
      const endTime = Date.now();

      const saveTime = endTime - startTime;
      expect(saveTime).toBeLessThan(1000); // Should take less than 1 second
    });

    it('should load checkpoint quickly', async () => {
      await checkpointManager.save(mockState);

      const startTime = Date.now();
      await checkpointManager.load();
      const endTime = Date.now();

      const loadTime = endTime - startTime;
      expect(loadTime).toBeLessThan(1000); // Should take less than 1 second
    });
  });
});
