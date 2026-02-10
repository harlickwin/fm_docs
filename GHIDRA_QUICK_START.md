# Ghidra Quick Start - Find Attack Speed Formula

## 🚀 Quick Steps

### 1. Launch Ghidra
```cmd
C:\ghidra\ghidra_12.0.2_PUBLIC\ghidraRun.bat
```

### 2. Create Project
- **File → New Project**
- Choose: **Non-Shared Project**
- Location: `C:\ghidra\projects`
- Name: `LegendOfCivilizations`

### 3. Import File
- **File → Import File**
- Select: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
- Click **OK** (auto-detects ARM format)

### 4. Analyze
- Double-click `libil2cpp.so`
- Click **Yes** to analyze
- **Wait 10-30 minutes** for analysis to complete

### 5. Run Automated Script
- **Window → Script Manager**
- Click **Script Directories** (folder icon)
- Add: `D:\Kiro\tournament-pro` (where find_attack_speed.py is)
- Find and double-click: `find_attack_speed.py`
- Review results in console

### 6. Manual Search (Alternative)
Press **G** and go to these addresses:

| Function | Address | Purpose |
|----------|---------|---------|
| HandleUnits | `5AF7094` | Main combat loop |
| Execute | `5AEE300` | Combat system entry |
| ExecuteAttack | `5AF96F4` | Attack execution |
| GetDamage | `5AF8E08` | Damage calculation |

## 🔍 What to Look For

### In Decompiled C Code:
```c
// Attack speed division
duration = baseDuration / attackSpeedMulti;
windupTime = baseWindupTime / attackSpeedMulti;

// Timer update
attackTimer -= deltaTime;
if (attackTimer <= 0) {
    // Execute attack
}
```

### In ARM Assembly:
```assembly
VLDR.32   s0, [r4, #0x58]    ; Load AttackDuration (offset 0x58)
VLDR.32   s1, [r5, #0x??]    ; Load AttackSpeedMulti
VDIV.F32  s2, s0, s1         ; Divide: s2 = s0 / s1
VSTR.32   s2, [r4, #0x58]    ; Store result
```

## 📊 Known Memory Offsets

From IL2CPP dump analysis:

| Field | Offset | Type | Description |
|-------|--------|------|-------------|
| AttackTimer | 0x50 | FD6 | Current attack countdown |
| AttackDuration | 0x58 | FD6 | Time between attacks |
| WindUpDuration | 0x68 | FD6 | Windup time before attack |

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **G** | Go to address |
| **Ctrl+E** | Search text |
| **Ctrl+Shift+E** | Search strings |
| **Ctrl+Shift+G** | Find references |
| **F** | Follow pointer |
| **L** | Rename symbol |
| **;** | Add comment |
| **Space** | Toggle disassembly/decompiler |

## 📝 Export Results

### Export Decompiled Code:
1. Right-click function
2. **Export → C/C++**
3. Save to: `C:\ghidra\attack_speed_code.c`

### Take Screenshot:
- **File → Export → Screenshot**

## 🎯 Success Criteria

You've found it when you see:
1. ✅ Division operation (`/` or `VDIV`)
2. ✅ References to offsets `0x50`, `0x58`, or `0x68`
3. ✅ Variables named like `AttackDuration`, `AttackSpeed`, `WindUp`
4. ✅ Pattern: `result = base / multiplier`

## 🐛 Troubleshooting

**Ghidra won't start?**
- Check Java: `java -version` (need 17+)
- Run as administrator

**Analysis stuck?**
- It's normal! 119 MB file takes time
- Check progress bar (bottom-right)
- Wait for "Ready" status

**Can't find functions?**
- Make sure analysis is complete
- Try the automated script
- Search by address with **G** key

**Script won't run?**
- Make sure you added the script directory
- Check console for errors
- Try manual search instead

## 📚 Full Guide

For detailed instructions, see: `GHIDRA_ANALYSIS_GUIDE.md`

---

**Current Status:**
- ✅ Ghidra installed: `C:\ghidra\ghidra_12.0.2_PUBLIC`
- ✅ Target file: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
- ✅ Automated script: `find_attack_speed.py`
- ⏳ Ready to analyze!

**Next:** Launch Ghidra and follow steps 1-6 above!
