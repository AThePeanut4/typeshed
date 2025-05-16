from _typeshed import Incomplete

class JsonWebToken:
    SENSITIVE_NAMES: Incomplete
    SENSITIVE_VALUES: Incomplete
    def __init__(self, algorithms, private_headers=None) -> None: ...
    def check_sensitive_data(self, payload) -> None:
        """Check if payload contains sensitive information."""
        ...
    def encode(self, header, payload, key, check: bool = True):
        """
        Encode a JWT with the given header, payload and key.

        :param header: A dict of JWS header
        :param payload: A dict to be encoded
        :param key: key used to sign the signature
        :param check: check if sensitive data in payload
        :return: bytes
        """
        ...
    def decode(self, s, key, claims_cls=None, claims_options=None, claims_params=None):
        """
        Decode the JWT with the given key. This is similar with
        :meth:`verify`, except that it will raise BadSignatureError when
        signature doesn't match.

        :param s: text of JWT
        :param key: key used to verify the signature
        :param claims_cls: class to be used for JWT claims
        :param claims_options: `options` parameters for claims_cls
        :param claims_params: `params` parameters for claims_cls
        :return: claims_cls instance
        :raise: BadSignatureError
        """
        ...

def decode_payload(bytes_payload): ...
def prepare_raw_key(raw): ...
def find_encode_key(key, header): ...
def create_load_key(key): ...
