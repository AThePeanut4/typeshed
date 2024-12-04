"""
passlib.win32 - MS Windows support - DEPRECATED, WILL BE REMOVED IN 1.8

the LMHASH and NTHASH algorithms are used in various windows related contexts,
but generally not in a manner compatible with how passlib is structured.

in particular, they have no identifying marks, both being
32 bytes of binary data. thus, they can't be easily identified
in a context with other hashes, so a CryptHandler hasn't been defined for them.

this module provided two functions to aid in any use-cases which exist.

.. warning::

    these functions should not be used for new code unless an existing
    system requires them, they are both known broken,
    and are beyond insecure on their own.

.. autofunction:: raw_lmhash
.. autofunction:: raw_nthash

See also :mod:`passlib.hash.nthash`.
"""

from typing import Any

from passlib.hash import nthash as nthash

raw_nthash: Any

def raw_lmhash(secret, encoding: str = "ascii", hex: bool = False):
    """encode password using des-based LMHASH algorithm; returns string of raw bytes, or unicode hex"""
    ...
