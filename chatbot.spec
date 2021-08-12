# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['chatbot.py'],
             pathex=['py파일 경로'],
             binaries=[],
             datas=[("파일 경로/anaconda3/Lib/site-packages/openpyxl/","./openpyxl"),
             ("파일경로/anaconda3/envs/chatbot/Lib/xml/etree","./xml.etree"),
             ("파일경로anaconda3/Lib/site-packages/konlpy/","./konlpy"),
             ("파일경로/anaconda3/Lib/site-packages/konlpy/java/","./konlpy/java"),
             ("파일경로/anaconda3/Lib/site-packages/konlpy/data/tagset/*","./konlpy/data/tagset"),
             ("파일경로/eta_assistant_results.xlsx","./eta_assistant_results.xlsx")],
             hiddenimports=["openpyxl","xml.etree"],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='chatbot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
