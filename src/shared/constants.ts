/**
 * Shared constants for Tournament Pro
 */

import { SubstatType } from './types';

// Base stats (after mount bonuses applied)
export const BASE_DAMAGE = 3907700;
export const BASE_HEALTH = 20667000;
export const MOUNT_DAMAGE_BONUS = 242;
export const MOUNT_HEALTH_BONUS = 230;

// Battle configuration
export const BATTLE_DURATION = 60; // seconds
export const BATTLE_TIME_STEP = 0.1; // seconds

// Substat max values per item at 100%
export const SUBSTAT_MAX_PER_ITEM: Record<SubstatType, number> = {
  damage: 15,
  meleeDamage: 50,
  rangedDamage: 15,
  criticalChance: 12,
  criticalDamage: 100,
  attackSpeed: 40,
  doubleChance: 40,
  health: 15,
  healthRegen: 6,
  lifesteal: 20,
  blockChance: 5,
  skillCooldown: 7,
  skillDamage: 30
};

// Default substats for PvP optimization
export const DEFAULT_PVP_SUBSTATS: SubstatType[] = [
  'criticalChance',
  'criticalDamage',
  'attackSpeed',
  'doubleChance',
  'rangedDamage',
  'health',
  'healthRegen',
  'lifesteal'
];

// Checkpoint configuration
export const DEFAULT_CHECKPOINT_INTERVAL = 300; // 5 minutes in seconds
export const CHECKPOINT_VERSION = '1.0.0';

// Progress update throttling
export const PROGRESS_UPDATE_INTERVAL = 1000; // 1 second in milliseconds
