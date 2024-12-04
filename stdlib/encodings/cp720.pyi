"""
Python Character Mapping Codec cp720 generated on Windows:
Vista 6.0.6002 SP2 Multiprocessor Free with the command:
  python Tools/unicode/genwincodec.py 720
"""

import codecs
from _codecs import _EncodingMap
from _typeshed import ReadableBuffer

class Codec(codecs.Codec):
    def encode(self, input: str, errors: str = "strict") -> tuple[bytes, int]: ...
    def decode(self, input: bytes, errors: str = "strict") -> tuple[str, int]: ...

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input: str, final: bool = False) -> bytes: ...

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input: ReadableBuffer, final: bool = False) -> str: ...

class StreamWriter(Codec, codecs.StreamWriter): ...
class StreamReader(Codec, codecs.StreamReader): ...

def getregentry() -> codecs.CodecInfo: ...

decoding_table: str
encoding_table: _EncodingMap
