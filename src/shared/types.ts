/**
 * Shared types between main and renderer processes
 */

export type SubstatType =
  | 'damage'
  | 'meleeDamage'
  | 'rangedDamage'
  | 'criticalChance'
  | 'criticalDamage'
  | 'attackSpeed'
  | 'doubleChance'
  | 'health'
  | 'healthRegen'
  | 'lifesteal'
  | 'blockChance'
  | 'skillCooldown'
  | 'skillDamage';

export type WeaponType = 'melee' | 'ranged';

export interface SubstatCollection {
  [key: string]: number | undefined;
  damage?: number;
  meleeDamage?: number;
  rangedDamage?: number;
  criticalChance?: number;
  criticalDamage?: number;
  attackSpeed?: number;
  doubleChance?: number;
  health?: number;
  healthRegen?: number;
  lifesteal?: number;
  blockChance?: number;
  skillCooldown?: number;
  skillDamage?: number;
}

export interface BuildStats {
  substats: SubstatCollection;
  dps: number;
  hps: number;
  maxHP: number;
  weaponType: WeaponType;
  description: string;
  slotAllocation: string;
}

export interface TournamentResult {
  build: BuildStats;
  wins: number;
  losses: number;
  draws: number;
  winRate: number;
  avgBattleDuration: number;
  totalDamageDealt: number;
}

export interface TournamentConfig {
  substats: {
    [key in SubstatType]: boolean;
  };
  weaponTypes: {
    ranged: boolean;
    melee: boolean;
  };
  substatMultiplier: number; // 0.01 to 1.0
  targetBuilds: number;
  outputDirectory: string;
  maxWorkers: number;
  checkpointInterval: number; // seconds
  includeMetaBuild: boolean;
  loadPreviousResults: boolean;
  previousResultsFile?: string;
}

export interface TournamentProgress {
  totalBattles: number;
  completedBattles: number;
  progress: number; // 0-100
  speed: number; // battles per second
  elapsed: number; // seconds
  remaining: number; // seconds
  workerStatus: WorkerStatus[];
}

export interface WorkerStatus {
  id: number;
  status: 'idle' | 'running' | 'completed' | 'error';
  completedBattles: number;
  speed: number;
}

export interface CompletedBattle {
  build1Index: number;
  build2Index: number;
  winner: 'build1' | 'build2' | 'draw';
}

export interface TournamentState {
  version: string;
  timestamp: number;
  config: TournamentConfig;
  builds: BuildStats[];
  completedBattles: CompletedBattle[];
  results: Record<string, TournamentResult>;
  nextBattleIndex: number;
  totalBattles: number;
}

export interface BattleAssignment {
  build1Index: number;
  build2Index: number;
  battleId: string;
}

export interface SystemInfo {
  totalCores: number;
  recommendedWorkers: number;
  cpuModel: string;
}

export interface ConfigPreset {
  id: string;
  name: string;
  description: string;
  config: Partial<TournamentConfig>;
}

export interface ValidationError {
  field: string;
  message: string;
  severity: 'error' | 'warning';
}

export interface RuntimeEstimate {
  totalBattles: number;
  estimatedSeconds: number;
  estimatedMinutes: number;
  estimatedHours: number;
  formattedTime: string;
  battlesPerSecond: number;
  confidence: 'low' | 'medium' | 'high';
}

// IPC Channel names
export const IPC_CHANNELS = {
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
