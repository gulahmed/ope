# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['win32traceutil.py'],
             pathex=['C:\\Users\\ray\\Desktop\\git_projects\\ope\\ope\\client_tools\\svc'],
             binaries=[('logo_icon.ico', '.')],
             datas=[],
             hiddenimports=['sip', 'win32timezone'],
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
          name='trace',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True , icon='logo_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='trace')
