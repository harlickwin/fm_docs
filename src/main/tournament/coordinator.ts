/**
 * Tournament Coordinator
 * Manages worker threads and coordinates tournament execution
 */

import { Worker } from 'worker_threads';
import * as path from 'path';
import { EventEmitter } from 'events';
import {
  TournamentConfig,
  TournamentProgress,
  TournamentResult,
  BuildStats,
  BattleAssignment,
  WorkerStatus,
  CompletedBattle
} from '../../shared/types';
import { CHECKPOINT_VERSION } from '../../shared/constants';
import { CheckpointManager } from './checkpoint';
import { getOptimalWorkerCount, validateWorkerCount } from '../utils/system';

interface WorkerInfo {
  worker: Worker;
  status: WorkerStatus;
  currentAssignment: BattleAssignment[] | null;
}

export class TournamentCoordinator extends EventEmitter {
  private config: TournamentConfig;
  private builds: BuildStats[] = [];
  private workers: WorkerInfo[] = [];
  private checkpoint: CheckpointManager;
  
  private totalBattles: number = 0;
  private completedBattles: number = 0;
  private nextBattleIndex: number = 0;
  private results: Map<string, TournamentResult> = new Map();
  private completedBattlesList: CompletedBattle[] = [];
  
  private isRunning: boolean = false;
  private isPaused: boolean = false;
  private startTime: number = 0;
  private lastProgressUpdate: number = 0;
  private lastCheckpointTime: number = 0;
  private checkpointTimer: NodeJS.Timeout | null = null;
  
  constructor(config: TournamentConfig) {
    super();
    this.config = config;
    this.checkpoint = new CheckpointManager(config.outputDirectory);
  }
  
  /**
   * Start the tournament
   */
  async start(builds: BuildStats[]): Promise<void> {
    if (this.isRunning) {
      throw new Error('Tournament is already running');
    }
    
    this.builds = builds;
    this.totalBattles = this.calculateTotalBattles(builds.length);
    this.isRunning = true;
    this.isPaused = false;
    this.startTime = Date.now();
    this.lastCheckpointTime = Date.now();
    
    // Initialize results map
    this.initializeResults();
    
    // Create worker pool
    await this.createWorkers();
    
    // Start distributing work
    this.distributeWork();
    
    // Start checkpoint timer
    this.startCheckpointTimer();
  }
  
  /**
   * Resume from checkpoint
   */
  async resume(): Promise<void> {
    const state = await this.checkpoint.load();
    if (!state) {
      throw new Error('No checkpoint found to resume from');
    }
    
    this.config = state.config;
    this.builds = state.builds;
    this.totalBattles = state.totalBattles;
    this.completedBattles = state.completedBattles.length;
    this.nextBattleIndex = state.nextBattleIndex;
    this.completedBattlesList = state.completedBattles;
    
    // Restore results
    this.results = new Map(Object.entries(state.results));
    
    this.isRunning = true;
    this.isPaused = false;
    this.startTime = Date.now();
    this.lastCheckpointTime = Date.now();
    
    // Create worker pool
    await this.createWorkers();
    
    // Start distributing work
    this.distributeWork();
    
    // Start checkpoint timer
    this.startCheckpointTimer();
  }
  
  /**
   * Pause the tournament
   */
  async pause(): Promise<void> {
    if (!this.isRunning || this.isPaused) {
      return;
    }
    
    this.isPaused = true;
    
    // Send pause message to all workers
    for (const workerInfo of this.workers) {
      workerInfo.worker.postMessage({ type: 'pause' });
    }
    
    // Save checkpoint
    await this.saveCheckpoint();
  }
  
  /**
   * Resume from pause
   */
  resumeFromPause(): void {
    if (!this.isRunning || !this.isPaused) {
      return;
    }
    
    this.isPaused = false;
    
    // Send resume message to all workers
    for (const workerInfo of this.workers) {
      workerInfo.worker.postMessage({ type: 'resume' });
    }
  }
  
  /**
   * Cancel the tournament
   */
  async cancel(): Promise<void> {
    if (!this.isRunning) {
      return;
    }
    
    this.isRunning = false;
    this.isPaused = false;
    
    // Stop checkpoint timer
    if (this.checkpointTimer) {
      clearInterval(this.checkpointTimer);
      this.checkpointTimer = null;
    }
    
    // Terminate all workers
    for (const workerInfo of this.workers) {
      await workerInfo.worker.terminate();
    }
    
    this.workers = [];
    this.emit('cancelled');
  }
  
  /**
   * Create worker pool
   */
  private async createWorkers(): Promise<void> {
    // Use configured worker count or optimal default
    const requestedWorkers = this.config.maxWorkers || getOptimalWorkerCount();
    const workerCount = validateWorkerCount(requestedWorkers);
    
    console.log(`Creating ${workerCount} worker threads (${requestedWorkers} requested)`);
    
    const workerPath = path.join(__dirname, 'worker.js');
    
    for (let i = 0; i < workerCount; i++) {
      const worker = new Worker(workerPath, {
        workerData: {
          workerId: i,
          config: this.config
        }
      });
      
      const workerInfo: WorkerInfo = {
        worker,
        status: {
          id: i,
          status: 'idle',
          completedBattles: 0,
          speed: 0
        },
        currentAssignment: null
      };
      
      // Set up message handler
      worker.on('message', (message) => this.handleWorkerMessage(i, message));
      
      // Set up error handler
      worker.on('error', (error) => this.handleWorkerError(i, error));
      
      // Set up exit handler
      worker.on('exit', (code) => this.handleWorkerExit(i, code));
      
      this.workers.push(workerInfo);
    }
  }
  
  /**
   * Check if all workers are complete
   */
  private allWorkersComplete(): boolean {
    return this.workers.every(w => w.status.status === 'completed' || w.status.status === 'idle') &&
           this.nextBattleIndex >= this.totalBattles;
  }
  
  /**
   * Calculate total number of battles (round-robin)
   */
  private calculateTotalBattles(buildCount: number): number {
    return (buildCount * (buildCount - 1)) / 2;
  }
  
  /**
   * Initialize results map
   */
  private initializeResults(): void {
    for (const build of this.builds) {
      const key = this.getBuildKey(build);
      this.results.set(key, {
        build,
        wins: 0,
        losses: 0,
        draws: 0,
        winRate: 0,
        avgBattleDuration: 0,
        totalDamageDealt: 0
      });
    }
  }
  
  /**
   * Distribute work to idle workers
   */
  private distributeWork(): void {
    if (!this.isRunning || this.isPaused) {
      return;
    }
    
    for (let i = 0; i < this.workers.length; i++) {
      const workerInfo = this.workers[i];
      
      if (workerInfo.status.status === 'idle' && this.nextBattleIndex < this.totalBattles) {
        // Assign batch of battles to worker
        const batchSize = Math.min(1000, this.totalBattles - this.nextBattleIndex);
        const assignments: BattleAssignment[] = [];
        
        for (let j = 0; j < batchSize; j++) {
          const battleIndex = this.nextBattleIndex + j;
          const { build1Index, build2Index } = this.getBattleIndices(battleIndex);
          
          // Check if this battle was already completed (from checkpoint)
          const alreadyCompleted = this.completedBattlesList.some(
            b => b.build1Index === build1Index && b.build2Index === build2Index
          );
          
          if (!alreadyCompleted) {
            assignments.push({
              build1Index,
              build2Index,
              battleId: `${build1Index}-${build2Index}`
            });
          }
        }
        
        if (assignments.length > 0) {
          workerInfo.currentAssignment = assignments;
          workerInfo.status.status = 'running';
          
          workerInfo.worker.postMessage({
            type: 'start',
            battles: assignments,
            builds: this.builds
          });
        }
        
        this.nextBattleIndex += batchSize;
      }
    }
  }
  
  /**
   * Get build indices for a battle index
   */
  private getBattleIndices(battleIndex: number): { build1Index: number; build2Index: number } {
    let count = 0;
    const n = this.builds.length;
    
    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        if (count === battleIndex) {
          return { build1Index: i, build2Index: j };
        }
        count++;
      }
    }
    
    throw new Error(`Invalid battle index: ${battleIndex}`);
  }
  
  /**
   * Handle message from worker
   */
  private handleWorkerMessage(workerId: number, message: any): void {
    const workerInfo = this.workers[workerId];
    
    switch (message.type) {
      case 'progress':
        workerInfo.status.completedBattles += message.completedBattles;
        workerInfo.status.speed = message.speed;
        this.completedBattles += message.completedBattles;
        
        // Update results
        if (message.results) {
          for (const [key, result] of Object.entries(message.results)) {
            const existing = this.results.get(key);
            if (existing) {
              existing.wins += (result as any).wins;
              existing.losses += (result as any).losses;
              existing.draws += (result as any).draws;
            }
          }
        }
        
        // Add to completed battles list
        if (message.completedBattlesList) {
          this.completedBattlesList.push(...message.completedBattlesList);
        }
        
        this.sendProgressUpdate();
        break;
        
      case 'complete':
        workerInfo.status.status = 'completed';
        workerInfo.currentAssignment = null;
        
        // Update results
        if (message.results) {
          for (const [key, result] of Object.entries(message.results)) {
            const existing = this.results.get(key);
            if (existing) {
              existing.wins += (result as any).wins;
              existing.losses += (result as any).losses;
              existing.draws += (result as any).draws;
            }
          }
        }
        
        // Add to completed battles list
        if (message.completedBattlesList) {
          this.completedBattlesList.push(...message.completedBattlesList);
        }
        
        // Check if all workers are done
        if (this.allWorkersComplete()) {
          this.handleTournamentComplete();
        } else {
          // Assign more work
          workerInfo.status.status = 'idle';
          this.distributeWork();
        }
        break;
        
      case 'error':
        this.handleWorkerError(workerId, new Error(message.error));
        break;
    }
  }
  
  /**
   * Handle worker error
   */
  private handleWorkerError(workerId: number, error: Error): void {
    console.error(`Worker ${workerId} error:`, error);
    this.workers[workerId].status.status = 'error';
    this.emit('error', error);
  }
  
  /**
   * Handle worker exit
   */
  private handleWorkerExit(workerId: number, code: number): void {
    if (code !== 0 && this.isRunning) {
      console.error(`Worker ${workerId} exited with code ${code}`);
      // TODO: Restart worker if needed
    }
  }
  
  /**
   * Send progress update to renderer
   */
  private sendProgressUpdate(): void {
    const now = Date.now();
    if (now - this.lastProgressUpdate < 1000) {
      return; // Throttle updates to 1 per second
    }
    
    this.lastProgressUpdate = now;
    
    const elapsed = (now - this.startTime) / 1000;
    const progress = (this.completedBattles / this.totalBattles) * 100;
    const speed = this.completedBattles / elapsed;
    const remaining = (this.totalBattles - this.completedBattles) / speed;
    
    const progressData: TournamentProgress = {
      totalBattles: this.totalBattles,
      completedBattles: this.completedBattles,
      progress,
      speed,
      elapsed,
      remaining,
      workerStatus: this.workers.map(w => w.status)
    };
    
    this.emit('progress', progressData);
  }
  
  /**
   * Start checkpoint timer with configurable interval
   */
  private startCheckpointTimer(): void {
    // Use configured interval (in seconds), default to 5 minutes
    const checkpointIntervalMs = (this.config.checkpointInterval || 300) * 1000;
    
    console.log(`Starting checkpoint timer with ${this.config.checkpointInterval || 300}s interval`);
    
    // Clear any existing timer
    if (this.checkpointTimer) {
      clearInterval(this.checkpointTimer);
    }
    
    // Set up periodic checkpoint saving
    this.checkpointTimer = setInterval(async () => {
      if (!this.isRunning || this.isPaused) {
        return;
      }
      
      const now = Date.now();
      if (now - this.lastCheckpointTime >= checkpointIntervalMs) {
        console.log('Periodic checkpoint triggered');
        await this.saveCheckpoint();
        this.lastCheckpointTime = now;
      }
    }, 10000); // Check every 10 seconds if checkpoint is due
  }
  
  /**
   * Stop checkpoint timer
   */
  private stopCheckpointTimer(): void {
    if (this.checkpointTimer) {
      clearInterval(this.checkpointTimer);
      this.checkpointTimer = null;
    }
  }
  
  /**
   * Save checkpoint (non-blocking background save)
   */
  private async saveCheckpoint(): Promise<void> {
    try {
      const state = {
        version: CHECKPOINT_VERSION,
        timestamp: Date.now(),
        config: this.config,
        builds: this.builds,
        completedBattles: this.completedBattlesList,
        results: Object.fromEntries(this.results),
        nextBattleIndex: this.nextBattleIndex,
        totalBattles: this.totalBattles
      };
      
      // Save asynchronously - won't block tournament execution
      await this.checkpoint.save(state);
      console.log(`Checkpoint saved at ${new Date().toISOString()}`);
    } catch (error) {
      console.error('Failed to save checkpoint:', error);
      // Don't throw - checkpoint failure shouldn't stop tournament
    }
  }
  
  /**
   * Handle tournament completion
   */
  private async handleTournamentComplete(): Promise<void> {
    this.isRunning = false;
    
    // Stop checkpoint timer
    this.stopCheckpointTimer();
    
    // Calculate final win rates
    for (const result of this.results.values()) {
      const totalGames = result.wins + result.losses + result.draws;
      result.winRate = totalGames > 0 ? (result.wins / totalGames) * 100 : 0;
    }
    
    // Terminate workers
    for (const workerInfo of this.workers) {
      await workerInfo.worker.terminate();
    }
    
    this.workers = [];
    
    // Clean up checkpoint and all backups
    await this.checkpoint.cleanup();
    
    // Emit completion event
    this.emit('complete', Array.from(this.results.values()));
  }
  
  /**
   * Get build key for results map
   */
  private getBuildKey(build: BuildStats): string {
    return build.description;
  }
}
