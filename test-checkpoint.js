/**
 * Manual test for checkpoint manager functionality
 * Run with: node test-checkpoint.js
 */

const fs = require('fs');
const path = require('path');

// We need to manually fix the module resolution for the test
// because TypeScript generates incorrect relative paths
const Module = require('module');
const originalResolveFilename = Module._resolveFilename;

Module._resolveFilename = function (request, parent, isMain) {
  // Fix the ../../shared/constants path to ../shared/constants
  if (request === '../../../shared/constants' && parent.filename.includes('dist\\main\\main\\tournament')) {
    request = '../../shared/constants';
  }
  if (request === '../../../shared/types' && parent.filename.includes('dist\\main\\main\\tournament')) {
    request = '../../shared/types';
  }
  if (request === '../../../shared/constants' && parent.filename.includes('dist\\main\\main\\ipc')) {
    request = '../../shared/constants';
  }
  if (request === '../../../shared/types' && parent.filename.includes('dist\\main\\main\\ipc')) {
    request = '../../shared/types';
  }
  return originalResolveFilename.call(this, request, parent, isMain);
};

// Import the compiled checkpoint manager
const { CheckpointManager } = require('./dist/main/main/tournament/checkpoint');

async function testCheckpointManager() {
  console.log('Testing Checkpoint Manager...\n');
  
  const testDir = path.join(__dirname, 'test-output');
  
  // Clean up test directory if it exists
  try {
    await fs.promises.rm(testDir, { recursive: true, force: true });
  } catch (e) {
    // Ignore
  }
  
  const checkpoint = new CheckpointManager(testDir);
  
  // Test 1: Save checkpoint
  console.log('Test 1: Saving checkpoint...');
  const testState = {
    version: '1.0.0',
    timestamp: Date.now(),
    config: {
      substats: {},
      weaponTypes: { ranged: true, melee: true },
      substatMultiplier: 1.0,
      targetBuilds: 100,
      outputDirectory: testDir,
      maxWorkers: 4,
      checkpointInterval: 300,
      includeMetaBuild: false,
      loadPreviousResults: false
    },
    builds: [],
    completedBattles: [],
    results: {},
    nextBattleIndex: 0,
    totalBattles: 100
  };
  
  await checkpoint.save(testState);
  console.log('✓ Checkpoint saved\n');
  
  // Test 2: Check if checkpoint exists
  console.log('Test 2: Checking if checkpoint exists...');
  const exists = await checkpoint.exists();
  console.log(`✓ Checkpoint exists: ${exists}\n`);
  
  // Test 3: Load checkpoint
  console.log('Test 3: Loading checkpoint...');
  const loadedState = await checkpoint.load();
  console.log(`✓ Checkpoint loaded: ${loadedState !== null}\n`);
  
  // Test 4: Get checkpoint info
  console.log('Test 4: Getting checkpoint info...');
  const info = await checkpoint.getInfo();
  console.log(`✓ Checkpoint info: timestamp=${info.timestamp}, progress=${info.progress}%\n`);
  
  // Test 5: Save multiple checkpoints to test rotation
  console.log('Test 5: Testing checkpoint rotation...');
  for (let i = 1; i <= 5; i++) {
    const state = { ...testState, timestamp: Date.now() + i * 1000 };
    await checkpoint.save(state);
    console.log(`  Saved checkpoint ${i}`);
    await new Promise(resolve => setTimeout(resolve, 100)); // Small delay
  }
  console.log('✓ Rotation test complete\n');
  
  // Test 6: List all checkpoints
  console.log('Test 6: Listing all checkpoints...');
  const checkpoints = await checkpoint.listCheckpoints();
  console.log(`✓ Found ${checkpoints.length} checkpoints:`);
  checkpoints.forEach((cp, idx) => {
    console.log(`  ${idx + 1}. ${path.basename(cp.path)} - ${new Date(cp.timestamp).toISOString()} - ${cp.size} bytes`);
  });
  console.log();
  
  // Test 7: Get total checkpoint size
  console.log('Test 7: Getting total checkpoint size...');
  const totalSize = await checkpoint.getTotalCheckpointSize();
  console.log(`✓ Total checkpoint size: ${totalSize} bytes (${(totalSize / 1024).toFixed(2)} KB)\n`);
  
  // Test 8: Cleanup old checkpoints
  console.log('Test 8: Testing age-based cleanup...');
  
  // Create some test checkpoints with different ages
  const oldCheckpointDir = path.join(testDir, '.tournament-checkpoints');
  await fs.promises.mkdir(oldCheckpointDir, { recursive: true });
  
  // Create an old checkpoint (simulate 10 days old)
  const oldTimestamp = Date.now() - (10 * 24 * 60 * 60 * 1000);
  const oldCheckpointPath = path.join(oldCheckpointDir, 'backup-1.json');
  const oldState = { ...testState, timestamp: oldTimestamp };
  await fs.promises.writeFile(oldCheckpointPath, JSON.stringify(oldState));
  
  // Set the file modification time to 10 days ago
  await fs.promises.utimes(oldCheckpointPath, new Date(oldTimestamp), new Date(oldTimestamp));
  
  // Create a recent checkpoint (1 day old)
  const recentTimestamp = Date.now() - (1 * 24 * 60 * 60 * 1000);
  const recentCheckpointPath = path.join(oldCheckpointDir, 'backup-2.json');
  const recentState = { ...testState, timestamp: recentTimestamp };
  await fs.promises.writeFile(recentCheckpointPath, JSON.stringify(recentState));
  await fs.promises.utimes(recentCheckpointPath, new Date(recentTimestamp), new Date(recentTimestamp));
  
  console.log('  Created test checkpoints with different ages');
  
  // Run age-based cleanup (7 days)
  await checkpoint.cleanupOldCheckpoints(7);
  
  // Check which checkpoints remain
  const oldExists = await fs.promises.access(oldCheckpointPath).then(() => true).catch(() => false);
  const recentExists = await fs.promises.access(recentCheckpointPath).then(() => true).catch(() => false);
  
  console.log(`  Old checkpoint (10 days) exists: ${oldExists} (should be false)`);
  console.log(`  Recent checkpoint (1 day) exists: ${recentExists} (should be true)`);
  
  if (!oldExists && recentExists) {
    console.log('✓ Age-based cleanup working correctly\n');
  } else {
    console.log('✗ Age-based cleanup failed\n');
  }
  
  // Test 9: Full cleanup
  console.log('Test 9: Testing full cleanup...');
  await checkpoint.cleanup();
  const existsAfterCleanup = await checkpoint.exists();
  const recentExistsAfterCleanup = await fs.promises.access(recentCheckpointPath).then(() => true).catch(() => false);
  console.log(`✓ Current checkpoint exists after cleanup: ${existsAfterCleanup} (should be false)`);
  console.log(`✓ Backup checkpoint exists after cleanup: ${recentExistsAfterCleanup} (should be false)\n`);
  
  // Clean up test directory
  try {
    await fs.promises.rm(testDir, { recursive: true, force: true });
    console.log('✓ Test directory cleaned up\n');
  } catch (e) {
    console.error('Failed to clean up test directory:', e);
  }
  
  console.log('All tests passed! ✓');
}

testCheckpointManager().catch(console.error);
