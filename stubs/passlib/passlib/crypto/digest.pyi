"""
passlib.crypto.digest -- crytographic helpers used by the password hashes in passlib

.. versionadded:: 1.7
"""

from _typeshed import Incomplete
from typing import Any

from passlib.utils import SequenceMixin

def lookup_hash(digest, return_unknown: bool = False, required: bool = True):
    """
    Returns a :class:`HashInfo` record containing information about a given hash function.
    Can be used to look up a hash constructor by name, normalize hash name representation, etc.

    :arg digest:
        This can be any of:

        * A string containing a :mod:`!hashlib` digest name (e.g. ``"sha256"``),
        * A string containing an IANA-assigned hash name,
        * A digest constructor function (e.g. ``hashlib.sha256``).

        Case is ignored, underscores are converted to hyphens,
        and various other cleanups are made.

    :param required:
        By default (True), this function will throw an :exc:`~passlib.exc.UnknownHashError` if no hash constructor
        can be found, or if the hash is not actually available.

        If this flag is False, it will instead return a dummy :class:`!HashInfo` record
        which will defer throwing the error until it's constructor function is called.
        This is mainly used by :func:`norm_hash_name`.

    :param return_unknown:

        .. deprecated:: 1.7.3

            deprecated, and will be removed in passlib 2.0.
            this acts like inverse of **required**.

    :returns HashInfo:
        :class:`HashInfo` instance containing information about specified digest.

        Multiple calls resolving to the same hash should always
        return the same :class:`!HashInfo` instance.
    """
    ...
def norm_hash_name(name, format: str = "hashlib"):
    """
    Normalize hash function name (convenience wrapper for :func:`lookup_hash`).

    :arg name:
        Original hash function name.

        This name can be a Python :mod:`~hashlib` digest name,
        a SCRAM mechanism name, IANA assigned hash name, etc.
        Case is ignored, and underscores are converted to hyphens.

    :param format:
        Naming convention to normalize to.
        Possible values are:

        * ``"hashlib"`` (the default) - normalizes name to be compatible
          with Python's :mod:`!hashlib`.

        * ``"iana"`` - normalizes name to IANA-assigned hash function name.
          For hashes which IANA hasn't assigned a name for, this issues a warning,
          and then uses a heuristic to return a "best guess" name.

    :returns:
        Hash name, returned as native :class:`!str`.
    """
    ...

class HashInfo(SequenceMixin):
    """
    Record containing information about a given hash algorithm, as returned :func:`lookup_hash`.

    This class exposes the following attributes:

    .. autoattribute:: const
    .. autoattribute:: digest_size
    .. autoattribute:: block_size
    .. autoattribute:: name
    .. autoattribute:: iana_name
    .. autoattribute:: aliases
    .. autoattribute:: supported

    This object can also be treated a 3-element sequence
    containing ``(const, digest_size, block_size)``.
    """
    name: Any
    iana_name: Any
    aliases: Any
    const: Any
    digest_size: Any
    block_size: Any
    error_text: Any
    unknown: bool
    def __init__(self, const, names, required: bool = True) -> None:
        """
        initialize new instance.
        :arg const:
            hash constructor
        :arg names:
            list of 2+ names. should be list of ``(name, iana_name, ... 0+ aliases)``.
            names must be lower-case. only iana name may be None.
        """
        ...
    @property
    def supported(self):
        """
        whether hash is available for use
        (if False, constructor will throw UnknownHashError if called)
        """
        ...
    @property
    def supported_by_fastpbkdf2(self):
        """helper to detect if hash is supported by fastpbkdf2()"""
        ...
    @property
    def supported_by_hashlib_pbkdf2(self):
        """helper to detect if hash is supported by hashlib.pbkdf2_hmac()"""
        ...

def compile_hmac(digest, key, multipart: bool = False): ...
def pbkdf1(digest, secret, salt, rounds, keylen: Incomplete | None = None): ...
def pbkdf2_hmac(digest, secret, salt, rounds, keylen: Incomplete | None = None): ...

__all__ = [
    # hash utils
    "lookup_hash",
    "HashInfo",
    "norm_hash_name",
    # hmac utils
    "compile_hmac",
    # kdfs
    "pbkdf1",
    "pbkdf2_hmac",
]
