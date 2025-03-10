"""
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
"""

from typing import Any

log: Any

class BaseEndpoint:
    def __init__(self) -> None: ...
    @property
    def valid_request_methods(self): ...
    @valid_request_methods.setter
    def valid_request_methods(self, valid_request_methods) -> None: ...
    @property
    def available(self): ...
    @available.setter
    def available(self, available) -> None: ...
    @property
    def catch_errors(self): ...
    @catch_errors.setter
    def catch_errors(self, catch_errors) -> None: ...

def catch_errors_and_unavailability(f): ...
