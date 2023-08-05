# auto-generated file
__all__ = ['lib', 'ffi']

import os
import sys
from cmsis_pack_manager._native__ffi import ffi

try:
    lib = ffi.dlopen(os.path.join(os.path.dirname(__file__),
                                  f"_native__lib.cp3{sys.version_info.minor}-win_amd64.pyd"), 0)
except:
    import sys
    lib = ffi.dlopen(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                                  f"_native__lib.cp3{sys.version_info.minor}-win_amd64.pyd"), 0)
del os
del sys
