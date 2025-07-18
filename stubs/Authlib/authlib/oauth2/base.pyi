from _typeshed import Incomplete

from authlib.common.errors import AuthlibHTTPError

def invalid_error_characters(text: str) -> list[str]:
    """
    Check whether the string only contains characters from the restricted ASCII set defined in RFC6749 for errors.

    https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1
    """
    ...

class OAuth2Error(AuthlibHTTPError):
    state: Incomplete
    redirect_uri: Incomplete
    redirect_fragment: Incomplete
    def __init__(
        self,
        description=None,
        uri=None,
        status_code=None,
        state=None,
        redirect_uri=None,
        redirect_fragment: bool = False,
        error=None,
    ) -> None: ...
    def get_body(self):
        """Get a list of body."""
        ...
    def __call__(self, uri=None): ...
