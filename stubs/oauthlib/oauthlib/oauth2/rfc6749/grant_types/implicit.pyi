"""
oauthlib.oauth2.rfc6749.grant_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from _typeshed import Incomplete
from logging import Logger

from oauthlib.common import Request

from ..tokens import TokenBase
from .base import GrantTypeBase

log: Logger

class ImplicitGrant(GrantTypeBase):
    """
    `Implicit Grant`_

     The implicit grant type is used to obtain access tokens (it does not
     support the issuance of refresh tokens) and is optimized for public
     clients known to operate a particular redirection URI.  These clients
     are typically implemented in a browser using a scripting language
     such as JavaScript.

     Unlike the authorization code grant type, in which the client makes
     separate requests for authorization and for an access token, the
     client receives the access token as the result of the authorization
     request.

     The implicit grant type does not include client authentication, and
     relies on the presence of the resource owner and the registration of
     the redirection URI.  Because the access token is encoded into the
     redirection URI, it may be exposed to the resource owner and other
     applications residing on the same device::

         +----------+
         | Resource |
         |  Owner   |
         |          |
         +----------+
              ^
              |
             (B)
         +----|-----+          Client Identifier     +---------------+
         |         -+----(A)-- & Redirection URI --->|               |
         |  User-   |                                | Authorization |
         |  Agent  -|----(B)-- User authenticates -->|     Server    |
         |          |                                |               |
         |          |<---(C)--- Redirection URI ----<|               |
         |          |          with Access Token     +---------------+
         |          |            in Fragment
         |          |                                +---------------+
         |          |----(D)--- Redirection URI ---->|   Web-Hosted  |
         |          |          without Fragment      |     Client    |
         |          |                                |    Resource   |
         |     (F)  |<---(E)------- Script ---------<|               |
         |          |                                +---------------+
         +-|--------+
           |    |
          (A)  (G) Access Token
           |    |
           ^    v
         +---------+
         |         |
         |  Client |
         |         |
         +---------+

    Note: The lines illustrating steps (A) and (B) are broken into two
    parts as they pass through the user-agent.

    Figure 4: Implicit Grant Flow

    The flow illustrated in Figure 4 includes the following steps:

    (A)  The client initiates the flow by directing the resource owner's
         user-agent to the authorization endpoint.  The client includes
         its client identifier, requested scope, local state, and a
         redirection URI to which the authorization server will send the
         user-agent back once access is granted (or denied).

    (B)  The authorization server authenticates the resource owner (via
         the user-agent) and establishes whether the resource owner
         grants or denies the client's access request.

    (C)  Assuming the resource owner grants access, the authorization
         server redirects the user-agent back to the client using the
         redirection URI provided earlier.  The redirection URI includes
         the access token in the URI fragment.

    (D)  The user-agent follows the redirection instructions by making a
         request to the web-hosted client resource (which does not
         include the fragment per [RFC2616]).  The user-agent retains the
         fragment information locally.

    (E)  The web-hosted client resource returns a web page (typically an
         HTML document with an embedded script) capable of accessing the
         full redirection URI including the fragment retained by the
         user-agent, and extracting the access token (and other
         parameters) contained in the fragment.

    (F)  The user-agent executes the script provided by the web-hosted
         client resource locally, which extracts the access token.

    (G)  The user-agent passes the access token to the client.

     See `Section 10.3`_ and `Section 10.16`_ for important security considerations
     when using the implicit grant.

     .. _`Implicit Grant`: https://tools.ietf.org/html/rfc6749#section-4.2
     .. _`Section 10.3`: https://tools.ietf.org/html/rfc6749#section-10.3
     .. _`Section 10.16`: https://tools.ietf.org/html/rfc6749#section-10.16
 
    """
    response_types: list[str]
    grant_allows_refresh_token: bool
    def create_authorization_response(
        self, request: Request, token_handler: TokenBase
    ) -> tuple[dict[str, str], str | None, int]:
        """
        Create an authorization response.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param token_handler: A token handler instance, for example of type
                              oauthlib.oauth2.BearerToken.

        The client constructs the request URI by adding the following
        parameters to the query component of the authorization endpoint URI
        using the "application/x-www-form-urlencoded" format, per `Appendix B`_:

        response_type
                REQUIRED.  Value MUST be set to "token" for standard OAuth2 implicit flow
                           or "id_token token" or just "id_token" for OIDC implicit flow

        client_id
                REQUIRED.  The client identifier as described in `Section 2.2`_.

        redirect_uri
                OPTIONAL.  As described in `Section 3.1.2`_.

        scope
                OPTIONAL.  The scope of the access request as described by
                `Section 3.3`_.

        state
                RECOMMENDED.  An opaque value used by the client to maintain
                state between the request and callback.  The authorization
                server includes this value when redirecting the user-agent back
                to the client.  The parameter SHOULD be used for preventing
                cross-site request forgery as described in `Section 10.12`_.

        The authorization server validates the request to ensure that all
        required parameters are present and valid.  The authorization server
        MUST verify that the redirection URI to which it will redirect the
        access token matches a redirection URI registered by the client as
        described in `Section 3.1.2`_.

        .. _`Section 2.2`: https://tools.ietf.org/html/rfc6749#section-2.2
        .. _`Section 3.1.2`: https://tools.ietf.org/html/rfc6749#section-3.1.2
        .. _`Section 3.3`: https://tools.ietf.org/html/rfc6749#section-3.3
        .. _`Section 10.12`: https://tools.ietf.org/html/rfc6749#section-10.12
        .. _`Appendix B`: https://tools.ietf.org/html/rfc6749#appendix-B
        """
        ...
    def create_token_response(self, request: Request, token_handler: TokenBase) -> tuple[dict[str, str], str | None, int]:
        """
        Return token or error embedded in the URI fragment.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param token_handler: A token handler instance, for example of type
                              oauthlib.oauth2.BearerToken.

        If the resource owner grants the access request, the authorization
        server issues an access token and delivers it to the client by adding
        the following parameters to the fragment component of the redirection
        URI using the "application/x-www-form-urlencoded" format, per
        `Appendix B`_:

        access_token
                REQUIRED.  The access token issued by the authorization server.

        token_type
                REQUIRED.  The type of the token issued as described in
                `Section 7.1`_.  Value is case insensitive.

        expires_in
                RECOMMENDED.  The lifetime in seconds of the access token.  For
                example, the value "3600" denotes that the access token will
                expire in one hour from the time the response was generated.
                If omitted, the authorization server SHOULD provide the
                expiration time via other means or document the default value.

        scope
                OPTIONAL, if identical to the scope requested by the client;
                otherwise, REQUIRED.  The scope of the access token as
                described by `Section 3.3`_.

        state
                REQUIRED if the "state" parameter was present in the client
                authorization request.  The exact value received from the
                client.

        The authorization server MUST NOT issue a refresh token.

        .. _`Appendix B`: https://tools.ietf.org/html/rfc6749#appendix-B
        .. _`Section 3.3`: https://tools.ietf.org/html/rfc6749#section-3.3
        .. _`Section 7.1`: https://tools.ietf.org/html/rfc6749#section-7.1
        """
        ...
    def validate_authorization_request(self, request: Request) -> tuple[Incomplete, dict[str, Incomplete]]:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
        ...
    def validate_token_request(self, request: Request) -> tuple[Incomplete, dict[str, Incomplete]]:
        """
        Check the token request for normal and fatal errors.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request

        This method is very similar to validate_authorization_request in
        the AuthorizationCodeGrant but differ in a few subtle areas.

        A normal error could be a missing response_type parameter or the client
        attempting to access scope it is not allowed to ask authorization for.
        Normal errors can safely be included in the redirection URI and
        sent back to the client.

        Fatal errors occur when the client_id or redirect_uri is invalid or
        missing. These must be caught by the provider and handled, how this
        is done is outside of the scope of OAuthLib but showing an error
        page describing the issue is a good idea.
        """
        ...
