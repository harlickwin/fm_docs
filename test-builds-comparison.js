/**
 * Test script to compare meta build vs champion builds with fixed attack speeds
 */

// Attack speed tiers (fixed)
const ATTACK_SPEED_TIERS = [
  { minPercent: 0, maxPercent: 7.1, attackInterval: 1.7 },
  { minPercent: 7.1, maxPercent: 15.4, attackInterval: 1.6 },
  { minPercent: 15.4, maxPercent: 25.0, attackInterval: 1.5 },
  { minPercent: 25.0, maxPercent: 36.4, attackInterval: 1.4 },
  { minPercent: 36.4, maxPercent: 50.0, attackInterval: 1.3 },
  { minPercent: 50.0, maxPercent: 66.7, attackInterval: 1.2 },
  { minPercent: 66.7, maxPercent: 87.5, attackInterval: 1.1 },
  { minPercent: 87.5, maxPercent: 114, attackInterval: 1.0 },
  { minPercent: 114, maxPercent: 150, attackInterval: 0.9 },
  { minPercent: 150, maxPercent: 200, attackInterval: 0.8 },
  { minPercent: 200, maxPercent: 275, attackInterval: 0.7 },
  { minPercent: 275, maxPercent: 400, attackInterval: 0.6 },
  { minPercent: 400, maxPercent: Infinity, attackInterval: 0.5 }
];

const BASE_DAMAGE = 3907700;
const BASE_HEALTH = 20667000;
const MOUNT_DAMAGE_BONUS = 242;
const MOUNT_HEALTH_BONUS = 230;

function getAttackInterval(attackSpeedPercent) {
  if (attackSpeedPercent > 400) return 0.4;
  
  for (const tier of ATTACK_SPEED_TIERS) {
    if (attackSpeedPercent >= tier.minPercent && attackSpeedPercent < tier.maxPercent) {
      return tier.attackInterval;
    }
  }
  return 1.7;
}

function getEffectiveAttackRate(attackInterval, doubleChancePercent) {
  const cappedDoubleChance = Math.min(doubleChancePercent, 100) / 100;
  const doubleDelay = attackInterval < 1.0 ? 0.1 : 0.2;
  const totalTimePerAttack = attackInterval + (cappedDoubleChance * doubleDelay);
  return 1 / totalTimePerAttack;
}

function calculateCritMultiplier(critChancePercent, critDamagePercent) {
  const cappedCritChance = Math.min(critChancePercent || 0, 100) / 100;
  const critDamage = (critDamagePercent || 0) / 100;
  const critMultiplier = 1.2 + critDamage;
  return (cappedCritChance * critMultiplier) + (1 - cappedCritChance);
}

function calculateDoubleMultiplier(doubleChancePercent) {
  const cappedDoubleChance = Math.min(doubleChancePercent || 0, 100) / 100;
  return 1 + cappedDoubleChance;
}

function calculateDPS(substats) {
  const generalDamage = (substats.damage || 0) / 100;
  const mountBonus = MOUNT_DAMAGE_BONUS / 100;
  const baseDamageWithGeneralBonuses = BASE_DAMAGE * (1 + mountBonus + generalDamage);
  
  const rangedDamage = (substats.rangedDamage || 0) / 100;
  const effectiveBaseDamage = baseDamageWithGeneralBonuses * (1 + rangedDamage);
  
  const doubleMultiplier = calculateDoubleMultiplier(substats.doubleChance || 0);
  const critMultiplier = calculateCritMultiplier(substats.criticalChance || 0, substats.criticalDamage || 0);
  
  const attackInterval = getAttackInterval(substats.attackSpeed || 0);
  const effectiveAttackRate = getEffectiveAttackRate(attackInterval, substats.doubleChance || 0);
  
  return effectiveBaseDamage * doubleMultiplier * critMultiplier * effectiveAttackRate;
}

function calculateHPS(substats, dps) {
  const healthBonus = (substats.health || 0) / 100;
  const mountBonus = MOUNT_HEALTH_BONUS / 100;
  const maxHealth = BASE_HEALTH * (1 + mountBonus + healthBonus);
  
  const healthRegenPercent = (substats.healthRegen || 0) / 100;
  const healthRegenPerSecond = maxHealth * healthRegenPercent;
  
  const lifestealPercent = (substats.lifesteal || 0) / 100;
  const lifestealPerSecond = dps * lifestealPercent;
  
  return healthRegenPerSecond + lifestealPerSecond;
}

function calculateMaxHP(substats) {
  const healthBonus = (substats.health || 0) / 100;
  const mountBonus = MOUNT_HEALTH_BONUS / 100;
  return BASE_HEALTH * (1 + mountBonus + healthBonus);
}

// Define REALISTIC builds to test (24 slots total, realistic distributions)
// Max per item: attackSpeed=40%, critChance=12%, critDmg=100%, double=40%, rangedDmg=15%, health=15%, regen=6%, lifesteal=20%

const builds = {
  metaBuild: {
    name: "Meta Build (Balanced)",
    substats: {
      criticalChance: 96,      // 8 slots * 12%
      criticalDamage: 800,     // 8 slots * 100%
      attackSpeed: 200,        // 5 slots * 40%
      doubleChance: 120,       // 3 slots * 40%
      rangedDamage: 0,         // 0 slots
      health: 0,               // 0 slots
      healthRegen: 0,          // 0 slots
      lifesteal: 0             // 0 slots
    }
  },
  
  glassCannon: {
    name: "Glass Cannon (Max Damage)",
    substats: {
      criticalChance: 100,     // 8.3 slots * 12% (capped at 100%)
      criticalDamage: 1600,    // 16 slots * 100%
      attackSpeed: 0,
      doubleChance: 0,
      rangedDamage: 0,
      health: 0,
      healthRegen: 0,
      lifesteal: 0
    }
  },
  
  balancedSurvival: {
    name: "Balanced Survival",
    substats: {
      criticalChance: 84,      // 7 slots * 12%
      criticalDamage: 700,     // 7 slots * 100%
      attackSpeed: 160,        // 4 slots * 40%
      doubleChance: 80,        // 2 slots * 40%
      rangedDamage: 0,
      health: 60,              // 4 slots * 15%
      healthRegen: 0,
      lifesteal: 0
    }
  },
  
  highAttackSpeed: {
    name: "High Attack Speed Build",
    substats: {
      criticalChance: 72,      // 6 slots * 12%
      criticalDamage: 600,     // 6 slots * 100%
      attackSpeed: 280,        // 7 slots * 40%
      doubleChance: 200,       // 5 slots * 40%
      rangedDamage: 0,
      health: 0,
      healthRegen: 0,
      lifesteal: 0
    }
  },
  
  lifestealer: {
    name: "Lifesteal Build",
    substats: {
      criticalChance: 72,      // 6 slots * 12%
      criticalDamage: 600,     // 6 slots * 100%
      attackSpeed: 160,        // 4 slots * 40%
      doubleChance: 80,        // 2 slots * 40%
      rangedDamage: 0,
      health: 0,
      healthRegen: 0,
      lifesteal: 120           // 6 slots * 20%
    }
  }
};

console.log("=".repeat(80));
console.log("BUILD COMPARISON WITH FIXED ATTACK SPEEDS");
console.log("=".repeat(80));
console.log("");

const results = [];

for (const [key, build] of Object.entries(builds)) {
  const dps = calculateDPS(build.substats);
  const hps = calculateHPS(build.substats, dps);
  const maxHP = calculateMaxHP(build.substats);
  const attackInterval = getAttackInterval(build.substats.attackSpeed || 0);
  const attackRate = getEffectiveAttackRate(attackInterval, build.substats.doubleChance || 0);
  
  results.push({
    name: build.name,
    dps,
    hps,
    maxHP,
    attackInterval,
    attackRate,
    netHPChange: hps - dps,
    survivalScore: (hps / dps) * maxHP
  });
  
  console.log(`${build.name}`);
  console.log("-".repeat(80));
  console.log(`  DPS: ${(dps / 1000000).toFixed(2)}M`);
  console.log(`  HPS: ${(hps / 1000000).toFixed(2)}M`);
  console.log(`  Max HP: ${(maxHP / 1000000).toFixed(2)}M`);
  console.log(`  Attack Interval: ${attackInterval.toFixed(2)}s`);
  console.log(`  Attacks/sec: ${attackRate.toFixed(3)}`);
  console.log(`  Net HP Change: ${((hps - dps) / 1000000).toFixed(2)}M/s`);
  console.log(`  Survival Score: ${(((hps / dps) * maxHP) / 1000000000).toFixed(2)}B`);
  console.log("");
}

console.log("=".repeat(80));
console.log("RANKINGS");
console.log("=".repeat(80));
console.log("");

console.log("By DPS (Highest to Lowest):");
results.sort((a, b) => b.dps - a.dps);
results.forEach((r, i) => {
  console.log(`  ${i + 1}. ${r.name}: ${(r.dps / 1000000).toFixed(2)}M`);
});
console.log("");

console.log("By Survival Score (Highest to Lowest):");
results.sort((a, b) => b.survivalScore - a.survivalScore);
results.forEach((r, i) => {
  console.log(`  ${i + 1}. ${r.name}: ${(r.survivalScore / 1000000000).toFixed(2)}B`);
});
console.log("");
