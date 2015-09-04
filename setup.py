from distutils.core import setup
from distutils.extension import Extension
from distutils.command.sdist import sdist as _sdist

cmdclass = {}


class sdist(_sdist):
    def run(self):
        from Cython.Build import cythonize
        cythonize(['sha256.pyx'])
        _sdist.run(self)
cmdclass['sdist'] = sdist


setup(
    name='sha256',
    version='0.1',
    description='sha256 library with midstate',
    author='Mark Peek',
    author_email='mark@peek.org',
    license="MIT",
    cmdclass=cmdclass,
    ext_modules=[Extension("sha256", ["sha256.c"])],
)
