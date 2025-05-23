"""
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
"""

from _typeshed import Incomplete
from collections.abc import Callable

from .base import Client, _TokenPlacement

class LegacyApplicationClient(Client):
    """
    A public client using the resource owner password and username directly.

    The resource owner password credentials grant type is suitable in
    cases where the resource owner has a trust relationship with the
    client, such as the device operating system or a highly privileged
    application.  The authorization server should take special care when
    enabling this grant type, and only allow it when other flows are not
    viable.

    The grant type is suitable for clients capable of obtaining the
    resource owner's credentials (username and password, typically using
    an interactive form).  It is also used to migrate existing clients
    using direct authentication schemes such as HTTP Basic or Digest
    authentication to OAuth by converting the stored credentials to an
    access token.

    The method through which the client obtains the resource owner
    credentials is beyond the scope of this specification.  The client
    MUST discard the credentials once an access token has been obtained.
    """
    grant_type: str
    def __init__(
        self,
        client_id: str,
        *,
        default_token_placement: _TokenPlacement = "auth_header",
        token_type: str = "Bearer",
        access_token: str | None = None,
        refresh_token: str | None = None,
        mac_key: str | bytes | bytearray | None = None,
        mac_algorithm: str | None = None,
        token: dict[str, Incomplete] | None = None,
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        state: str | None = None,
        redirect_url: str | None = None,
        state_generator: Callable[[], str] = ...,
        code_verifier: str | None = None,
        code_challenge: str | None = None,
        code_challenge_method: str | None = None,
        **kwargs,
    ) -> None: ...
    def prepare_request_body(
        self,
        username: str,
        password: str,
        body: str = "",
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        include_client_id: bool = False,
        *,
        code_verifier: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        **kwargs,
    ) -> str:
        """
        Add the resource owner password and username to the request body.

        The client makes a request to the token endpoint by adding the
        following parameters using the "application/x-www-form-urlencoded"
        format per `Appendix B`_ in the HTTP request entity-body:

        :param username:    The resource owner username.
        :param password:    The resource owner password.
        :param body: Existing request body (URL encoded string) to embed parameters
                     into. This may contain extra parameters. Default ''.
        :param scope:   The scope of the access request as described by
                        `Section 3.3`_.
        :param include_client_id: `True` to send the `client_id` in the
                                  body of the upstream request. This is required
                                  if the client is not authenticating with the
                                  authorization server as described in
                                  `Section 3.2.1`_. False otherwise (default).
        :type include_client_id: Boolean
        :param kwargs:  Extra credentials to include in the token request.

        If the client type is confidential or the client was issued client
        credentials (or assigned other authentication requirements), the
        client MUST authenticate with the authorization server as described
        in `Section 3.2.1`_.

        The prepared body will include all provided credentials as well as
        the ``grant_type`` parameter set to ``password``::

            >>> from oauthlib.oauth2 import LegacyApplicationClient
            >>> client = LegacyApplicationClient('your_id')
            >>> client.prepare_request_body(username='foo', password='bar', scope=['hello', 'world'])
            'grant_type=password&username=foo&scope=hello+world&password=bar'

        .. _`Appendix B`: https://tools.ietf.org/html/rfc6749#appendix-B
        .. _`Section 3.3`: https://tools.ietf.org/html/rfc6749#section-3.3
        .. _`Section 3.2.1`: https://tools.ietf.org/html/rfc6749#section-3.2.1
        """
        ...
