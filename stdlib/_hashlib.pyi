"""OpenSSL interface for hashlib module"""

import sys
from _typeshed import ReadableBuffer
from collections.abc import Callable
from types import ModuleType
from typing import AnyStr, Protocol, final, overload, type_check_only
from typing_extensions import Self, TypeAlias

_DigestMod: TypeAlias = str | Callable[[], _HashObject] | ModuleType | None

openssl_md_meth_names: frozenset[str]

@type_check_only
class _HashObject(Protocol):
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    def copy(self) -> Self: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def update(self, obj: ReadableBuffer, /) -> None: ...

class HASH:
    """
    A hash is an object used to calculate a checksum of a string of information.

    Methods:

    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object

    Attributes:

    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    def copy(self) -> Self:
        """Return a copy of the hash object."""
        ...
    def digest(self) -> bytes:
        """Return the digest value as a bytes object."""
        ...
    def hexdigest(self) -> str:
        """Return the digest value as a string of hexadecimal digits."""
        ...
    def update(self, obj: ReadableBuffer, /) -> None:
        """Update this hash object's state with the provided string."""
        ...

if sys.version_info >= (3, 10):
    class UnsupportedDigestmodError(ValueError): ...

class HASHXOF(HASH):
    """
    A hash is an object used to calculate a checksum of a string of information.

    Methods:

    update() -- updates the current digest with an additional string
    digest(length) -- return the current digest value
    hexdigest(length) -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object

    Attributes:

    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def digest(self, length: int) -> bytes:
        """Return the digest value as a bytes object."""
        ...
    def hexdigest(self, length: int) -> str:
        """Return the digest value as a string of hexadecimal digits."""
        ...

@final
class HMAC:
    """
    The object used to calculate HMAC of a message.

    Methods:

    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object

    Attributes:

    name -- the name, including the hash algorithm used by this object
    digest_size -- number of bytes in digest() output
    """
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    def copy(self) -> Self:
        """Return a copy ("clone") of the HMAC object."""
        ...
    def digest(self) -> bytes:
        """Return the digest of the bytes passed to the update() method so far."""
        ...
    def hexdigest(self) -> str:
        """
        Return hexadecimal digest of the bytes passed to the update() method so far.

        This may be used to exchange the value safely in email or other non-binary
        environments.
        """
        ...
    def update(self, msg: ReadableBuffer) -> None:
        """Update the HMAC object with msg."""
        ...

@overload
def compare_digest(a: ReadableBuffer, b: ReadableBuffer, /) -> bool:
    """
    Return 'a == b'.

    This function uses an approach designed to prevent
    timing analysis, making it appropriate for cryptography.

    a and b must both be of the same type: either str (ASCII only),
    or any bytes-like object.

    Note: If a and b are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of a and b--but not their values.
    """
    ...
@overload
def compare_digest(a: AnyStr, b: AnyStr, /) -> bool: ...
def get_fips_mode() -> int: ...
def hmac_new(key: bytes | bytearray, msg: ReadableBuffer = b"", digestmod: _DigestMod = None) -> HMAC: ...

if sys.version_info >= (3, 13):
    def new(
        name: str, data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_md5(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha1(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha224(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha256(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha384(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha512(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha3_224(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha3_256(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha3_384(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_sha3_512(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASH: ...
    def openssl_shake_128(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASHXOF: ...
    def openssl_shake_256(
        data: ReadableBuffer = b"", *, usedforsecurity: bool = True, string: ReadableBuffer | None = None
    ) -> HASHXOF: ...

else:
    def new(name: str, string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_md5(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha1(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha224(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha256(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha384(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha512(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha3_224(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha3_256(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha3_384(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_sha3_512(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASH: ...
    def openssl_shake_128(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASHXOF: ...
    def openssl_shake_256(string: ReadableBuffer = b"", *, usedforsecurity: bool = True) -> HASHXOF: ...

def hmac_digest(key: bytes | bytearray, msg: ReadableBuffer, digest: str) -> bytes: ...
def pbkdf2_hmac(
    hash_name: str, password: ReadableBuffer, salt: ReadableBuffer, iterations: int, dklen: int | None = None
) -> bytes:
    """Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function."""
    ...
def scrypt(
    password: ReadableBuffer, *, salt: ReadableBuffer, n: int, r: int, p: int, maxmem: int = 0, dklen: int = 64
) -> bytes:
    """scrypt password-based key derivation function."""
    ...
