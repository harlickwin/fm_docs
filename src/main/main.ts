/**
 * Electron Main Process
 * Entry point for Tournament Pro application
 */

import { app, BrowserWindow } from 'electron';
import * as path from 'path';
import { registerIpcHandlers, setMainWindow, checkForCheckpointOnStartup } from './ipc/handlers';
import { isFirstRun, initializeFirstRun, getApplicationPaths } from './utils/first-run';

let mainWindow: BrowserWindow | null = null;
let firstRunInfo: any = null;

function createWindow(): void {
  const preloadPath = path.join(__dirname, '../../preload/preload/preload.js');
  const rendererPath = path.join(__dirname, '../../renderer/index.html');
  
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: preloadPath,
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  // Load the app
  if (process.env.NODE_ENV === 'development') {
    mainWindow.loadURL('http://localhost:5173');
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(rendererPath);
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
  
  // Set main window reference for IPC handlers
  setMainWindow(mainWindow);
  
  // Check for existing checkpoints after window is ready
  mainWindow.webContents.on('did-finish-load', async () => {
    await checkForCheckpointOnStartup(mainWindow!);
  });
}

// App lifecycle
app.whenReady().then(() => {
  // Check if this is the first run
  if (isFirstRun()) {
    console.log('First run detected - initializing application...');
    firstRunInfo = initializeFirstRun();
    console.log('Application initialized:', firstRunInfo);
  } else {
    // Get application paths
    firstRunInfo = getApplicationPaths();
  }
  
  registerIpcHandlers();
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
