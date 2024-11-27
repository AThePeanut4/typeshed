"""passlib.handlers.digests - plain hash digests"""

from _typeshed import Incomplete
from typing import Any, ClassVar

import passlib.utils.handlers as uh

class HexDigestHash(uh.StaticHandler):
    """this provides a template for supporting passwords stored as plain hexadecimal hashes"""
    checksum_chars: ClassVar[str]
    supported: ClassVar[bool]

def create_hex_hash(digest, module="passlib.handlers.digests", django_name: Incomplete | None = None, required: bool = True):
    """
    create hex-encoded unsalted hasher for specified digest algorithm.

    .. versionchanged:: 1.7.3
        If called with unknown/supported digest, won't throw error immediately,
        but instead return a dummy hasher that will throw error when called.

        set ``required=True`` to restore old behavior.
    """
    ...

hex_md4: Any
hex_md5: Any
hex_sha1: Any
hex_sha256: Any
hex_sha512: Any

class htdigest(uh.MinimalHandler):
    """
    htdigest hash function.

    .. todo::
        document this hash
    """
    name: ClassVar[str]
    default_encoding: ClassVar[str]
    setting_kwds: ClassVar[tuple[str, ...]]
    context_kwds: ClassVar[tuple[str, ...]]
    @classmethod
    def hash(cls, secret, user, realm, encoding: Incomplete | None = None): ...  # type: ignore[override]
    @classmethod
    def verify(cls, secret, hash, user, realm, encoding: str = "utf-8"): ...  # type: ignore[override]
    @classmethod
    def identify(cls, hash): ...
    @classmethod
    def genconfig(cls): ...
    @classmethod
    def genhash(cls, secret, config, user, realm, encoding: Incomplete | None = None): ...  # type: ignore[override]
