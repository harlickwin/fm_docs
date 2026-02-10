#!/bin/bash
# Build script for all platforms

echo "Building Tournament Pro for all platforms..."

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

# Package for all platforms
echo "Packaging for all platforms..."
npm run package:all

if [ $? -eq 0 ]; then
  echo "✓ All platform builds complete!"
  echo "Output: dist-electron/"
  echo ""
  echo "Windows builds:"
  ls -lh dist-electron/*.exe 2>/dev/null || echo "  No .exe files found"
  echo ""
  echo "macOS builds:"
  ls -lh dist-electron/*.dmg 2>/dev/null || echo "  No .dmg files found"
  ls -lh dist-electron/*.zip 2>/dev/null || echo "  No .zip files found"
  echo ""
  echo "Linux builds:"
  ls -lh dist-electron/*.AppImage 2>/dev/null || echo "  No .AppImage files found"
  ls -lh dist-electron/*.deb 2>/dev/null || echo "  No .deb files found"
  ls -lh dist-electron/*.rpm 2>/dev/null || echo "  No .rpm files found"
else
  echo "✗ Packaging failed!"
  exit 1
fi
