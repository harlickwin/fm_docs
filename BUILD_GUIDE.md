# Tournament Pro - Build Guide

## Prerequisites

### All Platforms

- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher
- **Git**: For cloning the repository

### Platform-Specific Requirements

#### Windows
- **Windows 10/11**: 64-bit
- **Visual Studio Build Tools**: For native modules
- **NSIS**: Automatically downloaded by electron-builder

#### macOS
- **macOS 10.13+**: High Sierra or later
- **Xcode Command Line Tools**: `xcode-select --install`
- **Code Signing Certificate**: Optional, for distribution

#### Linux
- **Ubuntu 18.04+** or equivalent
- **Build essentials**: `sudo apt-get install build-essential`
- **Required libraries**:
  ```bash
  sudo apt-get install libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils libatspi2.0-0 libdrm2 libgbm1 libxcb-dri3-0
  ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd tournament-pro
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Verify installation**:
   ```bash
   npm run dev
   ```

## Development

### Running in Development Mode

```bash
npm run dev
```

This starts:
- Vite dev server for the renderer process (port 5173)
- TypeScript compiler in watch mode for the main process
- Hot reload for both processes

### Running Tests

```bash
# Run all tests
npm test

# Run tests with UI
npm run test:ui

# Run tests with coverage
npm run test:coverage
```

### Building for Development

```bash
# Build all components
npm run build

# Build main process only
npm run build:main

# Build renderer process only
npm run build:renderer
```

## Production Builds

### Quick Build Commands

```bash
# Build for current platform
npm run package

# Build for Windows
npm run package:win

# Build for macOS
npm run package:mac

# Build for Linux
npm run package:linux

# Build for all platforms
npm run package:all
```

### Using Build Scripts

#### Windows

**PowerShell/CMD**:
```cmd
scripts\build-windows.bat
```

**Git Bash/WSL**:
```bash
bash scripts/build-windows.sh
```

#### macOS

```bash
bash scripts/build-macos.sh
```

#### Linux

```bash
bash scripts/build-linux.sh
```

#### All Platforms

```bash
bash scripts/build-all.sh
```

## Build Output

### Directory Structure

```
tournament-pro/
├── dist/                    # Compiled source code
│   ├── main/               # Main process
│   ├── preload/            # Preload scripts
│   └── renderer/           # Renderer process
└── dist-electron/          # Packaged applications
    ├── win-unpacked/       # Windows unpacked
    ├── mac/                # macOS unpacked
    ├── linux-unpacked/     # Linux unpacked
    ├── *.exe               # Windows installers
    ├── *.dmg               # macOS disk images
    ├── *.AppImage          # Linux AppImages
    ├── *.deb               # Debian packages
    └── *.rpm               # RPM packages
```

### Build Artifacts

#### Windows
- **NSIS Installer**: `TournamentPro-Setup-1.0.0.exe`
- **Portable**: `TournamentPro-1.0.0-portable.exe`

#### macOS
- **DMG**: `TournamentPro-1.0.0.dmg`
- **ZIP**: `TournamentPro-1.0.0-mac.zip`

#### Linux
- **AppImage**: `TournamentPro-1.0.0.AppImage`
- **Debian**: `tournament-pro_1.0.0_amd64.deb`
- **RPM**: `tournament-pro-1.0.0.x86_64.rpm`
- **Tarball**: `tournament-pro-1.0.0.tar.gz`

## Configuration

### electron-builder.json

Main configuration file for electron-builder. Customize:

- **appId**: Application identifier
- **productName**: Display name
- **icon**: Application icons
- **files**: Files to include in build
- **extraResources**: Additional resources
- **target**: Build targets per platform

### package.json

Build configuration in `package.json`:

```json
{
  "build": {
    "appId": "com.tournament.pro",
    "productName": "Tournament Pro",
    "directories": {
      "output": "release"
    }
  }
}
```

## Code Signing

### Windows

1. **Obtain Code Signing Certificate**:
   - Purchase from certificate authority
   - Or use self-signed for testing

2. **Configure in electron-builder.json**:
   ```json
   {
     "win": {
       "certificateFile": "path/to/cert.pfx",
       "certificatePassword": "password"
     }
   }
   ```

3. **Or use environment variables**:
   ```bash
   set CSC_LINK=path/to/cert.pfx
   set CSC_KEY_PASSWORD=password
   npm run package:win
   ```

### macOS

1. **Obtain Apple Developer Certificate**:
   - Join Apple Developer Program
   - Create Developer ID Application certificate

2. **Configure in electron-builder.json**:
   ```json
   {
     "mac": {
       "identity": "Developer ID Application: Your Name (TEAM_ID)"
     }
   }
   ```

3. **Notarization** (optional):
   ```json
   {
     "mac": {
       "hardenedRuntime": true,
       "gatekeeperAssess": false,
       "notarize": {
         "teamId": "TEAM_ID"
       }
     }
   }
   ```

### Linux

Linux builds don't require code signing, but you can:
- Sign AppImages with GPG
- Sign packages with distribution-specific tools

## Troubleshooting

### Common Build Issues

#### "electron-builder not found"

```bash
npm install --save-dev electron-builder
```

#### "Cannot find module 'electron'"

```bash
npm install --save-dev electron
```

#### Windows: "NSIS Error"

- Ensure NSIS is installed or let electron-builder download it
- Check antivirus isn't blocking NSIS

#### macOS: "Code signing failed"

- Verify certificate is installed in Keychain
- Check certificate is valid and not expired
- Try without code signing first

#### Linux: "Missing dependencies"

```bash
# Ubuntu/Debian
sudo apt-get install -y libgtk-3-0 libnotify4 libnss3 libxss1

# Fedora
sudo dnf install gtk3 libnotify nss libXScrnSaver

# Arch
sudo pacman -S gtk3 libnotify nss
```

### Build Performance

#### Slow Builds

1. **Exclude unnecessary files**:
   ```json
   {
     "files": [
       "dist/**/*",
       "!dist/**/*.map"
     ]
   }
   ```

2. **Use compression level**:
   ```json
   {
     "compression": "normal"
   }
   ```

3. **Disable source maps** in production:
   ```typescript
   // vite.config.ts
   build: {
     sourcemap: false
   }
   ```

#### Large Bundle Size

1. **Analyze bundle**:
   ```bash
   npm run build:renderer -- --analyze
   ```

2. **Exclude dev dependencies**:
   - Ensure dev dependencies are in `devDependencies`
   - Use `--production` flag when needed

3. **Use asar archive**:
   ```json
   {
     "asar": true
   }
   ```

### Clean Builds

If builds are failing or behaving unexpectedly:

```bash
# Clean all build artifacts
npm run clean

# Remove node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Rebuild from scratch
npm run clean && npm install && npm run build
```

## CI/CD Integration

### GitHub Actions

Example workflow:

```yaml
name: Build

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: npm install
    
    - name: Build
      run: npm run build
    
    - name: Package
      run: npm run package
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: ${{ matrix.os }}-build
        path: dist-electron/
```

## Release Process

1. **Update version**:
   ```bash
   npm version patch  # or minor, major
   ```

2. **Build for all platforms**:
   ```bash
   npm run package:all
   ```

3. **Test builds**:
   - Install on clean machines
   - Verify all features work
   - Check file sizes

4. **Create release**:
   - Tag version in git
   - Upload builds to release page
   - Update changelog

5. **Distribute**:
   - Share download links
   - Update documentation
   - Announce release

## Best Practices

### Before Building

- [ ] Run all tests: `npm test`
- [ ] Update version number
- [ ] Update CHANGELOG.md
- [ ] Review electron-builder.json
- [ ] Check icon files exist
- [ ] Verify documentation is current

### During Building

- [ ] Build on clean environment
- [ ] Test on target platforms
- [ ] Verify file sizes are reasonable
- [ ] Check for console errors
- [ ] Test installation process

### After Building

- [ ] Test installed application
- [ ] Verify auto-update works (if enabled)
- [ ] Check application signing
- [ ] Test on multiple machines
- [ ] Document known issues

## Additional Resources

- [electron-builder Documentation](https://www.electron.build/)
- [Electron Documentation](https://www.electronjs.org/docs)
- [Vite Documentation](https://vitejs.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/)

## Support

For build issues:
1. Check this guide
2. Review electron-builder logs
3. Search electron-builder issues on GitHub
4. Ask in project discussions

---

**Happy Building!** 🚀
