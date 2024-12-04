from typing_extensions import Self

from .enums import CredentialType

class Username:
    """
    Username credentials

    This is an object suitable for passing to a remote's credentials
    callback and for returning from said callback.
    """
    def __init__(self, username: str) -> None: ...
    @property
    def credential_type(self) -> CredentialType: ...
    @property
    def credential_tuple(self) -> tuple[str]: ...
    def __call__(self, _url: str, _username: str | None, _allowed: CredentialType) -> Self: ...

class UserPass:
    """
    Username/Password credentials

    This is an object suitable for passing to a remote's credentials
    callback and for returning from said callback.
    """
    def __init__(self, username: str, password: str) -> None: ...
    @property
    def credential_type(self) -> CredentialType: ...
    @property
    def credential_tuple(self) -> tuple[str, str]: ...
    def __call__(self, _url: str, _username: str | None, _allowed: CredentialType) -> Self: ...

class Keypair:
    """
    SSH key pair credentials.

    This is an object suitable for passing to a remote's credentials
    callback and for returning from said callback.

    Parameters:

    username : str
        The username being used to authenticate with the remote server.

    pubkey : str
        The path to the user's public key file.

    privkey : str
        The path to the user's private key file.

    passphrase : str
        The password used to decrypt the private key file, or empty string if
        no passphrase is required.
    """
    def __init__(self, username: str, pubkey: str, privkey: str, passphrase: str) -> None: ...
    @property
    def credential_type(self) -> CredentialType: ...
    @property
    def credential_tuple(self) -> tuple[str, str, str, str]: ...
    def __call__(self, _url: str, _username: str | None, _allowed: CredentialType) -> Self: ...

class KeypairFromAgent(Keypair):
    def __init__(self, username: str) -> None: ...

class KeypairFromMemory(Keypair):
    @property
    def credential_type(self) -> CredentialType: ...
