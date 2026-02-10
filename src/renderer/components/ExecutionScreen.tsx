import React, { useState } from 'react';
import { TournamentConfig, TournamentProgress, TournamentResult } from '@shared/types';

interface Props {
  config: TournamentConfig;
  progress: TournamentProgress | null;
  results?: TournamentResult[] | null;
  isComplete?: boolean;
  onPause: () => void;
  onResume: () => void;
  onCancel: () => void;
  onExportResults?: (format: 'html' | 'json' | 'txt') => void;
  onOpenResults?: () => void;
}

const ExecutionScreen: React.FC<Props> = ({ 
  config, 
  progress, 
  results,
  isComplete = false,
  onPause, 
  onResume, 
  onCancel,
  onExportResults,
  onOpenResults
}) => {
  const [isPaused, setIsPaused] = useState(false);
  const [showCancelConfirm, setShowCancelConfirm] = useState(false);

  const formatTime = (seconds: number): string => {
    // Handle invalid or infinite values
    if (!isFinite(seconds) || seconds < 0) {
      return '—';
    }
    
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = Math.floor(seconds % 60);
    return `${hours}h ${minutes}m ${secs}s`;
  };

  const formatNumber = (num: number): string => {
    return num.toLocaleString();
  };

  const getStatusIcon = (status: string): string => {
    switch (status) {
      case 'running':
        return '🏃';
      case 'idle':
        return '⏸️';
      case 'completed':
        return '✅';
      case 'error':
        return '❌';
      default:
        return '⏳';
    }
  };

  const getStatusColor = (status: string): string => {
    switch (status) {
      case 'running':
        return '#28a745';
      case 'idle':
        return '#ffc107';
      case 'completed':
        return '#007bff';
      case 'error':
        return '#dc3545';
      default:
        return '#6c757d';
    }
  };

  const handlePause = () => {
    setIsPaused(true);
    onPause();
  };

  const handleResume = () => {
    setIsPaused(false);
    onResume();
  };

  const handleCancelClick = () => {
    setShowCancelConfirm(true);
  };

  const handleCancelConfirm = () => {
    setShowCancelConfirm(false);
    onCancel();
  };

  const handleCancelCancel = () => {
    setShowCancelConfirm(false);
  };

  // Determine if tournament is actively running
  const isRunning = progress && progress.workerStatus.some(w => w.status === 'running');

  // Get top builds for preview
  const topBuilds = results ? results.slice(0, 10) : [];

  return (
    <div className="screen">
      {/* Results Display - Show when tournament is complete */}
      {isComplete && results && results.length > 0 && (
        <div className="results-section">
          <div className="screen-header">
            <h1>✅ Tournament Complete!</h1>
            <p>Results are ready for review and export</p>
          </div>

          {/* Results Summary */}
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Total Builds</h3>
              <div className="value">{formatNumber(results.length)}</div>
            </div>

            <div className="stat-card">
              <h3>Total Battles</h3>
              <div className="value">{progress ? formatNumber(progress.totalBattles) : '—'}</div>
            </div>

            <div className="stat-card">
              <h3>Total Time</h3>
              <div className="value">{progress ? formatTime(progress.elapsed) : '—'}</div>
            </div>

            <div className="stat-card">
              <h3>Avg Speed</h3>
              <div className="value">
                {progress && isFinite(progress.speed) && progress.speed > 0 
                  ? formatNumber(Math.round(progress.speed))
                  : '—'}
              </div>
              <div style={{ fontSize: '0.9em', color: '#666', marginTop: '5px' }}>
                battles/sec
              </div>
            </div>
          </div>

          {/* Top Builds Preview */}
          <div className="top-builds-section">
            <h3 style={{ marginBottom: '15px' }}>🏆 Top 10 Builds</h3>
            <div className="top-builds-list">
              {topBuilds.map((result, index) => (
                <div key={index} className="top-build-item">
                  <div className="build-rank">
                    {index === 0 && '🥇'}
                    {index === 1 && '🥈'}
                    {index === 2 && '🥉'}
                    {index > 2 && `#${index + 1}`}
                  </div>
                  <div className="build-info">
                    <div className="build-description">
                      {result.build.description}
                    </div>
                    <div className="build-stats">
                      <span className="stat-badge">
                        {result.build.weaponType === 'melee' ? '⚔️' : '🏹'} {result.build.weaponType}
                      </span>
                      <span className="stat-badge">
                        DPS: {result.build.dps.toFixed(1)}
                      </span>
                      <span className="stat-badge">
                        HP: {formatNumber(Math.round(result.build.maxHP))}
                      </span>
                    </div>
                  </div>
                  <div className="build-results">
                    <div className="win-rate" style={{ 
                      color: result.winRate >= 60 ? '#28a745' : result.winRate >= 50 ? '#ffc107' : '#dc3545'
                    }}>
                      {result.winRate.toFixed(1)}%
                    </div>
                    <div className="record">
                      {result.wins}W - {result.losses}L - {result.draws}D
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Export Options */}
          <div className="export-section">
            <h3 style={{ marginBottom: '15px' }}>📤 Export Results</h3>
            <div className="button-group">
              {onExportResults && (
                <>
                  <button 
                    className="button button-secondary" 
                    onClick={() => onExportResults('html')}
                    title="Export as HTML file"
                  >
                    📄 Export HTML
                  </button>
                  <button 
                    className="button button-secondary" 
                    onClick={() => onExportResults('json')}
                    title="Export as JSON file"
                  >
                    📋 Export JSON
                  </button>
                  <button 
                    className="button button-secondary" 
                    onClick={() => onExportResults('txt')}
                    title="Export as text file"
                  >
                    📝 Export TXT
                  </button>
                </>
              )}
              {onOpenResults && (
                <button 
                  className="button button-primary" 
                  onClick={onOpenResults}
                  title="Open results directory"
                >
                  📁 Open Results Folder
                </button>
              )}
            </div>
          </div>

          {/* Return to Configuration */}
          <div style={{ marginTop: '30px', textAlign: 'center' }}>
            <button 
              className="button button-primary" 
              onClick={() => window.location.reload()}
              title="Start a new tournament"
            >
              🔄 New Tournament
            </button>
          </div>
        </div>
      )}

      {/* Running/Paused Tournament Display */}
      {!isComplete && (
        <>
          {/* Cancel Confirmation Dialog */}
          {showCancelConfirm && (
        <div className="checkpoint-dialog-overlay">
          <div className="checkpoint-dialog">
            <div className="checkpoint-dialog-header">
              <h2>⚠️ Cancel Tournament</h2>
            </div>
            <div className="checkpoint-dialog-content">
              <p className="checkpoint-message">
                Are you sure you want to cancel the tournament?
              </p>
              <div className="checkpoint-warning">
                <strong>Warning:</strong>
                <p>
                  The tournament will be stopped and a checkpoint will be saved. 
                  You can resume from this checkpoint later, but any in-progress 
                  battles will need to be restarted.
                </p>
              </div>
            </div>
            <div className="checkpoint-dialog-actions">
              <button className="btn btn-secondary" onClick={handleCancelCancel}>
                Continue Tournament
              </button>
              <button className="btn btn-warning" onClick={handleCancelConfirm}>
                Cancel Tournament
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="screen-header">
        <h1>
          {isPaused ? '⏸️ Tournament Paused' : '🏃 Tournament Running'}
        </h1>
        <p>
          {isPaused 
            ? 'Tournament execution is paused. Click Resume to continue.'
            : 'Multi-threaded PvP tournament in progress'}
        </p>
        {!isPaused && progress && (
          <div style={{ 
            fontSize: '0.85em', 
            color: '#666', 
            marginTop: '8px',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            justifyContent: 'center'
          }}>
            <span style={{ 
              display: 'inline-block',
              width: '8px',
              height: '8px',
              borderRadius: '50%',
              backgroundColor: '#28a745',
              animation: 'pulse 2s ease-in-out infinite'
            }} />
            <span>Live updates active</span>
          </div>
        )}
      </div>

      {progress && (
        <>
          {/* Progress Bar */}
          <div className="progress-container">
            <div className="progress-bar">
              <div 
                className="progress-fill" 
                style={{ 
                  width: `${progress.progress}%`,
                  background: isPaused 
                    ? 'linear-gradient(90deg, #ffc107 0%, #ff9800 100%)'
                    : 'linear-gradient(90deg, #667eea 0%, #764ba2 100%)'
                }}
              >
                {progress.progress.toFixed(2)}%
              </div>
            </div>
          </div>

          {/* Statistics Grid */}
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Completed Battles</h3>
              <div className="value">{formatNumber(progress.completedBattles)}</div>
              <div style={{ fontSize: '0.9em', color: '#666', marginTop: '5px' }}>
                of {formatNumber(progress.totalBattles)}
              </div>
            </div>

            <div className="stat-card">
              <h3>Speed</h3>
              <div className="value">
                {isPaused ? '—' : (isFinite(progress.speed) && progress.speed > 0 
                  ? formatNumber(Math.round(progress.speed))
                  : '—')}
              </div>
              <div style={{ fontSize: '0.9em', color: '#666', marginTop: '5px' }}>
                battles/sec
              </div>
            </div>

            <div className="stat-card">
              <h3>Elapsed Time</h3>
              <div className="value">{formatTime(progress.elapsed)}</div>
            </div>

            <div className="stat-card">
              <h3>Time Remaining</h3>
              <div className="value">
                {isPaused ? '—' : formatTime(progress.remaining)}
              </div>
            </div>
          </div>

          {/* Worker Status Section */}
          <div className="worker-status">
            <h3 style={{ marginBottom: '15px', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span>Worker Status</span>
              <span style={{ fontSize: '0.8em', color: '#666', fontWeight: 'normal' }}>
                ({progress.workerStatus.filter(w => w.status === 'running').length} active)
              </span>
            </h3>
            <div style={{ display: 'grid', gap: '10px' }}>
              {progress.workerStatus.map(worker => (
                <div key={worker.id} className={`worker-item ${worker.status}`}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{ fontSize: '1.5em' }}>
                      {getStatusIcon(worker.status)}
                    </span>
                    <div>
                      <strong>Worker {worker.id}</strong>
                      <span 
                        style={{ 
                          marginLeft: '10px', 
                          color: getStatusColor(worker.status),
                          fontWeight: '600',
                          textTransform: 'capitalize'
                        }}
                      >
                        {worker.status}
                      </span>
                    </div>
                  </div>
                  <div style={{ textAlign: 'right' }}>
                    <div>
                      {formatNumber(worker.completedBattles)} battles
                    </div>
                    <div style={{ fontSize: '0.9em', color: '#666' }}>
                      {worker.status === 'running' && isFinite(worker.speed) && worker.speed > 0
                        ? `${formatNumber(Math.round(worker.speed))} /sec`
                        : '—'}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}

      {!progress && (
        <div style={{ textAlign: 'center', padding: '40px', color: '#666' }}>
          <div style={{ fontSize: '3em', marginBottom: '20px' }}>⏳</div>
          <p style={{ fontSize: '1.2em' }}>Initializing tournament...</p>
          <p style={{ fontSize: '0.9em', marginTop: '10px' }}>
            Generating builds and preparing workers
          </p>
        </div>
      )}

      {/* Control Buttons */}
      <div className="button-group">
        {!isPaused && isRunning && (
          <button 
            className="button button-secondary" 
            onClick={handlePause}
            title="Pause the tournament"
          >
            ⏸️ Pause
          </button>
        )}
        {isPaused && (
          <button 
            className="button button-primary" 
            onClick={handleResume}
            title="Resume the tournament"
          >
            ▶️ Resume
          </button>
        )}
        <button 
          className="button button-danger" 
          onClick={handleCancelClick}
          title="Cancel the tournament (checkpoint will be saved)"
        >
          ❌ Cancel Tournament
        </button>
      </div>

      {/* Configuration Summary */}
      <div style={{ 
        marginTop: '30px', 
        padding: '20px', 
        background: '#f5f7fa', 
        borderRadius: '12px',
        border: '1px solid #e0e0e0'
      }}>
        <h4 style={{ marginBottom: '15px', color: '#333' }}>
          📋 Tournament Configuration
        </h4>
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '15px',
          fontSize: '0.9em'
        }}>
          <div>
            <div style={{ color: '#666', marginBottom: '5px' }}>Workers</div>
            <div style={{ fontWeight: '600', color: '#333' }}>
              {config.maxWorkers} threads
            </div>
          </div>
          <div>
            <div style={{ color: '#666', marginBottom: '5px' }}>Substat Multiplier</div>
            <div style={{ fontWeight: '600', color: '#333' }}>
              {(config.substatMultiplier * 100).toFixed(0)}%
            </div>
          </div>
          <div>
            <div style={{ color: '#666', marginBottom: '5px' }}>Target Builds</div>
            <div style={{ fontWeight: '600', color: '#333' }}>
              {formatNumber(config.targetBuilds)}
            </div>
          </div>
          <div>
            <div style={{ color: '#666', marginBottom: '5px' }}>Checkpoint Interval</div>
            <div style={{ fontWeight: '600', color: '#333' }}>
              {config.checkpointInterval}s
            </div>
          </div>
        </div>
        <div style={{ marginTop: '15px', paddingTop: '15px', borderTop: '1px solid #e0e0e0' }}>
          <div style={{ color: '#666', marginBottom: '5px' }}>Output Directory</div>
          <div style={{ 
            fontFamily: 'monospace', 
            fontSize: '0.85em',
            color: '#333',
            background: 'white',
            padding: '8px 12px',
            borderRadius: '6px',
            wordBreak: 'break-all'
          }}>
            {config.outputDirectory}
          </div>
        </div>
      </div>
        </>
      )}
    </div>
  );
};

export default ExecutionScreen;
