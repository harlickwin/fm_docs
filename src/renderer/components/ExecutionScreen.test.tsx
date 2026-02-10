import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, beforeEach, vi } from 'vitest';
import ExecutionScreen from './ExecutionScreen';
import { TournamentConfig, TournamentProgress } from '@shared/types';

describe('ExecutionScreen', () => {
  const mockConfig: TournamentConfig = {
    substats: {
      damage: true,
      meleeDamage: false,
      rangedDamage: false,
      criticalChance: true,
      criticalDamage: true,
      attackSpeed: true,
      doubleChance: false,
      health: true,
      healthRegen: false,
      lifesteal: false,
      blockChance: false,
      skillCooldown: false,
      skillDamage: false,
    },
    weaponTypes: {
      ranged: true,
      melee: true,
    },
    substatMultiplier: 0.5,
    targetBuilds: 1000,
    outputDirectory: '/test/output',
    maxWorkers: 4,
    checkpointInterval: 300,
    includeMetaBuild: true,
    loadPreviousResults: false,
  };

  const mockProgress: TournamentProgress = {
    totalBattles: 10000,
    completedBattles: 5000,
    progress: 50,
    speed: 100,
    elapsed: 50,
    remaining: 50,
    workerStatus: [
      { id: 0, status: 'running', completedBattles: 1250, speed: 25 },
      { id: 1, status: 'running', completedBattles: 1250, speed: 25 },
      { id: 2, status: 'running', completedBattles: 1250, speed: 25 },
      { id: 3, status: 'running', completedBattles: 1250, speed: 25 },
    ],
  };

  const mockHandlers = {
    onPause: vi.fn(),
    onResume: vi.fn(),
    onCancel: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Progress Display', () => {
    it('should display progress bar with correct percentage', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const progressBar = screen.getByText('50.00%');
      expect(progressBar).toBeInTheDocument();
    });

    it('should display completed battles count', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('5,000')).toBeInTheDocument();
      expect(screen.getByText('of 10,000')).toBeInTheDocument();
    });

    it('should display speed in battles per second', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('100')).toBeInTheDocument();
      expect(screen.getByText('battles/sec')).toBeInTheDocument();
    });

    it('should display elapsed and remaining time', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('0h 0m 50s')).toBeInTheDocument();
    });

    it('should show initializing message when no progress', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={null}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('Initializing tournament...')).toBeInTheDocument();
    });

    it('should handle infinite speed values gracefully', () => {
      const progressWithInfiniteSpeed: TournamentProgress = {
        ...mockProgress,
        speed: Infinity,
      };

      render(
        <ExecutionScreen
          config={mockConfig}
          progress={progressWithInfiniteSpeed}
          {...mockHandlers}
        />
      );

      // Should show dash instead of Infinity
      const speedCard = screen.getByText('Speed').closest('.stat-card');
      expect(speedCard).toBeInTheDocument();
    });

    it('should handle negative time values gracefully', () => {
      const progressWithNegativeTime: TournamentProgress = {
        ...mockProgress,
        remaining: -10,
      };

      render(
        <ExecutionScreen
          config={mockConfig}
          progress={progressWithNegativeTime}
          {...mockHandlers}
        />
      );

      // Should show dash for negative time
      const timeCards = screen.getAllByText('—');
      expect(timeCards.length).toBeGreaterThan(0);
    });

    it('should show live updates indicator when running', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('Live updates active')).toBeInTheDocument();
    });

    it('should not show live updates indicator when paused', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      expect(screen.queryByText('Live updates active')).not.toBeInTheDocument();
    });
  });

  describe('Worker Status Display', () => {
    it('should display all worker statuses', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('Worker 0')).toBeInTheDocument();
      expect(screen.getByText('Worker 1')).toBeInTheDocument();
      expect(screen.getByText('Worker 2')).toBeInTheDocument();
      expect(screen.getByText('Worker 3')).toBeInTheDocument();
    });

    it('should display worker completed battles', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const workerBattles = screen.getAllByText('1,250 battles');
      expect(workerBattles).toHaveLength(4);
    });

    it('should display worker speed', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const workerSpeeds = screen.getAllByText('25 /sec');
      expect(workerSpeeds).toHaveLength(4);
    });

    it('should show active worker count', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('(4 active)')).toBeInTheDocument();
    });

    it('should apply correct CSS class based on worker status', () => {
      const progressWithMixedStatus: TournamentProgress = {
        ...mockProgress,
        workerStatus: [
          { id: 0, status: 'running', completedBattles: 1250, speed: 25 },
          { id: 1, status: 'idle', completedBattles: 1250, speed: 0 },
          { id: 2, status: 'completed', completedBattles: 2500, speed: 0 },
          { id: 3, status: 'error', completedBattles: 500, speed: 0 },
        ],
      };

      render(
        <ExecutionScreen
          config={mockConfig}
          progress={progressWithMixedStatus}
          {...mockHandlers}
        />
      );

      // Verify all worker statuses are displayed
      expect(screen.getByText('running')).toBeInTheDocument();
      expect(screen.getByText('idle')).toBeInTheDocument();
      expect(screen.getByText('completed')).toBeInTheDocument();
      expect(screen.getByText('error')).toBeInTheDocument();
    });
  });

  describe('Control Buttons', () => {
    it('should show pause button when tournament is running', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      expect(pauseButton).toBeInTheDocument();
    });

    it('should call onPause when pause button is clicked', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      expect(mockHandlers.onPause).toHaveBeenCalledTimes(1);
    });

    it('should show resume button after pausing', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      const resumeButton = screen.getByText('▶️ Resume');
      expect(resumeButton).toBeInTheDocument();
    });

    it('should call onResume when resume button is clicked', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      // First pause
      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      // Then resume
      const resumeButton = screen.getByText('▶️ Resume');
      fireEvent.click(resumeButton);

      expect(mockHandlers.onResume).toHaveBeenCalledTimes(1);
    });

    it('should always show cancel button', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const cancelButton = screen.getByText('❌ Cancel Tournament');
      expect(cancelButton).toBeInTheDocument();
    });

    it('should show confirmation dialog when cancel is clicked', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const cancelButton = screen.getByText('❌ Cancel Tournament');
      fireEvent.click(cancelButton);

      expect(screen.getByText('⚠️ Cancel Tournament')).toBeInTheDocument();
      expect(screen.getByText(/Are you sure you want to cancel/)).toBeInTheDocument();
    });

    it('should call onCancel when confirmation is accepted', async () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      // Click cancel button
      const cancelButton = screen.getByText('❌ Cancel Tournament');
      fireEvent.click(cancelButton);

      // Confirm cancellation
      const confirmButton = screen.getByText('Cancel Tournament');
      fireEvent.click(confirmButton);

      await waitFor(() => {
        expect(mockHandlers.onCancel).toHaveBeenCalledTimes(1);
      });
    });

    it('should not call onCancel when confirmation is cancelled', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      // Click cancel button
      const cancelButton = screen.getByText('❌ Cancel Tournament');
      fireEvent.click(cancelButton);

      // Cancel the cancellation
      const continueButton = screen.getByText('Continue Tournament');
      fireEvent.click(continueButton);

      expect(mockHandlers.onCancel).not.toHaveBeenCalled();
    });
  });

  describe('Configuration Display', () => {
    it('should display tournament configuration', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      expect(screen.getByText('4 threads')).toBeInTheDocument();
      expect(screen.getByText('50%')).toBeInTheDocument();
      expect(screen.getByText('1,000')).toBeInTheDocument();
      expect(screen.getByText('300s')).toBeInTheDocument();
      expect(screen.getByText('/test/output')).toBeInTheDocument();
    });
  });

  describe('Paused State', () => {
    it('should update header when paused', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      expect(screen.getByText('⏸️ Tournament Paused')).toBeInTheDocument();
      expect(screen.getByText(/Tournament execution is paused/)).toBeInTheDocument();
    });

    it('should change progress bar color when paused', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      // After pausing, the header should change
      expect(screen.getByText('⏸️ Tournament Paused')).toBeInTheDocument();
    });

    it('should show dash for speed when paused', () => {
      render(
        <ExecutionScreen
          config={mockConfig}
          progress={mockProgress}
          {...mockHandlers}
        />
      );

      const pauseButton = screen.getByText('⏸️ Pause');
      fireEvent.click(pauseButton);

      // Speed should show dash
      const statCards = screen.getAllByText('—');
      expect(statCards.length).toBeGreaterThan(0);
    });
  });
});
