"use strict";
/**
 * Shared constants for Tournament Pro
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.PROGRESS_UPDATE_INTERVAL = exports.CHECKPOINT_VERSION = exports.DEFAULT_CHECKPOINT_INTERVAL = exports.DEFAULT_PVP_SUBSTATS = exports.SUBSTAT_MAX_PER_ITEM = exports.BATTLE_TIME_STEP = exports.BATTLE_DURATION = exports.MOUNT_HEALTH_BONUS = exports.MOUNT_DAMAGE_BONUS = exports.BASE_HEALTH = exports.BASE_DAMAGE = void 0;
// Base stats (after mount bonuses applied)
exports.BASE_DAMAGE = 3907700;
exports.BASE_HEALTH = 20667000;
exports.MOUNT_DAMAGE_BONUS = 242;
exports.MOUNT_HEALTH_BONUS = 230;
// Battle configuration
exports.BATTLE_DURATION = 60; // seconds
exports.BATTLE_TIME_STEP = 0.1; // seconds
// Substat max values per item at 100%
exports.SUBSTAT_MAX_PER_ITEM = {
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
exports.DEFAULT_PVP_SUBSTATS = [
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
exports.DEFAULT_CHECKPOINT_INTERVAL = 300; // 5 minutes in seconds
exports.CHECKPOINT_VERSION = '1.0.0';
// Progress update throttling
exports.PROGRESS_UPDATE_INTERVAL = 1000; // 1 second in milliseconds
