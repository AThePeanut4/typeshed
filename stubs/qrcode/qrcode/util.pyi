from collections.abc import Callable, Generator
from re import Pattern
from typing import Final, Literal, overload
from typing_extensions import TypeAlias

from ._types import ErrorCorrect, MaskPattern
from .base import RSBlock as RSBlock

MODE_NUMBER: Final[int] = 1
MODE_ALPHA_NUM: Final[int] = 2
MODE_8BIT_BYTE: Final[int] = 4
MODE_KANJI: Final[int] = 8

_MODE: TypeAlias = Literal[1, 2, 4, 8]

MODE_SIZE_SMALL: Final[dict[_MODE, int]]
MODE_SIZE_MEDIUM: Final[dict[_MODE, int]]
MODE_SIZE_LARGE: Final[dict[_MODE, int]]

ALPHA_NUM: Final[bytes]
RE_ALPHA_NUM: Final[Pattern[bytes]]
NUMBER_LENGTH: Final[dict[int, int]]
PATTERN_POSITION_TABLE: Final[list[list[int]]]
G15: Final[int]
G18: Final[int]
G15_MASK: Final[int]
PAD0: Final[int]
PAD1: Final[int]
BIT_LIMIT_TABLE: Final[list[list[int]]]

# In the implementation, MODE_KANJI is not accepted in all places
_SupportedMode: TypeAlias = Literal[1, 2, 4]

def BCH_type_info(data: int) -> int: ...
def BCH_type_number(data: int) -> int: ...
def BCH_digit(data: int) -> int: ...
def pattern_position(version: int) -> list[int]: ...
def mask_func(pattern: MaskPattern) -> Callable[[int, int], bool]:
    """Return the mask function for the given mask pattern."""
    ...
def mode_sizes_for_version(version: int) -> dict[_MODE, int]: ...
def length_in_bits(mode: _MODE, version: int) -> int: ...
def check_version(version: int) -> None: ...
def lost_point(modules: list[list[bool | None]]) -> int: ...
def optimal_data_chunks(data: str | bytes, minimum: int = 4) -> Generator[QRData, None, None]:
    """
    An iterator returning QRData chunks optimized to the data content.

    :param minimum: The minimum number of bytes in a row to split as a chunk.
    """
    ...
def to_bytestring(data: str | bytes) -> bytes:
    """
    Convert data to a (utf-8 encoded) byte-string if it isn't a byte-string
    already.
    """
    ...
def optimal_mode(data: bytes) -> _SupportedMode:
    """Calculate the optimal mode for this chunk of data."""
    ...

class QRData:
    """
    Data held in a QR compatible format.

    Doesn't currently handle KANJI.
    """
    mode: _SupportedMode
    data: bytes
    @overload
    def __init__(self, data: bytes | str, mode: _SupportedMode | None = None, check_data: Literal[True] = True) -> None:
        """
        If ``mode`` isn't provided, the most compact QR data type possible is
        chosen.
        """
        ...
    @overload
    def __init__(self, data: bytes, mode: _SupportedMode | None = None, *, check_data: Literal[False]) -> None:
        """
        If ``mode`` isn't provided, the most compact QR data type possible is
        chosen.
        """
        ...
    @overload
    def __init__(self, data: bytes, mode: _SupportedMode | None, check_data: Literal[False]) -> None:
        """
        If ``mode`` isn't provided, the most compact QR data type possible is
        chosen.
        """
        ...
    def __len__(self) -> int: ...
    def write(self, buffer: BitBuffer) -> None: ...

class BitBuffer:
    buffer: list[int]
    length: int
    def __init__(self) -> None: ...
    def get(self, index: int) -> bool: ...
    def put(self, num: int, length: int) -> None: ...
    def __len__(self) -> int: ...
    def put_bit(self, bit: bool) -> None: ...

def create_bytes(buffer: BitBuffer, rs_blocks: list[RSBlock]) -> list[int]: ...
def create_data(version: int, error_correction: ErrorCorrect, data_list: list[QRData]) -> list[int]: ...
