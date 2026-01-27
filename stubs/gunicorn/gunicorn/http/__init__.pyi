import socket
from collections.abc import Iterable

from gunicorn.config import Config
from gunicorn.http.message import Message as Message, Request as Request
from gunicorn.http.parser import RequestParser as RequestParser
from gunicorn.uwsgi.parser import UWSGIParser

from .._types import _AddressType

def get_parser(
    cfg: Config, source: socket.socket | Iterable[bytes], source_addr: _AddressType
) -> UWSGIParser | RequestParser:
    """
    Get appropriate parser based on protocol config.

    Args:
        cfg: Gunicorn config object
        source: Socket or iterable source
        source_addr: Source address tuple or None

    Returns:
        Parser instance (RequestParser or UWSGIParser)
    """
    ...

__all__ = ["Message", "Request", "RequestParser", "get_parser"]
