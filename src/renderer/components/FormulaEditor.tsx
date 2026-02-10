/**
 * Formula Editor Component
 * Allows editing of game formula configurations
 */

import React, { useState, useEffect } from 'react';
import { FormulaConfig, AttackSpeedTier, ValidationResult } from '../../shared/formula-types';

interface FormulaEditorProps {
  config: FormulaConfig;
  onSave: (config: FormulaConfig) => void;
  onCancel: () => void;
}

const FormulaEditor: React.FC<FormulaEditorProps> = ({ config: initialConfig, onSave, onCancel }) => {
  const [config, setConfig] = useState<FormulaConfig>(initialConfig);
  const [validation, setValidation] = useState<ValidationResult>({ valid: true, errors: [], warnings: [] });
  const [activeTab, setActiveTab] = useState<'basic' | 'tiers' | 'advanced'>('basic');

  useEffect(() => {
    validateConfig();
  }, [config]);

  const validateConfig = async () => {
    // Call validation through IPC
    const result = await (window as any).electron.validateFormulaConfig(config);
    setValidation(result);
  };

  const handleSave = () => {
    if (validation.valid) {
      onSave(config);
    }
  };

  const updateBasicField = (field: string, value: any) => {
    setConfig({ ...config, [field]: value });
  };

  const updateCriticalHit = (value: number) => {
    setConfig({
      ...config,
      criticalHit: { baseDamageMultiplier: value },
    });
  };

  const updateDoubleAttackDelay = (field: 'normal' | 'highAttackSpeed', value: number) => {
    setConfig({
      ...config,
      doubleAttackDelays: {
        ...config.doubleAttackDelays,
        [field]: value,
      },
    });
  };

  const updateCap = (field: keyof typeof config.caps, value: number) => {
    setConfig({
      ...config,
      caps: {
        ...config.caps,
        [field]: value,
      },
    });
  };

  const addAttackSpeedTier = () => {
    const lastTier = config.attackSpeedTiers[config.attackSpeedTiers.length - 1];
    const newTier: AttackSpeedTier = {
      minPercent: lastTier ? lastTier.maxPercent : 0,
      maxPercent: lastTier ? lastTier.maxPercent + 50 : 50,
      attackInterval: lastTier ? lastTier.attackInterval - 0.1 : 1.0,
    };

    setConfig({
      ...config,
      attackSpeedTiers: [...config.attackSpeedTiers, newTier],
    });
  };

  const updateAttackSpeedTier = (index: number, field: keyof AttackSpeedTier, value: number) => {
    const newTiers = [...config.attackSpeedTiers];
    newTiers[index] = { ...newTiers[index], [field]: value };
    setConfig({ ...config, attackSpeedTiers: newTiers });
  };

  const removeAttackSpeedTier = (index: number) => {
    if (config.attackSpeedTiers.length > 1) {
      const newTiers = config.attackSpeedTiers.filter((_, i) => i !== index);
      setConfig({ ...config, attackSpeedTiers: newTiers });
    }
  };

  return (
    <div className="formula-editor">
      <div className="formula-editor-header">
        <h2>📐 Formula Editor</h2>
        <p>Configure game formulas and constants</p>
      </div>

      {/* Tabs */}
      <div className="formula-tabs">
        <button
          className={`formula-tab ${activeTab === 'basic' ? 'active' : ''}`}
          onClick={() => setActiveTab('basic')}
        >
          Basic Settings
        </button>
        <button
          className={`formula-tab ${activeTab === 'tiers' ? 'active' : ''}`}
          onClick={() => setActiveTab('tiers')}
        >
          Attack Speed Tiers
        </button>
        <button
          className={`formula-tab ${activeTab === 'advanced' ? 'active' : ''}`}
          onClick={() => setActiveTab('advanced')}
        >
          Advanced
        </button>
      </div>

      {/* Content */}
      <div className="formula-editor-content">
        {activeTab === 'basic' && (
          <div className="formula-section">
            <div className="form-group">
              <label>Configuration Name</label>
              <input
                type="text"
                value={config.name}
                onChange={(e) => updateBasicField('name', e.target.value)}
                placeholder="My Custom Formulas"
              />
            </div>

            <div className="form-group">
              <label>Description</label>
              <textarea
                value={config.description}
                onChange={(e) => updateBasicField('description', e.target.value)}
                placeholder="Describe your formula configuration..."
                rows={3}
              />
            </div>

            <div className="form-group">
              <label>
                Critical Hit Damage Multiplier
                <span className="help-text">Base damage multiplier for critical hits (e.g., 1.2 = 120%)</span>
              </label>
              <input
                type="number"
                step="0.1"
                min="1.0"
                max="10.0"
                value={config.criticalHit.baseDamageMultiplier}
                onChange={(e) => updateCriticalHit(parseFloat(e.target.value))}
              />
              <div className="value-display">
                {(config.criticalHit.baseDamageMultiplier * 100).toFixed(0)}% damage
              </div>
            </div>

            <div className="form-group">
              <label>
                Melee Movement Delay
                <span className="help-text">Delay in seconds for melee weapons to close distance</span>
              </label>
              <input
                type="number"
                step="0.1"
                min="0.1"
                max="10.0"
                value={config.meleeMovementDelay}
                onChange={(e) => updateBasicField('meleeMovementDelay', parseFloat(e.target.value))}
              />
              <div className="value-display">{config.meleeMovementDelay.toFixed(1)}s</div>
            </div>

            <h3>Double Attack Delays</h3>

            <div className="form-group">
              <label>
                Normal Delay
                <span className="help-text">Delay between double attacks at normal attack speed</span>
              </label>
              <input
                type="number"
                step="0.05"
                min="0.05"
                max="1.0"
                value={config.doubleAttackDelays.normal}
                onChange={(e) => updateDoubleAttackDelay('normal', parseFloat(e.target.value))}
              />
              <div className="value-display">{config.doubleAttackDelays.normal.toFixed(2)}s</div>
            </div>

            <div className="form-group">
              <label>
                High Attack Speed Delay
                <span className="help-text">Delay between double attacks at high attack speed</span>
              </label>
              <input
                type="number"
                step="0.05"
                min="0.05"
                max="1.0"
                value={config.doubleAttackDelays.highAttackSpeed}
                onChange={(e) => updateDoubleAttackDelay('highAttackSpeed', parseFloat(e.target.value))}
              />
              <div className="value-display">{config.doubleAttackDelays.highAttackSpeed.toFixed(2)}s</div>
            </div>
          </div>
        )}

        {activeTab === 'tiers' && (
          <div className="formula-section">
            <div className="section-header">
              <h3>Attack Speed Tiers</h3>
              <button className="button button-secondary" onClick={addAttackSpeedTier}>
                + Add Tier
              </button>
            </div>

            <div className="tiers-list">
              {config.attackSpeedTiers.map((tier, index) => (
                <div key={index} className="tier-item">
                  <div className="tier-header">
                    <strong>Tier {index + 1}</strong>
                    {config.attackSpeedTiers.length > 1 && (
                      <button
                        className="button-icon button-danger"
                        onClick={() => removeAttackSpeedTier(index)}
                        title="Remove tier"
                      >
                        ✕
                      </button>
                    )}
                  </div>

                  <div className="tier-fields">
                    <div className="form-group">
                      <label>Min Attack Speed %</label>
                      <input
                        type="number"
                        step="1"
                        min="0"
                        value={tier.minPercent}
                        onChange={(e) => updateAttackSpeedTier(index, 'minPercent', parseFloat(e.target.value))}
                      />
                    </div>

                    <div className="form-group">
                      <label>Max Attack Speed %</label>
                      <input
                        type="number"
                        step="1"
                        min="0"
                        value={tier.maxPercent}
                        onChange={(e) => updateAttackSpeedTier(index, 'maxPercent', parseFloat(e.target.value))}
                      />
                    </div>

                    <div className="form-group">
                      <label>Attack Interval (seconds)</label>
                      <input
                        type="number"
                        step="0.1"
                        min="0.1"
                        value={tier.attackInterval}
                        onChange={(e) => updateAttackSpeedTier(index, 'attackInterval', parseFloat(e.target.value))}
                      />
                    </div>
                  </div>

                  <div className="tier-summary">
                    {tier.minPercent}% - {tier.maxPercent}% → {tier.attackInterval}s per attack
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'advanced' && (
          <div className="formula-section">
            <h3>Stat Caps</h3>

            <div className="form-group">
              <label>
                Attack Speed Cap
                <span className="help-text">Maximum attack speed percentage</span>
              </label>
              <input
                type="number"
                step="10"
                min="100"
                max="1000"
                value={config.caps.attackSpeed}
                onChange={(e) => updateCap('attackSpeed', parseFloat(e.target.value))}
              />
              <div className="value-display">{config.caps.attackSpeed}%</div>
            </div>

            <div className="form-group">
              <label>
                Critical Chance Cap
                <span className="help-text">Maximum critical hit chance</span>
              </label>
              <input
                type="number"
                step="5"
                min="0"
                max="100"
                value={config.caps.critChance}
                onChange={(e) => updateCap('critChance', parseFloat(e.target.value))}
              />
              <div className="value-display">{config.caps.critChance}%</div>
            </div>

            <div className="form-group">
              <label>
                Double Attack Chance Cap
                <span className="help-text">Maximum double attack chance</span>
              </label>
              <input
                type="number"
                step="5"
                min="0"
                max="100"
                value={config.caps.doubleChance}
                onChange={(e) => updateCap('doubleChance', parseFloat(e.target.value))}
              />
              <div className="value-display">{config.caps.doubleChance}%</div>
            </div>

            <h3>Metadata</h3>

            <div className="form-group">
              <label>Version</label>
              <input
                type="text"
                value={config.version}
                onChange={(e) => updateBasicField('version', e.target.value)}
                placeholder="1.0.0"
              />
            </div>

            <div className="info-box">
              <strong>Configuration ID:</strong> {config.id}<br />
              <strong>Created:</strong> {new Date(config.createdAt).toLocaleString()}
            </div>
          </div>
        )}
      </div>

      {/* Validation Messages */}
      {(validation.errors.length > 0 || validation.warnings.length > 0) && (
        <div className="validation-messages">
          {validation.errors.length > 0 && (
            <div className="validation-errors">
              <strong>❌ Errors:</strong>
              <ul>
                {validation.errors.map((error, i) => (
                  <li key={i}>{error}</li>
                ))}
              </ul>
            </div>
          )}

          {validation.warnings.length > 0 && (
            <div className="validation-warnings">
              <strong>⚠️ Warnings:</strong>
              <ul>
                {validation.warnings.map((warning, i) => (
                  <li key={i}>{warning}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}

      {/* Actions */}
      <div className="formula-editor-actions">
        <button className="button button-secondary" onClick={onCancel}>
          Cancel
        </button>
        <button
          className="button button-primary"
          onClick={handleSave}
          disabled={!validation.valid}
        >
          Save Configuration
        </button>
      </div>
    </div>
  );
};

export default FormulaEditor;
