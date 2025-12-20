from _typeshed import Incomplete

CONTENT_TYPE_FORM_URLENCODED: str
CONTENT_TYPE_MULTI_PART: str

class ClientAuth:
    SIGNATURE_METHODS: Incomplete
    @classmethod
    def register_signature_method(cls, name, sign) -> None:
        """
        Extend client signature methods.

        :param name: A string to represent signature method.
        :param sign: A function to generate signature.

        The ``sign`` method accept 2 parameters::

            def custom_sign_method(client, request):
                # client is the instance of Client.
                return "your-signed-string"


            Client.register_signature_method("custom-name", custom_sign_method)
        """
        ...
    client_id: Incomplete
    client_secret: Incomplete
    token: Incomplete
    token_secret: Incomplete
    redirect_uri: Incomplete
    signature_method: Incomplete
    signature_type: Incomplete
    rsa_key: Incomplete
    verifier: Incomplete
    realm: Incomplete
    force_include_body: Incomplete
    def __init__(
        self,
        client_id,
        client_secret=None,
        token=None,
        token_secret=None,
        redirect_uri=None,
        rsa_key=None,
        verifier=None,
        signature_method="HMAC-SHA1",
        signature_type="HEADER",
        realm=None,
        force_include_body: bool = False,
    ) -> None: ...
    def get_oauth_signature(self, method, uri, headers, body) -> str: ...
    def get_oauth_params(self, nonce, timestamp) -> list[Incomplete]: ...
    def sign(self, method, uri, headers, body) -> tuple[Incomplete, Incomplete, Incomplete]: ...
    def prepare(self, method, uri, headers, body) -> tuple[Incomplete, ...]: ...

def generate_nonce() -> str: ...
def generate_timestamp() -> str: ...
