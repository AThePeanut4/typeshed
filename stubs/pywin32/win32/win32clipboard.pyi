"""A module which supports the Windows Clipboard API."""

from typing import Any, Final

from win32.lib.pywintypes import error as error

def ChangeClipboardChain(hWndRemove: int, hWndNewNext: int, /): ...
def CloseClipboard(): ...
def CountClipboardFormats(): ...
def EmptyClipboard(): ...
def EnumClipboardFormats(_format: int = ..., /): ...
def GetClipboardData(_format, /) -> Any: ...  # str or bytes depending on the dib format
def GetClipboardDataHandle(_format, /): ...
def GetClipboardFormatName(_format, /) -> str: ...
def GetClipboardOwner(): ...
def GetClipboardSequenceNumber(): ...
def GetClipboardViewer(): ...
def GetGlobalMemory(hglobal: int, /) -> str: ...
def GetOpenClipboardWindow(): ...
def GetPriorityClipboardFormat(formats, /): ...
def IsClipboardFormatAvailable(format: int, /) -> int: ...
def OpenClipboard(hWnd: int | None = ..., /): ...
def RegisterClipboardFormat(name: str, /): ...
def SetClipboardData(_format, hMem, /): ...
def SetClipboardText(text, _format, /): ...
def SetClipboardViewer(hWndNewViewer: int, /) -> int: ...

CF_BITMAP: Final[int]
CF_DIB: Final[int]
CF_DIBV5: Final[int]
CF_DIF: Final[int]
CF_DSPBITMAP: Final[int]
CF_DSPENHMETAFILE: Final[int]
CF_DSPMETAFILEPICT: Final[int]
CF_DSPTEXT: Final[int]
CF_ENHMETAFILE: Final[int]
CF_HDROP: Final[int]
CF_LOCALE: Final[int]
CF_MAX: Final[int]
CF_METAFILEPICT: Final[int]
CF_OEMTEXT: Final[int]
CF_OWNERDISPLAY: Final[int]
CF_PALETTE: Final[int]
CF_PENDATA: Final[int]
CF_RIFF: Final[int]
CF_SYLK: Final[int]
CF_TEXT: Final[int]
CF_TIFF: Final[int]
CF_UNICODETEXT: Final[int]
CF_WAVE: Final[int]
UNICODE: bool
