from _typeshed import Incomplete

class BaseApp:
    client_cls: Incomplete
    OAUTH_APP_CONFIG: Incomplete
    def request(self, method, url, token: Incomplete | None = None, **kwargs): ...
    def get(self, url, **kwargs):
        """
        Invoke GET http request.

        If ``api_base_url`` configured, shortcut is available::

            client.get('users/lepture')
        """
        ...
    def post(self, url, **kwargs):
        """
        Invoke POST http request.

        If ``api_base_url`` configured, shortcut is available::

            client.post('timeline', json={'text': 'Hi'})
        """
        ...
    def patch(self, url, **kwargs):
        """
        Invoke PATCH http request.

        If ``api_base_url`` configured, shortcut is available::

            client.patch('profile', json={'name': 'Hsiaoming Yang'})
        """
        ...
    def put(self, url, **kwargs):
        """
        Invoke PUT http request.

        If ``api_base_url`` configured, shortcut is available::

            client.put('profile', json={'name': 'Hsiaoming Yang'})
        """
        ...
    def delete(self, url, **kwargs):
        """
        Invoke DELETE http request.

        If ``api_base_url`` configured, shortcut is available::

            client.delete('posts/123')
        """
        ...

class _RequestMixin: ...

class OAuth1Base:
    client_cls: Incomplete
    framework: Incomplete
    name: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    request_token_url: Incomplete
    request_token_params: Incomplete
    access_token_url: Incomplete
    access_token_params: Incomplete
    authorize_url: Incomplete
    authorize_params: Incomplete
    api_base_url: Incomplete
    client_kwargs: Incomplete
    def __init__(
        self,
        framework,
        name: Incomplete | None = None,
        fetch_token: Incomplete | None = None,
        client_id: Incomplete | None = None,
        client_secret: Incomplete | None = None,
        request_token_url: Incomplete | None = None,
        request_token_params: Incomplete | None = None,
        access_token_url: Incomplete | None = None,
        access_token_params: Incomplete | None = None,
        authorize_url: Incomplete | None = None,
        authorize_params: Incomplete | None = None,
        api_base_url: Incomplete | None = None,
        client_kwargs: Incomplete | None = None,
        user_agent: Incomplete | None = None,
        **kwargs,
    ) -> None: ...

class OAuth1Mixin(_RequestMixin, OAuth1Base):
    def request(self, method, url, token: Incomplete | None = None, **kwargs): ...
    def create_authorization_url(self, redirect_uri: Incomplete | None = None, **kwargs):
        """
        Generate the authorization url and state for HTTP redirect.

        :param redirect_uri: Callback or redirect URI for authorization.
        :param kwargs: Extra parameters to include.
        :return: dict
        """
        ...
    def fetch_access_token(self, request_token: Incomplete | None = None, **kwargs):
        """
        Fetch access token in one step.

        :param request_token: A previous request token for OAuth 1.
        :param kwargs: Extra parameters to fetch access token.
        :return: A token dict.
        """
        ...

class OAuth2Base:
    client_cls: Incomplete
    framework: Incomplete
    name: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    access_token_url: Incomplete
    access_token_params: Incomplete
    authorize_url: Incomplete
    authorize_params: Incomplete
    api_base_url: Incomplete
    client_kwargs: Incomplete
    compliance_fix: Incomplete
    client_auth_methods: Incomplete
    server_metadata: Incomplete
    def __init__(
        self,
        framework,
        name: Incomplete | None = None,
        fetch_token: Incomplete | None = None,
        update_token: Incomplete | None = None,
        client_id: Incomplete | None = None,
        client_secret: Incomplete | None = None,
        access_token_url: Incomplete | None = None,
        access_token_params: Incomplete | None = None,
        authorize_url: Incomplete | None = None,
        authorize_params: Incomplete | None = None,
        api_base_url: Incomplete | None = None,
        client_kwargs: Incomplete | None = None,
        server_metadata_url: Incomplete | None = None,
        compliance_fix: Incomplete | None = None,
        client_auth_methods: Incomplete | None = None,
        user_agent: Incomplete | None = None,
        **kwargs,
    ) -> None: ...

class OAuth2Mixin(_RequestMixin, OAuth2Base):
    def request(self, method, url, token: Incomplete | None = None, **kwargs): ...
    def load_server_metadata(self): ...
    def create_authorization_url(self, redirect_uri: Incomplete | None = None, **kwargs):
        """
        Generate the authorization url and state for HTTP redirect.

        :param redirect_uri: Callback or redirect URI for authorization.
        :param kwargs: Extra parameters to include.
        :return: dict
        """
        ...
    def fetch_access_token(self, redirect_uri: Incomplete | None = None, **kwargs):
        """
        Fetch access token in the final step.

        :param redirect_uri: Callback or Redirect URI that is used in
                             previous :meth:`authorize_redirect`.
        :param kwargs: Extra parameters to fetch access token.
        :return: A token dict.
        """
        ...
