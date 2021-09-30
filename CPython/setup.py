import os
from setuptools import setup, Extension

from src.__about__ import __title__, __version__, __description__

os.environ["CC"] = "gcc"

extension = Extension(__title__,
                      sources=[f'src/{__title__}.c'],
                      library_dirs=[os.getcwd()],
                      include_dirs=[os.getcwd()],
                      extra_link_args=[
                          f'-dynamiclib {__title__}.so']
                      )

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    ext_modules=[extension],
    # packages=[''],
    # package_dir={'': '.'},
    # package_data={'': ['GoExtensionExampleGo.so']},
    # include_package_data=True
)
