from collections.abc import Iterator
from typing import NamedTuple, SupportsIndex

from ._types import ErrorCorrect

EXP_TABLE: list[int]
LOG_TABLE: list[int]
RS_BLOCK_OFFSET: dict[ErrorCorrect, int]
RS_BLOCK_TABLE: tuple[tuple[int, int, int] | tuple[int, int, int, int, int, int], ...]

def glog(n: int) -> int: ...
def gexp(n: int) -> int: ...

class Polynomial:
    num: list[int]
    def __init__(self, num: list[int], shift: int) -> None: ...
    def __getitem__(self, index: SupportsIndex) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
    def __mul__(self, other: Polynomial) -> Polynomial: ...
    def __mod__(self, other: Polynomial) -> Polynomial: ...

class RSBlock(NamedTuple):
    """RSBlock(total_count, data_count)"""
    total_count: int
    data_count: int

def rs_blocks(version: int, error_correction: ErrorCorrect) -> list[RSBlock]: ...
