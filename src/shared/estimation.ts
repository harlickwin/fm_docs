/**
 * Runtime Estimation Utilities
 */

import { TournamentConfig, RuntimeEstimate } from './types';

/**
 * Estimate tournament runtime based on configuration
 * 
 * Estimation factors:
 * - Number of builds (N) results in N*(N-1)/2 battles
 * - Battle simulation speed varies based on:
 *   - Number of substats (more substats = slower simulation)
 *   - Weapon types (both types = more builds = more battles)
 *   - Worker count (linear speedup with diminishing returns)
 * 
 * Benchmarks (approximate, based on typical hardware):
 * - Simple builds (few substats): ~3,000,000 battles/sec per worker
 * - Medium builds (5-7 substats): ~2,000,000 battles/sec per worker
 * - Complex builds (10+ substats): ~1,500,000 battles/sec per worker
 */
export function estimateRuntime(config: TournamentConfig): RuntimeEstimate {
  // Calculate total battles (round-robin tournament)
  const totalBattles = (config.targetBuilds * (config.targetBuilds - 1)) / 2;

  // Estimate battles per second based on configuration complexity
  const baseSpeed = estimateBattleSpeed(config);
  
  // Apply worker scaling (with diminishing returns)
  const workerEfficiency = calculateWorkerEfficiency(config.maxWorkers);
  const effectiveSpeed = baseSpeed * config.maxWorkers * workerEfficiency;

  // Calculate time
  const estimatedSeconds = totalBattles / effectiveSpeed;
  const estimatedMinutes = estimatedSeconds / 60;
  const estimatedHours = estimatedMinutes / 60;

  // Format time string
  const formattedTime = formatTime(estimatedSeconds);

  // Determine confidence level
  const confidence = determineConfidence(config);

  return {
    totalBattles,
    estimatedSeconds,
    estimatedMinutes,
    estimatedHours,
    formattedTime,
    battlesPerSecond: effectiveSpeed,
    confidence,
  };
}

/**
 * Estimate battle simulation speed based on configuration complexity
 */
function estimateBattleSpeed(config: TournamentConfig): number {
  // Count active substats
  const activeSubstats = Object.values(config.substats).filter(v => v).length;

  // Base speed depends on substat count
  let baseSpeed: number;
  if (activeSubstats <= 4) {
    baseSpeed = 3000000; // Simple builds
  } else if (activeSubstats <= 7) {
    baseSpeed = 2000000; // Medium builds
  } else {
    baseSpeed = 1500000; // Complex builds
  }

  // Adjust for weapon types (both types = more diverse builds = slightly slower)
  if (config.weaponTypes.ranged && config.weaponTypes.melee) {
    baseSpeed *= 0.95;
  }

  // Adjust for substat multiplier (higher multiplier = stronger builds = longer battles)
  if (config.substatMultiplier > 0.8) {
    baseSpeed *= 0.95;
  } else if (config.substatMultiplier < 0.5) {
    baseSpeed *= 1.05;
  }

  return baseSpeed;
}

/**
 * Calculate worker efficiency (diminishing returns with more workers)
 */
function calculateWorkerEfficiency(workers: number): number {
  if (workers === 1) return 1.0;
  if (workers === 2) return 0.98;
  if (workers <= 4) return 0.95;
  if (workers <= 8) return 0.92;
  if (workers <= 16) return 0.88;
  return 0.85; // 16+ workers
}

/**
 * Format time in human-readable format
 */
function formatTime(seconds: number): string {
  if (seconds < 60) {
    return `${Math.round(seconds)}s`;
  }

  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = Math.round(seconds % 60);

  if (hours > 0) {
    if (minutes > 0) {
      return `${hours}h ${minutes}m`;
    }
    return `${hours}h`;
  }

  if (secs > 0 && minutes < 10) {
    return `${minutes}m ${secs}s`;
  }

  return `${minutes}m`;
}

/**
 * Determine confidence level of estimate
 */
function determineConfidence(config: TournamentConfig): 'low' | 'medium' | 'high' {
  // High confidence for typical configurations
  if (
    config.targetBuilds >= 1000 &&
    config.targetBuilds <= 50000 &&
    config.maxWorkers >= 2 &&
    config.maxWorkers <= 16
  ) {
    return 'high';
  }

  // Medium confidence for edge cases
  if (
    config.targetBuilds < 1000 ||
    config.targetBuilds > 100000 ||
    config.maxWorkers > 16
  ) {
    return 'medium';
  }

  // Low confidence for extreme cases
  return 'low';
}

/**
 * Get human-readable description of estimate confidence
 */
export function getConfidenceDescription(confidence: 'low' | 'medium' | 'high'): string {
  switch (confidence) {
    case 'high':
      return 'Estimate is based on typical configurations and should be accurate within ±20%';
    case 'medium':
      return 'Estimate may vary by ±30-50% depending on hardware and system load';
    case 'low':
      return 'Estimate is rough and may vary significantly based on many factors';
  }
}
