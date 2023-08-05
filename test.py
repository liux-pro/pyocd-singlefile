from PyInstaller.utils.hooks import get_package_paths

package_ = get_package_paths('pyocd')
print(package_)