/**
 * Help Dialog Component
 * Provides in-app help and documentation
 */

import React, { useState } from 'react';

interface HelpDialogProps {
  onClose: () => void;
}

const HelpDialog: React.FC<HelpDialogProps> = ({ onClose }) => {
  const [activeTab, setActiveTab] = useState<'quick-start' | 'configuration' | 'troubleshooting' | 'about'>('quick-start');

  return (
    <div className="help-overlay" onClick={onClose}>
      <div className="help-dialog" onClick={(e) => e.stopPropagation()}>
        {/* Header */}
        <div className="help-header">
          <h2>📚 Tournament Pro Help</h2>
          <button className="help-close" onClick={onClose}>✕</button>
        </div>

        {/* Tabs */}
        <div className="help-tabs">
          <button
            className={`help-tab ${activeTab === 'quick-start' ? 'active' : ''}`}
            onClick={() => setActiveTab('quick-start')}
          >
            🚀 Quick Start
          </button>
          <button
            className={`help-tab ${activeTab === 'configuration' ? 'active' : ''}`}
            onClick={() => setActiveTab('configuration')}
          >
            ⚙️ Configuration
          </button>
          <button
            className={`help-tab ${activeTab === 'troubleshooting' ? 'active' : ''}`}
            onClick={() => setActiveTab('troubleshooting')}
          >
            🔧 Troubleshooting
          </button>
          <button
            className={`help-tab ${activeTab === 'about' ? 'active' : ''}`}
            onClick={() => setActiveTab('about')}
          >
            ℹ️ About
          </button>
        </div>

        {/* Content */}
        <div className="help-content">
          {activeTab === 'quick-start' && (
            <div className="help-section">
              <h3>Getting Started</h3>
              
              <div className="help-step">
                <div className="step-number">1</div>
                <div className="step-content">
                  <h4>Configure Tournament</h4>
                  <p>Select substats, weapon types, and set the number of builds to test.</p>
                  <ul>
                    <li>Start with 1,000 builds for a balanced tournament</li>
                    <li>Select 5-7 core substats (damage, crit, attack speed, health)</li>
                    <li>Choose both weapon types to compare melee vs ranged</li>
                  </ul>
                </div>
              </div>

              <div className="help-step">
                <div className="step-number">2</div>
                <div className="step-content">
                  <h4>Start Tournament</h4>
                  <p>Review the estimated runtime and click "Start Tournament".</p>
                  <ul>
                    <li>Estimated time is based on your CPU and configuration</li>
                    <li>You can pause or cancel at any time</li>
                    <li>Progress is automatically saved every 5 minutes</li>
                  </ul>
                </div>
              </div>

              <div className="help-step">
                <div className="step-number">3</div>
                <div className="step-content">
                  <h4>Monitor Progress</h4>
                  <p>Watch real-time progress and worker status.</p>
                  <ul>
                    <li>Progress bar shows overall completion</li>
                    <li>Worker status shows each CPU core's activity</li>
                    <li>Speed is measured in battles per second</li>
                  </ul>
                </div>
              </div>

              <div className="help-step">
                <div className="step-number">4</div>
                <div className="step-content">
                  <h4>Review Results</h4>
                  <p>View top builds and export results.</p>
                  <ul>
                    <li>Top 10 builds are displayed with win rates</li>
                    <li>Export to HTML for sharing</li>
                    <li>Export to JSON for further analysis</li>
                  </ul>
                </div>
              </div>

              <div className="help-tip">
                <strong>💡 Pro Tip:</strong> Start with a small tournament (100 builds) to test your configuration before running a large one.
              </div>
            </div>
          )}

          {activeTab === 'configuration' && (
            <div className="help-section">
              <h3>Configuration Guide</h3>

              <div className="help-item">
                <h4>📊 Substats</h4>
                <p>Character attributes that vary across builds:</p>
                <ul>
                  <li><strong>Damage:</strong> Base damage output</li>
                  <li><strong>Critical Chance:</strong> Probability of critical hits</li>
                  <li><strong>Critical Damage:</strong> Critical hit damage multiplier</li>
                  <li><strong>Attack Speed:</strong> How quickly attacks are performed</li>
                  <li><strong>Health:</strong> Maximum hit points</li>
                  <li><strong>Lifesteal:</strong> Damage converted to healing</li>
                  <li><strong>Double Chance:</strong> Probability of double attacks</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>⚔️ Weapon Types</h4>
                <ul>
                  <li><strong>Melee:</strong> Close-range with movement delay</li>
                  <li><strong>Ranged:</strong> Long-range without movement delay</li>
                  <li><strong>Both:</strong> Test both types in same tournament</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>🎚️ Substat Multiplier</h4>
                <p>Controls the strength of substats:</p>
                <ul>
                  <li><strong>100%:</strong> Full strength (realistic)</li>
                  <li><strong>50%:</strong> Half strength (faster tournaments)</li>
                  <li><strong>25%:</strong> Quarter strength (very fast)</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>🎯 Target Builds</h4>
                <p>Number of unique builds to test:</p>
                <ul>
                  <li><strong>100-500:</strong> Quick test (minutes)</li>
                  <li><strong>1,000-5,000:</strong> Standard (30-60 min)</li>
                  <li><strong>10,000+:</strong> Comprehensive (hours)</li>
                </ul>
                <p><em>Total battles = N × (N-1) / 2</em></p>
              </div>

              <div className="help-item">
                <h4>🖥️ Worker Threads</h4>
                <p>Number of CPU cores to use:</p>
                <ul>
                  <li><strong>Recommended:</strong> Total cores - 1</li>
                  <li><strong>Maximum:</strong> All cores (may slow system)</li>
                  <li><strong>Minimum:</strong> 1 core (slowest)</li>
                </ul>
              </div>

              <div className="help-tip">
                <strong>💡 Pro Tip:</strong> Lower the substat multiplier for faster testing, then run a full 100% tournament with your final configuration.
              </div>
            </div>
          )}

          {activeTab === 'troubleshooting' && (
            <div className="help-section">
              <h3>Common Issues</h3>

              <div className="help-item">
                <h4>❌ Tournament Won't Start</h4>
                <p><strong>Solutions:</strong></p>
                <ul>
                  <li>Check that at least one substat is selected</li>
                  <li>Verify target builds is greater than 0</li>
                  <li>Ensure output directory exists and is writable</li>
                  <li>Look for validation errors at the bottom of the screen</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>💥 Application Crashed</h4>
                <p><strong>Solutions:</strong></p>
                <ul>
                  <li>Restart the application</li>
                  <li>Click "Resume Tournament" when prompted</li>
                  <li>Your progress is automatically saved</li>
                  <li>If crash persists, reduce worker threads</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>🐌 Tournament Too Slow</h4>
                <p><strong>Solutions:</strong></p>
                <ul>
                  <li>Reduce number of target builds</li>
                  <li>Lower substat multiplier to 50%</li>
                  <li>Select fewer substats</li>
                  <li>Increase worker threads</li>
                  <li>Close other applications</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>💾 Checkpoint Not Found</h4>
                <p><strong>Solutions:</strong></p>
                <ul>
                  <li>Check output directory for .checkpoint.json file</li>
                  <li>Verify output directory path is correct</li>
                  <li>Checkpoint may be corrupted - start fresh</li>
                  <li>Ensure checkpoints weren't manually deleted</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>📊 Results Look Wrong</h4>
                <p><strong>Solutions:</strong></p>
                <ul>
                  <li>Verify substats were correctly selected</li>
                  <li>Check weapon types match your intent</li>
                  <li>Ensure multiplier is set appropriately</li>
                  <li>Many draws are normal for similar builds</li>
                </ul>
              </div>

              <div className="help-tip">
                <strong>💡 Pro Tip:</strong> Check the TROUBLESHOOTING.md file in the application directory for detailed solutions.
              </div>
            </div>
          )}

          {activeTab === 'about' && (
            <div className="help-section">
              <div className="about-header">
                <div className="about-icon">🏆</div>
                <h3>Tournament Pro</h3>
                <p className="version">Version 1.0.0</p>
              </div>

              <div className="help-item">
                <h4>What is Tournament Pro?</h4>
                <p>
                  Tournament Pro is a desktop application for running PvP build tournaments.
                  It simulates battles between different character builds to determine which
                  combinations of stats and equipment are most effective in player-versus-player combat.
                </p>
              </div>

              <div className="help-item">
                <h4>Key Features</h4>
                <ul>
                  <li>⚡ <strong>Multi-threaded:</strong> Uses all CPU cores for fast results</li>
                  <li>💾 <strong>Auto-save:</strong> Automatic checkpoints prevent data loss</li>
                  <li>📊 <strong>Detailed Results:</strong> Export in HTML, JSON, or TXT</li>
                  <li>🎨 <strong>User-Friendly:</strong> No coding required</li>
                  <li>🔄 <strong>Checkpoint Recovery:</strong> Resume after crashes</li>
                  <li>🌐 <strong>Cross-Platform:</strong> Windows, macOS, Linux</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>System Requirements</h4>
                <ul>
                  <li><strong>OS:</strong> Windows 10+, macOS 10.13+, Linux (Ubuntu 18.04+)</li>
                  <li><strong>RAM:</strong> 4GB minimum (8GB recommended)</li>
                  <li><strong>Disk:</strong> 1GB free space</li>
                  <li><strong>CPU:</strong> Multi-core processor recommended</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>Documentation</h4>
                <p>Additional documentation files:</p>
                <ul>
                  <li><strong>USER_GUIDE.md:</strong> Complete user guide</li>
                  <li><strong>QUICK_START.md:</strong> Quick start guide</li>
                  <li><strong>TROUBLESHOOTING.md:</strong> Detailed troubleshooting</li>
                  <li><strong>README.md:</strong> Technical documentation</li>
                </ul>
              </div>

              <div className="help-item">
                <h4>License</h4>
                <p>
                  Tournament Pro is provided as-is for personal and clan use.
                  See LICENSE file for details.
                </p>
              </div>

              <div className="about-footer">
                <p>© 2024 Tournament Pro. All rights reserved.</p>
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="help-footer">
          <button className="button button-primary" onClick={onClose}>
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default HelpDialog;
