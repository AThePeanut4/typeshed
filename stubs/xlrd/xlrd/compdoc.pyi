"""
Implements the minimal functionality required
to extract a "Workbook" or "Book" stream (as one big string)
from an OLE2 Compound Document file.
"""

import sys
from _typeshed import SupportsWrite
from typing import Final

from .timemachine import *

SIGNATURE: Final[bytes]
EOCSID: Final[int]
FREESID: Final[int]
SATSID: Final[int]
MSATSID: Final[int]
EVILSID: Final[int]

class CompDocError(Exception): ...

class DirNode:
    DID: int
    name: str
    etype: int
    colour: int
    left_DID: int
    right_DID: int
    root_DID: int
    first_SID: int
    tot_size: int
    children: list[int]
    parent: int
    tsinfo: tuple[int, int, int, int]
    logfile: SupportsWrite[str]
    def __init__(self, DID: int, dent: bytes, DEBUG: int = 0, logfile: SupportsWrite[str] = sys.stdout) -> None: ...
    def dump(self, DEBUG: int = 1) -> None: ...

class CompDoc:
    """
    Compound document handler.

    :param mem:
      The raw contents of the file, as a string, or as an :class:`mmap.mmap`
      object. The only operation it needs to support is slicing.
    """
    logfile: SupportsWrite[str]
    ignore_workbook_corruption: bool
    DEBUG: int
    mem: bytes
    sec_size: int
    short_sec_size: int
    mem_data_secs: int
    mem_data_len: int
    seen: list[int]
    SAT: list[int]
    dirlist: list[DirNode]
    SSCS: str
    SSAT: list[int]
    def __init__(
        self, mem: bytes, logfile: SupportsWrite[str] = sys.stdout, DEBUG: int = 0, ignore_workbook_corruption: bool = False
    ) -> None: ...
    def get_named_stream(self, qname: str) -> bytes | None:
        """
        Interrogate the compound document's directory; return the stream as a
        string if found, otherwise return ``None``.

        :param qname:
          Name of the desired stream e.g. ``'Workbook'``.
          Should be in Unicode or convertible thereto.
        """
        ...
    def locate_named_stream(self, qname: str) -> tuple[bytes | None, int, int]:
        """
        Interrogate the compound document's directory.

        If the named stream is not found, ``(None, 0, 0)`` will be returned.

        If the named stream is found and is contiguous within the original
        byte sequence (``mem``) used when the document was opened,
        then ``(mem, offset_to_start_of_stream, length_of_stream)`` is returned.

        Otherwise a new string is built from the fragments and
        ``(new_string, 0, length_of_stream)`` is returned.

        :param qname:
          Name of the desired stream e.g. ``'Workbook'``.
          Should be in Unicode or convertible thereto.
        """
        ...

def x_dump_line(alist: list[int], stride: int, f: SupportsWrite[str], dpos: int, equal: int = 0) -> None: ...
def dump_list(alist: list[int], stride: int, f: SupportsWrite[str] = sys.stdout) -> None: ...
