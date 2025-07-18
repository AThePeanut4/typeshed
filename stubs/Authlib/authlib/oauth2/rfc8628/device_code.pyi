from _typeshed import Incomplete
from logging import Logger

from authlib.oauth2.rfc6749 import BaseGrant, TokenEndpointMixin

log: Logger
DEVICE_CODE_GRANT_TYPE: str

class DeviceCodeGrant(BaseGrant, TokenEndpointMixin):
    """
    This OAuth 2.0 [RFC6749] protocol extension enables OAuth clients to
    request user authorization from applications on devices that have
    limited input capabilities or lack a suitable browser.  Such devices
    include smart TVs, media consoles, picture frames, and printers,
    which lack an easy input method or a suitable browser required for
    traditional OAuth interactions. Here is the authorization flow::

        +----------+                                +----------------+
        |          |>---(A)-- Client Identifier --->|                |
        |          |                                |                |
        |          |<---(B)-- Device Code,      ---<|                |
        |          |          User Code,            |                |
        |  Device  |          & Verification URI    |                |
        |  Client  |                                |                |
        |          |  [polling]                     |                |
        |          |>---(E)-- Device Code       --->|                |
        |          |          & Client Identifier   |                |
        |          |                                |  Authorization |
        |          |<---(F)-- Access Token      ---<|     Server     |
        +----------+   (& Optional Refresh Token)   |                |
              v                                     |                |
              :                                     |                |
             (C) User Code & Verification URI       |                |
              :                                     |                |
              v                                     |                |
        +----------+                                |                |
        | End User |                                |                |
        |    at    |<---(D)-- End user reviews  --->|                |
        |  Browser |          authorization request |                |
        +----------+                                +----------------+

    This DeviceCodeGrant is the implementation of step (E) and (F).

    (E) While the end user reviews the client's request (step D), the
        client repeatedly polls the authorization server to find out if
        the user completed the user authorization step.  The client
        includes the device code and its client identifier.

    (F) The authorization server validates the device code provided by
        the client and responds with the access token if the client is
        granted access, an error if they are denied access, or an
        indication that the client should continue to poll.
    """
    GRANT_TYPE = DEVICE_CODE_GRANT_TYPE
    TOKEN_ENDPOINT_AUTH_METHODS: Incomplete
    def validate_token_request(self) -> None:
        """
        After displaying instructions to the user, the client creates an
        access token request and sends it to the token endpoint with the
        following parameters:

        grant_type
            REQUIRED.  Value MUST be set to
            "urn:ietf:params:oauth:grant-type:device_code".

        device_code
            REQUIRED.  The device verification code, "device_code" from the
            device authorization response.

        client_id
            REQUIRED if the client is not authenticating with the
            authorization server as described in Section 3.2.1. of [RFC6749].
            The client identifier as described in Section 2.2 of [RFC6749].

        For example, the client makes the following HTTPS request::

            POST /token HTTP/1.1
            Host: server.example.com
            Content-Type: application/x-www-form-urlencoded

            grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code
            &device_code=GmRhmhcxhwAzkoEqiMEg_DnyEysNkuNhszIySk9eS
            &client_id=1406020730
        """
        ...
    def create_token_response(self): ...
    def validate_device_credential(self, credential): ...
    def query_device_credential(self, device_code) -> None:
        """
        Get device credential from previously savings via ``DeviceAuthorizationEndpoint``.
        Developers MUST implement it in subclass::

            def query_device_credential(self, device_code):
                return DeviceCredential.get(device_code)

        :param device_code: a string represent the code.
        :return: DeviceCredential instance
        """
        ...
    def query_user_grant(self, user_code) -> None:
        """
        Get user and grant via the given user code. Developers MUST
        implement it in subclass::

            def query_user_grant(self, user_code):
                # e.g. we saved user grant info in redis
                data = redis.get("oauth_user_grant:" + user_code)
                if not data:
                    return None

                user_id, allowed = data.split()
                user = User.get(user_id)
                return user, bool(allowed)

        Note, user grant information is saved by verification endpoint.
        """
        ...
    def should_slow_down(self, credential) -> None:
        """
        The authorization request is still pending and polling should
        continue, but the interval MUST be increased by 5 seconds for this
        and all subsequent requests.
        """
        ...
