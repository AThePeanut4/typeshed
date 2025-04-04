from _typeshed import ReadableBuffer, Unused
from typing import IO, Any, BinaryIO, Final, Literal, NamedTuple, NoReturn, overload
from typing_extensions import Self, TypeAlias, deprecated

__all__ = ["open", "Error", "Wave_read", "Wave_write"]

_File: TypeAlias = str | IO[bytes]

class Error(Exception): ...

WAVE_FORMAT_PCM: Final = 1

class _wave_params(NamedTuple):
    """_wave_params(nchannels, sampwidth, framerate, nframes, comptype, compname)"""
    nchannels: int
    sampwidth: int
    framerate: int
    nframes: int
    comptype: str
    compname: str

class Wave_read:
    """
    Variables used in this class:

    These variables are available to the user though appropriate
    methods of this class:
    _file -- the open file with methods read(), close(), and seek()
              set through the __init__() method
    _nchannels -- the number of audio channels
              available through the getnchannels() method
    _nframes -- the number of audio frames
              available through the getnframes() method
    _sampwidth -- the number of bytes per audio sample
              available through the getsampwidth() method
    _framerate -- the sampling frequency
              available through the getframerate() method
    _comptype -- the AIFF-C compression type ('NONE' if AIFF)
              available through the getcomptype() method
    _compname -- the human-readable AIFF-C compression type
              available through the getcomptype() method
    _soundpos -- the position in the audio stream
              available through the tell() method, set through the
              setpos() method

    These variables are used internally only:
    _fmt_chunk_read -- 1 iff the FMT chunk has been read
    _data_seek_needed -- 1 iff positioned correctly in audio
              file for readframes()
    _data_chunk -- instantiation of a chunk class for the DATA chunk
    _framesize -- size of one frame in the file
    """
    def __init__(self, f: _File) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def __del__(self) -> None: ...
    def getfp(self) -> BinaryIO | None: ...
    def rewind(self) -> None: ...
    def close(self) -> None: ...
    def tell(self) -> int: ...
    def getnchannels(self) -> int: ...
    def getnframes(self) -> int: ...
    def getsampwidth(self) -> int: ...
    def getframerate(self) -> int: ...
    def getcomptype(self) -> str: ...
    def getcompname(self) -> str: ...
    def getparams(self) -> _wave_params: ...
    @deprecated("Deprecated in Python 3.13; removal scheduled for Python 3.15")
    def getmarkers(self) -> None: ...
    @deprecated("Deprecated in Python 3.13; removal scheduled for Python 3.15")
    def getmark(self, id: Any) -> NoReturn: ...
    def setpos(self, pos: int) -> None: ...
    def readframes(self, nframes: int) -> bytes: ...

class Wave_write:
    """
    Variables used in this class:

    These variables are user settable through appropriate methods
    of this class:
    _file -- the open file with methods write(), close(), tell(), seek()
              set through the __init__() method
    _comptype -- the AIFF-C compression type ('NONE' in AIFF)
              set through the setcomptype() or setparams() method
    _compname -- the human-readable AIFF-C compression type
              set through the setcomptype() or setparams() method
    _nchannels -- the number of audio channels
              set through the setnchannels() or setparams() method
    _sampwidth -- the number of bytes per audio sample
              set through the setsampwidth() or setparams() method
    _framerate -- the sampling frequency
              set through the setframerate() or setparams() method
    _nframes -- the number of audio frames written to the header
              set through the setnframes() or setparams() method

    These variables are used internally only:
    _datalength -- the size of the audio samples written to the header
    _nframeswritten -- the number of frames actually written
    _datawritten -- the size of the audio samples actually written
    """
    def __init__(self, f: _File) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def __del__(self) -> None: ...
    def setnchannels(self, nchannels: int) -> None: ...
    def getnchannels(self) -> int: ...
    def setsampwidth(self, sampwidth: int) -> None: ...
    def getsampwidth(self) -> int: ...
    def setframerate(self, framerate: float) -> None: ...
    def getframerate(self) -> int: ...
    def setnframes(self, nframes: int) -> None: ...
    def getnframes(self) -> int: ...
    def setcomptype(self, comptype: str, compname: str) -> None: ...
    def getcomptype(self) -> str: ...
    def getcompname(self) -> str: ...
    def setparams(self, params: _wave_params | tuple[int, int, int, int, str, str]) -> None: ...
    def getparams(self) -> _wave_params: ...
    @deprecated("Deprecated in Python 3.13; removal scheduled for Python 3.15")
    def setmark(self, id: Any, pos: Any, name: Any) -> NoReturn: ...
    @deprecated("Deprecated in Python 3.13; removal scheduled for Python 3.15")
    def getmark(self, id: Any) -> NoReturn: ...
    @deprecated("Deprecated in Python 3.13; removal scheduled for Python 3.15")
    def getmarkers(self) -> None: ...
    def tell(self) -> int: ...
    def writeframesraw(self, data: ReadableBuffer) -> None: ...
    def writeframes(self, data: ReadableBuffer) -> None: ...
    def close(self) -> None: ...

@overload
def open(f: _File, mode: Literal["r", "rb"]) -> Wave_read: ...
@overload
def open(f: _File, mode: Literal["w", "wb"]) -> Wave_write: ...
@overload
def open(f: _File, mode: str | None = None) -> Any: ...
