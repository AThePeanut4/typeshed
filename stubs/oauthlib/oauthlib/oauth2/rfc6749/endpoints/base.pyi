"""
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
"""

from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from logging import Logger

log: Logger

class BaseEndpoint:
    def __init__(self) -> None: ...
    @property
    def valid_request_methods(self) -> Sequence[str] | None: ...
    @valid_request_methods.setter
    def valid_request_methods(self, valid_request_methods: Sequence[str] | None) -> None: ...
    @property
    def available(self) -> bool: ...
    @available.setter
    def available(self, available: bool) -> None: ...
    @property
    def catch_errors(self) -> bool: ...
    @catch_errors.setter
    def catch_errors(self, catch_errors: bool) -> None: ...

def catch_errors_and_unavailability(
    f: Callable[..., tuple[dict[str, Incomplete], str, int]],
) -> Callable[..., tuple[dict[str, Incomplete], str, int]]: ...
