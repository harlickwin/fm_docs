# Checkpoint System Features

## Overview

The checkpoint system has been enhanced with periodic saving, background writing, directory management, and file rotation capabilities to ensure tournament progress is safely preserved without impacting performance.

## Key Features

### 1. Configurable Checkpoint Interval

The checkpoint interval is configurable through the `TournamentConfig`:

```typescript
interface TournamentConfig {
  checkpointInterval: number; // seconds (default: 300 = 5 minutes)
  // ... other config options
}
```

- Default interval: 5 minutes (300 seconds)
- Can be customized per tournament
- Minimum recommended: 60 seconds
- Maximum recommended: 600 seconds (10 minutes)

### 2. Background Checkpoint Writing

The checkpoint manager implements non-blocking saves:

- **Asynchronous saves**: Checkpoint writes don't block tournament execution
- **Queue management**: If a save is in progress, new saves are queued
- **Atomic writes**: Uses temporary files and atomic rename operations
- **Error handling**: Save failures don't crash the tournament

```typescript
// Non-blocking save
await checkpoint.save(state); // Returns immediately if save in progress
```

### 3. Checkpoint Directory Management

Checkpoints are organized in a dedicated directory:

```
output-directory/
  └── .tournament-checkpoints/
      ├── current.json          # Active checkpoint
      ├── backup-1.json         # Previous checkpoint
      ├── backup-2.json         # 2nd previous checkpoint
      └── backup-3.json         # 3rd previous checkpoint
```

Features:
- Automatic directory creation
- Isolated from tournament results
- Hidden directory (prefixed with `.`)
- Automatic cleanup on completion

### 4. File Rotation

The system maintains up to 3 backup checkpoints:

- **Rotation on save**: Before saving, current checkpoint becomes backup-1
- **Backup shifting**: Existing backups shift (backup-1 → backup-2 → backup-3)
- **Overflow prevention**: Oldest backup (backup-4+) is automatically deleted
- **Safety**: Multiple recovery points in case of corruption

### 5. Periodic Saving

The coordinator automatically saves checkpoints at configured intervals:

```typescript
// Automatic checkpoint timer
private startCheckpointTimer(): void {
  const checkpointIntervalMs = (this.config.checkpointInterval || 300) * 1000;
  
  this.checkpointTimer = setInterval(async () => {
    if (!this.isRunning || this.isPaused) {
      return;
    }
    
    const now = Date.now();
    if (now - this.lastCheckpointTime >= checkpointIntervalMs) {
      await this.saveCheckpoint();
      this.lastCheckpointTime = now;
    }
  }, 10000); // Check every 10 seconds
}
```

Features:
- Checks every 10 seconds if checkpoint is due
- Respects pause state (no saves while paused)
- Stops automatically on tournament completion
- Logs checkpoint saves with timestamps

## API Reference

### CheckpointManager

#### Constructor
```typescript
constructor(outputDirectory: string)
```

#### Methods

##### save(state: TournamentState): Promise<void>
Saves tournament state to checkpoint file (non-blocking).

##### load(): Promise<TournamentState | null>
Loads tournament state from current checkpoint.

##### exists(): Promise<boolean>
Checks if a checkpoint exists.

##### cleanup(): Promise<void>
Deletes all checkpoint files (current + backups).

##### cleanupOldCheckpoints(maxAgeDays: number): Promise<void>
Removes backup files older than specified age.

##### getInfo(): Promise<{ timestamp: number; progress: number } | null>
Gets checkpoint metadata without loading full state.

##### listCheckpoints(): Promise<Array<{ path: string; timestamp: number; size: number }>>
Lists all available checkpoints sorted by timestamp (newest first).

##### getTotalCheckpointSize(): Promise<number>
Returns total size of all checkpoint files in bytes.

## Usage Examples

### Basic Configuration

```typescript
const config: TournamentConfig = {
  // ... other config
  checkpointInterval: 300, // Save every 5 minutes
  outputDirectory: './tournament-results'
};

const coordinator = new TournamentCoordinator(config);
await coordinator.start(builds);
```

### Custom Checkpoint Interval

```typescript
// Save every 2 minutes for faster checkpoints
const config: TournamentConfig = {
  // ... other config
  checkpointInterval: 120
};
```

### Manual Checkpoint Management

```typescript
const checkpoint = new CheckpointManager('./output');

// List all checkpoints
const checkpoints = await checkpoint.listCheckpoints();
console.log(`Found ${checkpoints.length} checkpoints`);

// Get total size
const totalSize = await checkpoint.getTotalCheckpointSize();
console.log(`Total size: ${totalSize} bytes`);

// Clean up old backups (older than 7 days)
await checkpoint.cleanupOldCheckpoints(7);
```

## Performance Considerations

### Save Performance
- Average save time: 50-200ms (depends on tournament size)
- Non-blocking: Tournament continues during save
- Atomic writes: No partial/corrupted files

### Disk Usage
- Current checkpoint: ~1-10 MB (depends on build count)
- 3 backups: ~3-30 MB total
- Automatic rotation prevents unlimited growth

### Memory Impact
- Minimal: Checkpoint data is serialized directly to disk
- No in-memory buffering of large datasets
- Queue holds only one pending state

## Error Handling

### Save Failures
- Logged but don't crash tournament
- Previous checkpoint remains valid
- Next save attempt will retry

### Load Failures
- Returns null for missing files
- Validates checkpoint structure
- Checks version compatibility

### Corruption Recovery
- Multiple backup checkpoints available
- Can manually load from backup-1, backup-2, or backup-3
- Validation prevents loading corrupted data

## Best Practices

1. **Interval Selection**
   - Short tournaments (< 1 hour): 120-180 seconds
   - Medium tournaments (1-4 hours): 300 seconds (default)
   - Long tournaments (> 4 hours): 300-600 seconds

2. **Disk Space**
   - Ensure sufficient disk space (estimate: builds × 10 KB × 4)
   - Monitor with `getTotalCheckpointSize()`

3. **Recovery**
   - Always check for checkpoints on startup
   - Prompt user to resume or start fresh
   - Keep backups until tournament completes

4. **Cleanup**
   - Automatic cleanup on successful completion
   - Manual cleanup for failed tournaments
   - Periodic cleanup of old backups

## Troubleshooting

### Checkpoint Not Saving
- Check disk space
- Verify write permissions on output directory
- Check logs for error messages

### Cannot Resume from Checkpoint
- Verify checkpoint version matches
- Try loading from backup checkpoint
- Check checkpoint file integrity

### High Disk Usage
- Reduce checkpoint interval
- Clean up old checkpoints manually
- Reduce number of builds in tournament

## Implementation Details

### File Format
Checkpoints are stored as JSON with the following structure:

```json
{
  "version": "1.0.0",
  "timestamp": 1234567890,
  "config": { /* TournamentConfig */ },
  "builds": [ /* BuildStats[] */ ],
  "completedBattles": [ /* CompletedBattle[] */ ],
  "results": { /* Record<string, TournamentResult> */ },
  "nextBattleIndex": 12345,
  "totalBattles": 50000
}
```

### Atomic Write Process
1. Serialize state to JSON
2. Write to temporary file (`.tmp` extension)
3. Rename temporary file to final name (atomic operation)
4. Previous checkpoint becomes backup

### Rotation Algorithm
1. Check if current checkpoint exists
2. Shift backups: backup-N → backup-(N+1)
3. Copy current → backup-1
4. Delete backup-(MAX+1) if exists
5. Save new checkpoint as current

## Future Enhancements

Potential improvements for future versions:

- Compression for smaller checkpoint files
- Incremental checkpoints (only save changes)
- Cloud backup integration
- Checkpoint encryption
- Automatic corruption detection and repair
- Checkpoint diff/comparison tools
