"""
oauthlib.oauth2.rfc6749.grant_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from _typeshed import Incomplete
from typing import Any

from .base import GrantTypeBase as GrantTypeBase

log: Any

class RefreshTokenGrant(GrantTypeBase):
    """
    `Refresh token grant`_

    .. _`Refresh token grant`: https://tools.ietf.org/html/rfc6749#section-6
    """
    def __init__(self, request_validator: Incomplete | None = None, issue_new_refresh_tokens: bool = True, **kwargs) -> None: ...
    def create_token_response(self, request, token_handler):
        """
        Create a new access token from a refresh_token.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param token_handler: A token handler instance, for example of type
                              oauthlib.oauth2.BearerToken.

        If valid and authorized, the authorization server issues an access
        token as described in `Section 5.1`_. If the request failed
        verification or is invalid, the authorization server returns an error
        response as described in `Section 5.2`_.

        The authorization server MAY issue a new refresh token, in which case
        the client MUST discard the old refresh token and replace it with the
        new refresh token. The authorization server MAY revoke the old
        refresh token after issuing a new refresh token to the client. If a
        new refresh token is issued, the refresh token scope MUST be
        identical to that of the refresh token included by the client in the
        request.

        .. _`Section 5.1`: https://tools.ietf.org/html/rfc6749#section-5.1
        .. _`Section 5.2`: https://tools.ietf.org/html/rfc6749#section-5.2
        """
        ...
    def validate_token_request(self, request) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
        ...
