#!/bin/bash
# Build script for macOS

echo "Building Tournament Pro for macOS..."

# Clean previous builds
echo "Cleaning previous builds..."
npm run clean

# Build the application
echo "Building application..."
npm run build

if [ $? -ne 0 ]; then
  echo "Build failed!"
  exit 1
fi

# Package for macOS
echo "Packaging for macOS..."
npm run package:mac

if [ $? -eq 0 ]; then
  echo "✓ macOS build complete!"
  echo "Output: dist-electron/"
  ls -lh dist-electron/*.dmg 2>/dev/null || echo "No .dmg files found"
  ls -lh dist-electron/*.zip 2>/dev/null || echo "No .zip files found"
else
  echo "✗ macOS packaging failed!"
  exit 1
fi
