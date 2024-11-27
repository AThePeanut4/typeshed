"""
oauthlib.openid.connect.core.grant_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from _typeshed import Incomplete
from typing import Any

from .base import GrantTypeBase as GrantTypeBase

log: Any

class AuthorizationCodeGrant(GrantTypeBase):
    proxy_target: Any
    def __init__(self, request_validator: Incomplete | None = None, **kwargs) -> None: ...
    def add_id_token(self, token, token_handler, request):
        """
        Construct an initial version of id_token, and let the
        request_validator sign or encrypt it.

        The authorization_code version of this method is used to
        retrieve the nonce accordingly to the code storage.
        """
        ...
