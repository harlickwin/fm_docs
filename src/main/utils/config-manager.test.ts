/**
 * Configuration Manager Tests
 */

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { ConfigManager } from './config-manager';
import { TournamentConfig } from '../../shared/types';
import * as fs from 'fs/promises';

// Mock electron app
vi.mock('electron', () => ({
  app: {
    getPath: vi.fn(() => '/mock/user/data'),
  },
}));

// Mock fs/promises
vi.mock('fs/promises');

describe('ConfigManager', () => {
  let configManager: ConfigManager;
  const mockConfig: TournamentConfig = {
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
      blockChance: true,
      skillCooldown: false,
      skillDamage: false,
    },
    weaponTypes: {
      ranged: true,
      melee: false,
    },
    substatMultiplier: 0.75,
    targetBuilds: 10000,
    outputDirectory: '/test/output',
    maxWorkers: 4,
    checkpointInterval: 300,
    includeMetaBuild: true,
    loadPreviousResults: false,
  };

  beforeEach(() => {
    configManager = new ConfigManager();
    vi.clearAllMocks();
  });

  describe('save', () => {
    it('should save configuration to file', async () => {
      vi.mocked(fs.writeFile).mockResolvedValue(undefined);

      await configManager.save(mockConfig);

      expect(fs.writeFile).toHaveBeenCalled();
      
      // Verify the call was made with correct arguments
      const calls = vi.mocked(fs.writeFile).mock.calls;
      expect(calls.length).toBe(1);
      expect(calls[0][0]).toContain('config.json');
      expect(calls[0][2]).toBe('utf-8');

      // Verify the saved content
      const savedContent = calls[0][1] as string;
      const savedConfig = JSON.parse(savedContent);
      expect(savedConfig.substats).toEqual(mockConfig.substats);
      expect(savedConfig.weaponTypes).toEqual(mockConfig.weaponTypes);
      expect(savedConfig.substatMultiplier).toBe(0.75);
      expect(savedConfig.targetBuilds).toBe(10000);
    });

    it('should throw error if save fails', async () => {
      vi.mocked(fs.writeFile).mockRejectedValue(new Error('Write failed'));

      await expect(configManager.save(mockConfig)).rejects.toThrow(
        'Failed to save configuration'
      );
    });
  });

  describe('load', () => {
    it('should load configuration from file', async () => {
      const savedConfig = {
        substats: mockConfig.substats,
        weaponTypes: mockConfig.weaponTypes,
        substatMultiplier: mockConfig.substatMultiplier,
        targetBuilds: mockConfig.targetBuilds,
        outputDirectory: mockConfig.outputDirectory,
        maxWorkers: mockConfig.maxWorkers,
        checkpointInterval: mockConfig.checkpointInterval,
        includeMetaBuild: mockConfig.includeMetaBuild,
        loadPreviousResults: mockConfig.loadPreviousResults,
      };

      vi.mocked(fs.readFile).mockResolvedValue(JSON.stringify(savedConfig));

      const result = await configManager.load();

      expect(result).toEqual(savedConfig);
      expect(fs.readFile).toHaveBeenCalled();
      
      // Verify the call was made with correct arguments
      const calls = vi.mocked(fs.readFile).mock.calls;
      expect(calls.length).toBe(1);
      expect(calls[0][0]).toContain('config.json');
      expect(calls[0][1]).toBe('utf-8');
    });

    it('should return null if file does not exist', async () => {
      const error: any = new Error('File not found');
      error.code = 'ENOENT';
      vi.mocked(fs.readFile).mockRejectedValue(error);

      const result = await configManager.load();

      expect(result).toBeNull();
    });

    it('should return null if configuration is invalid', async () => {
      vi.mocked(fs.readFile).mockResolvedValue(JSON.stringify({ invalid: 'config' }));

      const result = await configManager.load();

      expect(result).toBeNull();
    });

    it('should return null if JSON parsing fails', async () => {
      vi.mocked(fs.readFile).mockResolvedValue('invalid json');

      const result = await configManager.load();

      expect(result).toBeNull();
    });
  });

  describe('exists', () => {
    it('should return true if config file exists', async () => {
      vi.mocked(fs.access).mockResolvedValue(undefined);

      const result = await configManager.exists();

      expect(result).toBe(true);
      expect(fs.access).toHaveBeenCalled();
      
      // Verify the call was made with correct path
      const calls = vi.mocked(fs.access).mock.calls;
      expect(calls.length).toBe(1);
      expect(calls[0][0]).toContain('config.json');
    });

    it('should return false if config file does not exist', async () => {
      vi.mocked(fs.access).mockRejectedValue(new Error('File not found'));

      const result = await configManager.exists();

      expect(result).toBe(false);
    });
  });

  describe('delete', () => {
    it('should delete configuration file', async () => {
      vi.mocked(fs.unlink).mockResolvedValue(undefined);

      await configManager.delete();

      expect(fs.unlink).toHaveBeenCalled();
      
      // Verify the call was made with correct path
      const calls = vi.mocked(fs.unlink).mock.calls;
      expect(calls.length).toBe(1);
      expect(calls[0][0]).toContain('config.json');
    });

    it('should not throw if file does not exist', async () => {
      const error: any = new Error('File not found');
      error.code = 'ENOENT';
      vi.mocked(fs.unlink).mockRejectedValue(error);

      await expect(configManager.delete()).resolves.not.toThrow();
    });

    it('should throw for other errors', async () => {
      const error = new Error('Permission denied');
      vi.mocked(fs.unlink).mockRejectedValue(error);

      await expect(configManager.delete()).rejects.toThrow('Permission denied');
    });
  });

  describe('configuration validation', () => {
    it('should accept valid configuration', async () => {
      const validConfig = {
        substats: mockConfig.substats,
        weaponTypes: mockConfig.weaponTypes,
        substatMultiplier: 0.5,
        targetBuilds: 5000,
        outputDirectory: '/test',
        maxWorkers: 2,
        checkpointInterval: 300,
        includeMetaBuild: true,
        loadPreviousResults: false,
      };

      vi.mocked(fs.readFile).mockResolvedValue(JSON.stringify(validConfig));

      const result = await configManager.load();

      expect(result).not.toBeNull();
      expect(result?.substatMultiplier).toBe(0.5);
    });

    it('should reject configuration without substats', async () => {
      const invalidConfig = {
        weaponTypes: mockConfig.weaponTypes,
        substatMultiplier: 0.5,
        targetBuilds: 5000,
      };

      vi.mocked(fs.readFile).mockResolvedValue(JSON.stringify(invalidConfig));

      const result = await configManager.load();

      expect(result).toBeNull();
    });

    it('should reject configuration without weaponTypes', async () => {
      const invalidConfig = {
        substats: mockConfig.substats,
        substatMultiplier: 0.5,
        targetBuilds: 5000,
      };

      vi.mocked(fs.readFile).mockResolvedValue(JSON.stringify(invalidConfig));

      const result = await configManager.load();

      expect(result).toBeNull();
    });

    it('should reject configuration with invalid types', async () => {
      const invalidConfig = {
        substats: mockConfig.substats,
        weaponTypes: mockConfig.weaponTypes,
        substatMultiplier: 'invalid',
        targetBuilds: 'invalid',
      };

      vi.mocked(fs.readFile).mockResolvedValue(JSON.stringify(invalidConfig));

      const result = await configManager.load();

      expect(result).toBeNull();
    });
  });
});
