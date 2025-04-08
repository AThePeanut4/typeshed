from .base import Client

class BackendApplicationClient(Client):
    """
    A public client utilizing the client credentials grant workflow.

    The client can request an access token using only its client
    credentials (or other supported means of authentication) when the
    client is requesting access to the protected resources under its
    control, or those of another resource owner which has been previously
    arranged with the authorization server (the method of which is beyond
    the scope of this specification).

    The client credentials grant type MUST only be used by confidential
    clients.

    Since the client authentication is used as the authorization grant,
    no additional authorization request is needed.
    """
    grant_type: str
    def prepare_request_body(
        self,
        body: str = "",
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        include_client_id: bool = False,
        *,
        code_verifier: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        **kwargs,
    ) -> str: ...
