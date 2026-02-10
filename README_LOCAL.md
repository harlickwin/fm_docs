# Tournament Pro

Advanced PvP Tournament System with Multi-threading, Checkpoints, and User-Friendly Interface

## Features

- **Multi-threaded Execution**: Utilizes multiple CPU cores for faster tournament completion
- **Automatic Checkpoints**: Saves progress every 5 minutes and recovers from crashes
- **User-Friendly UI**: Graphical interface for configuration and monitoring
- **Portable**: Single executable that works without technical setup
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Project Status

🚧 **Currently in Development** 🚧

### Completed
- ✅ Project structure created
- ✅ Package configuration
- ✅ TypeScript configuration
- ✅ Shared types defined

### In Progress
- 🔄 Core tournament engine
- 🔄 Worker thread implementation
- 🔄 Checkpoint system
- 🔄 UI components

### Planned
- ⏳ IPC communication
- ⏳ First-run experience
- ⏳ Documentation
- ⏳ Build and distribution

## Development

```bash
# Install dependencies
cd tournament-pro
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Package for distribution
npm run package        # All platforms
npm run package:win    # Windows only
npm run package:mac    # macOS only
npm run package:linux  # Linux only
```

## Architecture

```
tournament-pro/
├── src/
│   ├── main/              # Electron main process
│   │   ├── main.ts        # Application entry point
│   │   ├── tournament/    # Tournament engine
│   │   └── ipc/           # IPC handlers
│   ├── renderer/          # Electron renderer (UI)
│   │   ├── App.tsx
│   │   ├── components/
│   │   └── styles/
│   └── shared/            # Shared types and utilities
└── dist/                  # Build output
```

## Next Steps

1. Complete core tournament engine with multi-threading
2. Implement checkpoint and recovery system
3. Build React UI components
4. Set up IPC communication
5. Add first-run experience
6. Create documentation
7. Package and test distribution

## Requirements

- Node.js 18+
- npm or yarn
- For building: Platform-specific build tools (see electron-builder docs)

## License

MIT
