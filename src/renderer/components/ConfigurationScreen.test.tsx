/**
 * Unit tests for ConfigurationScreen component
 */

import React from 'react';
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ConfigurationScreen from './ConfigurationScreen';

// Mock the window.tournamentAPI
const mockTournamentAPI = {
  getSystemInfo: vi.fn(),
  checkForCheckpoint: vi.fn(),
  selectDirectory: vi.fn(),
  listPresets: vi.fn(),
  loadPreset: vi.fn(),
  savePreset: vi.fn(),
  deletePreset: vi.fn(),
  loadConfig: vi.fn(),
  saveConfig: vi.fn(),
};

beforeEach(() => {
  // Reset mocks
  vi.clearAllMocks();
  
  // Setup default mock responses
  mockTournamentAPI.getSystemInfo.mockResolvedValue({
    success: true,
    systemInfo: {
      totalCores: 8,
      recommendedWorkers: 7,
      cpuModel: 'Test CPU',
    },
  });
  
  mockTournamentAPI.checkForCheckpoint.mockResolvedValue({
    success: true,
    exists: false,
  });

  mockTournamentAPI.listPresets.mockResolvedValue({
    success: true,
    presets: [
      {
        id: 'quick-test',
        name: 'Quick Test',
        description: 'Fast tournament for testing',
        config: { targetBuilds: 1000 },
      },
    ],
  });

  mockTournamentAPI.loadConfig.mockResolvedValue({
    success: true,
    config: null,
  });

  mockTournamentAPI.saveConfig.mockResolvedValue({
    success: true,
  });
  
  // @ts-ignore - Mock the global window object
  global.window.tournamentAPI = mockTournamentAPI;
});

describe('ConfigurationScreen', () => {
  it('renders the configuration form', () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    expect(screen.getByText('🏆 Tournament Pro')).toBeInTheDocument();
    expect(screen.getByText('Configure your PvP tournament settings')).toBeInTheDocument();
  });

  it('displays substat selection checkboxes', () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    expect(screen.getByText('Substats to Include')).toBeInTheDocument();
    expect(screen.getByText('rangedDamage')).toBeInTheDocument();
    expect(screen.getByText('criticalChance')).toBeInTheDocument();
    expect(screen.getByText('attackSpeed')).toBeInTheDocument();
  });

  it('displays weapon type selection', () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    expect(screen.getByText('Weapon Types')).toBeInTheDocument();
    expect(screen.getByText('Ranged')).toBeInTheDocument();
    expect(screen.getByText('Melee')).toBeInTheDocument();
  });

  it('displays substat multiplier slider', () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    expect(screen.getByText(/Substat Multiplier:/)).toBeInTheDocument();
    const sliders = screen.getAllByRole('slider');
    const multiplierSlider = sliders.find(s => s.getAttribute('min') === '1' && s.getAttribute('max') === '100');
    expect(multiplierSlider).toBeDefined();
  });

  it('displays target builds input', () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    expect(screen.getByText('Target Builds')).toBeInTheDocument();
    const inputs = screen.getAllByRole('spinbutton');
    const targetBuildsInput = inputs.find(input => (input as HTMLInputElement).value === '10000');
    expect(targetBuildsInput).toBeDefined();
  });

  it('displays output directory picker', () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    expect(screen.getByText('Output Directory')).toBeInTheDocument();
    expect(screen.getByText('Browse')).toBeInTheDocument();
  });

  it('validates configuration before starting', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    // Try to start without selecting output directory
    const startButton = screen.getByText('Start Tournament');
    fireEvent.click(startButton);
    
    await waitFor(() => {
      expect(screen.getByText(/Output directory must be selected/)).toBeInTheDocument();
    });
    
    expect(onStart).not.toHaveBeenCalled();
  });

  it('updates substat multiplier when slider changes', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    const sliders = screen.getAllByRole('slider');
    const multiplierSlider = sliders.find(s => s.getAttribute('min') === '1' && s.getAttribute('max') === '100');
    
    if (multiplierSlider) {
      fireEvent.change(multiplierSlider, { target: { value: '50' } });
      
      await waitFor(() => {
        expect(screen.getByText(/Substat Multiplier: 50%/)).toBeInTheDocument();
      });
    }
  });

  it('fetches and displays system info on mount', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    await waitFor(() => {
      expect(mockTournamentAPI.getSystemInfo).toHaveBeenCalled();
      expect(mockTournamentAPI.listPresets).toHaveBeenCalled();
    });
  });

  it('displays runtime estimation', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    await waitFor(() => {
      expect(screen.getByText(/Tournament Statistics:/)).toBeInTheDocument();
      expect(screen.getByText(/Total Battles:/)).toBeInTheDocument();
      expect(screen.getByText(/Estimated Runtime:/)).toBeInTheDocument();
      expect(screen.getByText(/Battle Speed:/)).toBeInTheDocument();
    });
  });

  it('displays configuration presets dropdown', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    await waitFor(() => {
      expect(screen.getByText('Configuration Preset')).toBeInTheDocument();
      expect(screen.getByText('Save Preset')).toBeInTheDocument();
    });
  });

  it('shows validation errors in real-time', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    // Wait for initial render
    await waitFor(() => {
      expect(screen.getByText('rangedDamage')).toBeInTheDocument();
    });

    // Uncheck all substats to trigger validation error
    const substats = [
      'rangedDamage', 'criticalChance', 'criticalDamage', 'attackSpeed',
      'doubleChance', 'health', 'healthRegen', 'lifesteal', 'blockChance'
    ];

    for (const substat of substats) {
      const checkbox = screen.getByText(substat).previousSibling as HTMLInputElement;
      if (checkbox && checkbox.checked) {
        fireEvent.click(checkbox);
      }
    }
    
    await waitFor(() => {
      expect(screen.getByText(/At least one substat must be selected/)).toBeInTheDocument();
    });
  });

  it('disables start button when there are validation errors', async () => {
    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);
    
    const startButton = screen.getByText('Start Tournament') as HTMLButtonElement;
    
    // Initially should be disabled (no output directory)
    await waitFor(() => {
      expect(startButton.disabled).toBe(true);
    });
  });

  it('loads previous configuration on mount', async () => {
    const savedConfig = {
      substats: {
        damage: false,
        meleeDamage: false,
        rangedDamage: true,
        criticalChance: true,
        criticalDamage: true,
        attackSpeed: true,
        doubleChance: true,
        health: true,
        healthRegen: true,
        lifesteal: true,
        blockChance: true,
        skillCooldown: false,
        skillDamage: false,
      },
      weaponTypes: {
        ranged: true,
        melee: false,
      },
      substatMultiplier: 0.5,
      targetBuilds: 5000,
      outputDirectory: '/test/output',
      maxWorkers: 4,
      checkpointInterval: 300,
      includeMetaBuild: true,
      loadPreviousResults: false,
    };

    mockTournamentAPI.loadConfig.mockResolvedValue({
      success: true,
      config: savedConfig,
    });

    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);

    await waitFor(() => {
      expect(mockTournamentAPI.loadConfig).toHaveBeenCalled();
    });

    // Verify the loaded configuration is applied
    await waitFor(() => {
      expect(screen.getByText(/Substat Multiplier: 50%/)).toBeInTheDocument();
    });

    const targetBuildsInput = screen.getAllByRole('spinbutton').find(
      input => (input as HTMLInputElement).value === '5000'
    );
    expect(targetBuildsInput).toBeDefined();
  });

  it('saves configuration when starting tournament', async () => {
    mockTournamentAPI.selectDirectory.mockResolvedValue({
      success: true,
      path: '/test/output',
    });

    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);

    // Wait for initial load
    await waitFor(() => {
      expect(mockTournamentAPI.getSystemInfo).toHaveBeenCalled();
    });

    // Select output directory
    const browseButton = screen.getByText('Browse');
    fireEvent.click(browseButton);

    await waitFor(() => {
      expect(mockTournamentAPI.selectDirectory).toHaveBeenCalled();
    });

    // Start tournament
    const startButton = screen.getByText('Start Tournament');
    
    await waitFor(() => {
      expect(startButton).not.toBeDisabled();
    });

    fireEvent.click(startButton);

    await waitFor(() => {
      expect(mockTournamentAPI.saveConfig).toHaveBeenCalled();
      expect(onStart).toHaveBeenCalled();
    });
  });

  it('handles configuration load failure gracefully', async () => {
    mockTournamentAPI.loadConfig.mockResolvedValue({
      success: false,
      error: 'Failed to load config',
    });

    const onStart = vi.fn();
    render(<ConfigurationScreen onStart={onStart} />);

    await waitFor(() => {
      expect(mockTournamentAPI.loadConfig).toHaveBeenCalled();
    });

    // Should still render with default configuration
    expect(screen.getByText('🏆 Tournament Pro')).toBeInTheDocument();
  });
});
