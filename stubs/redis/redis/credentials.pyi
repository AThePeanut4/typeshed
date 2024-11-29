from abc import abstractmethod

class CredentialProvider:
    """Credentials Provider."""
    @abstractmethod
    def get_credentials(self) -> tuple[str] | tuple[str, str]: ...

class UsernamePasswordCredentialProvider(CredentialProvider):
    """
    Simple implementation of CredentialProvider that just wraps static
    username and password.
    """
    username: str
    password: str
    def __init__(self, username: str | None = None, password: str | None = None) -> None: ...
    def get_credentials(self) -> tuple[str] | tuple[str, str]: ...
