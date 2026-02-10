"use strict";
/**
 * Preload Script
 * Exposes safe IPC methods to renderer process
 */
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
const types_1 = require("../shared/types");
// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
electron_1.contextBridge.exposeInMainWorld('tournamentAPI', {
    // Tournament control
    startTournament: (config) => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.TOURNAMENT_START, config),
    pauseTournament: () => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.TOURNAMENT_PAUSE),
    resumeTournament: () => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.TOURNAMENT_RESUME),
    cancelTournament: () => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.TOURNAMENT_CANCEL),
    // Checkpoint control
    resumeFromCheckpoint: (config) => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.CHECKPOINT_RESUME, config),
    discardCheckpoint: (outputDirectory) => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.CHECKPOINT_DISCARD, outputDirectory),
    // File system
    selectDirectory: () => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.SELECT_DIRECTORY),
    // Configuration
    saveConfig: (config) => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.CONFIG_SAVE, config),
    loadConfig: () => electron_1.ipcRenderer.invoke(types_1.IPC_CHANNELS.CONFIG_LOAD),
    // Event listeners
    onProgress: (callback) => {
        const listener = (_event, progress) => callback(progress);
        electron_1.ipcRenderer.on(types_1.IPC_CHANNELS.TOURNAMENT_PROGRESS, listener);
        return () => electron_1.ipcRenderer.removeListener(types_1.IPC_CHANNELS.TOURNAMENT_PROGRESS, listener);
    },
    onComplete: (callback) => {
        const listener = (_event, results) => callback(results);
        electron_1.ipcRenderer.on(types_1.IPC_CHANNELS.TOURNAMENT_COMPLETE, listener);
        return () => electron_1.ipcRenderer.removeListener(types_1.IPC_CHANNELS.TOURNAMENT_COMPLETE, listener);
    },
    onError: (callback) => {
        const listener = (_event, error) => callback(error);
        electron_1.ipcRenderer.on(types_1.IPC_CHANNELS.TOURNAMENT_ERROR, listener);
        return () => electron_1.ipcRenderer.removeListener(types_1.IPC_CHANNELS.TOURNAMENT_ERROR, listener);
    },
    onCheckpointFound: (callback) => {
        const listener = (_event, info) => callback(info);
        electron_1.ipcRenderer.on(types_1.IPC_CHANNELS.CHECKPOINT_FOUND, listener);
        return () => electron_1.ipcRenderer.removeListener(types_1.IPC_CHANNELS.CHECKPOINT_FOUND, listener);
    }
});
