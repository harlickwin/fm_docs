import React, { useState, useEffect } from 'react';
import { TournamentConfig, SubstatType, SystemInfo, ConfigPreset, ValidationError } from '@shared/types';
import { validateConfig, hasErrors, getErrorsBySeverity } from '@shared/validation';
import { estimateRuntime, getConfidenceDescription } from '@shared/estimation';

interface Props {
  onStart: (config: TournamentConfig) => void;
}

const DEFAULT_CONFIG: TournamentConfig = {
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
  substatMultiplier: 0.75,
  targetBuilds: 10000,
  outputDirectory: '',
  maxWorkers: 1,
  checkpointInterval: 300,
  includeMetaBuild: true,
  loadPreviousResults: false,
};

const ConfigurationScreen: React.FC<Props> = ({ onStart }) => {
  const [config, setConfig] = useState<TournamentConfig>(DEFAULT_CONFIG);
  const [validationErrors, setValidationErrors] = useState<ValidationError[]>([]);
  const [systemInfo, setSystemInfo] = useState<SystemInfo | null>(null);
  const [checkpointWarning, setCheckpointWarning] = useState<string | null>(null);
  const [presets, setPresets] = useState<ConfigPreset[]>([]);
  const [selectedPreset, setSelectedPreset] = useState<string>('');
  const [showSavePreset, setShowSavePreset] = useState(false);
  const [presetName, setPresetName] = useState('');
  const [presetDescription, setPresetDescription] = useState('');

  useEffect(() => {
    // Fetch system info on mount
    const fetchSystemInfo = async () => {
      const result = await window.tournamentAPI.getSystemInfo();
      if (result.success && result.systemInfo) {
        setSystemInfo(result.systemInfo);
        // Set default max workers to recommended value
        setConfig(prev => ({
          ...prev,
          maxWorkers: result.systemInfo.recommendedWorkers
        }));
      }
    };
    fetchSystemInfo();

    // Load previous configuration
    const loadPreviousConfig = async () => {
      const result = await window.tournamentAPI.loadConfig();
      if (result.success && result.config) {
        // Merge loaded config with defaults, preserving system-specific values
        setConfig(prev => ({
          ...prev,
          ...result.config,
          // Keep the recommended workers if not set in saved config
          maxWorkers: result.config.maxWorkers || prev.maxWorkers,
        }));
      }
    };
    loadPreviousConfig();

    // Load presets
    loadPresets();
  }, []);

  // Real-time validation whenever config changes
  useEffect(() => {
    const errors = validateConfig(config);
    setValidationErrors(errors);
  }, [config]);

  // Load available presets
  const loadPresets = async () => {
    const result = await window.tournamentAPI.listPresets();
    if (result.success && result.presets) {
      setPresets(result.presets);
    }
  };

  // Check for checkpoint when output directory changes
  useEffect(() => {
    const checkForCheckpoint = async () => {
      if (!config.outputDirectory) {
        setCheckpointWarning(null);
        return;
      }

      const result = await window.tournamentAPI.checkForCheckpoint(config.outputDirectory);
      
      if (result.success && result.exists) {
        if (result.valid) {
          setCheckpointWarning(
            `⚠️ A checkpoint exists in this directory (${result.progress?.toFixed(1)}% complete). ` +
            `Starting a new tournament will overwrite it.`
          );
        } else {
          setCheckpointWarning(
            `⚠️ A corrupted checkpoint was found in this directory. It will be ignored.`
          );
        }
      } else {
        setCheckpointWarning(null);
      }
    };

    checkForCheckpoint();
  }, [config.outputDirectory]);

  const handleSubstatChange = (substat: SubstatType, checked: boolean) => {
    setConfig(prev => ({
      ...prev,
      substats: { ...prev.substats, [substat]: checked },
    }));
  };

  const handleWeaponTypeChange = (type: 'ranged' | 'melee', checked: boolean) => {
    setConfig(prev => ({
      ...prev,
      weaponTypes: { ...prev.weaponTypes, [type]: checked },
    }));
  };

  const handleStart = async () => {
    const errors = validateConfig(config);
    if (!hasErrors(errors)) {
      // Save configuration before starting
      await window.tournamentAPI.saveConfig(config);
      onStart(config);
    }
  };

  const selectDirectory = async () => {
    const result = await window.tournamentAPI.selectDirectory();
    if (result.success && result.path) {
      setConfig(prev => ({ ...prev, outputDirectory: result.path! }));
    }
  };

  const handlePresetSelect = async (presetId: string) => {
    setSelectedPreset(presetId);
    
    if (!presetId) return;

    const result = await window.tournamentAPI.loadPreset(presetId);
    if (result.success && result.preset) {
      // Merge preset config with current config (preserve output directory and workers)
      setConfig(prev => ({
        ...prev,
        ...result.preset.config,
        outputDirectory: prev.outputDirectory, // Keep current output directory
        maxWorkers: prev.maxWorkers, // Keep current worker count
      }));
    }
  };

  const handleSavePreset = async () => {
    if (!presetName.trim()) return;

    const preset: ConfigPreset = {
      id: `custom-${Date.now()}`,
      name: presetName,
      description: presetDescription,
      config: {
        substats: config.substats,
        weaponTypes: config.weaponTypes,
        substatMultiplier: config.substatMultiplier,
        targetBuilds: config.targetBuilds,
        includeMetaBuild: config.includeMetaBuild,
      },
    };

    const result = await window.tournamentAPI.savePreset(preset);
    if (result.success) {
      await loadPresets();
      setShowSavePreset(false);
      setPresetName('');
      setPresetDescription('');
      setSelectedPreset(preset.id);
    }
  };

  const estimate = estimateRuntime(config);
  const { errors: errorList, warnings: warningList } = getErrorsBySeverity(validationErrors);

  return (
    <div className="screen">
      <div className="screen-header">
        <h1>🏆 Tournament Pro</h1>
        <p>Configure your PvP tournament settings</p>
      </div>

      {/* Validation Errors */}
      {errorList.length > 0 && (
        <div style={{ background: '#f8d7da', padding: '15px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #dc3545' }}>
          <strong style={{ color: '#721c24', display: 'block', marginBottom: '8px' }}>❌ Errors:</strong>
          {errorList.map((error, i) => (
            <div key={i} style={{ color: '#721c24', marginLeft: '10px' }}>• {error.message}</div>
          ))}
        </div>
      )}

      {/* Validation Warnings */}
      {warningList.length > 0 && (
        <div style={{ background: '#fff3cd', padding: '15px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #ffc107' }}>
          <strong style={{ color: '#856404', display: 'block', marginBottom: '8px' }}>⚠️ Warnings:</strong>
          {warningList.map((warning, i) => (
            <div key={i} style={{ color: '#856404', marginLeft: '10px' }}>• {warning.message}</div>
          ))}
        </div>
      )}

      {/* Checkpoint Warning */}
      {checkpointWarning && (
        <div style={{ background: '#fff3cd', padding: '15px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #ffc107' }}>
          <div style={{ color: '#856404' }}>{checkpointWarning}</div>
        </div>
      )}

      {/* Configuration Presets */}
      <div className="form-group">
        <label>Configuration Preset</label>
        <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
          <select
            value={selectedPreset}
            onChange={(e) => handlePresetSelect(e.target.value)}
            style={{ flex: 1 }}
          >
            <option value="">Custom Configuration</option>
            {presets.map(preset => (
              <option key={preset.id} value={preset.id}>
                {preset.name} - {preset.description}
              </option>
            ))}
          </select>
          <button 
            className="button button-secondary" 
            onClick={() => setShowSavePreset(!showSavePreset)}
          >
            {showSavePreset ? 'Cancel' : 'Save Preset'}
          </button>
        </div>

        {/* Save Preset Form */}
        {showSavePreset && (
          <div style={{ background: '#f8f9fa', padding: '15px', borderRadius: '8px', marginTop: '10px' }}>
            <div style={{ marginBottom: '10px' }}>
              <label style={{ display: 'block', marginBottom: '5px', fontSize: '0.9em' }}>Preset Name</label>
              <input
                type="text"
                value={presetName}
                onChange={(e) => setPresetName(e.target.value)}
                placeholder="e.g., My Custom Setup"
                style={{ width: '100%' }}
              />
            </div>
            <div style={{ marginBottom: '10px' }}>
              <label style={{ display: 'block', marginBottom: '5px', fontSize: '0.9em' }}>Description</label>
              <input
                type="text"
                value={presetDescription}
                onChange={(e) => setPresetDescription(e.target.value)}
                placeholder="e.g., Optimized for ranged builds"
                style={{ width: '100%' }}
              />
            </div>
            <button 
              className="button button-primary" 
              onClick={handleSavePreset}
              disabled={!presetName.trim()}
              style={{ width: '100%' }}
            >
              Save Current Configuration
            </button>
          </div>
        )}
      </div>

      <div className="form-group">
        <label>Substats to Include</label>
        <div className="checkbox-group">
          {(Object.keys(config.substats) as SubstatType[]).map(substat => (
            <div key={substat} className="checkbox-item">
              <input
                type="checkbox"
                checked={config.substats[substat]}
                onChange={(e) => handleSubstatChange(substat, e.target.checked)}
              />
              <span>{substat}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="form-group">
        <label>Weapon Types</label>
        <div className="checkbox-group">
          <div className="checkbox-item">
            <input
              type="checkbox"
              checked={config.weaponTypes.ranged}
              onChange={(e) => handleWeaponTypeChange('ranged', e.target.checked)}
            />
            <span>Ranged</span>
          </div>
          <div className="checkbox-item">
            <input
              type="checkbox"
              checked={config.weaponTypes.melee}
              onChange={(e) => handleWeaponTypeChange('melee', e.target.checked)}
            />
            <span>Melee</span>
          </div>
        </div>
      </div>

      <div className="form-group">
        <label>Substat Multiplier: {(config.substatMultiplier * 100).toFixed(0)}%</label>
        <input
          type="range"
          min="1"
          max="100"
          value={config.substatMultiplier * 100}
          onChange={(e) => setConfig(prev => ({ ...prev, substatMultiplier: parseInt(e.target.value) / 100 }))}
        />
      </div>

      <div className="form-group">
        <label>Target Builds</label>
        <input
          type="number"
          value={config.targetBuilds}
          onChange={(e) => setConfig(prev => ({ ...prev, targetBuilds: parseInt(e.target.value) || 0 }))}
        />
      </div>

      <div className="form-group">
        <label>Output Directory</label>
        <div style={{ display: 'flex', gap: '10px' }}>
          <input
            type="text"
            value={config.outputDirectory}
            readOnly
            placeholder="Click to select..."
          />
          <button className="button button-secondary" onClick={selectDirectory}>
            Browse
          </button>
        </div>
      </div>

      <div className="form-group">
        <label>Max Workers: {config.maxWorkers}</label>
        {systemInfo && (
          <div style={{ fontSize: '0.9em', color: '#666', marginBottom: '5px' }}>
            CPU: {systemInfo.cpuModel} ({systemInfo.totalCores} cores)
            <br />
            Recommended: {systemInfo.recommendedWorkers} workers (leaves 1 core for UI)
          </div>
        )}
        <input
          type="range"
          min="1"
          max={systemInfo?.totalCores || 16}
          value={config.maxWorkers}
          onChange={(e) => setConfig(prev => ({ ...prev, maxWorkers: parseInt(e.target.value) }))}
        />
      </div>

      <div style={{ background: '#d4edda', padding: '15px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #28a745' }}>
        <div style={{ marginBottom: '10px' }}>
          <strong>📊 Tournament Statistics:</strong>
        </div>
        <div style={{ fontSize: '0.95em', lineHeight: '1.6' }}>
          <div>• Total Battles: <strong>{estimate.totalBattles.toLocaleString()}</strong></div>
          <div>• Estimated Runtime: <strong>{estimate.formattedTime}</strong></div>
          <div>• Battle Speed: <strong>{Math.round(estimate.battlesPerSecond).toLocaleString()}</strong> battles/sec</div>
          <div style={{ marginTop: '8px', fontSize: '0.9em', color: '#155724', fontStyle: 'italic' }}>
            {getConfidenceDescription(estimate.confidence)}
          </div>
        </div>
      </div>

      <button 
        className="button button-primary" 
        onClick={handleStart} 
        style={{ width: '100%' }}
        disabled={hasErrors(validationErrors)}
      >
        Start Tournament
      </button>
    </div>
  );
};

export default ConfigurationScreen;
