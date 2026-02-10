import React, { useState, useEffect } from 'react';
import ConfigurationScreen from './components/ConfigurationScreen';
import ExecutionScreen from './components/ExecutionScreen';
import { CheckpointRecoveryDialog } from './components/CheckpointRecoveryDialog';
import { TournamentConfig, TournamentProgress } from '@shared/types';
import './styles/App.css';

type AppScreen = 'config' | 'execution' | 'results';

interface CheckpointInfo {
  outputDirectory: string;
  timestamp: number;
  progress: number;
  config: TournamentConfig;
}

const App: React.FC = () => {
  const [screen, setScreen] = useState<AppScreen>('config');
  const [config, setConfig] = useState<TournamentConfig | null>(null);
  const [progress, setProgress] = useState<TournamentProgress | null>(null);
  const [checkpointInfo, setCheckpointInfo] = useState<CheckpointInfo | null>(null);
  const [showCheckpointDialog, setShowCheckpointDialog] = useState(false);

  useEffect(() => {
    // Listen for progress updates
    const unsubProgress = window.tournamentAPI.onProgress((progressData) => {
      setProgress(progressData);
    });

    // Listen for completion
    const unsubComplete = window.tournamentAPI.onComplete((results) => {
      alert('Tournament complete! Results saved.');
      setScreen('config');
      setProgress(null);
    });

    // Listen for errors
    const unsubError = window.tournamentAPI.onError((error) => {
      alert(`Error: ${error}`);
    });

    // Listen for checkpoint found on startup
    const unsubCheckpoint = window.tournamentAPI.onCheckpointFound((info: CheckpointInfo) => {
      console.log('Checkpoint found:', info);
      setCheckpointInfo(info);
      setShowCheckpointDialog(true);
    });

    return () => {
      unsubProgress();
      unsubComplete();
      unsubError();
      unsubCheckpoint();
    };
  }, []);

  const handleStartTournament = async (tournamentConfig: TournamentConfig) => {
    setConfig(tournamentConfig);
    setScreen('execution');
    const result = await window.tournamentAPI.startTournament(tournamentConfig);
    if (!result.success) {
      alert(`Failed to start tournament: ${result.error}`);
      setScreen('config');
    }
  };

  const handlePause = async () => {
    await window.tournamentAPI.pauseTournament();
  };

  const handleResume = async () => {
    await window.tournamentAPI.resumeTournament();
  };

  const handleCancel = async () => {
    if (window.confirm('Are you sure you want to cancel the tournament?')) {
      await window.tournamentAPI.cancelTournament();
      setScreen('config');
      setProgress(null);
    }
  };

  const handleResumeFromCheckpoint = async () => {
    if (!checkpointInfo) return;
    
    setShowCheckpointDialog(false);
    setConfig(checkpointInfo.config);
    setScreen('execution');
    
    const result = await window.tournamentAPI.resumeFromCheckpoint(checkpointInfo.config);
    if (!result.success) {
      alert(`Failed to resume tournament: ${result.error}`);
      setScreen('config');
    }
  };

  const handleDiscardCheckpoint = async () => {
    if (!checkpointInfo) return;
    
    if (window.confirm('Are you sure you want to delete the checkpoint? This cannot be undone.')) {
      const result = await window.tournamentAPI.discardCheckpoint(checkpointInfo.outputDirectory);
      if (result.success) {
        setShowCheckpointDialog(false);
        setCheckpointInfo(null);
      } else {
        alert(`Failed to discard checkpoint: ${result.error}`);
      }
    }
  };

  const handleCancelCheckpointDialog = () => {
    setShowCheckpointDialog(false);
  };

  return (
    <div className="app">
      {showCheckpointDialog && checkpointInfo && (
        <CheckpointRecoveryDialog
          checkpointInfo={checkpointInfo}
          onResume={handleResumeFromCheckpoint}
          onDiscard={handleDiscardCheckpoint}
          onCancel={handleCancelCheckpointDialog}
        />
      )}
      
      {screen === 'config' && (
        <ConfigurationScreen onStart={handleStartTournament} />
      )}
      {screen === 'execution' && (
        <ExecutionScreen
          config={config!}
          progress={progress}
          onPause={handlePause}
          onResume={handleResume}
          onCancel={handleCancel}
        />
      )}
    </div>
  );
};

export default App;
