@echo off
REM Build script for Windows

echo Building Tournament Pro for Windows...

REM Clean previous builds
echo Cleaning previous builds...
call npm run clean

REM Build the application
echo Building application...
call npm run build

if %errorlevel% neq 0 (
  echo Build failed!
  exit /b 1
)

REM Package for Windows
echo Packaging for Windows...
call npm run package:win

if %errorlevel% equ 0 (
  echo ✓ Windows build complete!
  echo Output: dist-electron\
  dir dist-electron\*.exe 2>nul || echo No .exe files found
) else (
  echo ✗ Windows packaging failed!
  exit /b 1
)
