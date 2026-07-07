# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

block_cipher = None

# -- Collect data files dynamically -------------------------------------------
_datas = []

# data/ — YAML, JSON, ZIP
for _pat in ['*.yaml', '*.json', '*.zip']:
    for _p in Path('data').glob(_pat):
        _datas.append((str(_p), 'data'))

# fonts/ — all font files
for _p in Path('fonts').iterdir():
    if _p.is_file():
        _datas.append((str(_p), 'fonts'))

# images/ — entire directory
_datas.append(('images', 'images'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=_datas,
    hiddenimports=[
        'PyQt6.sip',
        'PyQt6.QtNetwork',
        'reportlab.graphics',
        'reportlab.graphics.charts',
        'reportlab.lib.pagesizes',
        'PIL._imaging',
        'certifi',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Dev/test
        'pytest', 'pytest_qt', 'unittest', '_pytest',
        # Unused PyQt6 modules
        'PyQt6.QtBluetooth',
        'PyQt6.QtDesigner',
        'PyQt6.QtHelp',
        'PyQt6.QtMultimedia',
        'PyQt6.QtMultimediaWidgets',
        'PyQt6.QtNfc',
        'PyQt6.QtPositioning',
        'PyQt6.QtQml',
        'PyQt6.QtQuick',
        'PyQt6.QtQuickWidgets',
        'PyQt6.QtRemoteObjects',
        'PyQt6.QtSensors',
        'PyQt6.QtSerialPort',
        'PyQt6.QtSql',
        'PyQt6.QtTest',
        'PyQt6.QtTextToSpeech',
        'PyQt6.QtWebChannel',
        'PyQt6.QtWebEngineCore',
        'PyQt6.QtWebEngineQuick',
        'PyQt6.QtWebEngineWidgets',
        'PyQt6.QtWebSockets',
        'PyQt6.QtXml',
        # Unused stdlib
        'tkinter',
        'xmlrpc', 'pydoc', 'doctest', 'difflib',
        'turtle', 'curses',
        # Unused PIL formats
        'PIL.BmpImagePlugin', 'PIL.DdsImagePlugin',
        'PIL.EpsImagePlugin', 'PIL.FitsImagePlugin',
        'PIL.GifImagePlugin', 'PIL.IcnsImagePlugin',
        'PIL.PsdImagePlugin', 'PIL.TiffImagePlugin',
        'PIL.WebPImagePlugin', 'PIL.XpmImagePlugin',
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
    [],
    exclude_binaries=True,
    name='BTOverrideCardGenerator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='images/bt_logo.ico',
    version='version_metadata.txt',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='BT_Override_Card_Generator',
)
