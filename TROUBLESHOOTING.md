# Tournament Pro - Troubleshooting Guide

## Common Issues and Solutions

### Installation and Startup Issues

#### Application Won't Launch

**Symptoms**: Double-clicking the executable does nothing, or error message appears

**Solutions**:

1. **Check System Requirements**:
   - Windows 10/11, macOS 10.13+, or Linux (Ubuntu 18.04+)
   - 4GB RAM minimum (8GB recommended)
   - 1GB free disk space

2. **Run as Administrator** (Windows):
   - Right-click Tournament Pro executable
   - Select "Run as administrator"

3. **Check Antivirus**:
   - Some antivirus software may block the application
   - Add Tournament Pro to your antivirus whitelist
   - Temporarily disable antivirus to test

4. **Verify Download**:
   - Re-download the application
   - Ensure download completed fully
   - Check file size matches expected size

5. **Check Dependencies** (Linux):
   ```bash
   # Install required libraries
   sudo apt-get install libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils libatspi2.0-0 libdrm2 libgbm1 libxcb-dri3-0
   ```

#### First-Run Setup Fails

**Symptoms**: Setup wizard crashes or doesn't complete

**Solutions**:

1. **Check Permissions**:
   - Ensure write access to Documents folder
   - Verify user has permission to create directories

2. **Manual Directory Creation**:
   ```
   Windows: C:\Users\[YourName]\Documents\TournamentPro\Results
   macOS: /Users/[YourName]/Documents/TournamentPro/Results
   Linux: /home/[YourName]/Documents/TournamentPro/Results
   ```

3. **Reset First-Run**:
   - Delete `.tournament-pro-initialized` file from user data directory
   - Restart application

### Configuration Issues

#### Can't Select Output Directory

**Symptoms**: Browse button doesn't work or selected directory doesn't save

**Solutions**:

1. **Check Permissions**:
   - Ensure you have write access to the selected directory
   - Try selecting a different directory

2. **Use Default Directory**:
   - Click "Reset to Default" button
   - Default is always writable

3. **Manual Path Entry**:
   - Type the path directly instead of browsing
   - Use forward slashes (/) even on Windows

#### Validation Errors

**Symptoms**: Red error messages appear, can't start tournament

**Common Errors and Fixes**:

| Error | Solution |
|-------|----------|
| "At least one substat must be selected" | Check at least one substat checkbox |
| "Target builds must be greater than 0" | Enter a number > 0 in Target Builds |
| "Output directory does not exist" | Click Browse and select valid directory |
| "Invalid substat multiplier" | Ensure multiplier is between 1-100% |
| "At least one weapon type must be selected" | Check Melee or Ranged |

#### Estimated Runtime Shows "—"

**Symptoms**: Runtime estimation doesn't appear

**Solutions**:

1. **Complete Configuration**:
   - Ensure all required fields are filled
   - Select at least one substat
   - Enter valid target builds number

2. **Wait for Calculation**:
   - Estimation may take 1-2 seconds
   - Try changing a value to trigger recalculation

### Tournament Execution Issues

#### Tournament Won't Start

**Symptoms**: Clicking "Start Tournament" does nothing

**Solutions**:

1. **Check Validation**:
   - Look for red error messages
   - Fix all validation errors first

2. **Check Disk Space**:
   - Ensure at least 1GB free space
   - Clear old tournament results if needed

3. **Restart Application**:
   - Close and reopen Tournament Pro
   - Try starting tournament again

4. **Check Output Directory**:
   - Verify directory exists
   - Ensure it's writable
   - Try a different directory

#### Tournament Crashes Immediately

**Symptoms**: Tournament starts but crashes within seconds

**Solutions**:

1. **Reduce Worker Threads**:
   - Lower to 1 or 2 workers
   - Test if it runs successfully
   - Gradually increase workers

2. **Reduce Build Count**:
   - Start with 100 builds
   - Verify it completes
   - Increase gradually

3. **Check Memory**:
   - Close other applications
   - Ensure 4GB+ RAM available
   - Restart computer if needed

4. **Update Application**:
   - Download latest version
   - Check for bug fixes

#### Progress Stuck at 0%

**Symptoms**: Tournament starts but progress doesn't increase

**Solutions**:

1. **Wait Longer**:
   - Initial build generation takes time
   - Wait 1-2 minutes before worrying

2. **Check Worker Status**:
   - Verify workers show "running" status
   - If all show "idle", restart tournament

3. **Check CPU Usage**:
   - Open Task Manager / Activity Monitor
   - Verify Tournament Pro is using CPU
   - If not, restart application

#### Extremely Slow Progress

**Symptoms**: Tournament runs but very slowly

**Solutions**:

1. **Optimize Configuration**:
   - Reduce number of builds
   - Lower substat multiplier to 50%
   - Select fewer substats

2. **Increase Workers**:
   - Use more CPU cores
   - Recommended: Total cores - 1

3. **Close Other Applications**:
   - Free up CPU resources
   - Close browsers, games, etc.

4. **Check System Load**:
   - Verify CPU isn't thermal throttling
   - Ensure adequate cooling
   - Check for background processes

### Checkpoint and Recovery Issues

#### Checkpoint Not Detected

**Symptoms**: Application restarts but doesn't offer to resume

**Solutions**:

1. **Check Output Directory**:
   - Look for `.checkpoint.json` file
   - Verify it's in the correct directory

2. **Manual Resume**:
   - Note the output directory path
   - Restart application
   - Select same output directory
   - Checkpoint should be detected

3. **Checkpoint Corruption**:
   - If checkpoint is corrupted, start fresh
   - Delete `.checkpoint.json` file
   - Start new tournament

#### Can't Resume from Checkpoint

**Symptoms**: "Resume Tournament" fails or crashes

**Solutions**:

1. **Verify Checkpoint Integrity**:
   - Open `.checkpoint.json` in text editor
   - Check if it's valid JSON
   - If corrupted, start fresh

2. **Check Disk Space**:
   - Ensure adequate free space
   - Checkpoint resume needs space for results

3. **Start Fresh**:
   - Click "Start Fresh" instead
   - Previous checkpoint will be backed up

#### Checkpoint File Too Large

**Symptoms**: Checkpoint files consuming too much disk space

**Solutions**:

1. **Reduce Checkpoint Frequency**:
   - Increase checkpoint interval to 600+ seconds
   - Reduces number of checkpoints

2. **Clean Up Old Checkpoints**:
   - Delete old `.checkpoint.json` files
   - Keep only recent checkpoints
   - Application auto-cleans checkpoints older than 7 days

3. **Complete Tournaments**:
   - Checkpoints are deleted on completion
   - Don't leave tournaments incomplete

### Results and Export Issues

#### No Results Displayed

**Symptoms**: Tournament completes but no results shown

**Solutions**:

1. **Check Output Directory**:
   - Verify results files were created
   - Look for `results.json`, `results.html`, `results.txt`

2. **Restart Application**:
   - Close and reopen Tournament Pro
   - Results should load automatically

3. **Manual Export**:
   - Check output directory manually
   - Open HTML file in browser

#### Export Fails

**Symptoms**: Export buttons don't create files

**Solutions**:

1. **Check Permissions**:
   - Verify write access to output directory
   - Try exporting to different directory

2. **Check Disk Space**:
   - Ensure adequate free space
   - Results can be 1-50MB depending on size

3. **Try Different Format**:
   - If HTML fails, try JSON or TXT
   - Different formats have different requirements

4. **Manual Copy**:
   - Results are already saved in output directory
   - Copy files manually if export fails

#### Results Look Incorrect

**Symptoms**: Win rates, DPS, or other stats seem wrong

**Solutions**:

1. **Verify Configuration**:
   - Check substats were correctly selected
   - Verify weapon types match intent
   - Ensure multiplier is appropriate

2. **Check for Ties**:
   - Many draws can skew win rates
   - This is normal for similar builds

3. **Run Again**:
   - Results are deterministic
   - Running same config should give same results
   - If different, report as bug

### Performance Issues

#### High CPU Usage

**Symptoms**: Computer becomes slow or unresponsive

**Solutions**:

1. **Reduce Workers**:
   - Lower worker count to N-2 or N-3
   - Leaves more CPU for system

2. **Pause Tournament**:
   - Click Pause when you need to use computer
   - Resume when ready

3. **Close Other Applications**:
   - Free up CPU resources
   - Run tournament when computer is idle

#### High Memory Usage

**Symptoms**: Application uses excessive RAM

**Solutions**:

1. **Reduce Build Count**:
   - Lower target builds
   - Memory usage scales with build count

2. **Restart Application**:
   - Memory leaks may occur in long sessions
   - Restart periodically for long tournaments

3. **Close Other Applications**:
   - Free up RAM
   - Ensure 4GB+ available

#### Disk Space Issues

**Symptoms**: Running out of disk space

**Solutions**:

1. **Clean Up Old Results**:
   - Delete old tournament directories
   - Keep only recent results

2. **Change Output Directory**:
   - Move to drive with more space
   - External drives work fine

3. **Reduce Tournament Size**:
   - Fewer builds = smaller results
   - Lower multiplier = smaller checkpoints

### Platform-Specific Issues

#### Windows Issues

**Windows Defender Blocks Application**:
- Click "More info" → "Run anyway"
- Or add to Windows Defender exclusions

**DLL Missing Errors**:
- Install Visual C++ Redistributable
- Download from Microsoft website

**Permission Denied**:
- Run as Administrator
- Check folder permissions

#### macOS Issues

**"App is damaged" Error**:
```bash
xattr -cr /path/to/TournamentPro.app
```

**Gatekeeper Blocks App**:
- System Preferences → Security & Privacy
- Click "Open Anyway"

**Permission Denied**:
- Grant Full Disk Access in System Preferences
- Security & Privacy → Privacy → Full Disk Access

#### Linux Issues

**Missing Libraries**:
```bash
# Ubuntu/Debian
sudo apt-get install libgtk-3-0 libnotify4 libnss3 libxss1

# Fedora
sudo dnf install gtk3 libnotify nss libXScrnSaver

# Arch
sudo pacman -S gtk3 libnotify nss
```

**AppImage Won't Run**:
```bash
chmod +x TournamentPro.AppImage
./TournamentPro.AppImage
```

**Wayland Issues**:
- Try running with X11 instead
- Set `GDK_BACKEND=x11` environment variable

## Advanced Troubleshooting

### Enable Debug Logging

1. **Windows**:
   ```
   TournamentPro.exe --enable-logging
   ```

2. **macOS**:
   ```bash
   /Applications/TournamentPro.app/Contents/MacOS/TournamentPro --enable-logging
   ```

3. **Linux**:
   ```bash
   ./TournamentPro --enable-logging
   ```

Logs are saved to:
- Windows: `%APPDATA%\TournamentPro\logs`
- macOS: `~/Library/Logs/TournamentPro`
- Linux: `~/.config/TournamentPro/logs`

### Reset Application

To completely reset Tournament Pro:

1. **Close Application**

2. **Delete User Data**:
   - Windows: `%APPDATA%\TournamentPro`
   - macOS: `~/Library/Application Support/TournamentPro`
   - Linux: `~/.config/TournamentPro`

3. **Restart Application**:
   - First-run setup will appear again
   - All settings reset to defaults

### Check System Resources

**Windows**:
- Task Manager → Performance tab
- Check CPU, Memory, Disk usage

**macOS**:
- Activity Monitor
- Check CPU, Memory, Disk tabs

**Linux**:
```bash
htop  # or top
df -h  # disk space
free -h  # memory
```

## Getting Help

If you've tried these solutions and still have issues:

1. **Gather Information**:
   - Operating system and version
   - Tournament Pro version
   - Tournament configuration used
   - Error messages (screenshots helpful)
   - Steps to reproduce the issue

2. **Check for Updates**:
   - Download latest version
   - Check if issue is fixed

3. **Report Bug**:
   - Include all gathered information
   - Attach log files if available
   - Describe expected vs actual behavior

## Known Issues

### Current Known Issues

1. **Large Tournaments (50,000+ builds)**:
   - May cause memory issues on systems with <16GB RAM
   - Workaround: Split into multiple smaller tournaments

2. **Very Long Tournaments (24+ hours)**:
   - Progress updates may slow down
   - Workaround: Restart application periodically

3. **Network Drives**:
   - Checkpoint saves may be slow
   - Workaround: Use local drive for output

### Planned Fixes

- Improved memory management for large tournaments
- Better error messages for common issues
- Automatic recovery from worker crashes
- Progress update optimization

---

**Still having issues? Check the User Guide or contact support with detailed information about your problem.**
