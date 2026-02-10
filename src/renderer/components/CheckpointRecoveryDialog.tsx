/**
 * Checkpoint Recovery Dialog
 * Prompts user to resume from checkpoint or start fresh
 */

import React from 'react';
import { TournamentConfig } from '../../shared/types';

interface CheckpointInfo {
  outputDirectory: string;
  timestamp: number;
  progress: number;
  config: TournamentConfig;
}

interface CheckpointRecoveryDialogProps {
  checkpointInfo: CheckpointInfo;
  onResume: () => void;
  onDiscard: () => void;
  onCancel: () => void;
}

export const CheckpointRecoveryDialog: React.FC<CheckpointRecoveryDialogProps> = ({
  checkpointInfo,
  onResume,
  onDiscard,
  onCancel
}) => {
  const formatTimestamp = (timestamp: number): string => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };

  const formatProgress = (progress: number): string => {
    return `${progress.toFixed(1)}%`;
  };

  return (
    <div className="checkpoint-dialog-overlay">
      <div className="checkpoint-dialog">
        <div className="checkpoint-dialog-header">
          <h2>🔄 Checkpoint Found</h2>
        </div>
        
        <div className="checkpoint-dialog-content">
          <p className="checkpoint-message">
            An incomplete tournament was found. Would you like to resume from where you left off?
          </p>
          
          <div className="checkpoint-info">
            <div className="checkpoint-info-row">
              <span className="checkpoint-label">Last Saved:</span>
              <span className="checkpoint-value">{formatTimestamp(checkpointInfo.timestamp)}</span>
            </div>
            
            <div className="checkpoint-info-row">
              <span className="checkpoint-label">Progress:</span>
              <span className="checkpoint-value">{formatProgress(checkpointInfo.progress)}</span>
            </div>
            
            <div className="checkpoint-info-row">
              <span className="checkpoint-label">Location:</span>
              <span className="checkpoint-value checkpoint-path">{checkpointInfo.outputDirectory}</span>
            </div>
            
            <div className="checkpoint-info-row">
              <span className="checkpoint-label">Target Builds:</span>
              <span className="checkpoint-value">{checkpointInfo.config.targetBuilds}</span>
            </div>
            
            <div className="checkpoint-info-row">
              <span className="checkpoint-label">Workers:</span>
              <span className="checkpoint-value">{checkpointInfo.config.maxWorkers}</span>
            </div>
          </div>
          
          <div className="checkpoint-warning">
            <strong>⚠️ Note:</strong> If you choose to start fresh, the checkpoint will be deleted and cannot be recovered.
          </div>
        </div>
        
        <div className="checkpoint-dialog-actions">
          <button 
            className="btn btn-primary"
            onClick={onResume}
            title="Continue from where you left off"
          >
            ▶️ Resume Tournament
          </button>
          
          <button 
            className="btn btn-warning"
            onClick={onDiscard}
            title="Delete checkpoint and start a new tournament"
          >
            🗑️ Start Fresh
          </button>
          
          <button 
            className="btn btn-secondary"
            onClick={onCancel}
            title="Close this dialog and decide later"
          >
            ❌ Cancel
          </button>
        </div>
      </div>
    </div>
  );
};
