@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo   Building WEB AI Standalone Executable for Windows
echo ========================================================
echo.

:: Check python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b 1
)

:: Install PyInstaller and dependencies if needed
echo [*] Checking dependencies...
pip install -r requirements.txt
pip install pyinstaller

:: Clean previous builds
echo [*] Cleaning previous build caches...
if exist build rd /s /q build
if exist dist rd /s /q dist

:: Build executable
echo [*] Running PyInstaller with optimized exclusions...
pyinstaller WEB_AI_OS.spec --clean --noconfirm

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   [SUCCESS] Windows executable built successfully!
    echo   Location: dist\WEB_AI_OS.exe
    echo ========================================================
) else (
    echo.
    echo [ERROR] Build failed! Check the output above.
)

pause
