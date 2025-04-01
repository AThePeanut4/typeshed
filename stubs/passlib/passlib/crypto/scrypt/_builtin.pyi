"""passlib.utils.scrypt._builtin -- scrypt() kdf in pure-python"""

from collections.abc import Generator
from typing import Any

class ScryptEngine:
    """
    helper class used to run scrypt kdf, see scrypt() for frontend

    .. warning::
        this class does NO validation of the input ranges or types.

        it's not intended to be used directly,
        but only as a backend for :func:`passlib.utils.scrypt.scrypt()`.
    """
    n: int
    r: int
    p: int
    smix_bytes: int
    iv_bytes: int
    bmix_len: int
    bmix_half_len: int
    bmix_struct: Any
    integerify: Any
    @classmethod
    def execute(cls, secret, salt, n, r, p, keylen):
        """create engine & run scrypt() hash calculation"""
        ...
    def __init__(self, n, r, p): ...
    def run(self, secret, salt, keylen): ...
    def smix(self, input) -> Generator[None, None, Any]: ...
    def bmix(self, source, target) -> None: ...

__all__ = ["ScryptEngine"]
