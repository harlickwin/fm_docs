/**
 * Setup Wizard Component
 * Shown on first run to guide users through initial setup
 */

import React, { useState, useEffect } from 'react';

interface SetupWizardProps {
  onComplete: (config: any) => void;
  systemInfo: any;
  defaultOutputPath: string;
}

const SetupWizard: React.FC<SetupWizardProps> = ({ onComplete, systemInfo, defaultOutputPath }) => {
  const [step, setStep] = useState(1);
  const [config, setConfig] = useState({
    maxWorkers: systemInfo?.recommendedWorkers || 1,
    outputDirectory: defaultOutputPath,
  });

  const totalSteps = 4;

  const handleNext = () => {
    if (step < totalSteps) {
      setStep(step + 1);
    } else {
      onComplete(config);
    }
  };

  const handleBack = () => {
    if (step > 1) {
      setStep(step - 1);
    }
  };

  const handleSkip = () => {
    onComplete(config);
  };

  return (
    <div className="wizard-overlay">
      <div className="wizard-container">
        {/* Header */}
        <div className="wizard-header">
          <h1>🎉 Welcome to Tournament Pro!</h1>
          <p>Let's get you set up in just a few steps</p>
          <div className="wizard-progress">
            <div className="wizard-progress-bar" style={{ width: `${(step / totalSteps) * 100}%` }} />
          </div>
          <div className="wizard-step-indicator">
            Step {step} of {totalSteps}
          </div>
        </div>

        {/* Step Content */}
        <div className="wizard-content">
          {step === 1 && (
            <div className="wizard-step">
              <div className="wizard-icon">🏆</div>
              <h2>What is Tournament Pro?</h2>
              <p className="wizard-description">
                Tournament Pro is a powerful tool for running PvP build tournaments. 
                It simulates battles between different character builds to find the strongest combinations.
              </p>
              <div className="wizard-features">
                <div className="wizard-feature">
                  <span className="feature-icon">⚡</span>
                  <div>
                    <strong>Multi-threaded</strong>
                    <p>Uses all your CPU cores for fast results</p>
                  </div>
                </div>
                <div className="wizard-feature">
                  <span className="feature-icon">💾</span>
                  <div>
                    <strong>Auto-save</strong>
                    <p>Automatic checkpoints prevent data loss</p>
                  </div>
                </div>
                <div className="wizard-feature">
                  <span className="feature-icon">📊</span>
                  <div>
                    <strong>Detailed Results</strong>
                    <p>Export results in multiple formats</p>
                  </div>
                </div>
              </div>
            </div>
          )}

          {step === 2 && (
            <div className="wizard-step">
              <div className="wizard-icon">🖥️</div>
              <h2>CPU Configuration</h2>
              <p className="wizard-description">
                Tournament Pro can use multiple CPU cores to run tournaments faster.
              </p>
              <div className="wizard-info-box">
                <div className="info-row">
                  <span className="info-label">CPU Model:</span>
                  <span className="info-value">{systemInfo?.cpuModel || 'Unknown'}</span>
                </div>
                <div className="info-row">
                  <span className="info-label">Total Cores:</span>
                  <span className="info-value">{systemInfo?.totalCores || 1}</span>
                </div>
                <div className="info-row">
                  <span className="info-label">Recommended Workers:</span>
                  <span className="info-value">{systemInfo?.recommendedWorkers || 1}</span>
                </div>
              </div>
              <div className="wizard-form-group">
                <label>
                  <strong>Worker Threads:</strong>
                  <span className="label-hint">
                    (We recommend using {systemInfo?.recommendedWorkers || 1} workers)
                  </span>
                </label>
                <input
                  type="range"
                  min="1"
                  max={systemInfo?.totalCores || 1}
                  value={config.maxWorkers}
                  onChange={(e) => setConfig({ ...config, maxWorkers: parseInt(e.target.value) })}
                  className="wizard-slider"
                />
                <div className="slider-value">{config.maxWorkers} workers</div>
              </div>
              <div className="wizard-tip">
                💡 <strong>Tip:</strong> Using N-1 cores (leaving one for your system) provides the best performance.
              </div>
            </div>
          )}

          {step === 3 && (
            <div className="wizard-step">
              <div className="wizard-icon">📁</div>
              <h2>Output Directory</h2>
              <p className="wizard-description">
                Choose where tournament results will be saved.
              </p>
              <div className="wizard-form-group">
                <label>
                  <strong>Results Directory:</strong>
                </label>
                <div className="directory-input-group">
                  <input
                    type="text"
                    value={config.outputDirectory}
                    onChange={(e) => setConfig({ ...config, outputDirectory: e.target.value })}
                    className="wizard-input"
                    readOnly
                  />
                  <button
                    className="button button-secondary"
                    onClick={async () => {
                      const result = await (window as any).electron.selectDirectory();
                      if (result.success && result.path) {
                        setConfig({ ...config, outputDirectory: result.path });
                      }
                    }}
                  >
                    Browse...
                  </button>
                </div>
              </div>
              <div className="wizard-info-box">
                <p>
                  <strong>Default location:</strong><br />
                  {defaultOutputPath}
                </p>
                <p style={{ marginTop: '10px', fontSize: '0.9em', color: '#666' }}>
                  Results will be organized in timestamped subdirectories.
                  You can change this location later in the configuration screen.
                </p>
              </div>
            </div>
          )}

          {step === 4 && (
            <div className="wizard-step">
              <div className="wizard-icon">🚀</div>
              <h2>You're All Set!</h2>
              <p className="wizard-description">
                Tournament Pro is ready to use. Here's a quick guide to get started:
              </p>
              <div className="wizard-guide">
                <div className="guide-step">
                  <span className="guide-number">1</span>
                  <div>
                    <strong>Configure Your Tournament</strong>
                    <p>Select substats, weapon types, and other options</p>
                  </div>
                </div>
                <div className="guide-step">
                  <span className="guide-number">2</span>
                  <div>
                    <strong>Start the Tournament</strong>
                    <p>Click "Start Tournament" to begin the simulation</p>
                  </div>
                </div>
                <div className="guide-step">
                  <span className="guide-number">3</span>
                  <div>
                    <strong>Monitor Progress</strong>
                    <p>Watch real-time progress and worker status</p>
                  </div>
                </div>
                <div className="guide-step">
                  <span className="guide-number">4</span>
                  <div>
                    <strong>Review Results</strong>
                    <p>Export and analyze tournament results</p>
                  </div>
                </div>
              </div>
              <div className="wizard-tip">
                💡 <strong>Tip:</strong> Use the Help menu anytime for detailed documentation and troubleshooting.
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="wizard-footer">
          <div className="wizard-actions-left">
            {step > 1 && (
              <button className="button button-secondary" onClick={handleBack}>
                ← Back
              </button>
            )}
          </div>
          <div className="wizard-actions-right">
            {step < totalSteps && (
              <button className="button button-secondary" onClick={handleSkip}>
                Skip Setup
              </button>
            )}
            <button className="button button-primary" onClick={handleNext}>
              {step === totalSteps ? 'Get Started' : 'Next →'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SetupWizard;
