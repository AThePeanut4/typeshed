from _typeshed import Incomplete
from logging import Logger
from typing import TypedDict
from typing_extensions import TypeAlias

import requests
from oauthlib.oauth1 import Client

from . import OAuth1

# should be dict[str, str] but could look different
_ParsedToken: TypeAlias = dict[str, Incomplete]

class _TokenDict(TypedDict, total=False):
    oauth_token: Incomplete  # oauthlib.oauth1.Client.resource_owner_key
    oauth_token_secret: Incomplete  # oauthlib.oauth1.Client.resource_token_secret
    oauth_verifier: Incomplete  # oauthlib.oauth1.Client.oauth_verifier

log: Logger

def urldecode(body):
    """Parse query or json to python dictionary"""
    ...

class TokenRequestDenied(ValueError):
    response: requests.Response
    def __init__(self, message: str, response: requests.Response) -> None: ...
    @property
    def status_code(self) -> int:
        """For backwards-compatibility purposes"""
        ...

class TokenMissing(ValueError):
    response: requests.Response
    def __init__(self, message: str, response: requests.Response) -> None: ...

class VerifierMissing(ValueError): ...

class OAuth1Session(requests.Session):
    """
    Request signing and convenience methods for the oauth dance.

    What is the difference between OAuth1Session and OAuth1?

    OAuth1Session actually uses OAuth1 internally and its purpose is to assist
    in the OAuth workflow through convenience methods to prepare authorization
    URLs and parse the various token and redirection responses. It also provide
    rudimentary validation of responses.

    An example of the OAuth workflow using a basic CLI app and Twitter.

    >>> # Credentials obtained during the registration.
    >>> client_key = 'client key'
    >>> client_secret = 'secret'
    >>> callback_uri = 'https://127.0.0.1/callback'
    >>>
    >>> # Endpoints found in the OAuth provider API documentation
    >>> request_token_url = 'https://api.twitter.com/oauth/request_token'
    >>> authorization_url = 'https://api.twitter.com/oauth/authorize'
    >>> access_token_url = 'https://api.twitter.com/oauth/access_token'
    >>>
    >>> oauth_session = OAuth1Session(client_key,client_secret=client_secret, callback_uri=callback_uri)
    >>>
    >>> # First step, fetch the request token.
    >>> oauth_session.fetch_request_token(request_token_url)
    {
        'oauth_token': 'kjerht2309u',
        'oauth_token_secret': 'lsdajfh923874',
    }
    >>>
    >>> # Second step. Follow this link and authorize
    >>> oauth_session.authorization_url(authorization_url)
    'https://api.twitter.com/oauth/authorize?oauth_token=sdf0o9823sjdfsdf&oauth_callback=https%3A%2F%2F127.0.0.1%2Fcallback'
    >>>
    >>> # Third step. Fetch the access token
    >>> redirect_response = input('Paste the full redirect URL here.')
    >>> oauth_session.parse_authorization_response(redirect_response)
    {
        'oauth_token: 'kjerht2309u',
        'oauth_token_secret: 'lsdajfh923874',
        'oauth_verifier: 'w34o8967345',
    }
    >>> oauth_session.fetch_access_token(access_token_url)
    {
        'oauth_token': 'sdf0o9823sjdfsdf',
        'oauth_token_secret': '2kjshdfp92i34asdasd',
    }
    >>> # Done. You can now make OAuth requests.
    >>> status_url = 'http://api.twitter.com/1/statuses/update.json'
    >>> new_status = {'status':  'hello world!'}
    >>> oauth_session.post(status_url, data=new_status)
    <Response [200]>
    """
    auth: OAuth1
    def __init__(
        self,
        client_key,
        client_secret=None,
        resource_owner_key=None,
        resource_owner_secret=None,
        callback_uri=None,
        signature_method="HMAC-SHA1",
        signature_type="AUTH_HEADER",
        rsa_key=None,
        verifier=None,
        client_class: type[Client] | None = None,
        force_include_body: bool = False,
        *,
        encoding: str = "utf-8",
        nonce=None,
        timestamp=None,
    ) -> None: ...
    @property
    def token(self) -> _TokenDict: ...
    @token.setter
    def token(self, value: _TokenDict) -> None: ...
    @property
    def authorized(self) -> bool: ...
    def authorization_url(self, url: str, request_token=None, **kwargs) -> str: ...
    def fetch_request_token(self, url: str, realm=None, **request_kwargs) -> _ParsedToken: ...
    def fetch_access_token(self, url: str, verifier=None, **request_kwargs) -> _ParsedToken: ...
    def parse_authorization_response(self, url: str) -> _ParsedToken: ...
    def rebuild_auth(self, prepared_request: requests.PreparedRequest, response: requests.Response) -> None: ...
