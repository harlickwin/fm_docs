/**
 * Build Generator
 * Generates builds based on tournament configuration
 */

import { TournamentConfig, BuildStats, SubstatType, SubstatCollection } from '../../shared/types';
import {
  calculateDPS,
  calculateHealingPerSecond
} from '../../shared/calculations';
import {
  BASE_DAMAGE,
  BASE_HEALTH,
  MOUNT_DAMAGE_BONUS,
  MOUNT_HEALTH_BONUS,
  SUBSTAT_MAX_PER_ITEM
} from '../../shared/constants';

/**
 * Generate builds based on configuration
 */
export async function generateBuilds(config: TournamentConfig): Promise<BuildStats[]> {
  const builds: BuildStats[] = [];
  
  // Get enabled substats
  const enabledSubstats = Object.entries(config.substats)
    .filter(([_, enabled]) => enabled)
    .map(([type, _]) => type as SubstatType);
  
  if (enabledSubstats.length === 0) {
    throw new Error('No substats selected');
  }
  
  // Calculate max values per item based on multiplier
  const maxValues: Record<SubstatType, number> = {} as any;
  for (const substat of enabledSubstats) {
    maxValues[substat] = SUBSTAT_MAX_PER_ITEM[substat] * config.substatMultiplier;
  }
  
  // Generate builds using intelligent sampling
  const targetBuilds = config.targetBuilds;
  const slotsPerSubstat = 24; // Total equipment slots
  
  // Strategy 1: Focused builds (70% of builds)
  const focusedCount = Math.floor(targetBuilds * 0.7);
  for (let i = 0; i < focusedCount; i++) {
    const build = generateFocusedBuild(enabledSubstats, maxValues, slotsPerSubstat, config);
    builds.push(build);
  }
  
  // Strategy 2: Balanced builds (20% of builds)
  const balancedCount = Math.floor(targetBuilds * 0.2);
  for (let i = 0; i < balancedCount; i++) {
    const build = generateBalancedBuild(enabledSubstats, maxValues, slotsPerSubstat, config);
    builds.push(build);
  }
  
  // Strategy 3: Random builds (10% of builds)
  const randomCount = targetBuilds - focusedCount - balancedCount;
  for (let i = 0; i < randomCount; i++) {
    const build = generateRandomBuild(enabledSubstats, maxValues, slotsPerSubstat, config);
    builds.push(build);
  }
  
  return builds;
}

/**
 * Generate a focused build (concentrates on 2-3 substats)
 */
function generateFocusedBuild(
  substats: SubstatType[],
  maxValues: Record<SubstatType, number>,
  totalSlots: number,
  config: TournamentConfig
): BuildStats {
  const selectedSubstats = selectRandomSubstats(substats, 2, 3);
  const allocation: Record<SubstatType, number> = {} as any;
  
  // Distribute slots among selected substats
  const slotsPerStat = Math.floor(totalSlots / selectedSubstats.length);
  let remainingSlots = totalSlots;
  
  for (let i = 0; i < selectedSubstats.length; i++) {
    const substat = selectedSubstats[i];
    const slots = i === selectedSubstats.length - 1 ? remainingSlots : slotsPerStat;
    allocation[substat] = slots;
    remainingSlots -= slots;
  }
  
  return createBuildFromAllocation(allocation, maxValues, config, 'Focused');
}

/**
 * Generate a balanced build (distributes across 4-6 substats)
 */
function generateBalancedBuild(
  substats: SubstatType[],
  maxValues: Record<SubstatType, number>,
  totalSlots: number,
  config: TournamentConfig
): BuildStats {
  const selectedSubstats = selectRandomSubstats(substats, 4, 6);
  const allocation: Record<SubstatType, number> = {} as any;
  
  // Distribute slots more evenly
  let remainingSlots = totalSlots;
  
  for (let i = 0; i < selectedSubstats.length; i++) {
    const substat = selectedSubstats[i];
    const minSlots = 2;
    const maxSlots = Math.floor(remainingSlots / (selectedSubstats.length - i));
    const slots = Math.floor(Math.random() * (maxSlots - minSlots + 1)) + minSlots;
    
    allocation[substat] = slots;
    remainingSlots -= slots;
  }
  
  // Distribute remaining slots
  if (remainingSlots > 0) {
    const randomSubstat = selectedSubstats[Math.floor(Math.random() * selectedSubstats.length)];
    allocation[randomSubstat] += remainingSlots;
  }
  
  return createBuildFromAllocation(allocation, maxValues, config, 'Balanced');
}

/**
 * Generate a random build
 */
function generateRandomBuild(
  substats: SubstatType[],
  maxValues: Record<SubstatType, number>,
  totalSlots: number,
  config: TournamentConfig
): BuildStats {
  const allocation: Record<SubstatType, number> = {} as any;
  let remainingSlots = totalSlots;
  
  while (remainingSlots > 0) {
    const randomSubstat = substats[Math.floor(Math.random() * substats.length)];
    const slots = Math.min(remainingSlots, Math.floor(Math.random() * 5) + 1);
    
    allocation[randomSubstat] = (allocation[randomSubstat] || 0) + slots;
    remainingSlots -= slots;
  }
  
  return createBuildFromAllocation(allocation, maxValues, config, 'Random');
}

/**
 * Select random substats
 */
function selectRandomSubstats(substats: SubstatType[], min: number, max: number): SubstatType[] {
  const count = Math.floor(Math.random() * (max - min + 1)) + min;
  const shuffled = [...substats].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(count, substats.length));
}

/**
 * Create build from slot allocation
 */
function createBuildFromAllocation(
  allocation: Record<SubstatType, number>,
  maxValues: Record<SubstatType, number>,
  config: TournamentConfig,
  strategy: string
): BuildStats {
  const substats: SubstatCollection = {};
  const slotDesc: string[] = [];
  
  for (const [substat, slots] of Object.entries(allocation)) {
    if (slots > 0) {
      const value = slots * maxValues[substat as SubstatType];
      substats[substat as SubstatType] = value;
      slotDesc.push(`${substat}:${slots}`);
    }
  }
  
  // Determine weapon type
  const weaponType = config.weaponTypes.ranged ? 'ranged' : 'melee';
  
  // Calculate stats
  const dps = calculateDPS(
    BASE_DAMAGE,
    substats,
    weaponType,
    weaponType === 'melee' ? 2.2 : 0,
    MOUNT_DAMAGE_BONUS
  );
  
  const hps = calculateHealingPerSecond(
    BASE_HEALTH,
    substats,
    dps,
    MOUNT_HEALTH_BONUS
  );
  
  const healthBonus = (substats.health || 0) / 100;
  const mountBonus = MOUNT_HEALTH_BONUS / 100;
  const maxHP = BASE_HEALTH * (1 + mountBonus + healthBonus);
  
  return {
    substats,
    dps,
    hps,
    maxHP,
    weaponType,
    description: `${strategy}-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
    slotAllocation: slotDesc.join(', ')
  };
}
