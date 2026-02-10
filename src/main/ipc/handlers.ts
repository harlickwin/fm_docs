/**
 * IPC Handlers
 * Handles communication between main and renderer processes
 */

import { ipcMain, dialog, BrowserWindow } from 'electron';
import * as fs from 'fs';
import * as path from 'path';
import { TournamentCoordinator } from '../tournament/coordinator';
import { CheckpointManager } from '../tournament/checkpoint';
import { TournamentConfig, BuildStats, IPC_CHANNELS, ConfigPreset, TournamentResult } from '../../shared/types';
import { generateBuilds } from '../tournament/build-generator';
import { getSystemInfo } from '../utils/system';
import { PresetManager } from '../utils/preset-manager';
import { ConfigManager } from '../utils/config-manager';

let coordinator: TournamentCoordinator | null = null;
let mainWindow: BrowserWindow | null = null;
const presetManager = new PresetManager();
const configManager = new ConfigManager();

/**
 * Write tournament results to files
 */
async function writeResultsToFiles(outputDirectory: string, results: TournamentResult[], config: TournamentConfig): Promise<void> {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  
  // Sort results by win rate
  const sortedResults = [...results].sort((a, b) => b.winRate - a.winRate);
  
  // 1. Write JSON results file
  const jsonFile = path.join(outputDirectory, `tournament-results-${timestamp}.json`);
  const jsonData = {
    generatedAt: new Date().toISOString(),
    config,
    totalBuilds: results.length,
    results: sortedResults
  };
  await fs.promises.writeFile(jsonFile, JSON.stringify(jsonData, null, 2));
  
  // 2. Write text summary file
  const textFile = path.join(outputDirectory, `tournament-summary-${timestamp}.txt`);
  let textOutput = `Tournament Results\n`;
  textOutput += `Generated: ${new Date().toISOString()}\n`;
  textOutput += `Total Builds: ${results.length}\n\n`;
  textOutput += `Top 10 Builds:\n`;
  textOutput += `${'='.repeat(80)}\n\n`;
  
  sortedResults.slice(0, 10).forEach((result, index) => {
    textOutput += `${index + 1}. Win Rate: ${result.winRate.toFixed(2)}%\n`;
    textOutput += `   Wins: ${result.wins} | Losses: ${result.losses} | Draws: ${result.draws}\n`;
    textOutput += `   Weapon: ${result.build.weaponType}\n`;
    textOutput += `   Stats: ${JSON.stringify(result.build.substats)}\n\n`;
  });
  
  await fs.promises.writeFile(textFile, textOutput);
  
  // 3. Write HTML report
  const htmlFile = path.join(outputDirectory, `tournament-report-${timestamp}.html`);
  const html = generateHTMLReport(sortedResults, config);
  await fs.promises.writeFile(htmlFile, html);
  
  console.log(`Results written to ${outputDirectory}:`);
  console.log(`  - ${path.basename(jsonFile)}`);
  console.log(`  - ${path.basename(textFile)}`);
  console.log(`  - ${path.basename(htmlFile)}`);
}

/**
 * Generate HTML report
 */
function generateHTMLReport(results: TournamentResult[], config: TournamentConfig): string {
  const topBuilds = results.slice(0, 20);
  
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tournament Pro Results</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: #333;
    }
    .container {
      background: white;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    h1 {
      color: #667eea;
      margin-bottom: 10px;
    }
    .meta {
      color: #666;
      margin-bottom: 30px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    th, td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #eee;
    }
    th {
      background: #f8f9fa;
      font-weight: 600;
      color: #667eea;
    }
    tr:hover {
      background: #f8f9fa;
    }
    .win-rate {
      font-weight: bold;
      color: #10b981;
    }
    .weapon {
      display: inline-block;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
    }
    .weapon-melee {
      background: #fef3c7;
      color: #92400e;
    }
    .weapon-ranged {
      background: #dbeafe;
      color: #1e40af;
    }
    .stats {
      font-size: 12px;
      color: #666;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🏆 Tournament Pro Results</h1>
    <div class="meta">
      <p>Generated: ${new Date().toISOString()}</p>
      <p>Total Builds: ${results.length} | Target Builds: ${config.targetBuilds}</p>
    </div>
    
    <h2>Top 20 Builds</h2>
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Win Rate</th>
          <th>W/L/D</th>
          <th>Weapon</th>
          <th>Key Stats</th>
        </tr>
      </thead>
      <tbody>
        ${topBuilds.map((result, index) => `
          <tr>
            <td>${index + 1}</td>
            <td class="win-rate">${result.winRate.toFixed(2)}%</td>
            <td>${result.wins}/${result.losses}/${result.draws}</td>
            <td><span class="weapon weapon-${result.build.weaponType}">${result.build.weaponType}</span></td>
            <td class="stats">${formatStats(result.build.substats)}</td>
          </tr>
        `).join('')}
      </tbody>
    </table>
  </div>
</body>
</html>`;
}

/**
 * Format substats for display
 */
function formatStats(substats: any): string {
  const entries = Object.entries(substats)
    .filter(([_, value]) => value && value !== 0)
    .slice(0, 5);
  return entries.map(([key, value]) => `${key}: ${value}`).join(', ');
}

/**
 * Set the main window reference
 */
export function setMainWindow(window: BrowserWindow): void {
  mainWindow = window;
}

/**
 * Register all IPC handlers
 */
export function registerIpcHandlers(): void {
  // Tournament start
  ipcMain.handle(IPC_CHANNELS.TOURNAMENT_START, async (event, config: TournamentConfig) => {
    try {
      if (coordinator) {
        throw new Error('Tournament is already running');
      }
      
      // Create coordinator
      coordinator = new TournamentCoordinator(config);
      
      // Set up event listeners
      coordinator.on('progress', (progress) => {
        mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_PROGRESS, progress);
      });
      
      coordinator.on('complete', async (results: TournamentResult[]) => {
        // Write results to files
        try {
          await writeResultsToFiles(config.outputDirectory, results, config);
        } catch (error) {
          console.error('Error writing results:', error);
          mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_ERROR, `Results saved but file writing failed: ${(error as Error).message}`);
        }
        
        mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_COMPLETE, results);
        coordinator = null;
      });
      
      coordinator.on('error', (error) => {
        mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_ERROR, error.message);
        coordinator = null;
      });
      
      coordinator.on('cancelled', () => {
        coordinator = null;
      });
      
      // Generate builds
      const builds = await generateBuilds(config);
      
      // Start tournament
      await coordinator.start(builds);
      
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Tournament pause
  ipcMain.handle(IPC_CHANNELS.TOURNAMENT_PAUSE, async () => {
    try {
      if (!coordinator) {
        throw new Error('No tournament is running');
      }
      
      await coordinator.pause();
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Tournament resume
  ipcMain.handle(IPC_CHANNELS.TOURNAMENT_RESUME, async () => {
    try {
      if (!coordinator) {
        throw new Error('No tournament is running');
      }
      
      coordinator.resumeFromPause();
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Tournament cancel
  ipcMain.handle(IPC_CHANNELS.TOURNAMENT_CANCEL, async () => {
    try {
      if (!coordinator) {
        throw new Error('No tournament is running');
      }
      
      await coordinator.cancel();
      coordinator = null;
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Checkpoint resume
  ipcMain.handle(IPC_CHANNELS.CHECKPOINT_RESUME, async (event, config: TournamentConfig) => {
    try {
      if (coordinator) {
        throw new Error('Tournament is already running');
      }
      
      // Create coordinator
      coordinator = new TournamentCoordinator(config);
      
      // Set up event listeners
      coordinator.on('progress', (progress) => {
        mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_PROGRESS, progress);
      });
      
      coordinator.on('complete', async (results: TournamentResult[]) => {
        // Write results to files
        try {
          await writeResultsToFiles(config.outputDirectory, results, config);
        } catch (error) {
          console.error('Error writing results:', error);
          mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_ERROR, `Results saved but file writing failed: ${(error as Error).message}`);
        }
        
        mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_COMPLETE, results);
        coordinator = null;
      });
      
      coordinator.on('error', (error) => {
        mainWindow?.webContents.send(IPC_CHANNELS.TOURNAMENT_ERROR, error.message);
        coordinator = null;
      });
      
      coordinator.on('cancelled', () => {
        coordinator = null;
      });
      
      // Resume from checkpoint
      await coordinator.resume();
      
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Checkpoint discard
  ipcMain.handle(IPC_CHANNELS.CHECKPOINT_DISCARD, async (event, outputDirectory: string) => {
    try {
      const checkpointManager = new CheckpointManager(outputDirectory);
      await checkpointManager.cleanup();
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Manual checkpoint cleanup
  ipcMain.handle(IPC_CHANNELS.CHECKPOINT_CLEANUP, async (event, outputDirectory: string) => {
    try {
      const checkpointManager = new CheckpointManager(outputDirectory);
      await checkpointManager.cleanup();
      return { success: true, message: 'All checkpoints cleaned up successfully' };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Age-based checkpoint cleanup
  ipcMain.handle(IPC_CHANNELS.CHECKPOINT_CLEANUP_OLD, async (event, outputDirectory: string, maxAgeDays?: number) => {
    try {
      const checkpointManager = new CheckpointManager(outputDirectory);
      await checkpointManager.cleanupOldCheckpoints(maxAgeDays);
      return { success: true, message: `Old checkpoints cleaned up (older than ${maxAgeDays || 7} days)` };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Select directory
  ipcMain.handle(IPC_CHANNELS.SELECT_DIRECTORY, async () => {
    try {
      const result = await dialog.showOpenDialog({
        properties: ['openDirectory', 'createDirectory']
      });
      
      if (result.canceled) {
        return { success: false, cancelled: true };
      }
      
      return { success: true, path: result.filePaths[0] };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Config save
  ipcMain.handle(IPC_CHANNELS.CONFIG_SAVE, async (event, config: TournamentConfig) => {
    try {
      await configManager.save(config);
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Config load
  ipcMain.handle(IPC_CHANNELS.CONFIG_LOAD, async () => {
    try {
      const config = await configManager.load();
      return { success: true, config };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Get system info
  ipcMain.handle(IPC_CHANNELS.SYSTEM_INFO, async () => {
    try {
      const systemInfo = getSystemInfo();
      return { success: true, systemInfo };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Check for checkpoint in specific directory
  ipcMain.handle(IPC_CHANNELS.CHECKPOINT_CHECK, async (event, outputDirectory: string) => {
    try {
      const checkpointManager = new CheckpointManager(outputDirectory);
      const exists = await checkpointManager.exists();
      
      if (!exists) {
        return { success: true, exists: false };
      }
      
      // Load and validate checkpoint
      const state = await checkpointManager.load();
      
      if (!state || !checkpointManager.validate(state)) {
        return { 
          success: true, 
          exists: true, 
          valid: false,
          error: 'Checkpoint file is corrupted or invalid'
        };
      }
      
      // Get checkpoint info
      const info = await checkpointManager.getInfo();
      
      return {
        success: true,
        exists: true,
        valid: true,
        timestamp: info?.timestamp,
        progress: info?.progress,
        config: state.config
      };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });

  // Preset save
  ipcMain.handle(IPC_CHANNELS.PRESET_SAVE, async (event, preset: ConfigPreset) => {
    try {
      await presetManager.save(preset);
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });

  // Preset load
  ipcMain.handle(IPC_CHANNELS.PRESET_LOAD, async (event, id: string) => {
    try {
      const preset = await presetManager.load(id);
      if (!preset) {
        return { success: false, error: 'Preset not found' };
      }
      return { success: true, preset };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });

  // Preset list
  ipcMain.handle(IPC_CHANNELS.PRESET_LIST, async () => {
    try {
      const userPresets = await presetManager.list();
      const builtInPresets = presetManager.getBuiltInPresets();
      return { 
        success: true, 
        presets: [...builtInPresets, ...userPresets] 
      };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });

  // Preset delete
  ipcMain.handle(IPC_CHANNELS.PRESET_DELETE, async (event, id: string) => {
    try {
      await presetManager.delete(id);
      return { success: true };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
  
  // Get first-run info
  ipcMain.handle('app:first-run-info', async () => {
    try {
      const { isFirstRun, getApplicationPaths } = require('../utils/first-run');
      const info = getApplicationPaths();
      return { 
        success: true, 
        isFirstRun: isFirstRun(),
        ...info
      };
    } catch (error) {
      return { success: false, error: (error as Error).message };
    }
  });
}

/**
 * Check for existing checkpoint on startup
 */
export async function checkForCheckpoint(outputDirectory: string): Promise<boolean> {
  const checkpointManager = new CheckpointManager(outputDirectory);
  return await checkpointManager.exists();
}

/**
 * Check for existing checkpoints on application startup
 * Scans common output directories for checkpoint files
 */
export async function checkForCheckpointOnStartup(window: BrowserWindow): Promise<void> {
  try {
    // Get user's home directory and common output locations
    const os = require('os');
    const fs = require('fs/promises');
    const path = require('path');
    
    const homeDir = os.homedir();
    const commonDirs = [
      path.join(homeDir, 'Documents', 'TournamentPro'),
      path.join(homeDir, 'TournamentPro'),
      path.join(process.cwd(), 'output'),
      path.join(process.cwd(), 'tournaments')
    ];
    
    // Check each directory for checkpoints
    for (const dir of commonDirs) {
      try {
        await fs.access(dir);
        const checkpointManager = new CheckpointManager(dir);
        
        // Perform age-based cleanup (default 7 days)
        await checkpointManager.cleanupOldCheckpoints(7);
        
        const exists = await checkpointManager.exists();
        
        if (exists) {
          // Validate checkpoint integrity
          const state = await checkpointManager.load();
          
          if (state && checkpointManager.validate(state)) {
            // Get checkpoint info
            const info = await checkpointManager.getInfo();
            
            if (info) {
              // Send checkpoint found event to renderer
              window.webContents.send(IPC_CHANNELS.CHECKPOINT_FOUND, {
                outputDirectory: dir,
                timestamp: info.timestamp,
                progress: info.progress,
                config: state.config
              });
              
              console.log(`Valid checkpoint found in ${dir}`);
              return; // Only notify about the first valid checkpoint found
            }
          } else {
            console.log(`Invalid or corrupted checkpoint found in ${dir}, ignoring`);
          }
        }
      } catch (error) {
        // Directory doesn't exist or can't be accessed, skip
        continue;
      }
    }
    
    console.log('No valid checkpoints found on startup');
  } catch (error) {
    console.error('Error checking for checkpoints on startup:', error);
  }
}
