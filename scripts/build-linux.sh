#!/bin/bash
# Build script for Linux

echo "Building Tournament Pro for Linux..."

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

# Package for Linux
echo "Packaging for Linux..."
npm run package:linux

if [ $? -eq 0 ]; then
  echo "✓ Linux build complete!"
  echo "Output: dist-electron/"
  ls -lh dist-electron/*.AppImage 2>/dev/null || echo "No .AppImage files found"
  ls -lh dist-electron/*.deb 2>/dev/null || echo "No .deb files found"
  ls -lh dist-electron/*.rpm 2>/dev/null || echo "No .rpm files found"
else
  echo "✗ Linux packaging failed!"
  exit 1
fi
