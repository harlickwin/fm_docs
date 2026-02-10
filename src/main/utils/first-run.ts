/**
 * First-run detection and setup utilities
 */

import { app } from 'electron';
import * as fs from 'fs';
import * as path from 'path';

const FIRST_RUN_MARKER = '.tournament-pro-initialized';

export interface FirstRunInfo {
  isFirstRun: boolean;
  userDataPath: string;
  outputPath: string;
  configPath: string;
  checkpointsPath: string;
  presetsPath: string;
}

/**
 * Check if this is the first run of the application
 */
export function isFirstRun(): boolean {
  const userDataPath = app.getPath('userData');
  const markerPath = path.join(userDataPath, FIRST_RUN_MARKER);
  return !fs.existsSync(markerPath);
}

/**
 * Mark the application as initialized (no longer first run)
 */
export function markAsInitialized(): void {
  const userDataPath = app.getPath('userData');
  const markerPath = path.join(userDataPath, FIRST_RUN_MARKER);
  
  const initData = {
    initializedAt: new Date().toISOString(),
    version: app.getVersion(),
    platform: process.platform,
  };
  
  fs.writeFileSync(markerPath, JSON.stringify(initData, null, 2), 'utf-8');
}

/**
 * Create necessary directories for the application
 */
export function createDirectories(): FirstRunInfo {
  const userDataPath = app.getPath('userData');
  const documentsPath = app.getPath('documents');
  
  // Create main application directories
  const outputPath = path.join(documentsPath, 'TournamentPro', 'Results');
  const configPath = path.join(userDataPath, 'config');
  const checkpointsPath = path.join(userDataPath, 'checkpoints');
  const presetsPath = path.join(userDataPath, 'presets');
  
  // Ensure all directories exist
  const directories = [
    userDataPath,
    outputPath,
    configPath,
    checkpointsPath,
    presetsPath,
  ];
  
  for (const dir of directories) {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
  }
  
  return {
    isFirstRun: isFirstRun(),
    userDataPath,
    outputPath,
    configPath,
    checkpointsPath,
    presetsPath,
  };
}

/**
 * Initialize the application on first run
 */
export function initializeFirstRun(): FirstRunInfo {
  const info = createDirectories();
  
  // Create default configuration file if it doesn't exist
  const defaultConfigPath = path.join(info.configPath, 'default-config.json');
  if (!fs.existsSync(defaultConfigPath)) {
    const defaultConfig = {
      substats: {
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
        skillCooldown: false,
        skillDamage: false,
      },
      weaponTypes: {
        ranged: true,
        melee: true,
      },
      substatMultiplier: 1.0,
      targetBuilds: 1000,
      outputDirectory: info.outputPath,
      maxWorkers: Math.max(1, require('os').cpus().length - 1),
      checkpointInterval: 300,
      includeMetaBuild: true,
      loadPreviousResults: false,
    };
    
    fs.writeFileSync(defaultConfigPath, JSON.stringify(defaultConfig, null, 2), 'utf-8');
  }
  
  // Create README in output directory
  const readmePath = path.join(info.outputPath, 'README.txt');
  if (!fs.existsSync(readmePath)) {
    const readme = `Tournament Pro Results Directory
================================

This directory contains the results of your PvP build tournaments.

Each tournament creates a timestamped subdirectory with:
- results.json: Complete tournament results in JSON format
- results.html: Human-readable HTML report
- results.txt: Plain text summary

You can safely delete old tournament results to free up space.

For more information, visit the Help menu in Tournament Pro.
`;
    fs.writeFileSync(readmePath, readme, 'utf-8');
  }
  
  // Mark as initialized
  markAsInitialized();
  
  return info;
}

/**
 * Get application paths (creates directories if needed)
 */
export function getApplicationPaths(): FirstRunInfo {
  const info = createDirectories();
  return info;
}

/**
 * Reset first-run status (for testing or troubleshooting)
 */
export function resetFirstRun(): void {
  const userDataPath = app.getPath('userData');
  const markerPath = path.join(userDataPath, FIRST_RUN_MARKER);
  
  if (fs.existsSync(markerPath)) {
    fs.unlinkSync(markerPath);
  }
}
