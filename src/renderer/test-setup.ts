/**
 * Test setup file for Vitest
 */

import { expect, afterEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';
import * as matchers from '@testing-library/jest-dom/matchers';

// Extend Vitest's expect with jest-dom matchers
expect.extend(matchers);

// Cleanup after each test
afterEach(() => {
  cleanup();
});

// Mock window.tournamentAPI
if (typeof window !== 'undefined') {
  (window as any).tournamentAPI = {
    onProgress: vi.fn(() => vi.fn()),
    onComplete: vi.fn(() => vi.fn()),
    onError: vi.fn(() => vi.fn()),
    onCheckpointFound: vi.fn(() => vi.fn()),
    startTournament: vi.fn(),
    pauseTournament: vi.fn(),
    resumeTournament: vi.fn(),
    cancelTournament: vi.fn(),
    resumeFromCheckpoint: vi.fn(),
    discardCheckpoint: vi.fn(),
  };
}
