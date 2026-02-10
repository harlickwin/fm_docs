#!/bin/bash
# Build script for Windows

echo "Building Tournament Pro for Windows..."

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

# Package for Windows
echo "Packaging for Windows..."
npm run package:win

if [ $? -eq 0 ]; then
  echo "✓ Windows build complete!"
  echo "Output: dist-electron/"
  ls -lh dist-electron/*.exe 2>/dev/null || echo "No .exe files found"
else
  echo "✗ Windows packaging failed!"
  exit 1
fi
