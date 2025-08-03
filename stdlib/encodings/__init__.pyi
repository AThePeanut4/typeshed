import sys
from codecs import CodecInfo

class CodecRegistryError(LookupError, SystemError): ...

def normalize_encoding(encoding: str | bytes) -> str:
    """
    Normalize an encoding name.

    Normalization works as follows: all non-alphanumeric
    characters except the dot used for Python package names are
    collapsed and replaced with a single underscore, e.g. '  -;#'
    becomes '_'. Leading and trailing underscores are removed.

    Note that encoding names should be ASCII only.
    """
    ...
def search_function(encoding: str) -> CodecInfo | None: ...

if sys.version_info >= (3, 14) and sys.platform == "win32":
    def win32_code_page_search_function(encoding: str) -> CodecInfo | None: ...

# Needed for submodules
def __getattr__(name: str): ...  # incomplete module
