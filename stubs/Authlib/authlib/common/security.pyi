from typing import Final

UNICODE_ASCII_CHARACTER_SET: Final[str]

def generate_token(length: int = 30, chars: str = ...) -> str: ...
def is_secure_transport(uri: str) -> bool:
    """Check if the uri is over ssl."""
    ...
