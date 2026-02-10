/**
 * Configuration Manager
 * Handles saving and loading of tournament configuration
 */

import * as fs from 'fs/promises';
import * as path from 'path';
import { app } from 'electron';
import { TournamentConfig } from '../../shared/types';

export class ConfigManager {
  private configPath: string;

  constructor() {
    const userDataPath = app.getPath('userData');
    this.configPath = path.join(userDataPath, 'config.json');
  }

  /**
   * Save configuration to file
   */
  async save(config: TournamentConfig): Promise<void> {
    try {
      // Create a copy without sensitive/runtime-specific fields
      const configToSave = {
        substats: config.substats,
        weaponTypes: config.weaponTypes,
        substatMultiplier: config.substatMultiplier,
        targetBuilds: config.targetBuilds,
        outputDirectory: config.outputDirectory,
        maxWorkers: config.maxWorkers,
        checkpointInterval: config.checkpointInterval,
        includeMetaBuild: config.includeMetaBuild,
        loadPreviousResults: config.loadPreviousResults,
      };

      await fs.writeFile(
        this.configPath,
        JSON.stringify(configToSave, null, 2),
        'utf-8'
      );
    } catch (error) {
      console.error('Failed to save configuration:', error);
      throw new Error(`Failed to save configuration: ${(error as Error).message}`);
    }
  }

  /**
   * Load configuration from file
   */
  async load(): Promise<TournamentConfig | null> {
    try {
      const data = await fs.readFile(this.configPath, 'utf-8');
      const config = JSON.parse(data) as TournamentConfig;
      
      // Validate that the loaded config has the required structure
      if (!this.isValidConfig(config)) {
        console.warn('Loaded configuration is invalid, returning null');
        return null;
      }

      return config;
    } catch (error) {
      // File doesn't exist or can't be read
      if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
        return null; // No saved config yet
      }
      
      console.error('Failed to load configuration:', error);
      return null;
    }
  }

  /**
   * Check if configuration file exists
   */
  async exists(): Promise<boolean> {
    try {
      await fs.access(this.configPath);
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Delete saved configuration
   */
  async delete(): Promise<void> {
    try {
      await fs.unlink(this.configPath);
    } catch (error) {
      // Ignore if file doesn't exist
      if ((error as NodeJS.ErrnoException).code !== 'ENOENT') {
        throw error;
      }
    }
  }

  /**
   * Validate configuration structure
   */
  private isValidConfig(config: any): config is TournamentConfig {
    return (
      config &&
      typeof config === 'object' &&
      config.substats &&
      typeof config.substats === 'object' &&
      config.weaponTypes &&
      typeof config.weaponTypes === 'object' &&
      typeof config.substatMultiplier === 'number' &&
      typeof config.targetBuilds === 'number'
    );
  }
}
