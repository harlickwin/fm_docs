"use strict";
/**
 * Shared types between main and renderer processes
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.IPC_CHANNELS = void 0;
// IPC Channel names
exports.IPC_CHANNELS = {
    TOURNAMENT_START: 'tournament:start',
    TOURNAMENT_PAUSE: 'tournament:pause',
    TOURNAMENT_RESUME: 'tournament:resume',
    TOURNAMENT_CANCEL: 'tournament:cancel',
    TOURNAMENT_PROGRESS: 'tournament:progress',
    TOURNAMENT_COMPLETE: 'tournament:complete',
    TOURNAMENT_ERROR: 'tournament:error',
    CHECKPOINT_FOUND: 'checkpoint:found',
    CHECKPOINT_RESUME: 'checkpoint:resume',
    CHECKPOINT_DISCARD: 'checkpoint:discard',
    CONFIG_SAVE: 'config:save',
    CONFIG_LOAD: 'config:load',
    SELECT_DIRECTORY: 'select:directory',
};
