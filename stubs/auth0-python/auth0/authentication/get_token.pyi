from .base import AuthenticationBase as AuthenticationBase

class GetToken(AuthenticationBase):
    """
    /oauth/token related endpoints

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """
    def authorization_code(self, code: str, redirect_uri: str | None, grant_type: str = "authorization_code"):
        """
        Authorization code grant

        This is the OAuth 2.0 grant that regular web apps utilize in order
        to access an API. Use this endpoint to exchange an Authorization Code
        for a Token.

        Args:
            code (str): The Authorization Code received from the /authorize Calls

            redirect_uri (str, optional): This is required only if it was set at
            the GET /authorize endpoint. The values must match

            grant_type (str): Denotes the flow you're using. For authorization code
            use authorization_code

        Returns:
            access_token, id_token
        """
        ...
    def authorization_code_pkce(
        self, code_verifier: str, code: str, redirect_uri: str | None, grant_type: str = "authorization_code"
    ):
        """
        Authorization code pkce grant

        This is the OAuth 2.0 grant that mobile apps utilize in order to access an API.
        Use this endpoint to exchange an Authorization Code for a Token.

        Args:
            code_verifier (str): Cryptographically random key that was used to generate
            the code_challenge passed to /authorize.

            code (str): The Authorization Code received from the /authorize Calls

            redirect_uri (str, optional): This is required only if it was set at
            the GET /authorize endpoint. The values must match

            grant_type (str): Denotes the flow you're using. For authorization code pkce
            use authorization_code

        Returns:
            access_token, id_token
        """
        ...
    def client_credentials(self, audience: str, grant_type: str = "client_credentials", organization: str | None = None):
        """
        Client credentials grant

        This is the OAuth 2.0 grant that server processes utilize in
        order to access an API. Use this endpoint to directly request
        an access_token by using the Application Credentials (a Client Id and
        a Client Secret).

        Args:
            audience (str): The unique identifier of the target API you want to access.

            grant_type (str, optional): Denotes the flow you're using. For client credentials use "client_credentials"

            organization (str, optional): Optional Organization name or ID. When included, the access token returned
            will include the org_id and org_name claims

        Returns:
            access_token
        """
        ...
    def login(
        self,
        username: str,
        password: str,
        scope: str | None = None,
        realm: str | None = None,
        audience: str | None = None,
        grant_type: str = "http://auth0.com/oauth/grant-type/password-realm",
        forwarded_for: str | None = None,
    ): ...
    def refresh_token(self, refresh_token: str, scope: str = "", grant_type: str = "refresh_token"): ...
    def passwordless_login(self, username: str, otp: str, realm: str, scope: str, audience: str): ...
    def backchannel_login(self, auth_req_id: str, grant_type: str = "urn:openid:params:grant-type:ciba"): ...
    def access_token_for_connection(
        self,
        subject_token_type: str,
        subject_token: str,
        requested_token_type: str,
        connection: str | None = None,
        grant_type: str = ...,
    ): ...
