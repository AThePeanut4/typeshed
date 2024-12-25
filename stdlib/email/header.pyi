"""Header encoding and decoding functionality."""

from collections.abc import Iterable
from email.charset import Charset
from typing import Any, ClassVar

__all__ = ["Header", "decode_header", "make_header"]

class Header:
    def __init__(
        self,
        s: bytes | bytearray | str | None = None,
        charset: Charset | str | None = None,
        maxlinelen: int | None = None,
        header_name: str | None = None,
        continuation_ws: str = " ",
        errors: str = "strict",
    ) -> None: ...
    def append(self, s: bytes | bytearray | str, charset: Charset | str | None = None, errors: str = "strict") -> None: ...
    def encode(self, splitchars: str = ";, \t", maxlinelen: int | None = None, linesep: str = "\n") -> str: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, value: object, /) -> bool:
        """Return self!=value."""
        ...

# decode_header() either returns list[tuple[str, None]] if the header
# contains no encoded parts, or list[tuple[bytes, str | None]] if the header
# contains at least one encoded part.
def decode_header(header: Header | str) -> list[tuple[Any, Any | None]]:
    """
    Decode a message header value without converting charset.

    Returns a list of (string, charset) pairs containing each of the decoded
    parts of the header.  Charset is None for non-encoded parts of the header,
    otherwise a lower-case string containing the name of the character set
    specified in the encoded string.

    header may be a string that may or may not contain RFC2047 encoded words,
    or it may be a Header object.

    An email.errors.HeaderParseError may be raised when certain decoding error
    occurs (e.g. a base64 decoding exception).
    """
    ...
def make_header(
    decoded_seq: Iterable[tuple[bytes | bytearray | str, str | None]],
    maxlinelen: int | None = None,
    header_name: str | None = None,
    continuation_ws: str = " ",
) -> Header:
    """
    Create a Header from a sequence of pairs as returned by decode_header()

    decode_header() takes a header value string and returns a sequence of
    pairs of the format (decoded_string, charset) where charset is the string
    name of the character set.

    This function takes one of those sequence of pairs and returns a Header
    instance.  Optional maxlinelen, header_name, and continuation_ws are as in
    the Header constructor.
    """
    ...
