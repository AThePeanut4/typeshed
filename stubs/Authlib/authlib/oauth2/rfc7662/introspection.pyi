from authlib.oauth2.rfc6749 import TokenEndpoint

class IntrospectionEndpoint(TokenEndpoint):
    """
    Implementation of introspection endpoint which is described in
    `RFC7662`_.

    .. _RFC7662: https://tools.ietf.org/html/rfc7662
    """
    ENDPOINT_NAME: str
    def authenticate_token(self, request, client):
        """
        The protected resource calls the introspection endpoint using an HTTP
        ``POST`` request with parameters sent as
        "application/x-www-form-urlencoded" data. The protected resource sends a
        parameter representing the token along with optional parameters
        representing additional context that is known by the protected resource
        to aid the authorization server in its response.

        token
            **REQUIRED**  The string value of the token. For access tokens, this
            is the ``access_token`` value returned from the token endpoint
            defined in OAuth 2.0. For refresh tokens, this is the
            ``refresh_token`` value returned from the token endpoint as defined
            in OAuth 2.0.

        token_type_hint
            **OPTIONAL**  A hint about the type of the token submitted for
            introspection.
        """
        ...
    def check_params(self, request, client) -> None: ...
    def create_endpoint_response(self, request):
        """
        Validate introspection request and create the response.

        :returns: (status_code, body, headers)
        """
        ...
    def create_introspection_payload(self, token): ...
    def check_permission(self, token, client, request): ...
    def query_token(self, token_string, token_type_hint): ...
    def introspect_token(self, token): ...
