/**
 * Core calculation utilities for DPS and PvP battles
 * Copied from main project with minimal modifications
 */

import { SubstatCollection, WeaponType } from './types';

// Attack speed tier system (exact values from game table)
export const ATTACK_SPEED_TIERS = [
  { minPercent: 0, maxPercent: 7.1, attackInterval: 1.7 },      // = 0%
  { minPercent: 7.1, maxPercent: 15.4, attackInterval: 1.6 },   // < 7.1%
  { minPercent: 15.4, maxPercent: 25.0, attackInterval: 1.5 },  // < 15.4%
  { minPercent: 25.0, maxPercent: 36.4, attackInterval: 1.4 },  // <= 25.0%
  { minPercent: 36.4, maxPercent: 50.0, attackInterval: 1.3 },  // < 36.4%
  { minPercent: 50.0, maxPercent: 66.7, attackInterval: 1.2 },  // <= 50.0%
  { minPercent: 66.7, maxPercent: 87.5, attackInterval: 1.1 },  // < 66.7%
  { minPercent: 87.5, maxPercent: 114, attackInterval: 1.0 },   // <= 87.5%
  { minPercent: 114, maxPercent: 150, attackInterval: 0.9 },    // < 114%
  { minPercent: 150, maxPercent: 200, attackInterval: 0.8 },    // <= 150%
  { minPercent: 200, maxPercent: 275, attackInterval: 0.7 },    // <= 200%
  { minPercent: 275, maxPercent: 400, attackInterval: 0.6 },    // <= 275%
  { minPercent: 400, maxPercent: Infinity, attackInterval: 0.5 } // <= 400%
];

export const DOUBLE_ATTACK_DELAYS = {
  NORMAL: 0.2,
  HIGH_ATTACK_SPEED: 0.1
};

export function getAttackInterval(attackSpeedPercent: number): number {
  // Handle > 400% case (0.4s interval)
  if (attackSpeedPercent > 400) {
    return 0.4;
  }
  
  // Find the matching tier
  for (const tier of ATTACK_SPEED_TIERS) {
    if (attackSpeedPercent >= tier.minPercent && attackSpeedPercent < tier.maxPercent) {
      return tier.attackInterval;
    }
  }
  
  // Fallback to base interval (should never reach here)
  return 1.7;
}

export function getEffectiveAttackRate(
  attackInterval: number,
  doubleChancePercent: number,
  meleeMovementDelay: number = 0
): number {
  const cappedDoubleChance = Math.min(doubleChancePercent, 100) / 100;
  const doubleDelay = attackInterval < 1.0
    ? DOUBLE_ATTACK_DELAYS.HIGH_ATTACK_SPEED
    : DOUBLE_ATTACK_DELAYS.NORMAL;
  
  const totalTimePerAttack = attackInterval + (cappedDoubleChance * doubleDelay) + meleeMovementDelay;
  return 1 / totalTimePerAttack;
}

export function calculateEffectiveBaseDamage(
  baseDamage: number,
  substats: SubstatCollection,
  weaponType: WeaponType,
  mountDamageBonus: number = 0
): number {
  const generalDamage = (substats.damage || 0) / 100;
  const mountBonus = mountDamageBonus / 100;
  const baseDamageWithGeneralBonuses = baseDamage * (1 + mountBonus + generalDamage);
  
  const weaponSpecificDamage = weaponType === 'melee'
    ? (substats.meleeDamage || 0) / 100
    : (substats.rangedDamage || 0) / 100;
  
  return baseDamageWithGeneralBonuses * (1 + weaponSpecificDamage);
}

export function calculateDoubleMultiplier(doubleChancePercent: number): number {
  const cappedDoubleChance = Math.min(doubleChancePercent || 0, 100) / 100;
  return 1 + cappedDoubleChance;
}

export function calculateCritMultiplier(
  critChancePercent: number,
  critDamagePercent: number
): number {
  const cappedCritChance = Math.min(critChancePercent || 0, 100) / 100;
  const critDamage = (critDamagePercent || 0) / 100;
  const critMultiplier = 1.2 + critDamage;
  return (cappedCritChance * critMultiplier) + (1 - cappedCritChance);
}

export function calculateDPS(
  baseDamage: number,
  substats: SubstatCollection,
  weaponType: WeaponType,
  meleeMovementDelay: number = 2.2,
  mountDamageBonus: number = 0
): number {
  const effectiveBaseDamage = calculateEffectiveBaseDamage(baseDamage, substats, weaponType, mountDamageBonus);
  const doubleMultiplier = calculateDoubleMultiplier(substats.doubleChance || 0);
  const critMultiplier = calculateCritMultiplier(
    substats.criticalChance || 0,
    substats.criticalDamage || 0
  );
  
  const attackInterval = getAttackInterval(substats.attackSpeed || 0);
  const movementDelay = weaponType === 'melee' ? meleeMovementDelay : 0;
  const effectiveAttackRate = getEffectiveAttackRate(
    attackInterval,
    substats.doubleChance || 0,
    movementDelay
  );
  
  return effectiveBaseDamage * doubleMultiplier * critMultiplier * effectiveAttackRate;
}

export function calculateHealingPerSecond(
  baseHealth: number,
  substats: SubstatCollection,
  dps: number,
  mountHealthBonus: number = 0
): number {
  const healthBonus = (substats.health || 0) / 100;
  const mountBonus = mountHealthBonus / 100;
  const maxHealth = baseHealth * (1 + mountBonus + healthBonus);
  
  const healthRegenPercent = (substats.healthRegen || 0) / 100;
  const healthRegenPerSecond = maxHealth * healthRegenPercent;
  
  const lifestealPercent = (substats.lifesteal || 0) / 100;
  const lifestealPerSecond = dps * lifestealPercent;
  
  return healthRegenPerSecond + lifestealPerSecond;
}
