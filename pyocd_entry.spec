# -*- mode: python ; coding: utf-8 -*-

import os
import glob
import platform
import sys

from PyInstaller.building.api import PYZ, EXE
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import get_package_paths, collect_dynamic_libs

is_windows = (platform.system() == "Windows")
is_os_64bit = platform.machine().endswith("64")
if not is_windows or not is_os_64bit:
    print("only support windows x64")
    exit(-1)

binaries = []
binaries += [(os.path.join(get_package_paths('libusb_package')[1], r"libusb-1.0.dll"), ".")]

binaries += [
    (os.path.join(get_package_paths('pyocd')[1], r'debug\sequences\sequences.lark'),
     r'pyocd\debug\sequences'),
    (os.path.join(get_package_paths('cmsis_pack_manager')[1], r'cmsis_pack_manager\native.so'),
     r'cmsis_pack_manager\cmsis_pack_manager'),
]

datas = []

print("binaries", binaries)
print("datas", datas)

a = Analysis(['pyocd_entry.py'],
             pathex=[],
             binaries=binaries,
             datas=datas,
             hiddenimports=['usb'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          a.binaries,  # comment if using collect
          a.zipfiles,  # comment if using collect
          a.datas,  # comment if using collect
          [],
          # exclude_binaries=True, # un-comment if using collect
          name='pyocd',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],  # comment if using collect
          runtime_tmpdir=None,  # comment if using collect
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon="pyocd.ico")  # 设置程序的图标
