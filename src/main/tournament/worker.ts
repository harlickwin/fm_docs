/**
 * Worker Thread for Battle Simulation
 * Executes PvP battles independently
 */

import { parentPort, workerData } from 'worker_threads';
import {
  BuildStats,
  BattleAssignment,
  TournamentResult,
  CompletedBattle
} from '../../shared/types';
import {
  calculateDPS,
  calculateHealingPerSecond
} from '../../shared/calculations';
import {
  BASE_DAMAGE,
  BASE_HEALTH,
  MOUNT_DAMAGE_BONUS,
  MOUNT_HEALTH_BONUS,
  BATTLE_DURATION,
  BATTLE_TIME_STEP
} from '../../shared/constants';

interface WorkerMessage {
  type: 'start' | 'pause' | 'resume' | 'cancel';
  battles?: BattleAssignment[];
  builds?: BuildStats[];
}

interface PvPResult {
  winner: 'build1' | 'build2' | 'draw';
  build1FinalHP: number;
  build2FinalHP: number;
  battleDuration: number;
}

let isPaused = false;
let isCancelled = false;
let currentBuilds: BuildStats[] = [];
let results: Map<string, TournamentResult> = new Map();
let completedBattlesList: CompletedBattle[] = [];

/**
 * Simulate a 60-second PvP battle
 */
function simulatePvPBattle(build1: BuildStats, build2: BuildStats): PvPResult {
  let hp1 = build1.maxHP;
  let hp2 = build2.maxHP;
  
  let elapsedTime = 0;
  
  while (elapsedTime < BATTLE_DURATION) {
    // Apply damage and healing
    hp1 -= build2.dps * BATTLE_TIME_STEP;
    hp1 += build1.hps * BATTLE_TIME_STEP;
    hp1 = Math.min(hp1, build1.maxHP);
    
    hp2 -= build1.dps * BATTLE_TIME_STEP;
    hp2 += build2.hps * BATTLE_TIME_STEP;
    hp2 = Math.min(hp2, build2.maxHP);
    
    // Check for deaths
    if (hp1 <= 0 && hp2 <= 0) {
      return {
        winner: 'draw',
        build1FinalHP: 0,
        build2FinalHP: 0,
        battleDuration: elapsedTime
      };
    }
    
    if (hp1 <= 0) {
      return {
        winner: 'build2',
        build1FinalHP: 0,
        build2FinalHP: hp2,
        battleDuration: elapsedTime
      };
    }
    
    if (hp2 <= 0) {
      return {
        winner: 'build1',
        build1FinalHP: hp1,
        build2FinalHP: 0,
        battleDuration: elapsedTime
      };
    }
    
    elapsedTime += BATTLE_TIME_STEP;
  }
  
  // Timeout - determine winner by HP percentage
  const hp1Percent = (hp1 / build1.maxHP) * 100;
  const hp2Percent = (hp2 / build2.maxHP) * 100;
  
  if (Math.abs(hp1Percent - hp2Percent) < 0.1) {
    return {
      winner: 'draw',
      build1FinalHP: hp1,
      build2FinalHP: hp2,
      battleDuration: BATTLE_DURATION
    };
  }
  
  return {
    winner: hp1Percent > hp2Percent ? 'build1' : 'build2',
    build1FinalHP: hp1,
    build2FinalHP: hp2,
    battleDuration: BATTLE_DURATION
  };
}

/**
 * Process a batch of battles
 */
function processBattles(battles: BattleAssignment[], builds: BuildStats[]): void {
  currentBuilds = builds;
  results.clear();
  completedBattlesList = [];
  
  // Initialize results
  for (const build of builds) {
    const key = getBuildKey(build);
    results.set(key, {
      build,
      wins: 0,
      losses: 0,
      draws: 0,
      winRate: 0,
      avgBattleDuration: 0,
      totalDamageDealt: 0
    });
  }
  
  const startTime = Date.now();
  let completedCount = 0;
  let lastProgressReport = Date.now();
  
  for (const battle of battles) {
    // Check for pause or cancel
    if (isCancelled) {
      return;
    }
    
    while (isPaused) {
      // Busy wait during pause (not ideal but simple)
      // In production, use proper synchronization
    }
    
    const build1 = builds[battle.build1Index];
    const build2 = builds[battle.build2Index];
    
    // Simulate battle
    const result = simulatePvPBattle(build1, build2);
    
    // Update results
    const key1 = getBuildKey(build1);
    const key2 = getBuildKey(build2);
    
    const result1 = results.get(key1)!;
    const result2 = results.get(key2)!;
    
    if (result.winner === 'build1') {
      result1.wins++;
      result2.losses++;
      completedBattlesList.push({
        build1Index: battle.build1Index,
        build2Index: battle.build2Index,
        winner: 'build1'
      });
    } else if (result.winner === 'build2') {
      result1.losses++;
      result2.wins++;
      completedBattlesList.push({
        build1Index: battle.build1Index,
        build2Index: battle.build2Index,
        winner: 'build2'
      });
    } else {
      result1.draws++;
      result2.draws++;
      completedBattlesList.push({
        build1Index: battle.build1Index,
        build2Index: battle.build2Index,
        winner: 'draw'
      });
    }
    
    completedCount++;
    
    // Send progress update every 1000 battles or 5 seconds
    const now = Date.now();
    if (completedCount % 1000 === 0 || now - lastProgressReport >= 5000) {
      const elapsed = (now - startTime) / 1000;
      const speed = completedCount / elapsed;
      
      parentPort?.postMessage({
        type: 'progress',
        completedBattles: completedCount,
        speed,
        results: Object.fromEntries(results),
        completedBattlesList: completedBattlesList.slice()
      });
      
      lastProgressReport = now;
      completedBattlesList = []; // Clear after sending
    }
  }
  
  // Send final completion message
  parentPort?.postMessage({
    type: 'complete',
    completedBattles: completedCount,
    results: Object.fromEntries(results),
    completedBattlesList
  });
}

/**
 * Get build key for results map
 */
function getBuildKey(build: BuildStats): string {
  return build.description;
}

/**
 * Handle messages from main thread
 */
if (parentPort) {
  parentPort.on('message', (message: WorkerMessage) => {
    switch (message.type) {
      case 'start':
        if (message.battles && message.builds) {
          isPaused = false;
          isCancelled = false;
          processBattles(message.battles, message.builds);
        }
        break;
        
      case 'pause':
        isPaused = true;
        break;
        
      case 'resume':
        isPaused = false;
        break;
        
      case 'cancel':
        isCancelled = true;
        break;
    }
  });
}
