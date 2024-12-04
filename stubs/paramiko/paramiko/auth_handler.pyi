"""`.AuthHandler`"""

from collections.abc import Callable
from threading import Event
from typing_extensions import TypeAlias

from paramiko.pkey import PKey
from paramiko.ssh_gss import _SSH_GSSAuth
from paramiko.transport import Transport

_InteractiveCallback: TypeAlias = Callable[[str, str, list[tuple[str, bool]]], list[str]]

class AuthHandler:
    """Internal class to handle the mechanics of authentication."""
    transport: Transport
    username: str | None
    authenticated: bool
    auth_event: Event | None
    auth_method: str
    banner: str | None
    password: str | None
    private_key: PKey | None
    interactive_handler: _InteractiveCallback | None
    submethods: str | None
    auth_username: str | None
    auth_fail_count: int
    gss_host: str | None
    gss_deleg_creds: bool
    def __init__(self, transport: Transport) -> None: ...
    def is_authenticated(self) -> bool: ...
    def get_username(self) -> str | None: ...
    def auth_none(self, username: str, event: Event) -> None: ...
    def auth_publickey(self, username: str, key: PKey, event: Event) -> None: ...
    def auth_password(self, username: str, password: str, event: Event) -> None: ...
    def auth_interactive(self, username: str, handler: _InteractiveCallback, event: Event, submethods: str = "") -> None:
        """response_list = handler(title, instructions, prompt_list)"""
        ...
    def auth_gssapi_with_mic(self, username: str, gss_host: str, gss_deleg_creds: bool, event: Event) -> None: ...
    def auth_gssapi_keyex(self, username: str, event: Event) -> None: ...
    def abort(self) -> None: ...
    def wait_for_response(self, event: Event) -> list[str]: ...

class GssapiWithMicAuthHandler:
    """
    A specialized Auth handler for gssapi-with-mic

    During the GSSAPI token exchange we need a modified dispatch table,
    because the packet type numbers are not unique.
    """
    method: str
    sshgss: _SSH_GSSAuth
    def __init__(self, delegate: AuthHandler, sshgss: _SSH_GSSAuth) -> None: ...
    def abort(self) -> None: ...
    @property
    def transport(self) -> Transport: ...
    @property
    def auth_username(self) -> str: ...
    @property
    def gss_host(self) -> str: ...
