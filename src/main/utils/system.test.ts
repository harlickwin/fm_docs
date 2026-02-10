/**
 * Unit tests for system utilities
 */

import { describe, it, expect } from 'vitest';
import * as os from 'os';
import { detectCPUCores, getOptimalWorkerCount, getSystemInfo, validateWorkerCount } from './system';

describe('System Utilities', () => {
  describe('detectCPUCores', () => {
    it('should return the number of CPU cores', () => {
      const cores = detectCPUCores();
      const expectedCores = os.cpus().length;
      
      expect(cores).toBe(expectedCores);
      expect(cores).toBeGreaterThan(0);
    });
  });

  describe('getOptimalWorkerCount', () => {
    it('should return N-1 cores (minimum 1)', () => {
      const optimalWorkers = getOptimalWorkerCount();
      const totalCores = os.cpus().length;
      const expectedWorkers = Math.max(1, totalCores - 1);
      
      expect(optimalWorkers).toBe(expectedWorkers);
      expect(optimalWorkers).toBeGreaterThanOrEqual(1);
      
      if (totalCores > 1) {
        expect(optimalWorkers).toBeLessThan(totalCores);
      }
    });
  });

  describe('getSystemInfo', () => {
    it('should return complete system information', () => {
      const systemInfo = getSystemInfo();
      
      expect(systemInfo.totalCores).toBeGreaterThan(0);
      expect(systemInfo.recommendedWorkers).toBeGreaterThanOrEqual(1);
      expect(typeof systemInfo.cpuModel).toBe('string');
      expect(systemInfo.cpuModel.length).toBeGreaterThan(0);
      expect(systemInfo.totalCores).toBe(os.cpus().length);
      expect(systemInfo.recommendedWorkers).toBe(getOptimalWorkerCount());
    });
  });

  describe('validateWorkerCount', () => {
    it('should ensure at least 1 worker', () => {
      expect(validateWorkerCount(0)).toBe(1);
      expect(validateWorkerCount(-5)).toBe(1);
      expect(validateWorkerCount(1)).toBe(1);
    });

    it('should cap at total cores', () => {
      const totalCores = os.cpus().length;
      
      expect(validateWorkerCount(totalCores)).toBe(totalCores);
      expect(validateWorkerCount(totalCores + 1)).toBe(totalCores);
      expect(validateWorkerCount(totalCores + 100)).toBe(totalCores);
    });

    it('should allow valid values', () => {
      const totalCores = os.cpus().length;
      const midValue = Math.floor(totalCores / 2);
      
      if (midValue >= 1) {
        expect(validateWorkerCount(midValue)).toBe(midValue);
      }
    });
  });
});
