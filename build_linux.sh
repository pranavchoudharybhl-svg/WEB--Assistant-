#!/usr/bin/env bash
set -e

echo "========================================================"
echo "  Building WEB AI Standalone Executable for Linux"
echo "========================================================"
echo ""

# Ensure Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 is not installed or not in PATH."
    exit 1
fi

echo "[*] Installing dependencies & PyInstaller..."
pip install -r requirements.txt
pip install pyinstaller

echo "[*] Cleaning previous build caches..."
rm -rf build dist

echo "[*] Running PyInstaller..."
pyinstaller WEB_AI_OS.spec --clean --noconfirm

if [ -f "dist/WEB_AI_OS" ]; then
    chmod +x dist/WEB_AI_OS
    echo ""
    echo "========================================================"
    echo "  [SUCCESS] Linux binary built successfully!"
    echo "  Location: dist/WEB_AI_OS"
    echo "========================================================"
else
    echo "[ERROR] Linux build failed."
    exit 1
fi
