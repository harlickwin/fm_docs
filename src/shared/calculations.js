"use strict";
/**
 * Core calculation utilities for DPS and PvP battles
 * Copied from main project with minimal modifications
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.DOUBLE_ATTACK_DELAYS = exports.ATTACK_SPEED_TIERS = void 0;
exports.getAttackInterval = getAttackInterval;
exports.getEffectiveAttackRate = getEffectiveAttackRate;
exports.calculateEffectiveBaseDamage = calculateEffectiveBaseDamage;
exports.calculateDoubleMultiplier = calculateDoubleMultiplier;
exports.calculateCritMultiplier = calculateCritMultiplier;
exports.calculateDPS = calculateDPS;
exports.calculateHealingPerSecond = calculateHealingPerSecond;
// Attack speed tier system
exports.ATTACK_SPEED_TIERS = [
    { minPercent: 0, maxPercent: 25, attackInterval: 1.0 },
    { minPercent: 25, maxPercent: 50, attackInterval: 0.9 },
    { minPercent: 50, maxPercent: 75, attackInterval: 0.8 },
    { minPercent: 75, maxPercent: 100, attackInterval: 0.7 },
    { minPercent: 100, maxPercent: 125, attackInterval: 0.6 },
    { minPercent: 125, maxPercent: 150, attackInterval: 0.55 },
    { minPercent: 150, maxPercent: 175, attackInterval: 0.5 },
    { minPercent: 175, maxPercent: 200, attackInterval: 0.45 },
    { minPercent: 200, maxPercent: 225, attackInterval: 0.4 },
    { minPercent: 225, maxPercent: 250, attackInterval: 0.38 },
    { minPercent: 250, maxPercent: 275, attackInterval: 0.36 },
    { minPercent: 275, maxPercent: 300, attackInterval: 0.34 },
    { minPercent: 300, maxPercent: 325, attackInterval: 0.32 },
    { minPercent: 325, maxPercent: 350, attackInterval: 0.3 },
    { minPercent: 350, maxPercent: 375, attackInterval: 0.28 },
    { minPercent: 375, maxPercent: 400, attackInterval: 0.26 },
    { minPercent: 400, maxPercent: Infinity, attackInterval: 0.26 }
];
exports.DOUBLE_ATTACK_DELAYS = {
    NORMAL: 0.2,
    HIGH_ATTACK_SPEED: 0.1
};
function getAttackInterval(attackSpeedPercent) {
    const cappedAttackSpeed = Math.min(attackSpeedPercent, 400);
    for (const tier of exports.ATTACK_SPEED_TIERS) {
        if (cappedAttackSpeed >= tier.minPercent && cappedAttackSpeed < tier.maxPercent) {
            return tier.attackInterval;
        }
    }
    return exports.ATTACK_SPEED_TIERS[exports.ATTACK_SPEED_TIERS.length - 1].attackInterval;
}
function getEffectiveAttackRate(attackInterval, doubleChancePercent, meleeMovementDelay = 0) {
    const cappedDoubleChance = Math.min(doubleChancePercent, 100) / 100;
    const doubleDelay = attackInterval < 1.0
        ? exports.DOUBLE_ATTACK_DELAYS.HIGH_ATTACK_SPEED
        : exports.DOUBLE_ATTACK_DELAYS.NORMAL;
    const totalTimePerAttack = attackInterval + (cappedDoubleChance * doubleDelay) + meleeMovementDelay;
    return 1 / totalTimePerAttack;
}
function calculateEffectiveBaseDamage(baseDamage, substats, weaponType, mountDamageBonus = 0) {
    const generalDamage = (substats.damage || 0) / 100;
    const mountBonus = mountDamageBonus / 100;
    const baseDamageWithGeneralBonuses = baseDamage * (1 + mountBonus + generalDamage);
    const weaponSpecificDamage = weaponType === 'melee'
        ? (substats.meleeDamage || 0) / 100
        : (substats.rangedDamage || 0) / 100;
    return baseDamageWithGeneralBonuses * (1 + weaponSpecificDamage);
}
function calculateDoubleMultiplier(doubleChancePercent) {
    const cappedDoubleChance = Math.min(doubleChancePercent || 0, 100) / 100;
    return 1 + cappedDoubleChance;
}
function calculateCritMultiplier(critChancePercent, critDamagePercent) {
    const cappedCritChance = Math.min(critChancePercent || 0, 100) / 100;
    const critDamage = (critDamagePercent || 0) / 100;
    const critMultiplier = 1.2 + critDamage;
    return (cappedCritChance * critMultiplier) + (1 - cappedCritChance);
}
function calculateDPS(baseDamage, substats, weaponType, meleeMovementDelay = 2.2, mountDamageBonus = 0) {
    const effectiveBaseDamage = calculateEffectiveBaseDamage(baseDamage, substats, weaponType, mountDamageBonus);
    const doubleMultiplier = calculateDoubleMultiplier(substats.doubleChance || 0);
    const critMultiplier = calculateCritMultiplier(substats.criticalChance || 0, substats.criticalDamage || 0);
    const attackInterval = getAttackInterval(substats.attackSpeed || 0);
    const movementDelay = weaponType === 'melee' ? meleeMovementDelay : 0;
    const effectiveAttackRate = getEffectiveAttackRate(attackInterval, substats.doubleChance || 0, movementDelay);
    return effectiveBaseDamage * doubleMultiplier * critMultiplier * effectiveAttackRate;
}
function calculateHealingPerSecond(baseHealth, substats, dps, mountHealthBonus = 0) {
    const healthBonus = (substats.health || 0) / 100;
    const mountBonus = mountHealthBonus / 100;
    const maxHealth = baseHealth * (1 + mountBonus + healthBonus);
    const healthRegenPercent = (substats.healthRegen || 0) / 100;
    const healthRegenPerSecond = maxHealth * healthRegenPercent;
    const lifestealPercent = (substats.lifesteal || 0) / 100;
    const lifestealPerSecond = dps * lifestealPercent;
    return healthRegenPerSecond + lifestealPerSecond;
}
