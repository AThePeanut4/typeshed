"""
oauthlib.openid.connect.core.grant_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from _typeshed import Incomplete
from typing import Any

from .base import GrantTypeBase as GrantTypeBase

log: Any

class ImplicitGrant(GrantTypeBase):
    proxy_target: Any
    def __init__(self, request_validator: Incomplete | None = None, **kwargs) -> None: ...
    def add_id_token(self, token, token_handler, request): ...  # type: ignore[override]
    def openid_authorization_validator(self, request):
        """
        Additional validation when following the implicit flow.
        
        """
        ...
