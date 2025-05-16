from _typeshed import Incomplete

from authlib.jose import JWTClaims

__all__ = ["IDToken", "CodeIDToken", "ImplicitIDToken", "HybridIDToken", "UserInfo", "get_claim_cls_by_response_type"]

class IDToken(JWTClaims):
    ESSENTIAL_CLAIMS: Incomplete
    def validate(self, now=None, leeway: int = 0) -> None: ...
    def validate_auth_time(self) -> None: ...
    def validate_nonce(self) -> None: ...
    def validate_acr(self): ...
    def validate_amr(self) -> None: ...
    def validate_azp(self) -> None: ...
    def validate_at_hash(self) -> None: ...

class CodeIDToken(IDToken):
    RESPONSE_TYPES: Incomplete

class ImplicitIDToken(IDToken):
    RESPONSE_TYPES: Incomplete
    ESSENTIAL_CLAIMS: Incomplete
    def validate_at_hash(self) -> None:
        """
        If the ID Token is issued from the Authorization Endpoint with an
        access_token value, which is the case for the response_type value
        id_token token, this is REQUIRED; it MAY NOT be used when no Access
        Token is issued, which is the case for the response_type value
        id_token.
        """
        ...

class HybridIDToken(ImplicitIDToken):
    RESPONSE_TYPES: Incomplete
    def validate(self, now=None, leeway: int = 0) -> None: ...
    def validate_c_hash(self) -> None: ...

class UserInfo(dict[str, object]):
    """
    The standard claims of a UserInfo object. Defined per `Section 5.1`_.

    .. _`Section 5.1`: http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims
    """
    REGISTERED_CLAIMS: Incomplete
    def __getattr__(self, key): ...

def get_claim_cls_by_response_type(response_type): ...
