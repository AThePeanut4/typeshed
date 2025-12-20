from authlib.oauth2.rfc6749 import TokenEndpoint

class RevocationEndpoint(TokenEndpoint):
    """
    Implementation of revocation endpoint which is described in
    `RFC7009`_.

    .. _RFC7009: https://tools.ietf.org/html/rfc7009
    """
    ENDPOINT_NAME: str
    def authenticate_token(self, request, client):
        """
        The client constructs the request by including the following
        parameters using the "application/x-www-form-urlencoded" format in
        the HTTP request entity-body:

        token
            REQUIRED.  The token that the client wants to get revoked.

        token_type_hint
            OPTIONAL.  A hint about the type of the token submitted for
            revocation.
        """
        ...
    def check_params(self, request, client) -> None: ...
    def create_endpoint_response(self, request): ...
    def query_token(self, token_string, token_type_hint): ...
    def revoke_token(self, token, request): ...
