from _typeshed import Incomplete

class JWSAlgorithm:
    """
    Interface for JWS algorithm. JWA specification (RFC7518) SHOULD
    implement the algorithms for JWS with this base implementation.
    """
    name: Incomplete
    description: Incomplete
    algorithm_type: str
    algorithm_location: str
    def prepare_key(self, raw_data) -> None: ...
    def sign(self, msg, key): ...
    def verify(self, msg, sig, key) -> bool: ...

class JWSHeader(dict[str, object]):
    """
    Header object for JWS. It combine the protected header and unprotected
    header together. JWSHeader itself is a dict of the combined dict. e.g.

        >>> protected = {"alg": "HS256"}
        >>> header = {"kid": "a"}
        >>> jws_header = JWSHeader(protected, header)
        >>> print(jws_header)
        {'alg': 'HS256', 'kid': 'a'}
        >>> jws_header.protected == protected
        >>> jws_header.header == header

    :param protected: dict of protected header
    :param header: dict of unprotected header
    """
    protected: Incomplete
    header: Incomplete
    def __init__(self, protected, header) -> None: ...
    @classmethod
    def from_dict(cls, obj): ...

class JWSObject(dict[str, object]):
    """A dict instance to represent a JWS object."""
    header: Incomplete
    payload: Incomplete
    type: Incomplete
    def __init__(self, header, payload, type: str = "compact") -> None: ...
    @property
    def headers(self):
        """Alias of ``header`` for JSON typed JWS."""
        ...
