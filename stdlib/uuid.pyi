r"""
UUID objects (universally unique identifiers) according to RFC 4122.

This module provides immutable UUID objects (class UUID) and the functions
uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5
UUIDs as specified in RFC 4122.

If all you want is a unique ID, you should probably call uuid1() or uuid4().
Note that uuid1() may compromise privacy since it creates a UUID containing
the computer's network address.  uuid4() creates a random UUID.

Typical usage:

    >>> import uuid

    # make a UUID based on the host ID and current time
    >>> uuid.uuid1()    # doctest: +SKIP
    UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

    # make a UUID using an MD5 hash of a namespace UUID and a name
    >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

    # make a random UUID
    >>> uuid.uuid4()    # doctest: +SKIP
    UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

    # make a UUID using a SHA-1 hash of a namespace UUID and a name
    >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

    # make a UUID from a string of hex digits (braces and hyphens ignored)
    >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

    # convert a UUID to a string of hex digits in standard form
    >>> str(x)
    '00010203-0405-0607-0809-0a0b0c0d0e0f'

    # get the raw 16 bytes of the UUID
    >>> x.bytes
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

    # make a UUID from a 16-byte string
    >>> uuid.UUID(bytes=x.bytes)
    UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')
"""

import builtins
import sys
from _typeshed import Unused
from enum import Enum
from typing_extensions import TypeAlias

_FieldsType: TypeAlias = tuple[int, int, int, int, int, int]

class SafeUUID(Enum):
    """An enumeration."""
    safe = 0
    unsafe = -1
    unknown = None

class UUID:
    """
    Instances of the UUID class represent UUIDs as specified in RFC 4122.
    UUID objects are immutable, hashable, and usable as dictionary keys.
    Converting a UUID to a string with str() yields something in the form
    '12345678-1234-1234-1234-123456789abc'.  The UUID constructor accepts
    five possible forms: a similar string of hexadecimal digits, or a tuple
    of six integer fields (with 32-bit, 16-bit, 16-bit, 8-bit, 8-bit, and
    48-bit values respectively) as an argument named 'fields', or a string
    of 16 bytes (with all the integer fields in big-endian order) as an
    argument named 'bytes', or a string of 16 bytes (with the first three
    fields in little-endian order) as an argument named 'bytes_le', or a
    single 128-bit integer as an argument named 'int'.

    UUIDs have these read-only attributes:

        bytes       the UUID as a 16-byte string (containing the six
                    integer fields in big-endian byte order)

        bytes_le    the UUID as a 16-byte string (with time_low, time_mid,
                    and time_hi_version in little-endian byte order)

        fields      a tuple of the six integer fields of the UUID,
                    which are also available as six individual attributes
                    and two derived attributes:

            time_low                the first 32 bits of the UUID
            time_mid                the next 16 bits of the UUID
            time_hi_version         the next 16 bits of the UUID
            clock_seq_hi_variant    the next 8 bits of the UUID
            clock_seq_low           the next 8 bits of the UUID
            node                    the last 48 bits of the UUID

            time                    the 60-bit timestamp
            clock_seq               the 14-bit sequence number

        hex         the UUID as a 32-character hexadecimal string

        int         the UUID as a 128-bit integer

        urn         the UUID as a URN as specified in RFC 4122

        variant     the UUID variant (one of the constants RESERVED_NCS,
                    RFC_4122, RESERVED_MICROSOFT, or RESERVED_FUTURE)

        version     the UUID version number (1 through 5, meaningful only
                    when the variant is RFC_4122)

        is_safe     An enum indicating whether the UUID has been generated in
                    a way that is safe for multiprocessing applications, via
                    uuid_generate_time_safe(3).
    """
    def __init__(
        self,
        hex: str | None = None,
        bytes: builtins.bytes | None = None,
        bytes_le: builtins.bytes | None = None,
        fields: _FieldsType | None = None,
        int: builtins.int | None = None,
        version: builtins.int | None = None,
        *,
        is_safe: SafeUUID = ...,
    ) -> None:
        r"""
        Create a UUID from either a string of 32 hexadecimal digits,
        a string of 16 bytes as the 'bytes' argument, a string of 16 bytes
        in little-endian order as the 'bytes_le' argument, a tuple of six
        integers (32-bit time_low, 16-bit time_mid, 16-bit time_hi_version,
        8-bit clock_seq_hi_variant, 8-bit clock_seq_low, 48-bit node) as
        the 'fields' argument, or a single 128-bit integer as the 'int'
        argument.  When a string of hex digits is given, curly braces,
        hyphens, and a URN prefix are all optional.  For example, these
        expressions all yield the same UUID:

        UUID('{12345678-1234-5678-1234-567812345678}')
        UUID('12345678123456781234567812345678')
        UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
        UUID(bytes='\x12\x34\x56\x78'*4)
        UUID(bytes_le='\x78\x56\x34\x12\x34\x12\x78\x56' +
                      '\x12\x34\x56\x78\x12\x34\x56\x78')
        UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
        UUID(int=0x12345678123456781234567812345678)

        Exactly one of 'hex', 'bytes', 'bytes_le', 'fields', or 'int' must
        be given.  The 'version' argument is optional; if given, the resulting
        UUID will have its variant and version set according to RFC 4122,
        overriding the given 'hex', 'bytes', 'bytes_le', 'fields', or 'int'.

        is_safe is an enum exposed as an attribute on the instance.  It
        indicates whether the UUID has been generated in a way that is safe
        for multiprocessing applications, via uuid_generate_time_safe(3).
        """
        ...
    @property
    def is_safe(self) -> SafeUUID: ...
    @property
    def bytes(self) -> builtins.bytes: ...
    @property
    def bytes_le(self) -> builtins.bytes: ...
    @property
    def clock_seq(self) -> builtins.int: ...
    @property
    def clock_seq_hi_variant(self) -> builtins.int: ...
    @property
    def clock_seq_low(self) -> builtins.int: ...
    @property
    def fields(self) -> _FieldsType: ...
    @property
    def hex(self) -> str: ...
    @property
    def int(self) -> builtins.int: ...
    @property
    def node(self) -> builtins.int: ...
    @property
    def time(self) -> builtins.int: ...
    @property
    def time_hi_version(self) -> builtins.int: ...
    @property
    def time_low(self) -> builtins.int: ...
    @property
    def time_mid(self) -> builtins.int: ...
    @property
    def urn(self) -> str: ...
    @property
    def variant(self) -> str: ...
    @property
    def version(self) -> builtins.int | None: ...
    def __int__(self) -> builtins.int: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: UUID) -> bool: ...
    def __le__(self, other: UUID) -> bool: ...
    def __gt__(self, other: UUID) -> bool: ...
    def __ge__(self, other: UUID) -> bool: ...
    def __hash__(self) -> builtins.int: ...

if sys.version_info >= (3, 9):
    def getnode() -> int:
        """
        Get the hardware address as a 48-bit positive integer.

        The first time this runs, it may launch a separate program, which could
        be quite slow.  If all attempts to obtain the hardware address fail, we
        choose a random 48-bit number with its eighth bit set to 1 as recommended
        in RFC 4122.
        """
        ...

else:
    def getnode(*, getters: Unused = None) -> int: ...  # undocumented

def uuid1(node: int | None = None, clock_seq: int | None = None) -> UUID:
    """
    Generate a UUID from a host ID, sequence number, and the current time.
    If 'node' is not given, getnode() is used to obtain the hardware
    address.  If 'clock_seq' is given, it is used as the sequence number;
    otherwise a random 14-bit sequence number is chosen.
    """
    ...

if sys.version_info >= (3, 12):
    def uuid3(namespace: UUID, name: str | bytes) -> UUID:
        """Generate a UUID from the MD5 hash of a namespace UUID and a name."""
        ...

else:
    def uuid3(namespace: UUID, name: str) -> UUID:
        """Generate a UUID from the MD5 hash of a namespace UUID and a name."""
        ...

def uuid4() -> UUID:
    """Generate a random UUID."""
    ...

if sys.version_info >= (3, 12):
    def uuid5(namespace: UUID, name: str | bytes) -> UUID:
        """Generate a UUID from the SHA-1 hash of a namespace UUID and a name."""
        ...

else:
    def uuid5(namespace: UUID, name: str) -> UUID:
        """Generate a UUID from the SHA-1 hash of a namespace UUID and a name."""
        ...

NAMESPACE_DNS: UUID
NAMESPACE_URL: UUID
NAMESPACE_OID: UUID
NAMESPACE_X500: UUID
RESERVED_NCS: str
RFC_4122: str
RESERVED_MICROSOFT: str
RESERVED_FUTURE: str

if sys.version_info >= (3, 12):
    def main() -> None:
        """Run the uuid command line interface."""
        ...
