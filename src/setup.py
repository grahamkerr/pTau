from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os
import numpy
from distutils import sysconfig
#import numpy.distutils.intelccompiler
import numpy.distutils.ccompiler
import platform as plt
import sys
import pathlib

p = pathlib.Path(sys.executable)
root_dir = str(pathlib.Path(*p.parts[0:-2]))
comp_flags=['-O3','-std=c++14','-march=native','-fPIC', '-fopenmp']

os.system('rm pyTau.cpp')

# if(plt.system() == 'Darwin'):
# root_dir = '/opt/local/'
# CC = 'clang'
# CXX= 'clang++'
# link_opts = ["-stdlib=libc++","-bundle","-undefined","dynamic_lookup"]
# else:
#     root_dir = '/usr/'
#     CC = 'gcc'
#     CXX= 'g++'
#     link_opts = ["-shared"]

## Set up for Graham Kerr because Mac OS + a gov laptop (no admin rights) makes life harder than it should be!
root_dir = '/Users/gskerr1/00_Packages/gcc-10.1.0/'
CC = 'gcc-10.1'
CXX = 'g++-10.1'
link_opts = ["-bundle","-undefined","dynamic_lookup"]

os.environ["CC"] = CC
os.environ["CXX"] = CXX

from distutils import sysconfig
sysconfig.get_config_vars()['CFLAGS'] = ''
sysconfig.get_config_vars()['OPT'] = ''
sysconfig.get_config_vars()['PY_CFLAGS'] = ''
sysconfig.get_config_vars()['PY_CORE_CFLAGS'] = ''
sysconfig.get_config_vars()['CC'] =  CC
sysconfig.get_config_vars()['CXX'] = CXX
sysconfig.get_config_vars()['BASECFLAGS'] = ''
sysconfig.get_config_vars()['CCSHARED'] = ''
sysconfig.get_config_vars()['LDSHARED'] = CC
sysconfig.get_config_vars()['CPP'] = CXX
sysconfig.get_config_vars()['CPPFLAGS'] = ''
sysconfig.get_config_vars()['BLDSHARED'] = ''
sysconfig.get_config_vars()['CONFIGURE_LDFLAGS'] = ''
sysconfig.get_config_vars()['LDFLAGS'] = ''
sysconfig.get_config_vars()['PY_LDFLAGS'] = ''



extension = Extension("pTau",
                      sources=["pyTau.pyx"], 
                      include_dirs=["./", root_dir+"/include/",numpy.get_include()],
                      language="c++",
                      extra_compile_args=comp_flags,
                      extra_link_args=comp_flags+link_opts,
                      library_dirs=[root_dir+'/lib/','./'],
                      libraries=[])

extension.cython_directives = {'language_level': "3"}

setup(
    name = 'pTau',
    version = '1.0',
    author = 'J. de la Cruz Rodriguez (ISP-SU 2021)',
    ext_modules=[extension],
    cmdclass = {'build_ext': build_ext}
)

