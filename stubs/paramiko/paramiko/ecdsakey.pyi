"""ECDSA keys"""

from _typeshed import FileDescriptorOrPath, ReadableBuffer
from collections.abc import Callable, Sequence
from typing import IO, Any

from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurve, EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from paramiko.message import Message
from paramiko.pkey import PKey

class _ECDSACurve:
    """
    Represents a specific ECDSA Curve (nistp256, nistp384, etc).

    Handles the generation of the key format identifier and the selection of
    the proper hash function. Also grabs the proper curve from the 'ecdsa'
    package.
    """
    nist_name: str
    key_length: int
    key_format_identifier: str
    hash_object: type[HashAlgorithm]
    curve_class: type[EllipticCurve]
    def __init__(self, curve_class: type[EllipticCurve], nist_name: str) -> None: ...

class _ECDSACurveSet:
    """
    A collection to hold the ECDSA curves. Allows querying by oid and by key
    format identifier. The two ways in which ECDSAKey needs to be able to look
    up curves.
    """
    ecdsa_curves: Sequence[_ECDSACurve]
    def __init__(self, ecdsa_curves: Sequence[_ECDSACurve]) -> None: ...
    def get_key_format_identifier_list(self) -> list[str]: ...
    def get_by_curve_class(self, curve_class: type[Any]) -> _ECDSACurve | None: ...
    def get_by_key_format_identifier(self, key_format_identifier: str) -> _ECDSACurve | None: ...
    def get_by_key_length(self, key_length: int) -> _ECDSACurve | None: ...

class ECDSAKey(PKey):
    """
    Representation of an ECDSA key which can be used to sign and verify SSH2
    data.
    """
    verifying_key: EllipticCurvePublicKey
    signing_key: EllipticCurvePrivateKey
    public_blob: None
    ecdsa_curve: _ECDSACurve | None
    def __init__(
        self,
        msg: Message | None = None,
        data: ReadableBuffer | None = None,
        filename: FileDescriptorOrPath | None = None,
        password: str | None = None,
        vals: tuple[EllipticCurvePrivateKey, EllipticCurvePublicKey] | None = None,
        file_obj: IO[str] | None = None,
        validate_point: bool = True,
    ) -> None: ...
    @classmethod
    def supported_key_format_identifiers(cls: Any) -> list[str]: ...
    def asbytes(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def sign_ssh_data(self, data: bytes, algorithm: str | None = None) -> Message: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
    def write_private_key_file(self, filename: FileDescriptorOrPath, password: str | None = None) -> None: ...
    def write_private_key(self, file_obj: IO[str], password: str | None = None) -> None: ...
    @classmethod
    def generate(
        cls, curve: EllipticCurve = ..., progress_func: Callable[..., object] | None = None, bits: int | None = None
    ) -> ECDSAKey:
        """
        Generate a new private ECDSA key.  This factory function can be used to
        generate a new host key or authentication key.

        :param progress_func: Not used for this type of key.
        :returns: A new private key (`.ECDSAKey`) object
        """
        ...
