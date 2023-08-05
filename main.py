import shutil
from PyInstaller.utils.hooks import get_package_paths
cmsis_pack_manager_dir = get_package_paths('cmsis_pack_manager')[1]
shutil.copy("_native.py", cmsis_pack_manager_dir)