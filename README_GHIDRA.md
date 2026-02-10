# 🎯 Ghidra Setup Complete - Ready to Find Attack Speed Formula!

## ✅ What's Been Done

1. **Downloaded Ghidra 12.0.2** (486 MB)
2. **Extracted to**: `C:\ghidra\ghidra_12.0.2_PUBLIC`
3. **Verified Java 25** is installed
4. **Created analysis scripts and guides**
5. **Ghidra is running** (should be open now)

## 🚀 Quick Start (3 Steps)

### 1️⃣ Create Project in Ghidra
- File → New Project → Non-Shared Project
- Location: `C:\ghidra\projects`
- Name: `LegendOfCivilizations`

### 2️⃣ Import libil2cpp.so
- File → Import File
- Select: `C:\apktool\config-armeabi-out\lib\armeabi-v7a\libil2cpp.so`
- Click OK (auto-detects ARM format)

### 3️⃣ Analyze & Search
- Double-click `libil2cpp.so` → Click "Yes" to analyze
- **Wait 10-30 minutes** for analysis
- Then run: `find_attack_speed.py` script

## 📚 Documentation Created

| File | Purpose |
|------|---------|
| **GHIDRA_QUICK_START.md** | ⚡ Fast reference guide |
| **GHIDRA_ANALYSIS_GUIDE.md** | 📖 Detailed walkthrough |
| **find_attack_speed.py** | 🤖 Automated search script |
| **NATIVE_CODE_ANALYSIS_SUMMARY.md** | 📊 Technical overview |
| **CODE_LOCATIONS.md** | 🗺️ IL2CPP dump reference |

## 🎯 What We're Looking For

The **exact ARM assembly code** that calculates:

```c
effectiveTime = baseTime / attackSpeedMulti
```

Specifically at these addresses:
- **0x5AF7094** - HandleUnits (main combat loop)
- **0x5AEE300** - Execute (combat entry)
- **0x5AF96F4** - ExecuteAttack

## 🔍 Expected Result

### In ARM Assembly:
```assembly
VLDR.32   s0, [r4, #0x58]    ; Load AttackDuration
VLDR.32   s1, [r5, #0x??]    ; Load AttackSpeedMulti
VDIV.F32  s2, s0, s1         ; DIVIDE: s2 = s0 / s1 ← THE PROOF!
VSTR.32   s2, [r4, #0x58]    ; Store result
```

### In Decompiled C:
```c
unit->AttackDuration = weapon->AttackDuration / stats->AttackSpeedMulti;
unit->WindUpDuration = weapon->WindupTime / stats->AttackSpeedMulti;
```

## ⚡ Automated Script Usage

Once Ghidra analysis is complete:

1. **Window → Script Manager**
2. Click **Script Directories** icon
3. Add: `D:\Kiro\tournament-pro`
4. Find: `find_attack_speed.py`
5. Double-click to run
6. Review console output

The script will:
- ✅ Find functions at known addresses
- ✅ Search for division operations
- ✅ Look for memory offsets (0x50, 0x58, 0x68)
- ✅ Decompile and show relevant code
- ✅ Highlight potential matches

## 🎮 Manual Navigation

If you prefer manual exploration:

1. Press **G** (Go To)
2. Enter: `5AF7094`
3. Look at **Decompiler** window (right side)
4. Search for division operations (`/`)
5. Check for offsets `0x50`, `0x58`, `0x68`

## 📊 Known Memory Offsets

From IL2CPP dump:

```
UnitEntity structure:
  +0x50: AttackTimer      (current countdown)
  +0x58: AttackDuration   (time between attacks)
  +0x68: WindUpDuration   (windup time)
```

## ⌨️ Essential Shortcuts

| Key | Action |
|-----|--------|
| **G** | Go to address |
| **Ctrl+E** | Search text |
| **Ctrl+Shift+E** | Search strings |
| **Space** | Toggle disassembly/decompiler |
| **F** | Follow reference |

## 🎯 Success = Finding This

You've found the formula when you see:

1. ✅ Division operation (`VDIV` or `/`)
2. ✅ References to offsets `0x58` or `0x68`
3. ✅ Variables like `AttackDuration`, `AttackSpeed`
4. ✅ Pattern: `result = base / multiplier`

## 📤 Export Results

When you find it:

1. **Right-click function** → Export → C/C++
2. Save to: `C:\ghidra\attack_speed_code.c`
3. **Or take screenshot**: File → Export → Screenshot

## 🐛 Troubleshooting

**Ghidra not open?**
```cmd
C:\ghidra\ghidra_12.0.2_PUBLIC\ghidraRun.bat
```

**Analysis taking forever?**
- Normal for 119 MB file!
- Check progress bar (bottom-right)
- Wait for "Ready" status

**Can't find functions?**
- Make sure analysis is complete
- Try automated script
- Use address search (G key)

## 📈 Time Estimate

- **Ghidra analysis**: 10-30 minutes (automated)
- **Finding code**: 15-60 minutes (with script)
- **Total**: ~1-2 hours for definitive answer

## 🎓 Learning Resources

- **Ghidra Docs**: `C:\ghidra\ghidra_12.0.2_PUBLIC\docs\index.html`
- **ARM Reference**: https://developer.arm.com/documentation/
- **Our Guides**: See files listed above

## 💡 Why This Matters

Finding the exact native code proves:
- ✅ The formula is division (not multiplication)
- ✅ Higher AttackSpeedMulti = faster attacks
- ✅ Our calculator uses the correct formula
- ✅ We understand the game mechanics completely

## 🎬 Next Steps

1. **If Ghidra is open**: Follow Quick Start steps
2. **If not**: Run `C:\ghidra\ghidra_12.0.2_PUBLIC\ghidraRun.bat`
3. **Read**: `GHIDRA_QUICK_START.md` for detailed steps
4. **Run**: `find_attack_speed.py` after analysis completes
5. **Report**: What you find!

---

## 📁 File Locations

```
C:\ghidra\
  └── ghidra_12.0.2_PUBLIC\          ← Ghidra installation
      └── ghidraRun.bat              ← Launch Ghidra

C:\apktool\
  └── config-armeabi-out\
      └── lib\armeabi-v7a\
          └── libil2cpp.so           ← Target file (119 MB)

D:\Kiro\tournament-pro\
  ├── find_attack_speed.py           ← Automated script
  ├── GHIDRA_QUICK_START.md          ← Quick reference
  ├── GHIDRA_ANALYSIS_GUIDE.md       ← Detailed guide
  ├── NATIVE_CODE_ANALYSIS_SUMMARY.md ← Technical overview
  └── CODE_LOCATIONS.md              ← IL2CPP reference
```

---

**🎯 READY TO GO!** Open Ghidra and start the analysis!

**Questions?** Check the guides or let me know what you find!
