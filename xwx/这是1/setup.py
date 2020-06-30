import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'D:\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Python\Python36\tcl\tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('index.py', targetName='index.exe', base=base)
]

include_files = [
    r'D:\Python\Python36\DLLs\tcl86t.dll',
    r'D:\Python\Python36\DLLs\tk86t.dll'
]

buildOptions = dict(
    packages=[], excludes=[],
    include_files=include_files,
)

setup(
    name='测试1.0',
    version='1.0',
    description='测试',
    options=dict(build_exe=buildOptions),
    executables=executables
)