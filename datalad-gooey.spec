# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cli.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['datalad', 'datalad_gooey', 'datalad_gooey.simplified_api'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='datalad-gooey',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='datalad-gooey',
)
app = BUNDLE(
    coll,
    name='datalad-gooey.app',
    icon='datalad_gooey_logo.icns',
    bundle_identifier=None,
)
