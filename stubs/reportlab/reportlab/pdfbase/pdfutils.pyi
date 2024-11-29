from _typeshed import Incomplete
from typing import Final

__version__: Final[str]

def makeA85Image(filename, IMG: Incomplete | None = None, detectJpeg: bool = False): ...
def makeRawImage(filename, IMG: Incomplete | None = None, detectJpeg: bool = False): ...
def cacheImageFile(filename, returnInMemory: int = 0, IMG: Incomplete | None = None):
    """Processes image as if for encoding, saves to a file with .a85 extension."""
    ...
def preProcessImages(spec) -> None:
    r"""
    Preprocesses one or more image files.

    Accepts either a filespec ('C:\mydir\*.jpg') or a list
    of image filenames, crunches them all to save time.  Run this
    to save huge amounts of time when repeatedly building image
    documents.
    """
    ...
def cachedImageExists(filename):
    """
    Determines if a cached image already exists for a given file.

    Determines if a cached image exists which has the same name
    and equal or newer date to the given file.
    """
    ...
def readJPEGInfo(image):
    """Read width, height and number of components from open JPEG file."""
    ...

class _fusc:
    def __init__(self, k, n) -> None: ...
    def encrypt(self, s): ...
    def decrypt(self, s): ...
