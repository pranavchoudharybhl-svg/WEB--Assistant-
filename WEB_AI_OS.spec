# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_all, collect_submodules, collect_data_files

block_cipher = None

# Base directory
base_dir = Path('.').resolve()

# Collect dependencies
datas = [
    (str(base_dir / 'frontend'), 'frontend'),
]

# Hidden imports for FastAPI, Uvicorn, SQLite, HTTPX, and Starlette
hiddenimports = [
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespans',
    'uvicorn.lifespans.on',
    'fastapi',
    'fastapi.middleware.cors',
    'fastapi.staticfiles',
    'fastapi.responses',
    'starlette',
    'starlette.middleware',
    'starlette.middleware.cors',
    'starlette.staticfiles',
    'starlette.responses',
    'pydantic',
    'psutil',
    'httpx',
    'bs4',
    'sqlite3',
    'dotenv',
    'backend',
    'backend.main',
    'backend.config',
    'backend.database',
    'backend.database.database',
    'backend.database.models',
    'backend.api',
    'backend.api.chat',
    'backend.api.factcheck',
    'backend.api.tasks',
    'backend.api.conversations',
    'backend.api.files',
    'backend.api.memory',
    'backend.api.tools',
    'backend.api.system',
    'backend.services',
    'backend.services.assistant',
    'backend.services.factchecker',
    'backend.services.heartbeat',
    'backend.services.search',
    'backend.services.task_service',
    'backend.tools',
    'backend.tools.registry',
    'backend.tools.system_tools',
    'backend.tools.file_tools',
    'backend.tools.web_tools',
    'backend.ai',
    'backend.ai.base',
    'backend.ai.router',
    'backend.ai.prompts',
    'backend.ai.gemini_provider',
    'backend.ai.ollama_provider',
    'backend.memory',
    'backend.memory.manager',
]

a = Analysis(
    ['run.py'],
    pathex=[str(base_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'unittest',
        'test',
        'xmlrpc',
        'pydoc_data',
        'curses',
        'turtle',
        'idlelib',
        'matplotlib',
        'scipy',
        'pandas',
        'IPython',
        'notebook',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WEB_AI_OS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
