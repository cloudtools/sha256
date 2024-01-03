from setuptools import setup
from Cython.Build import cythonize


setup(
    name='sha256',
    version='1.0',
    description='sha256 library with midstate',
    author='Mark Peek',
    author_email='mark@peek.org',
    license="MIT",
    ext_modules=cythonize(['sha256.pyx']),
    test_suite="tests",
)
