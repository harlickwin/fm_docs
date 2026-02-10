/**
 * System utilities for detecting hardware capabilities
 */

import * as os from 'os';

/**
 * Detect the number of available CPU cores
 * @returns The total number of CPU cores available
 */
export function detectCPUCores(): number {
  return os.cpus().length;
}

/**
 * Calculate the optimal number of worker threads for tournament execution
 * Uses N-1 cores to leave one core for the main process and UI
 * @returns The recommended number of worker threads (minimum 1)
 */
export function getOptimalWorkerCount(): number {
  const cpuCount = detectCPUCores();
  return Math.max(1, cpuCount - 1);
}

/**
 * Get system information for display
 * @returns Object containing CPU information
 */
export function getSystemInfo(): {
  totalCores: number;
  recommendedWorkers: number;
  cpuModel: string;
} {
  const cpus = os.cpus();
  return {
    totalCores: cpus.length,
    recommendedWorkers: getOptimalWorkerCount(),
    cpuModel: cpus[0]?.model || 'Unknown CPU'
  };
}

/**
 * Validate worker count configuration
 * @param workerCount The requested number of workers
 * @returns Validated worker count (clamped to valid range)
 */
export function validateWorkerCount(workerCount: number): number {
  const totalCores = detectCPUCores();
  
  // Ensure at least 1 worker
  if (workerCount < 1) {
    return 1;
  }
  
  // Warn if using all cores (should leave one for main process)
  if (workerCount >= totalCores) {
    console.warn(`Worker count (${workerCount}) >= total cores (${totalCores}). This may impact UI responsiveness.`);
  }
  
  // Cap at total cores (don't allow more workers than cores)
  return Math.min(workerCount, totalCores);
}
