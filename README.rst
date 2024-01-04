This is a SHA-256 implementation that allows for setting and getting
the mid-state information. This was needed to enable repeated hashing
against a (potentially large) fixed prefix.

Performance
===========
The original version of this was written in Python. While the Cython
version will be much faster, this is not a highly optimized library and
relies on the native C compiler for optimization.

Cythonize
=========
This repository does not contain the generated C code from Cython. To
recreate the C code run the cythonize step via::

    python3 -m pip install --upgrade build
    python3 -m build

Testing
=======
To run the unit test suite:

    python3 -m pip install --upgrade nox
    python3 -m nox

Authors
=======
The original author was Thomas Dixon for a python version of this code.
Sam Rushing added the midstate access and converted it to Cython_.
Nigel Drego added the context state setter/getter.

LICENSE
=======
This is licensed under the `MIT license`_ based on the original
license from Thomas Dixon.

.. _Cython: http://cython.org
.. _`MIT license`: http://opensource.org/licenses/MIT
