# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run_game.py'],
             pathex=['bullet.py', 'button.py', 'game_stats.py', 'game_functions.py', 'settings.py', 'ship.py', 'rectangle.py', 'F:\\packed file\\rabbit'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='rabbit_head',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='./images/timg.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='rabbit_head')
