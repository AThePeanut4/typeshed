from _typeshed import Incomplete
from collections.abc import Sequence
from enum import Enum
from typing import Any, NamedTuple

from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey as Ed448PrivateKey, Ed448PublicKey as Ed448PublicKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey as Ed25519PrivateKey,
    Ed25519PublicKey as Ed25519PublicKey,
)
from cryptography.hazmat.primitives.asymmetric.x448 import X448PrivateKey as X448PrivateKey, X448PublicKey as X448PublicKey
from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey as X25519PrivateKey,
    X25519PublicKey as X25519PublicKey,
)
from jwcrypto.common import JWException

class UnimplementedOKPCurveKey:
    @classmethod
    def generate(cls) -> None: ...
    @classmethod
    def from_public_bytes(cls, *args) -> None: ...
    @classmethod
    def from_private_bytes(cls, *args) -> None: ...

ImplementedOkpCurves: Sequence[str]
priv_bytes: Incomplete

JWKTypesRegistry: Incomplete

class ParmType(Enum):
    """An enumeration."""
    name: str
    b64: str
    b64u: str
    unsupported: str

class JWKParameter(NamedTuple):
    """Parameter(description, public, required, type)"""
    description: Incomplete
    public: Incomplete
    required: Incomplete
    type: Incomplete

JWKValuesRegistry: Incomplete
JWKParamsRegistry: Incomplete
JWKEllipticCurveRegistry: Incomplete
JWKUseRegistry: Incomplete
JWKOperationsRegistry: Incomplete
JWKpycaCurveMap: Incomplete
IANANamedInformationHashAlgorithmRegistry: Incomplete

class InvalidJWKType(JWException):
    """
    Invalid JWK Type Exception.

    This exception is raised when an invalid parameter type is used.
    """
    value: Incomplete
    def __init__(self, value: Incomplete | None = None) -> None: ...

class InvalidJWKUsage(JWException):
    """
    Invalid JWK usage Exception.

    This exception is raised when an invalid key usage is requested,
    based on the key type and declared usage constraints.
    """
    value: Incomplete
    use: Incomplete
    def __init__(self, use, value) -> None: ...

class InvalidJWKOperation(JWException):
    """
    Invalid JWK Operation Exception.

    This exception is raised when an invalid key operation is requested,
    based on the key type and declared usage constraints.
    """
    op: Incomplete
    values: Incomplete
    def __init__(self, operation, values) -> None: ...

class InvalidJWKValue(JWException):
    """
    Invalid JWK Value Exception.

    This exception is raised when an invalid/unknown value is used in the
    context of an operation that requires specific values to be used based
    on the key type or other constraints.
    """
    ...

class JWK(dict[str, Any]):
    """
    JSON Web Key object

    This object represents a Key.
    It must be instantiated by using the standard defined key/value pairs
    as arguments of the initialization function.
    """
    def __init__(self, **kwargs) -> None:
        r"""
        Creates a new JWK object.

        The function arguments must be valid parameters as defined in the
        'IANA JSON Web Key Set Parameters registry' and specified in
        the :data:`JWKParamsRegistry` variable. The 'kty' parameter must
        always be provided and its value must be a valid one as defined
        by the 'IANA JSON Web Key Types registry' and specified in the
        :data:`JWKTypesRegistry` variable. The valid key parameters per
        key type are defined in the :data:`JWKValuesRegistry` variable.

        To generate a new random key call the class method generate() with
        the appropriate 'kty' parameter, and other parameters as needed (key
        size, public exponents, curve types, etc..)

        Valid options per type, when generating new keys:
         * oct: size(int)
         * RSA: public_exponent(int), size(int)
         * EC: crv(str) (one of P-256, P-384, P-521, secp256k1)
         * OKP: crv(str) (one of Ed25519, Ed448, X25519, X448)

        Deprecated:
        Alternatively if the 'generate' parameter is provided with a
        valid key type as value then a new key will be generated according
        to the defaults or provided key strength options (type specific).

        :param \**kwargs: parameters (optional).

        :raises InvalidJWKType: if the key type is invalid
        :raises InvalidJWKValue: if incorrect or inconsistent parameters
            are provided.
        """
        ...
    @classmethod
    def generate(cls, **kwargs): ...
    def generate_key(self, **params) -> None: ...
    def import_key(self, **kwargs) -> None: ...
    @classmethod
    def from_json(cls, key):
        """
        Creates a RFC 7517 JWK from the standard JSON format.

        :param key: The RFC 7517 representation of a JWK.

        :return: A JWK object that holds the json key.
        :rtype: JWK
        """
        ...
    def export(self, private_key: bool = True, as_dict: bool = False):
        """
        Exports the key in the standard JSON format.
        Exports the key regardless of type, if private_key is False
        and the key is_symmetric an exception is raised.

        :param private_key(bool): Whether to export the private key.
                                  Defaults to True.

        :return: A portable representation of the key.
            If as_dict is True then a dictionary is returned.
            By default a json string
        :rtype: `str` or `dict`
        """
        ...
    def export_public(self, as_dict: bool = False):
        """
        Exports the public key in the standard JSON format.
        It fails if one is not available like when this function
        is called on a symmetric key.

        :param as_dict(bool): If set to True export as python dict not JSON

        :return: A portable representation of the public key only.
            If as_dict is True then a dictionary is returned.
            By default a json string
        :rtype: `str` or `dict`
        """
        ...
    def export_private(self, as_dict: bool = False):
        """
        Export the private key in the standard JSON format.
        It fails for a JWK that has only a public key or is symmetric.

        :param as_dict(bool): If set to True export as python dict not JSON

        :return: A portable representation of a private key.
            If as_dict is True then a dictionary is returned.
            By default a json string
        :rtype: `str` or `dict`
        """
        ...
    def export_symmetric(self, as_dict: bool = False): ...
    def public(self): ...
    @property
    def has_public(self) -> bool:
        """Whether this JWK has an asymmetric Public key value."""
        ...
    @property
    def has_private(self) -> bool:
        """Whether this JWK has an asymmetric Private key value."""
        ...
    @property
    def is_symmetric(self) -> bool:
        """Whether this JWK is a symmetric key."""
        ...
    @property
    def key_type(self):
        """The Key type"""
        ...
    @property
    def key_id(self):
        """
        The Key ID.
        Provided by the kid parameter if present, otherwise returns None.
        """
        ...
    @property
    def key_curve(self):
        """The Curve Name."""
        ...
    def get_curve(self, arg):
        """
        Gets the Elliptic Curve associated with the key.

        :param arg: an optional curve name

        :raises InvalidJWKType: the key is not an EC or OKP key.
        :raises InvalidJWKValue: if the curve name is invalid.

        :return: An EllipticCurve object
        :rtype: `EllipticCurve`
        """
        ...
    def get_op_key(self, operation: Incomplete | None = None, arg: Incomplete | None = None):
        """
        Get the key object associated to the requested operation.
        For example the public RSA key for the 'verify' operation or
        the private EC key for the 'decrypt' operation.

        :param operation: The requested operation.
         The valid set of operations is available in the
         :data:`JWKOperationsRegistry` registry.
        :param arg: An optional, context specific, argument.
         For example a curve name.

        :raises InvalidJWKOperation: if the operation is unknown or
         not permitted with this key.
        :raises InvalidJWKUsage: if the use constraints do not permit
         the operation.

        :return: A Python Cryptography key object for asymmetric keys
            or a baseurl64_encoded octet string for symmetric keys
        """
        ...
    def import_from_pyca(self, key) -> None: ...
    def import_from_pem(self, data, password: Incomplete | None = None, kid: Incomplete | None = None) -> None:
        """
        Imports a key from data loaded from a PEM file.
        The key may be encrypted with a password.
        Private keys (PKCS#8 format), public keys, and X509 certificate's
        public keys can be imported with this interface.

        :param data(bytes): The data contained in a PEM file.
        :param password(bytes): An optional password to unwrap the key.
        """
        ...
    def export_to_pem(self, private_key: bool = False, password: bool = False):
        """
        Exports keys to a data buffer suitable to be stored as a PEM file.
        Either the public or the private key can be exported to a PEM file.
        For private keys the PKCS#8 format is used. If a password is provided
        the best encryption method available as determined by the cryptography
        module is used to wrap the key.

        :param private_key: Whether the private key should be exported.
         Defaults to `False` which means the public key is exported by default.
        :param password(bytes): A password for wrapping the private key.
         Defaults to False which will cause the operation to fail. To avoid
         encryption the user must explicitly pass None, otherwise the user
         needs to provide a password in a bytes buffer.

        :return: A serialized bytes buffer containing a PEM formatted key.
        :rtype: `bytes`
        """
        ...
    @classmethod
    def from_pyca(cls, key): ...
    @classmethod
    def from_pem(cls, data, password: Incomplete | None = None):
        """
        Creates a key from PKCS#8 formatted data loaded from a PEM file.
           See the function `import_from_pem` for details.

        :param data(bytes): The data contained in a PEM file.
        :param password(bytes): An optional password to unwrap the key.

        :return: A JWK object.
        :rtype: JWK
        """
        ...
    def thumbprint(self, hashalg=...):
        """
        Returns the key thumbprint as specified by RFC 7638.

        :param hashalg: A hash function (defaults to SHA256)

        :return: A base64url encoded digest of the key
        :rtype: `str`
        """
        ...
    def thumbprint_uri(self, hname: str = "sha-256"):
        """
        Returns the key thumbprint URI as specified by RFC 9278.

        :param hname: A hash function name as specified in IANA's
         Named Information registry:
         https://www.iana.org/assignments/named-information/
         Values from `IANANamedInformationHashAlgorithmRegistry`

        :return: A JWK Thumbprint URI
        :rtype: `str`
        """
        ...
    @classmethod
    def from_password(cls, password):
        """
        Creates a symmetric JWK key from a user password.

        :param password: A password in utf8 format.

        :return: a JWK object
        :rtype: JWK
        """
        ...
    def setdefault(self, key: str, default: Incomplete | None = None): ...

class JWKSet(dict[str, Any]):
    """
    A set of JWK objects.

    Inherits from the standard 'dict' builtin type.
    Creates a special key 'keys' that is of a type derived from 'set'
    The 'keys' attribute accepts only :class:`jwcrypto.jwk.JWK` elements.
    """
    def add(self, elem) -> None: ...
    def export(self, private_keys: bool = True, as_dict: bool = False):
        """
        Exports a RFC 7517 key set.
           Exports as json by default, or as dict if requested.

        :param private_key(bool): Whether to export private keys.
                                  Defaults to True.
        :param as_dict(bool): Whether to return a dict instead of
                              a JSON object

        :return: A portable representation of the key set.
            If as_dict is True then a dictionary is returned.
            By default a json string
        :rtype: `str` or `dict`
        """
        ...
    def import_keyset(self, keyset) -> None:
        """
        Imports a RFC 7517 key set using the standard JSON format.

        :param keyset: The RFC 7517 representation of a JOSE key set.
        """
        ...
    @classmethod
    def from_json(cls, keyset):
        """
        Creates a RFC 7517 key set from the standard JSON format.

        :param keyset: The RFC 7517 representation of a JOSE key set.

        :return: A JWKSet object.
        :rtype: JWKSet
        """
        ...
    def get_key(self, kid):
        """
        Gets a key from the set.
        :param kid: the 'kid' key identifier.

        :return: A JWK from the set
        :rtype: JWK
        """
        ...
    def get_keys(self, kid):
        """
        Gets keys from the set with matching kid.
        :param kid: the 'kid' key identifier.

        :return: a List of keys
        :rtype: `list`
        """
        ...
    def setdefault(self, key: str, default: Incomplete | None = None): ...
