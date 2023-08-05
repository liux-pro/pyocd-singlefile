# -*- mode: python ; coding: utf-8 -*-

import glob
import platform
import sys

from PyInstaller.utils.hooks import (get_package_paths, collect_dynamic_libs)


block_cipher = None

is_windows = (platform.system() == "Windows")
is_os_64bit = platform.machine().endswith("64")
pyversion = platform.python_version().split(".")

# Get binary extension libraries...

# Capstone for disassembly.
capstone_libs = collect_dynamic_libs("capstone")



cpm_libs = []

binaries = capstone_libs + cpm_libs
binaries += [(os.path.join(get_package_paths('libusb_package')[1], r"libusb-1.0.dll"), ".")]

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
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries, # comment if using collect
          a.zipfiles, # comment if using collect
          a.datas,  # comment if using collect
          [],
          # exclude_binaries=True, # un-comment if using collect
          name='pyocd',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[], # comment if using collect
          runtime_tmpdir=None, # comment if using collect
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )