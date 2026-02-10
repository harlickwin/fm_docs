/**
 * Checkpoint Manager
 * Handles saving and loading tournament state with periodic saving and rotation
 */

import * as fs from 'fs/promises';
import * as path from 'path';
import { TournamentState } from '../../shared/types';
import { CHECKPOINT_VERSION } from '../../shared/constants';

const MAX_CHECKPOINT_FILES = 3; // Keep last 3 checkpoints for safety
const CHECKPOINT_DIR = '.tournament-checkpoints';

export class CheckpointManager {
  private outputDirectory: string;
  private checkpointDir: string;
  private checkpointPath: string;
  private isSaving: boolean = false;
  private pendingSave: TournamentState | null = null;
  
  constructor(outputDirectory: string) {
    this.outputDirectory = outputDirectory;
    this.checkpointDir = path.join(outputDirectory, CHECKPOINT_DIR);
    this.checkpointPath = path.join(this.checkpointDir, 'current.json');
  }
  
  /**
   * Initialize checkpoint directory
   */
  private async ensureCheckpointDirectory(): Promise<void> {
    try {
      await fs.mkdir(this.checkpointDir, { recursive: true });
    } catch (error) {
      console.error('Failed to create checkpoint directory:', error);
      throw error;
    }
  }
  
  /**
   * Save tournament state to checkpoint file (non-blocking)
   * If a save is already in progress, queue the new state
   */
  async save(state: TournamentState): Promise<void> {
    // If already saving, queue this state for next save
    if (this.isSaving) {
      this.pendingSave = state;
      return;
    }
    
    this.isSaving = true;
    
    try {
      await this.performSave(state);
      
      // If there's a pending save, process it now
      if (this.pendingSave) {
        const nextState = this.pendingSave;
        this.pendingSave = null;
        await this.performSave(nextState);
      }
    } finally {
      this.isSaving = false;
    }
  }
  
  /**
   * Perform the actual save operation
   */
  private async performSave(state: TournamentState): Promise<void> {
    try {
      // Ensure checkpoint directory exists
      await this.ensureCheckpointDirectory();
      
      // Rotate existing checkpoints before saving new one
      await this.rotateCheckpoints();
      
      // Write to temporary file first (atomic write)
      const tempPath = `${this.checkpointPath}.tmp`;
      const data = JSON.stringify(state, null, 2);
      
      await fs.writeFile(tempPath, data, 'utf-8');
      
      // Rename to final path (atomic operation)
      await fs.rename(tempPath, this.checkpointPath);
      
      console.log(`Checkpoint saved: ${this.checkpointPath}`);
    } catch (error) {
      console.error('Failed to save checkpoint:', error);
      throw error;
    }
  }
  
  /**
   * Rotate checkpoint files to maintain history
   * Keeps the last MAX_CHECKPOINT_FILES checkpoints
   */
  private async rotateCheckpoints(): Promise<void> {
    try {
      // Check if current checkpoint exists
      const currentExists = await this.exists();
      if (!currentExists) {
        return;
      }
      
      // Shift existing backups
      for (let i = MAX_CHECKPOINT_FILES - 1; i > 0; i--) {
        const oldPath = path.join(this.checkpointDir, `backup-${i}.json`);
        const newPath = path.join(this.checkpointDir, `backup-${i + 1}.json`);
        
        try {
          await fs.access(oldPath);
          await fs.rename(oldPath, newPath);
        } catch {
          // File doesn't exist, skip
        }
      }
      
      // Move current to backup-1
      const backup1Path = path.join(this.checkpointDir, 'backup-1.json');
      await fs.copyFile(this.checkpointPath, backup1Path);
      
      // Delete oldest backup if it exceeds limit
      const oldestPath = path.join(this.checkpointDir, `backup-${MAX_CHECKPOINT_FILES + 1}.json`);
      try {
        await fs.unlink(oldestPath);
      } catch {
        // File doesn't exist, ignore
      }
    } catch (error) {
      console.error('Failed to rotate checkpoints:', error);
      // Don't throw - rotation failure shouldn't prevent saving
    }
  }
  
  /**
   * Load tournament state from checkpoint file
   */
  async load(): Promise<TournamentState | null> {
    try {
      const data = await fs.readFile(this.checkpointPath, 'utf-8');
      const state = JSON.parse(data) as TournamentState;
      
      // Validate checkpoint
      if (!this.validate(state)) {
        console.error('Invalid checkpoint file');
        return null;
      }
      
      console.log(`Checkpoint loaded: ${this.checkpointPath}`);
      return state;
    } catch (error) {
      if ((error as any).code === 'ENOENT') {
        // File doesn't exist
        return null;
      }
      
      console.error('Failed to load checkpoint:', error);
      return null;
    }
  }
  
  /**
   * Check if checkpoint exists
   */
  async exists(): Promise<boolean> {
    try {
      await fs.access(this.checkpointPath);
      return true;
    } catch {
      return false;
    }
  }
  
  /**
   * Delete checkpoint file and all backups
   */
  async cleanup(): Promise<void> {
    try {
      // Delete current checkpoint
      try {
        await fs.unlink(this.checkpointPath);
        console.log('Current checkpoint cleaned up');
      } catch (error) {
        if ((error as any).code !== 'ENOENT') {
          console.error('Failed to cleanup current checkpoint:', error);
        }
      }
      
      // Delete all backup checkpoints
      for (let i = 1; i <= MAX_CHECKPOINT_FILES; i++) {
        const backupPath = path.join(this.checkpointDir, `backup-${i}.json`);
        try {
          await fs.unlink(backupPath);
        } catch {
          // Ignore if file doesn't exist
        }
      }
      
      // Try to remove checkpoint directory if empty
      try {
        await fs.rmdir(this.checkpointDir);
        console.log('Checkpoint directory removed');
      } catch {
        // Directory not empty or doesn't exist, ignore
      }
    } catch (error) {
      console.error('Failed to cleanup checkpoints:', error);
    }
  }
  
  /**
   * Clean up old checkpoint files based on age
   * Removes backup files older than the specified age in days
   */
  async cleanupOldCheckpoints(maxAgeDays: number = 7): Promise<void> {
    try {
      const maxAgeMs = maxAgeDays * 24 * 60 * 60 * 1000;
      const now = Date.now();
      
      for (let i = 1; i <= MAX_CHECKPOINT_FILES; i++) {
        const backupPath = path.join(this.checkpointDir, `backup-${i}.json`);
        
        try {
          const stats = await fs.stat(backupPath);
          const age = now - stats.mtimeMs;
          
          if (age > maxAgeMs) {
            await fs.unlink(backupPath);
            console.log(`Deleted old checkpoint: backup-${i}.json (age: ${Math.floor(age / (24 * 60 * 60 * 1000))} days)`);
          }
        } catch {
          // File doesn't exist or can't be accessed, skip
        }
      }
    } catch (error) {
      console.error('Failed to cleanup old checkpoints:', error);
    }
  }
  
  /**
   * Validate checkpoint structure
   */
  validate(checkpoint: any): boolean {
    if (!checkpoint || typeof checkpoint !== 'object') {
      return false;
    }
    
    // Check required fields
    const requiredFields = [
      'version',
      'timestamp',
      'config',
      'builds',
      'completedBattles',
      'results',
      'nextBattleIndex',
      'totalBattles'
    ];
    
    for (const field of requiredFields) {
      if (!(field in checkpoint)) {
        console.error(`Missing required field: ${field}`);
        return false;
      }
    }
    
    // Check version compatibility
    if (checkpoint.version !== CHECKPOINT_VERSION) {
      console.error(`Incompatible checkpoint version: ${checkpoint.version}`);
      return false;
    }
    
    // Check data types
    if (!Array.isArray(checkpoint.builds)) {
      console.error('Invalid builds array');
      return false;
    }
    
    if (!Array.isArray(checkpoint.completedBattles)) {
      console.error('Invalid completedBattles array');
      return false;
    }
    
    if (typeof checkpoint.results !== 'object') {
      console.error('Invalid results object');
      return false;
    }
    
    if (typeof checkpoint.nextBattleIndex !== 'number') {
      console.error('Invalid nextBattleIndex');
      return false;
    }
    
    if (typeof checkpoint.totalBattles !== 'number') {
      console.error('Invalid totalBattles');
      return false;
    }
    
    return true;
  }
  
  /**
   * Get checkpoint info without loading full state
   */
  async getInfo(): Promise<{ timestamp: number; progress: number } | null> {
    try {
      const data = await fs.readFile(this.checkpointPath, 'utf-8');
      const state = JSON.parse(data) as TournamentState;
      
      const progress = (state.completedBattles.length / state.totalBattles) * 100;
      
      return {
        timestamp: state.timestamp,
        progress
      };
    } catch {
      return null;
    }
  }
  
  /**
   * List all available checkpoints (current + backups)
   */
  async listCheckpoints(): Promise<Array<{ path: string; timestamp: number; size: number }>> {
    const checkpoints: Array<{ path: string; timestamp: number; size: number }> = [];
    
    try {
      // Check current checkpoint
      try {
        const stats = await fs.stat(this.checkpointPath);
        const data = await fs.readFile(this.checkpointPath, 'utf-8');
        const state = JSON.parse(data) as TournamentState;
        
        checkpoints.push({
          path: this.checkpointPath,
          timestamp: state.timestamp,
          size: stats.size
        });
      } catch {
        // Current checkpoint doesn't exist
      }
      
      // Check backup checkpoints
      for (let i = 1; i <= MAX_CHECKPOINT_FILES; i++) {
        const backupPath = path.join(this.checkpointDir, `backup-${i}.json`);
        
        try {
          const stats = await fs.stat(backupPath);
          const data = await fs.readFile(backupPath, 'utf-8');
          const state = JSON.parse(data) as TournamentState;
          
          checkpoints.push({
            path: backupPath,
            timestamp: state.timestamp,
            size: stats.size
          });
        } catch {
          // Backup doesn't exist, skip
        }
      }
    } catch (error) {
      console.error('Failed to list checkpoints:', error);
    }
    
    return checkpoints.sort((a, b) => b.timestamp - a.timestamp);
  }
  
  /**
   * Get total size of all checkpoint files
   */
  async getTotalCheckpointSize(): Promise<number> {
    const checkpoints = await this.listCheckpoints();
    return checkpoints.reduce((total, cp) => total + cp.size, 0);
  }
}
