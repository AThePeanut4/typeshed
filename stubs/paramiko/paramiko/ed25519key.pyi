from _typeshed import FileDescriptorOrPath, ReadableBuffer
from typing import IO

from paramiko.message import Message
from paramiko.pkey import PKey

class Ed25519Key(PKey):
    """
    Representation of an `Ed25519 <https://ed25519.cr.yp.to/>`_ key.

    .. note::
        Ed25519 key support was added to OpenSSH in version 6.5.

    .. versionadded:: 2.2
    .. versionchanged:: 2.3
        Added a ``file_obj`` parameter to match other key classes.
    """
    public_blob: None
    def __init__(
        self,
        msg: Message | None = None,
        data: ReadableBuffer | None = None,
        filename: FileDescriptorOrPath | None = None,
        password: str | None = None,
        file_obj: IO[str] | None = None,
    ) -> None: ...
    def asbytes(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def sign_ssh_data(self, data: bytes, algorithm: str | None = None) -> Message: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
