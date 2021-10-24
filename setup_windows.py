import os.path
import re
import sys
from pprint import pprint

from setuptools import Extension, find_packages, setup


def verify_folders(folders):
    folders_real = []
    for folder in folders:
        if not os.path.exists(folder):
            print('Invalid folder: %s' % folder)
        else:
            folders_real.append(os.path.realpath(folder))

    return folders_real


VERSION="0.5.2"

_incdirs = ['./netsnmp']
_libdirs = []

args = sys.argv[:]
for arg in args:
    if '--incdir' in arg:
        incdir = arg.split('=')[1]
        sys.argv.remove(arg)
        _incdirs.append(incdir)
    if '--libdir' in arg:
        libdir = arg.split('=')[1]
        sys.argv.remove(arg)
        _libdirs.append(libdir)
    if '--include-dirs' in arg:
        inc = arg.split('=')[1]
        _incdirs += inc.split(';')
    if '--library-dirs' in arg:
        inc = arg.split('=')[1]
        _libdirs += inc.split(';')


incdirs = verify_folders(_incdirs)
libdirs = verify_folders(_libdirs)

print('Include folders:')
pprint(incdirs)
print('Library folders:')
pprint(libdirs)
print('Library folders not verified:')
pprint(_libdirs)

if not incdirs:
    raise FileNotFoundError('No valid include folders')

if not libdirs:
    raise FileNotFoundError('No valid library folders')

# Asynchronous IPC
libs = ['netsnmp', 'zmq', 'czmq']

setup(
    name="netsnmp-py",
    version=VERSION,
    description='Python NET-SNMP Bindings',
    author='Gabe Pacuilla',
    author_email='root@un1x.su',
    url='https://github.com/xstaticxgpx/netsnmp-py3',
    license='MIT License',
    download_url='https://github.com/xstaticxgpx/netsnmp-py3/archive/v%s.tar.gz' % VERSION,
    packages=find_packages(),
    ext_modules = [
       Extension("netsnmp._api",
                 ["netsnmp/session.c",
                  "netsnmp/get.c",
                  "netsnmp/get_async.c",
                  "netsnmp/interface.c",
                  "netsnmp/_api.c"],
                 library_dirs=libdirs,
                 include_dirs=incdirs,
                 libraries=libs)
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: C',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)
