/**
 * Preload Script
 * Exposes safe IPC methods to renderer process
 */

import { contextBridge, ipcRenderer } from 'electron';

// Inline types and constants to avoid module resolution issues in packaged app
interface TournamentConfig {
  substats: { [key: string]: boolean };
  weaponTypes: { ranged: boolean; melee: boolean };
  substatMultiplier: number;
  targetBuilds: number;
  outputDirectory: string;
  maxWorkers: number;
  checkpointInterval: number;
  includeMetaBuild: boolean;
  loadPreviousResults: boolean;
  previousResultsFile?: string;
}

interface TournamentProgress {
  totalBattles: number;
  completedBattles: number;
  progress: number;
  speed: number;
  elapsed: number;
  remaining: number;
  workerStatus: any[];
}

interface TournamentResult {
  build: any;
  wins: number;
  losses: number;
  draws: number;
  winRate: number;
  avgBattleDuration: number;
  totalDamageDealt: number;
}

interface SystemInfo {
  cpuCount: number;
  totalMemory: number;
  freeMemory: number;
  platform: string;
  arch: string;
}

const IPC_CHANNELS = {
  TOURNAMENT_START: 'tournament:start',
  TOURNAMENT_PAUSE: 'tournament:pause',
  TOURNAMENT_RESUME: 'tournament:resume',
  TOURNAMENT_CANCEL: 'tournament:cancel',
  TOURNAMENT_PROGRESS: 'tournament:progress',
  TOURNAMENT_COMPLETE: 'tournament:complete',
  TOURNAMENT_ERROR: 'tournament:error',
  CHECKPOINT_FOUND: 'checkpoint:found',
  CHECKPOINT_CHECK: 'checkpoint:check',
  CHECKPOINT_RESUME: 'checkpoint:resume',
  CHECKPOINT_DISCARD: 'checkpoint:discard',
  CHECKPOINT_CLEANUP: 'checkpoint:cleanup',
  CHECKPOINT_CLEANUP_OLD: 'checkpoint:cleanup-old',
  CONFIG_SAVE: 'config:save',
  CONFIG_LOAD: 'config:load',
  PRESET_SAVE: 'preset:save',
  PRESET_LOAD: 'preset:load',
  PRESET_LIST: 'preset:list',
  PRESET_DELETE: 'preset:delete',
  SELECT_DIRECTORY: 'select:directory',
  SYSTEM_INFO: 'system:info',
} as const;

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('tournamentAPI', {
  // Tournament control
  startTournament: (config: TournamentConfig) => 
    ipcRenderer.invoke(IPC_CHANNELS.TOURNAMENT_START, config),
  
  pauseTournament: () => 
    ipcRenderer.invoke(IPC_CHANNELS.TOURNAMENT_PAUSE),
  
  resumeTournament: () => 
    ipcRenderer.invoke(IPC_CHANNELS.TOURNAMENT_RESUME),
  
  cancelTournament: () => 
    ipcRenderer.invoke(IPC_CHANNELS.TOURNAMENT_CANCEL),
  
  // Checkpoint control
  resumeFromCheckpoint: (config: TournamentConfig) => 
    ipcRenderer.invoke(IPC_CHANNELS.CHECKPOINT_RESUME, config),
  
  discardCheckpoint: (outputDirectory: string) => 
    ipcRenderer.invoke(IPC_CHANNELS.CHECKPOINT_DISCARD, outputDirectory),
  
  checkForCheckpoint: (outputDirectory: string) =>
    ipcRenderer.invoke(IPC_CHANNELS.CHECKPOINT_CHECK, outputDirectory),
  
  cleanupCheckpoints: (outputDirectory: string) =>
    ipcRenderer.invoke(IPC_CHANNELS.CHECKPOINT_CLEANUP, outputDirectory),
  
  cleanupOldCheckpoints: (outputDirectory: string, maxAgeDays?: number) =>
    ipcRenderer.invoke(IPC_CHANNELS.CHECKPOINT_CLEANUP_OLD, outputDirectory, maxAgeDays),
  
  // File system
  selectDirectory: () => 
    ipcRenderer.invoke(IPC_CHANNELS.SELECT_DIRECTORY),
  
  // Configuration
  saveConfig: (config: TournamentConfig) => 
    ipcRenderer.invoke(IPC_CHANNELS.CONFIG_SAVE, config),
  
  loadConfig: () => 
    ipcRenderer.invoke(IPC_CHANNELS.CONFIG_LOAD),
  
  // Presets
  savePreset: (preset: any) =>
    ipcRenderer.invoke(IPC_CHANNELS.PRESET_SAVE, preset),
  
  loadPreset: (id: string) =>
    ipcRenderer.invoke(IPC_CHANNELS.PRESET_LOAD, id),
  
  listPresets: () =>
    ipcRenderer.invoke(IPC_CHANNELS.PRESET_LIST),
  
  deletePreset: (id: string) =>
    ipcRenderer.invoke(IPC_CHANNELS.PRESET_DELETE, id),
  
  // System info
  getSystemInfo: () => 
    ipcRenderer.invoke(IPC_CHANNELS.SYSTEM_INFO),
  
  // Event listeners
  onProgress: (callback: (progress: TournamentProgress) => void) => {
    const listener = (_event: any, progress: TournamentProgress) => callback(progress);
    ipcRenderer.on(IPC_CHANNELS.TOURNAMENT_PROGRESS, listener);
    return () => ipcRenderer.removeListener(IPC_CHANNELS.TOURNAMENT_PROGRESS, listener);
  },
  
  onComplete: (callback: (results: TournamentResult[]) => void) => {
    const listener = (_event: any, results: TournamentResult[]) => callback(results);
    ipcRenderer.on(IPC_CHANNELS.TOURNAMENT_COMPLETE, listener);
    return () => ipcRenderer.removeListener(IPC_CHANNELS.TOURNAMENT_COMPLETE, listener);
  },
  
  onError: (callback: (error: string) => void) => {
    const listener = (_event: any, error: string) => callback(error);
    ipcRenderer.on(IPC_CHANNELS.TOURNAMENT_ERROR, listener);
    return () => ipcRenderer.removeListener(IPC_CHANNELS.TOURNAMENT_ERROR, listener);
  },
  
  onCheckpointFound: (callback: (info: any) => void) => {
    const listener = (_event: any, info: any) => callback(info);
    ipcRenderer.on(IPC_CHANNELS.CHECKPOINT_FOUND, listener);
    return () => ipcRenderer.removeListener(IPC_CHANNELS.CHECKPOINT_FOUND, listener);
  }
});

// Type declaration for TypeScript
declare global {
  interface Window {
    tournamentAPI: {
      startTournament: (config: TournamentConfig) => Promise<{ success: boolean; error?: string }>;
      pauseTournament: () => Promise<{ success: boolean; error?: string }>;
      resumeTournament: () => Promise<{ success: boolean; error?: string }>;
      cancelTournament: () => Promise<{ success: boolean; error?: string }>;
      resumeFromCheckpoint: (config: TournamentConfig) => Promise<{ success: boolean; error?: string }>;
      discardCheckpoint: (outputDirectory: string) => Promise<{ success: boolean; error?: string }>;
      checkForCheckpoint: (outputDirectory: string) => Promise<{ 
        success: boolean; 
        exists?: boolean; 
        valid?: boolean;
        timestamp?: number;
        progress?: number;
        config?: TournamentConfig;
        error?: string;
      }>;
      cleanupCheckpoints: (outputDirectory: string) => Promise<{ success: boolean; message?: string; error?: string }>;
      cleanupOldCheckpoints: (outputDirectory: string, maxAgeDays?: number) => Promise<{ success: boolean; message?: string; error?: string }>;
      selectDirectory: () => Promise<{ success: boolean; path?: string; cancelled?: boolean; error?: string }>;
      saveConfig: (config: TournamentConfig) => Promise<{ success: boolean; error?: string }>;
      loadConfig: () => Promise<{ success: boolean; config?: TournamentConfig; error?: string }>;
      savePreset: (preset: any) => Promise<{ success: boolean; error?: string }>;
      loadPreset: (id: string) => Promise<{ success: boolean; preset?: any; error?: string }>;
      listPresets: () => Promise<{ success: boolean; presets?: any[]; error?: string }>;
      deletePreset: (id: string) => Promise<{ success: boolean; error?: string }>;
      getSystemInfo: () => Promise<{ success: boolean; systemInfo?: SystemInfo; error?: string }>;
      onProgress: (callback: (progress: TournamentProgress) => void) => () => void;
      onComplete: (callback: (results: TournamentResult[]) => void) => () => void;
      onError: (callback: (error: string) => void) => () => void;
      onCheckpointFound: (callback: (info: any) => void) => () => void;
    };
  }
}
