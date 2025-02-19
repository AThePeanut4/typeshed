def fp_str(*a): ...
def unicode2T1(utext, fonts): ...
def instanceStringWidthT1(self, text, size, encoding: str = "utf8"): ...
def instanceStringWidthTTF(self, text, size, encoding: str = "utf8"): ...
def hex32(i): ...
def add32(x, y):
    """Calculate (x + y) modulo 2**32"""
    ...
def calcChecksum(data):
    """Calculates TTF-style checksums"""
    ...
def escapePDF(s): ...
def asciiBase85Encode(input):
    """
    Encodes input using ASCII-Base85 coding.

    This is a compact encoding used for binary data within
    a PDF file.  Four bytes of binary data become five bytes of
    ASCII.  This is the default method used for encoding images.
    """
    ...
def asciiBase85Decode(input):
    """
    Decodes input using ASCII-Base85 coding.

    This is not normally used - Acrobat Reader decodes for you
    - but a round trip is essential for testing.
    """
    ...
def sameFrag(f, g):
    """returns 1 if two ParaFrags map out the same"""
    ...
