# Tournament Pro - Distribution Testing Guide

## Overview

This guide outlines the testing procedures for Tournament Pro distribution packages across Windows, macOS, and Linux platforms. Follow these checklists to ensure all builds work correctly before release.

## Pre-Testing Setup

### Test Environments

Prepare clean test environments for each platform:

#### Windows
- **Windows 10**: Clean installation or VM
- **Windows 11**: Clean installation or VM
- **No development tools**: Test as end-user would experience

#### macOS
- **macOS 10.13+**: Clean installation or VM
- **No Xcode**: Test without development environment
- **Gatekeeper enabled**: Test security features

#### Linux
- **Ubuntu 20.04/22.04**: Most common distribution
- **Fedora**: RPM-based testing
- **Arch**: Rolling release testing
- **Clean user account**: No development tools

### Required Test Files

- [ ] Latest build artifacts from `dist-electron/`
- [ ] Test configuration files
- [ ] Sample tournament data
- [ ] Documentation files

## Windows Testing

### Installation Testing

#### NSIS Installer (`TournamentPro-Setup-1.0.0.exe`)

- [ ] **Download and verify**:
  - File size is reasonable (50-150 MB)
  - No corruption during download
  - Antivirus doesn't flag as malware

- [ ] **Installation process**:
  - Double-click installer
  - UAC prompt appears (if applicable)
  - Installation wizard opens
  - Can choose installation directory
  - Desktop shortcut created (if selected)
  - Start menu entry created
  - Installation completes without errors

- [ ] **First launch**:
  - Application launches from desktop shortcut
  - Application launches from Start menu
  - Setup wizard appears (first run)
  - No console windows appear
  - Application icon displays correctly

#### Portable Version (`TournamentPro-1.0.0-portable.exe`)

- [ ] **Extraction and launch**:
  - File runs without installation
  - Creates necessary directories
  - No admin rights required
  - Can run from USB drive
  - Settings persist in portable directory

### Functionality Testing

- [ ] **Configuration screen**:
  - All controls work
  - Validation messages appear
  - Directory browser works
  - Presets load/save
  - System info displays correctly

- [ ] **Tournament execution**:
  - Tournament starts successfully
  - Progress updates in real-time
  - Worker threads utilize CPU
  - Pause/resume works
  - Cancel saves checkpoint

- [ ] **Results and export**:
  - Results display correctly
  - HTML export works
  - JSON export works
  - TXT export works
  - Files open in default applications

- [ ] **Checkpoint recovery**:
  - Checkpoint saves automatically
  - Recovery dialog appears on restart
  - Resume continues from checkpoint
  - Discard starts fresh

- [ ] **Help and documentation**:
  - Help dialog opens
  - All tabs display correctly
  - Documentation files accessible
  - Links work (if any)

### Performance Testing

- [ ] **CPU usage**:
  - Uses configured number of workers
  - CPU usage is reasonable
  - Doesn't freeze system
  - Releases CPU when paused

- [ ] **Memory usage**:
  - Memory usage is reasonable (<2GB for 1000 builds)
  - No memory leaks during long runs
  - Memory released after completion

- [ ] **Disk usage**:
  - Results files are reasonable size
  - Checkpoints don't grow excessively
  - Old checkpoints cleaned up

### Uninstallation Testing

- [ ] **Uninstall process**:
  - Uninstaller runs from Control Panel
  - Application files removed
  - Desktop shortcut removed
  - Start menu entry removed
  - User data preserved (Documents/TournamentPro)

## macOS Testing

### Installation Testing

#### DMG (`TournamentPro-1.0.0.dmg`)

- [ ] **Download and verify**:
  - File size is reasonable (50-150 MB)
  - DMG mounts successfully
  - No corruption warnings

- [ ] **Installation process**:
  - Drag to Applications folder
  - Application copies successfully
  - DMG ejects cleanly

- [ ] **First launch**:
  - Application launches from Applications
  - Gatekeeper warning appears (if unsigned)
  - Can bypass Gatekeeper (System Preferences)
  - Setup wizard appears (first run)
  - Application icon displays correctly in Dock

#### ZIP (`TournamentPro-1.0.0-mac.zip`)

- [ ] **Extraction and launch**:
  - ZIP extracts successfully
  - Application bundle is valid
  - Launches without errors
  - Can move to Applications folder

### Functionality Testing

Same as Windows, plus:

- [ ] **macOS-specific**:
  - Menu bar integration works
  - Dock icon updates correctly
  - Notifications work (if applicable)
  - Full screen mode works
  - Window management works

### Performance Testing

Same as Windows, plus:

- [ ] **macOS-specific**:
  - Works on Intel Macs
  - Works on Apple Silicon (M1/M2)
  - Rosetta translation works (if needed)
  - Battery usage is reasonable (laptops)

### Uninstallation Testing

- [ ] **Uninstall process**:
  - Drag to Trash from Applications
  - Application removed successfully
  - User data preserved (~/Library/Application Support)

## Linux Testing

### Installation Testing

#### AppImage (`TournamentPro-1.0.0.AppImage`)

- [ ] **Download and verify**:
  - File size is reasonable (50-150 MB)
  - File has execute permissions
  - No corruption during download

- [ ] **Launch process**:
  - Make executable: `chmod +x TournamentPro-1.0.0.AppImage`
  - Double-click or run from terminal
  - FUSE works (or fallback works)
  - Application launches successfully
  - Desktop integration works (optional)

#### Debian Package (`tournament-pro_1.0.0_amd64.deb`)

- [ ] **Installation**:
  - Install: `sudo dpkg -i tournament-pro_1.0.0_amd64.deb`
  - Dependencies resolve automatically
  - Or: `sudo apt install ./tournament-pro_1.0.0_amd64.deb`
  - Desktop entry created
  - Application appears in menu

- [ ] **Launch**:
  - Launches from application menu
  - Launches from terminal: `tournament-pro`
  - Icon displays correctly

#### RPM Package (`tournament-pro-1.0.0.x86_64.rpm`)

- [ ] **Installation**:
  - Install: `sudo rpm -i tournament-pro-1.0.0.x86_64.rpm`
  - Or: `sudo dnf install tournament-pro-1.0.0.x86_64.rpm`
  - Dependencies resolve
  - Desktop entry created

- [ ] **Launch**:
  - Launches from application menu
  - Launches from terminal
  - Icon displays correctly

### Functionality Testing

Same as Windows, plus:

- [ ] **Linux-specific**:
  - Works on X11
  - Works on Wayland
  - File dialogs work
  - System tray works (if applicable)
  - Desktop notifications work

### Performance Testing

Same as Windows, plus:

- [ ] **Linux-specific**:
  - Works with different desktop environments (GNOME, KDE, XFCE)
  - GPU acceleration works (if applicable)
  - No excessive CPU usage

### Uninstallation Testing

#### AppImage
- [ ] Simply delete the file
- [ ] User data preserved (~/.config/TournamentPro)

#### Debian
- [ ] `sudo apt remove tournament-pro`
- [ ] Application removed
- [ ] User data preserved

#### RPM
- [ ] `sudo rpm -e tournament-pro`
- [ ] Application removed
- [ ] User data preserved

## Cross-Platform Testing

### Feature Parity

Verify all features work identically across platforms:

- [ ] Configuration options
- [ ] Tournament execution
- [ ] Results display
- [ ] Export formats
- [ ] Checkpoint system
- [ ] Help documentation

### File Compatibility

- [ ] Configuration files work across platforms
- [ ] Checkpoint files work across platforms
- [ ] Results files work across platforms
- [ ] Presets work across platforms

### UI Consistency

- [ ] Layout is consistent
- [ ] Fonts render correctly
- [ ] Icons display correctly
- [ ] Colors are consistent
- [ ] Spacing is appropriate

## Regression Testing

Test previously reported issues:

- [ ] Issue #1: [Description]
- [ ] Issue #2: [Description]
- [ ] Issue #3: [Description]

## Performance Benchmarks

Run standardized tests:

### Small Tournament (100 builds)
- [ ] Windows: Time to complete
- [ ] macOS: Time to complete
- [ ] Linux: Time to complete

### Medium Tournament (1000 builds)
- [ ] Windows: Time to complete
- [ ] macOS: Time to complete
- [ ] Linux: Time to complete

### Large Tournament (5000 builds)
- [ ] Windows: Time to complete
- [ ] macOS: Time to complete
- [ ] Linux: Time to complete

## Security Testing

### Code Signing

- [ ] **Windows**: Installer is signed (if applicable)
- [ ] **macOS**: Application is signed (if applicable)
- [ ] **macOS**: Application is notarized (if applicable)

### Permissions

- [ ] Application requests only necessary permissions
- [ ] File access is limited to user directories
- [ ] No unnecessary network access
- [ ] No suspicious behavior flagged by antivirus

## Documentation Testing

- [ ] **README.md**: Accurate and up-to-date
- [ ] **USER_GUIDE.md**: All features documented
- [ ] **QUICK_START.md**: Easy to follow
- [ ] **TROUBLESHOOTING.md**: Common issues covered
- [ ] **BUILD_GUIDE.md**: Build instructions work

## Accessibility Testing

- [ ] Keyboard navigation works
- [ ] Tab order is logical
- [ ] Focus indicators visible
- [ ] Text is readable (contrast, size)
- [ ] Screen reader compatible (basic)

## Stress Testing

### Long-Running Tournaments

- [ ] 24-hour tournament completes
- [ ] No memory leaks
- [ ] Checkpoints work correctly
- [ ] Application remains responsive

### Large Datasets

- [ ] 10,000+ builds
- [ ] Results export successfully
- [ ] UI remains responsive
- [ ] File sizes are manageable

### System Limits

- [ ] Works with 1 CPU core
- [ ] Works with 32+ CPU cores
- [ ] Works with 4GB RAM
- [ ] Works with limited disk space

## User Acceptance Testing

### Non-Technical Users

- [ ] Can install without help
- [ ] Can configure tournament
- [ ] Can start tournament
- [ ] Can understand results
- [ ] Can export results

### Technical Users

- [ ] Can customize configuration
- [ ] Can use advanced features
- [ ] Can troubleshoot issues
- [ ] Can build from source

## Test Results Template

```
Platform: [Windows/macOS/Linux]
Version: [OS Version]
Build: [Build Number]
Date: [Test Date]
Tester: [Name]

Installation: [PASS/FAIL]
Functionality: [PASS/FAIL]
Performance: [PASS/FAIL]
Uninstallation: [PASS/FAIL]

Issues Found:
1. [Description]
2. [Description]

Notes:
[Additional observations]
```

## Sign-Off Checklist

Before releasing:

- [ ] All critical tests pass on all platforms
- [ ] No critical bugs remain
- [ ] Performance is acceptable
- [ ] Documentation is complete
- [ ] Build artifacts are signed (if applicable)
- [ ] Release notes are prepared
- [ ] Download links are ready
- [ ] Support channels are prepared

## Post-Release Monitoring

After release:

- [ ] Monitor download statistics
- [ ] Track crash reports
- [ ] Collect user feedback
- [ ] Monitor support requests
- [ ] Track performance metrics
- [ ] Plan next release

---

## Notes

- Test on clean machines whenever possible
- Document all issues found
- Retest after fixes
- Keep test results for future reference
- Update this guide based on findings

**Remember**: Thorough testing prevents user frustration and support burden!
