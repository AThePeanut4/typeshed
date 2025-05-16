from collections.abc import Mapping
from typing import Any, SupportsInt
from typing_extensions import deprecated

from jwcrypto.common import JWException, JWKeyNotFound
from jwcrypto.jwk import JWK, JWKSet

JWTClaimsRegistry: Mapping[str, str]
JWT_expect_type: bool

class JWTExpired(JWException):
    """
    JSON Web Token is expired.

    This exception is raised when a token is expired according to its claims.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWTNotYetValid(JWException):
    """
    JSON Web Token is not yet valid.

    This exception is raised when a token is not valid yet according to its
    claims.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWTMissingClaim(JWException):
    """
    JSON Web Token claim is invalid.

    This exception is raised when a claim does not match the expected value.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWTInvalidClaimValue(JWException):
    """
    JSON Web Token claim is invalid.

    This exception is raised when a claim does not match the expected value.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWTInvalidClaimFormat(JWException):
    """
    JSON Web Token claim format is invalid.

    This exception is raised when a claim is not in a valid format.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

@deprecated("")
class JWTMissingKeyID(JWException):
    """
    JSON Web Token is missing key id.

    This exception is raised when trying to decode a JWT with a key set
    that does not have a kid value in its header.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWTMissingKey(JWKeyNotFound):
    """
    JSON Web Token is using a key not in the key set.

    This exception is raised if the key that was used is not available
    in the passed key set.
    """
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWT:
    """
    JSON Web token object

    This object represent a generic token.
    """
    deserializelog: list[str] | None
    def __init__(
        self,
        header: dict[str, Any] | str | None = None,
        claims: dict[str, Any] | str | None = None,
        jwt=None,
        key: JWK | JWKSet | None = None,
        algs=None,
        default_claims=None,
        check_claims=None,
        expected_type=None,
    ) -> None: ...
    @property
    def header(self) -> str: ...
    @header.setter
    def header(self, h: dict[str, Any] | str) -> None: ...
    @property
    def claims(self) -> str: ...
    @claims.setter
    def claims(self, data: str) -> None: ...
    @property
    def token(self): ...
    @token.setter
    def token(self, t) -> None: ...
    @property
    def leeway(self) -> int: ...
    @leeway.setter
    def leeway(self, lwy: SupportsInt) -> None: ...
    @property
    def validity(self) -> int: ...
    @validity.setter
    def validity(self, v: SupportsInt) -> None: ...
    @property
    def expected_type(self): ...
    @expected_type.setter
    def expected_type(self, v) -> None: ...
    def norm_typ(self, val): ...
    def make_signed_token(self, key: JWK) -> None: ...
    def make_encrypted_token(self, key: JWK) -> None: ...
    def validate(self, key: JWK | JWKSet) -> None: ...
    def deserialize(self, jwt, key=None) -> None: ...
    def serialize(self, compact: bool = True) -> str: ...
    @classmethod
    def from_jose_token(cls, token):
        """
        Creates a JWT object from a serialized JWT token.

        :param token: A string with the json or compat representation
         of the token.

        :raises InvalidJWEData or InvalidJWSObject: if the raw object is an
         invalid JWT token.

        :return: A JWT token
        :rtype: JWT
        """
        ...
    def __eq__(self, other: object) -> bool: ...
