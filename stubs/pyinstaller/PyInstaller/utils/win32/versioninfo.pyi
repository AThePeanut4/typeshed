from _typeshed import SliceableBuffer
from collections.abc import Sequence
from typing import Literal, Protocol
from typing_extensions import TypeAlias

_FourIntSequence: TypeAlias = Sequence[int]
_TwoIntSequence: TypeAlias = Sequence[int]

class _Kid(Protocol):
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "", /) -> str: ...

# Used by other types referenced in https://pyinstaller.org/en/stable/spec-files.html#spec-file-operation
class VSVersionInfo:
    """
    WORD  wLength;        // length of the VS_VERSION_INFO structure
    WORD  wValueLength;   // length of the Value member
    WORD  wType;          // 1 means text, 0 means binary
    WCHAR szKey[];        // Contains the Unicode string "VS_VERSION_INFO".
    WORD  Padding1[];
    VS_FIXEDFILEINFO Value;
    WORD  Padding2[];
    WORD  Children[];     // zero or more StringFileInfo or VarFileInfo
                          // structures (or both) that are children of the
                          // current version structure.
    """
    ffi: FixedFileInfo | None
    kids: list[_Kid]
    def __init__(self, ffi: FixedFileInfo | None = None, kids: list[_Kid] | None = None) -> None: ...
    def fromRaw(self, data: SliceableBuffer) -> int: ...
    def toRaw(self) -> bytes: ...
    def __eq__(self, other: object) -> bool: ...
    def __str__(self, indent: str = "") -> str: ...

class FixedFileInfo:
    """
    DWORD dwSignature;        //Contains the value 0xFEEFO4BD
    DWORD dwStrucVersion;     // binary version number of this structure.
                              // The high-order word of this member contains
                              // the major version number, and the low-order
                              // word contains the minor version number.
    DWORD dwFileVersionMS;    // most significant 32 bits of the file's binary
                              // version number
    DWORD dwFileVersionLS;    //
    DWORD dwProductVersionMS; // most significant 32 bits of the binary version
                              // number of the product with which this file was
                              // distributed
    DWORD dwProductVersionLS; //
    DWORD dwFileFlagsMask;    // bitmask that specifies the valid bits in
                              // dwFileFlags. A bit is valid only if it was
                              // defined when the file was created.
    DWORD dwFileFlags;        // VS_FF_DEBUG, VS_FF_PATCHED etc.
    DWORD dwFileOS;           // VOS_NT, VOS_WINDOWS32 etc.
    DWORD dwFileType;         // VFT_APP etc.
    DWORD dwFileSubtype;      // 0 unless VFT_DRV or VFT_FONT or VFT_VXD
    DWORD dwFileDateMS;
    DWORD dwFileDateLS;
    """
    sig: Literal[0xFEEF04BD]
    strucVersion: Literal[0x10000]
    fileVersionMS: int
    fileVersionLS: int
    productVersionMS: int
    productVersionLS: int
    fileFlagsMask: int
    fileFlags: int
    fileOS: int
    fileType: int
    fileSubtype: int
    fileDateMS: int
    fileDateLS: int
    def __init__(
        self,
        filevers: _FourIntSequence = ...,
        prodvers: _FourIntSequence = ...,
        mask: int = 0x3F,
        flags: int = 0x0,
        OS: int = 0x40004,
        fileType: int = 0x1,
        subtype: int = 0x0,
        date: _TwoIntSequence = ...,
    ) -> None: ...
    def fromRaw(self, data: SliceableBuffer, i: int) -> int: ...
    def toRaw(self) -> bytes: ...
    def __eq__(self, other: object) -> bool: ...
    def __str__(self, indent: str = "") -> str: ...
