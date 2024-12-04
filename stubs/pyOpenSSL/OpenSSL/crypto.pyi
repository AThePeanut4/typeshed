from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Callable, Iterable, Sequence
from datetime import datetime
from typing import Any
from typing_extensions import TypeAlias, deprecated

from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey, DSAPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.x509 import Certificate, CertificateRevocationList, CertificateSigningRequest

_Key: TypeAlias = DSAPrivateKey | DSAPublicKey | RSAPrivateKey | RSAPublicKey

FILETYPE_PEM: int
FILETYPE_ASN1: int
FILETYPE_TEXT: int

TYPE_RSA: int
TYPE_DSA: int
TYPE_DH: int
TYPE_EC: int

class _EllipticCurve:
    """
    A representation of a supported elliptic curve.

    @cvar _curves: :py:obj:`None` until an attempt is made to load the curves.
        Thereafter, a :py:type:`set` containing :py:type:`_EllipticCurve`
        instances each of which represents one curve supported by the system.
    @type _curves: :py:type:`NoneType` or :py:type:`set`
    """
    def __init__(self, lib: Incomplete | None, nid: int, name: str) -> None:
        """
        :param _lib: The :py:mod:`cryptography` binding instance used to
            interface with OpenSSL.

        :param _nid: The OpenSSL NID identifying the curve this object
            represents.
        :type _nid: :py:class:`int`

        :param name: The OpenSSL short name identifying the curve this object
            represents.
        :type name: :py:class:`unicode`
        """
        ...

class Error(Exception):
    """An error occurred in an `OpenSSL.crypto` API."""
    ...

class PKey:
    """A class representing an DSA or RSA public key or key pair."""
    def __init__(self) -> None: ...
    def bits(self) -> int:
        """
        Returns the number of bits of the key

        :return: The number of bits of the key.
        """
        ...
    def check(self) -> bool:
        """
        Check the consistency of an RSA private key.

        This is the Python equivalent of OpenSSL's ``RSA_check_key``.

        :return: ``True`` if key is consistent.

        :raise OpenSSL.crypto.Error: if the key is inconsistent.

        :raise TypeError: if the key is of a type which cannot be checked.
            Only RSA keys can currently be checked.
        """
        ...
    @classmethod
    def from_cryptography_key(cls, crypto_key: _Key) -> PKey:
        """
        Construct based on a ``cryptography`` *crypto_key*.

        :param crypto_key: A ``cryptography`` key.
        :type crypto_key: One of ``cryptography``'s `key interfaces`_.

        :rtype: PKey

        .. versionadded:: 16.1.0
        """
        ...
    def generate_key(self, type: int, bits: int) -> None:
        """
        Generate a key pair of the given type, with the given number of bits.

        This generates a key "into" the this object.

        :param type: The key type.
        :type type: :py:data:`TYPE_RSA` or :py:data:`TYPE_DSA`
        :param bits: The number of bits.
        :type bits: :py:data:`int` ``>= 0``
        :raises TypeError: If :py:data:`type` or :py:data:`bits` isn't
            of the appropriate type.
        :raises ValueError: If the number of bits isn't an integer of
            the appropriate size.
        :return: ``None``
        """
        ...
    def to_cryptography_key(self) -> _Key:
        """
        Export as a ``cryptography`` key.

        :rtype: One of ``cryptography``'s `key interfaces`_.

        .. _key interfaces: https://cryptography.io/en/latest/hazmat/            primitives/asymmetric/rsa/#key-interfaces

        .. versionadded:: 16.1.0
        """
        ...
    def type(self) -> int:
        """
        Returns the type of the key

        :return: The type of the key.
        """
        ...

class X509Name:
    """
    An X.509 Distinguished Name.

    :ivar countryName: The country of the entity.
    :ivar C: Alias for  :py:attr:`countryName`.

    :ivar stateOrProvinceName: The state or province of the entity.
    :ivar ST: Alias for :py:attr:`stateOrProvinceName`.

    :ivar localityName: The locality of the entity.
    :ivar L: Alias for :py:attr:`localityName`.

    :ivar organizationName: The organization name of the entity.
    :ivar O: Alias for :py:attr:`organizationName`.

    :ivar organizationalUnitName: The organizational unit of the entity.
    :ivar OU: Alias for :py:attr:`organizationalUnitName`

    :ivar commonName: The common name of the entity.
    :ivar CN: Alias for :py:attr:`commonName`.

    :ivar emailAddress: The e-mail address of the entity.
    """
    countryName: str
    C: str
    stateOrProvinceName: str
    ST: str
    localityName: str
    L: str
    organizationName: str
    O: str
    organizationalUnitName: str
    OU: str
    commonName: str
    CN: str
    emailAddress: str
    def __init__(self, name: X509Name) -> None:
        """
        Create a new X509Name, copying the given X509Name instance.

        :param name: The name to copy.
        :type name: :py:class:`X509Name`
        """
        ...
    def der(self) -> bytes:
        """
        Return the DER encoding of this name.

        :return: The DER encoded form of this name.
        :rtype: :py:class:`bytes`
        """
        ...
    def get_components(self) -> list[tuple[bytes, bytes]]:
        """
        Returns the components of this name, as a sequence of 2-tuples.

        :return: The components of this name.
        :rtype: :py:class:`list` of ``name, value`` tuples.
        """
        ...
    def hash(self) -> int:
        """
        Return an integer representation of the first four bytes of the
        MD5 digest of the DER representation of the name.

        This is the Python equivalent of OpenSSL's ``X509_NAME_hash``.

        :return: The (integer) hash of this name.
        :rtype: :py:class:`int`
        """
        ...

class X509:
    """An X.509 certificate."""
    def __init__(self) -> None: ...
    def add_extensions(self, extensions: Iterable[X509Extension]) -> None:
        """
        Add extensions to the certificate.

        :param extensions: The extensions to add.
        :type extensions: An iterable of :py:class:`X509Extension` objects.
        :return: ``None``
        """
        ...
    def digest(self, digest_name: str) -> bytes:
        """
        Return the digest of the X509 object.

        :param digest_name: The name of the digest algorithm to use.
        :type digest_name: :py:class:`str`

        :return: The digest of the object, formatted as
            :py:const:`b":"`-delimited hex pairs.
        :rtype: :py:class:`bytes`
        """
        ...
    @classmethod
    def from_cryptography(cls, crypto_cert: Certificate) -> X509:
        """
        Construct based on a ``cryptography`` *crypto_cert*.

        :param crypto_key: A ``cryptography`` X.509 certificate.
        :type crypto_key: ``cryptography.x509.Certificate``

        :rtype: X509

        .. versionadded:: 17.1.0
        """
        ...
    def get_extension(self, index: int) -> X509Extension:
        """
        Get a specific extension of the certificate by index.

        Extensions on a certificate are kept in order. The index
        parameter selects which extension will be returned.

        :param int index: The index of the extension to retrieve.
        :return: The extension at the specified index.
        :rtype: :py:class:`X509Extension`
        :raises IndexError: If the extension index was out of bounds.

        .. versionadded:: 0.12
        """
        ...
    def get_extension_count(self) -> int:
        """
        Get the number of extensions on this certificate.

        :return: The number of extensions.
        :rtype: :py:class:`int`

        .. versionadded:: 0.12
        """
        ...
    def get_issuer(self) -> X509Name:
        """
        Return the issuer of this certificate.

        This creates a new :class:`X509Name` that wraps the underlying issuer
        name field on the certificate. Modifying it will modify the underlying
        certificate, and will have the effect of modifying any other
        :class:`X509Name` that refers to this issuer.

        :return: The issuer of this certificate.
        :rtype: :class:`X509Name`
        """
        ...
    def get_notAfter(self) -> bytes | None:
        """
        Get the timestamp at which the certificate stops being valid.

        The timestamp is formatted as an ASN.1 TIME::

            YYYYMMDDhhmmssZ

        :return: A timestamp string, or ``None`` if there is none.
        :rtype: bytes or NoneType
        """
        ...
    def get_notBefore(self) -> bytes | None:
        """
        Get the timestamp at which the certificate starts being valid.

        The timestamp is formatted as an ASN.1 TIME::

            YYYYMMDDhhmmssZ

        :return: A timestamp string, or ``None`` if there is none.
        :rtype: bytes or NoneType
        """
        ...
    def get_pubkey(self) -> PKey:
        """
        Get the public key of the certificate.

        :return: The public key.
        :rtype: :py:class:`PKey`
        """
        ...
    def get_serial_number(self) -> int:
        """
        Return the serial number of this certificate.

        :return: The serial number.
        :rtype: int
        """
        ...
    def get_signature_algorithm(self) -> bytes:
        """
        Return the signature algorithm used in the certificate.

        :return: The name of the algorithm.
        :rtype: :py:class:`bytes`

        :raises ValueError: If the signature algorithm is undefined.

        .. versionadded:: 0.13
        """
        ...
    def get_subject(self) -> X509Name:
        """
        Return the subject of this certificate.

        This creates a new :class:`X509Name` that wraps the underlying subject
        name field on the certificate. Modifying it will modify the underlying
        certificate, and will have the effect of modifying any other
        :class:`X509Name` that refers to this subject.

        :return: The subject of this certificate.
        :rtype: :class:`X509Name`
        """
        ...
    def get_version(self) -> int:
        """
        Return the version number of the certificate.

        :return: The version number of the certificate.
        :rtype: :py:class:`int`
        """
        ...
    def gmtime_adj_notAfter(self, amount: int) -> None:
        """
        Adjust the time stamp on which the certificate stops being valid.

        :param int amount: The number of seconds by which to adjust the
            timestamp.
        :return: ``None``
        """
        ...
    def gmtime_adj_notBefore(self, amount: int) -> None:
        """
        Adjust the timestamp on which the certificate starts being valid.

        :param amount: The number of seconds by which to adjust the timestamp.
        :return: ``None``
        """
        ...
    def has_expired(self) -> bool:
        """
        Check whether the certificate has expired.

        :return: ``True`` if the certificate has expired, ``False`` otherwise.
        :rtype: bool
        """
        ...
    def set_issuer(self, issuer: X509Name) -> None:
        """
        Set the issuer of this certificate.

        :param issuer: The issuer.
        :type issuer: :py:class:`X509Name`

        :return: ``None``
        """
        ...
    def set_notAfter(self, when: bytes) -> None:
        """
        Set the timestamp at which the certificate stops being valid.

        The timestamp is formatted as an ASN.1 TIME::

            YYYYMMDDhhmmssZ

        :param bytes when: A timestamp string.
        :return: ``None``
        """
        ...
    def set_notBefore(self, when: bytes) -> None:
        """
        Set the timestamp at which the certificate starts being valid.

        The timestamp is formatted as an ASN.1 TIME::

            YYYYMMDDhhmmssZ

        :param bytes when: A timestamp string.
        :return: ``None``
        """
        ...
    def set_pubkey(self, pkey: PKey) -> None:
        """
        Set the public key of the certificate.

        :param pkey: The public key.
        :type pkey: :py:class:`PKey`

        :return: :py:data:`None`
        """
        ...
    def set_serial_number(self, serial: int) -> None:
        """
        Set the serial number of the certificate.

        :param serial: The new serial number.
        :type serial: :py:class:`int`

        :return: :py:data`None`
        """
        ...
    def set_subject(self, subject: X509Name) -> None:
        """
        Set the subject of this certificate.

        :param subject: The subject.
        :type subject: :py:class:`X509Name`

        :return: ``None``
        """
        ...
    def set_version(self, version: int) -> None:
        """
        Set the version number of the certificate. Note that the
        version value is zero-based, eg. a value of 0 is V1.

        :param version: The version number of the certificate.
        :type version: :py:class:`int`

        :return: ``None``
        """
        ...
    def sign(self, pkey: PKey, digest: str) -> None:
        """
        Sign the certificate with this key and digest type.

        :param pkey: The key to sign with.
        :type pkey: :py:class:`PKey`

        :param digest: The name of the message digest to use.
        :type digest: :py:class:`str`

        :return: :py:data:`None`
        """
        ...
    def subject_name_hash(self) -> bytes:
        """
        Return the hash of the X509 subject.

        :return: The hash of the subject.
        :rtype: :py:class:`bytes`
        """
        ...
    def to_cryptography(self) -> Certificate:
        """
        Export as a ``cryptography`` certificate.

        :rtype: ``cryptography.x509.Certificate``

        .. versionadded:: 17.1.0
        """
        ...

class X509Req:
    """An X.509 certificate signing requests."""
    def __init__(self) -> None: ...
    def add_extensions(self, extensions: Iterable[X509Extension]) -> None:
        """
        Add extensions to the certificate signing request.

        :param extensions: The X.509 extensions to add.
        :type extensions: iterable of :py:class:`X509Extension`
        :return: ``None``
        """
        ...
    @classmethod
    def from_cryptography(cls, crypto_req: CertificateSigningRequest) -> X509Req:
        """
        Construct based on a ``cryptography`` *crypto_req*.

        :param crypto_req: A ``cryptography`` X.509 certificate signing request
        :type crypto_req: ``cryptography.x509.CertificateSigningRequest``

        :rtype: X509Req

        .. versionadded:: 17.1.0
        """
        ...
    def get_extensions(self) -> list[X509Extension]:
        """
        Get X.509 extensions in the certificate signing request.

        :return: The X.509 extensions in this request.
        :rtype: :py:class:`list` of :py:class:`X509Extension` objects.

        .. versionadded:: 0.15
        """
        ...
    def get_pubkey(self) -> PKey:
        """
        Get the public key of the certificate signing request.

        :return: The public key.
        :rtype: :py:class:`PKey`
        """
        ...
    def get_subject(self) -> X509Name:
        """
        Return the subject of this certificate signing request.

        This creates a new :class:`X509Name` that wraps the underlying subject
        name field on the certificate signing request. Modifying it will modify
        the underlying signing request, and will have the effect of modifying
        any other :class:`X509Name` that refers to this subject.

        :return: The subject of this certificate signing request.
        :rtype: :class:`X509Name`
        """
        ...
    def get_version(self) -> int:
        """
        Get the version subfield (RFC 2459, section 4.1.2.1) of the certificate
        request.

        :return: The value of the version subfield.
        :rtype: :py:class:`int`
        """
        ...
    def set_pubkey(self, pkey: PKey) -> None:
        """
        Set the public key of the certificate signing request.

        :param pkey: The public key to use.
        :type pkey: :py:class:`PKey`

        :return: ``None``
        """
        ...
    def set_version(self, version: int) -> None:
        """
        Set the version subfield (RFC 2986, section 4.1) of the certificate
        request.

        :param int version: The version number.
        :return: ``None``
        """
        ...
    def sign(self, pkey: PKey, digest: str) -> None:
        """
        Sign the certificate signing request with this key and digest type.

        :param pkey: The key pair to sign with.
        :type pkey: :py:class:`PKey`
        :param digest: The name of the message digest to use for the signature,
            e.g. :py:data:`"sha256"`.
        :type digest: :py:class:`str`
        :return: ``None``
        """
        ...
    def to_cryptography(self) -> CertificateSigningRequest:
        """
        Export as a ``cryptography`` certificate signing request.

        :rtype: ``cryptography.x509.CertificateSigningRequest``

        .. versionadded:: 17.1.0
        """
        ...
    def verify(self, pkey: PKey) -> bool:
        """
        Verifies the signature on this certificate signing request.

        :param PKey key: A public key.

        :return: ``True`` if the signature is correct.
        :rtype: bool

        :raises OpenSSL.crypto.Error: If the signature is invalid or there is a
            problem verifying the signature.
        """
        ...

@deprecated("X509Extension support in pyOpenSSL is deprecated. You should use the APIs in cryptography.")
class X509Extension:
    """An X.509 v3 certificate extension."""
    def __init__(
        self, type_name: bytes, critical: bool, value: bytes, subject: X509 | None = None, issuer: X509 | None = None
    ) -> None:
        """
        Initializes an X509 extension.

        :param type_name: The name of the type of extension_ to create.
        :type type_name: :py:data:`bytes`

        :param bool critical: A flag indicating whether this is a critical
            extension.

        :param value: The OpenSSL textual representation of the extension's
            value.
        :type value: :py:data:`bytes`

        :param subject: Optional X509 certificate to use as subject.
        :type subject: :py:class:`X509`

        :param issuer: Optional X509 certificate to use as issuer.
        :type issuer: :py:class:`X509`

        .. _extension: https://www.openssl.org/docs/manmaster/man5/
            x509v3_config.html#STANDARD-EXTENSIONS
        """
        ...
    def get_critical(self) -> bool:
        """
        Returns the critical field of this X.509 extension.

        :return: The critical field.
        """
        ...
    def get_data(self) -> bytes:
        """
        Returns the data of the X509 extension, encoded as ASN.1.

        :return: The ASN.1 encoded data of this X509 extension.
        :rtype: :py:data:`bytes`

        .. versionadded:: 0.12
        """
        ...
    def get_short_name(self) -> bytes:
        """
        Returns the short type name of this X.509 extension.

        The result is a byte string such as :py:const:`b"basicConstraints"`.

        :return: The short type name.
        :rtype: :py:data:`bytes`

        .. versionadded:: 0.12
        """
        ...

@deprecated("CRL support in pyOpenSSL is deprecated. You should use the APIs in cryptography.")
class Revoked:
    """A certificate revocation."""
    def __init__(self) -> None: ...
    def all_reasons(self) -> list[bytes]:
        """
        Return a list of all the supported reason strings.

        This list is a copy; modifying it does not change the supported reason
        strings.

        :return: A list of reason strings.
        :rtype: :class:`list` of :class:`bytes`
        """
        ...
    def get_reason(self) -> bytes | None:
        """
        Get the reason of this revocation.

        :return: The reason, or ``None`` if there is none.
        :rtype: bytes or NoneType

        .. seealso::

            :meth:`all_reasons`, which gives you a list of all supported
            reasons this method might return.
        """
        ...
    def get_rev_date(self) -> bytes:
        """
        Get the revocation timestamp.

        :return: The timestamp of the revocation, as ASN.1 TIME.
        :rtype: bytes
        """
        ...
    def get_serial(self) -> bytes:
        """
        Get the serial number.

        The serial number is formatted as a hexadecimal number encoded in
        ASCII.

        :return: The serial number.
        :rtype: bytes
        """
        ...
    def set_reason(self, reason: bytes | None) -> None:
        """
        Set the reason of this revocation.

        If :data:`reason` is ``None``, delete the reason instead.

        :param reason: The reason string.
        :type reason: :class:`bytes` or :class:`NoneType`

        :return: ``None``

        .. seealso::

            :meth:`all_reasons`, which gives you a list of all supported
            reasons which you might pass to this method.
        """
        ...
    def set_rev_date(self, when: bytes) -> None:
        """
        Set the revocation timestamp.

        :param bytes when: The timestamp of the revocation,
            as ASN.1 TIME.
        :return: ``None``
        """
        ...
    def set_serial(self, hex_str: bytes) -> None:
        """
        Set the serial number.

        The serial number is formatted as a hexadecimal number encoded in
        ASCII.

        :param bytes hex_str: The new serial number.

        :return: ``None``
        """
        ...

@deprecated("CRL support in pyOpenSSL is deprecated. You should use the APIs in cryptography.")
class CRL:
    """A certificate revocation list."""
    def __init__(self) -> None: ...
    def add_revoked(self, revoked: Revoked) -> None:
        """
        Add a revoked (by value not reference) to the CRL structure

        This revocation will be added by value, not by reference. That
        means it's okay to mutate it after adding: it won't affect
        this CRL.

        :param Revoked revoked: The new revocation.
        :return: ``None``
        """
        ...
    def export(self, cert: X509, key: PKey, type: int = 1, days: int = 100, digest: bytes = ...) -> bytes:
        """
        Export the CRL as a string.

        :param X509 cert: The certificate used to sign the CRL.
        :param PKey key: The key used to sign the CRL.
        :param int type: The export format, either :data:`FILETYPE_PEM`,
            :data:`FILETYPE_ASN1`, or :data:`FILETYPE_TEXT`.
        :param int days: The number of days until the next update of this CRL.
        :param bytes digest: The name of the message digest to use (eg
            ``b"sha256"``).
        :rtype: bytes
        """
        ...
    @classmethod
    def from_cryptography(cls, crypto_crl: CertificateRevocationList) -> CRL:
        """
        Construct based on a ``cryptography`` *crypto_crl*.

        :param crypto_crl: A ``cryptography`` certificate revocation list
        :type crypto_crl: ``cryptography.x509.CertificateRevocationList``

        :rtype: CRL

        .. versionadded:: 17.1.0
        """
        ...
    def get_issuer(self) -> X509Name:
        """
        Get the CRL's issuer.

        .. versionadded:: 16.1.0

        :rtype: X509Name
        """
        ...
    def get_revoked(self) -> tuple[Revoked, ...]:
        """
        Return the revocations in this certificate revocation list.

        These revocations will be provided by value, not by reference.
        That means it's okay to mutate them: it won't affect this CRL.

        :return: The revocations in this CRL.
        :rtype: :class:`tuple` of :class:`Revocation`
        """
        ...
    def set_lastUpdate(self, when: bytes) -> None:
        """
        Set when the CRL was last updated.

        The timestamp is formatted as an ASN.1 TIME::

            YYYYMMDDhhmmssZ

        .. versionadded:: 16.1.0

        :param bytes when: A timestamp string.
        :return: ``None``
        """
        ...
    def set_nextUpdate(self, when: bytes) -> None:
        """
        Set when the CRL will next be updated.

        The timestamp is formatted as an ASN.1 TIME::

            YYYYMMDDhhmmssZ

        .. versionadded:: 16.1.0

        :param bytes when: A timestamp string.
        :return: ``None``
        """
        ...
    def set_version(self, version: int) -> None:
        """
        Set the CRL version.

        .. versionadded:: 16.1.0

        :param int version: The version of the CRL.
        :return: ``None``
        """
        ...
    def sign(self, issuer_cert: X509, issuer_key: PKey, digest: bytes) -> None:
        """
        Sign the CRL.

        Signing a CRL enables clients to associate the CRL itself with an
        issuer. Before a CRL is meaningful to other OpenSSL functions, it must
        be signed by an issuer.

        This method implicitly sets the issuer's name based on the issuer
        certificate and private key used to sign the CRL.

        .. versionadded:: 16.1.0

        :param X509 issuer_cert: The issuer's certificate.
        :param PKey issuer_key: The issuer's private key.
        :param bytes digest: The digest method to sign the CRL with.
        """
        ...
    def to_cryptography(self) -> CertificateRevocationList:
        """
        Export as a ``cryptography`` CRL.

        :rtype: ``cryptography.x509.CertificateRevocationList``

        .. versionadded:: 17.1.0
        """
        ...

class X509Store:
    """
    An X.509 store.

    An X.509 store is used to describe a context in which to verify a
    certificate. A description of a context may include a set of certificates
    to trust, a set of certificate revocation lists, verification flags and
    more.

    An X.509 store, being only a description, cannot be used by itself to
    verify a certificate. To carry out the actual verification process, see
    :class:`X509StoreContext`.
    """
    def __init__(self) -> None: ...
    def add_cert(self, cert: X509) -> None:
        """
        Adds a trusted certificate to this store.

        Adding a certificate with this method adds this certificate as a
        *trusted* certificate.

        :param X509 cert: The certificate to add to this store.

        :raises TypeError: If the certificate is not an :class:`X509`.

        :raises OpenSSL.crypto.Error: If OpenSSL was unhappy with your
            certificate.

        :return: ``None`` if the certificate was added successfully.
        """
        ...
    def add_crl(self, crl: CRL | CertificateRevocationList) -> None:
        """
        Add a certificate revocation list to this store.

        The certificate revocation lists added to a store will only be used if
        the associated flags are configured to check certificate revocation
        lists.

        .. versionadded:: 16.1.0

        :param crl: The certificate revocation list to add to this store.
        :type crl: ``Union[CRL, cryptography.x509.CertificateRevocationList]``
        :return: ``None`` if the certificate revocation list was added
            successfully.
        """
        ...
    def load_locations(self, cafile: StrOrBytesPath, capath: StrOrBytesPath | None = None) -> None:
        """
        Let X509Store know where we can find trusted certificates for the
        certificate chain.  Note that the certificates have to be in PEM
        format.

        If *capath* is passed, it must be a directory prepared using the
        ``c_rehash`` tool included with OpenSSL.  Either, but not both, of
        *cafile* or *capath* may be ``None``.

        .. note::

          Both *cafile* and *capath* may be set simultaneously.

          Call this method multiple times to add more than one location.
          For example, CA certificates, and certificate revocation list bundles
          may be passed in *cafile* in subsequent calls to this method.

        .. versionadded:: 20.0

        :param cafile: In which file we can find the certificates (``bytes`` or
                       ``unicode``).
        :param capath: In which directory we can find the certificates
                       (``bytes`` or ``unicode``).

        :return: ``None`` if the locations were set successfully.

        :raises OpenSSL.crypto.Error: If both *cafile* and *capath* is ``None``
            or the locations could not be set for any reason.
        """
        ...
    def set_flags(self, flags: int) -> None:
        """
        Set verification flags to this store.

        Verification flags can be combined by oring them together.

        .. note::

          Setting a verification flag sometimes requires clients to add
          additional information to the store, otherwise a suitable error will
          be raised.

          For example, in setting flags to enable CRL checking a
          suitable CRL must be added to the store otherwise an error will be
          raised.

        .. versionadded:: 16.1.0

        :param int flags: The verification flags to set on this store.
            See :class:`X509StoreFlags` for available constants.
        :return: ``None`` if the verification flags were successfully set.
        """
        ...
    def set_time(self, vfy_time: datetime) -> None:
        """
        Set the time against which the certificates are verified.

        Normally the current time is used.

        .. note::

          For example, you can determine if a certificate was valid at a given
          time.

        .. versionadded:: 17.0.0

        :param datetime vfy_time: The verification time to set on this store.
        :return: ``None`` if the verification time was successfully set.
        """
        ...

class X509StoreContext:
    """
    An X.509 store context.

    An X.509 store context is used to carry out the actual verification process
    of a certificate in a described context. For describing such a context, see
    :class:`X509Store`.

    :param X509Store store: The certificates which will be trusted for the
        purposes of any verifications.
    :param X509 certificate: The certificate to be verified.
    :param chain: List of untrusted certificates that may be used for building
        the certificate chain. May be ``None``.
    :type chain: :class:`list` of :class:`X509`
    """
    def __init__(self, store: X509Store, certificate: X509, chain: Sequence[X509] | None = None) -> None: ...
    def get_verified_chain(self) -> list[X509]:
        """
        Verify a certificate in a context and return the complete validated
        chain.

        :raises X509StoreContextError: If an error occurred when validating a
          certificate in the context. Sets ``certificate`` attribute to
          indicate which certificate caused the error.

        .. versionadded:: 20.0
        """
        ...
    def set_store(self, store: X509Store) -> None:
        """
        Set the context's X.509 store.

        .. versionadded:: 0.15

        :param X509Store store: The store description which will be used for
            the purposes of any *future* verifications.
        """
        ...
    def verify_certificate(self) -> None:
        """
        Verify a certificate in a context.

        .. versionadded:: 0.15

        :raises X509StoreContextError: If an error occurred when validating a
          certificate in the context. Sets ``certificate`` attribute to
          indicate which certificate caused the error.
        """
        ...

class X509StoreContextError(Exception):
    """
    An exception raised when an error occurred while verifying a certificate
    using `OpenSSL.X509StoreContext.verify_certificate`.

    :ivar certificate: The certificate which caused verificate failure.
    :type certificate: :class:`X509`
    """
    errors: list[Any]
    certificate: X509
    def __init__(self, message: str, errors: list[Any], certificate: X509) -> None: ...

class X509StoreFlags:
    """
    Flags for X509 verification, used to change the behavior of
    :class:`X509Store`.

    See `OpenSSL Verification Flags`_ for details.

    .. _OpenSSL Verification Flags:
        https://www.openssl.org/docs/manmaster/man3/X509_VERIFY_PARAM_set_flags.html
    """
    CRL_CHECK: int
    CRL_CHECK_ALL: int
    IGNORE_CRITICAL: int
    X509_STRICT: int
    ALLOW_PROXY_CERTS: int
    POLICY_CHECK: int
    EXPLICIT_POLICY: int
    INHIBIT_MAP: int
    NOTIFY_POLICY: int
    CHECK_SS_SIGNATURE: int
    CB_ISSUER_CHECK: int
    PARTIAL_CHAIN: int

def get_elliptic_curves() -> set[_EllipticCurve]:
    """
    Return a set of objects representing the elliptic curves supported in the
    OpenSSL build in use.

    The curve objects have a :py:class:`unicode` ``name`` attribute by which
    they identify themselves.

    The curve objects are useful as values for the argument accepted by
    :py:meth:`Context.set_tmp_ecdh` to specify which elliptical curve should be
    used for ECDHE key exchange.
    """
    ...
def get_elliptic_curve(name: str) -> _EllipticCurve:
    """
    Return a single curve object selected by name.

    See :py:func:`get_elliptic_curves` for information about curve objects.

    :param name: The OpenSSL short name identifying the curve object to
        retrieve.
    :type name: :py:class:`unicode`

    If the named curve is not supported then :py:class:`ValueError` is raised.
    """
    ...
def dump_certificate(type: int, cert: X509) -> bytes:
    """
    Dump the certificate *cert* into a buffer string encoded with the type
    *type*.

    :param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1, or
        FILETYPE_TEXT)
    :param cert: The certificate to dump
    :return: The buffer with the dumped certificate in
    """
    ...
def load_certificate(type: int, buffer: bytes) -> X509:
    """
    Load a certificate (X509) from the string *buffer* encoded with the
    type *type*.

    :param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)

    :param bytes buffer: The buffer the certificate is stored in

    :return: The X509 object
    """
    ...
def dump_certificate_request(type: int, req: X509Req) -> bytes:
    """
    Dump the certificate request *req* into a buffer string encoded with the
    type *type*.

    :param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    :param req: The certificate request to dump
    :return: The buffer with the dumped certificate request in
    """
    ...
def load_certificate_request(type: int, buffer: bytes) -> X509Req:
    """
    Load a certificate request (X509Req) from the string *buffer* encoded with
    the type *type*.

    :param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    :param buffer: The buffer the certificate request is stored in
    :return: The X509Req object
    """
    ...
def dump_privatekey(
    type: int, pkey: PKey, cipher: str | None = None, passphrase: bytes | Callable[[], bytes] | None = None
) -> bytes:
    """
    Dump the private key *pkey* into a buffer string encoded with the type
    *type*.  Optionally (if *type* is :const:`FILETYPE_PEM`) encrypting it
    using *cipher* and *passphrase*.

    :param type: The file type (one of :const:`FILETYPE_PEM`,
        :const:`FILETYPE_ASN1`, or :const:`FILETYPE_TEXT`)
    :param PKey pkey: The PKey to dump
    :param cipher: (optional) if encrypted PEM format, the cipher to use
    :param passphrase: (optional) if encrypted PEM format, this can be either
        the passphrase to use, or a callback for providing the passphrase.

    :return: The buffer with the dumped key in
    :rtype: bytes
    """
    ...
def load_privatekey(type: int, buffer: str | bytes, passphrase: bytes | Callable[[], bytes] | None = None) -> PKey:
    """
    Load a private key (PKey) from the string *buffer* encoded with the type
    *type*.

    :param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    :param buffer: The buffer the key is stored in
    :param passphrase: (optional) if encrypted PEM format, this can be
                       either the passphrase to use, or a callback for
                       providing the passphrase.

    :return: The PKey object
    """
    ...
def dump_publickey(type: int, pkey: PKey) -> bytes:
    """
    Dump a public key to a buffer.

    :param type: The file type (one of :data:`FILETYPE_PEM` or
        :data:`FILETYPE_ASN1`).
    :param PKey pkey: The public key to dump
    :return: The buffer with the dumped key in it.
    :rtype: bytes
    """
    ...
def load_publickey(type: int, buffer: str | bytes) -> PKey:
    """
    Load a public key from a buffer.

    :param type: The file type (one of :data:`FILETYPE_PEM`,
        :data:`FILETYPE_ASN1`).
    :param buffer: The buffer the key is stored in.
    :type buffer: A Python string object, either unicode or bytestring.
    :return: The PKey object.
    :rtype: :class:`PKey`
    """
    ...
@deprecated("sign() is deprecated. Use the equivalent APIs in cryptography.")
def sign(pkey: PKey, data: str | bytes, digest: str) -> bytes:
    """
    Sign a data string using the given key and message digest.

    :param pkey: PKey to sign with
    :param data: data to be signed
    :param digest: message digest to use
    :return: signature

    .. versionadded:: 0.11
    """
    ...
@deprecated("verify() is deprecated. Use the equivalent APIs in cryptography.")
def verify(cert: X509, signature: bytes, data: str | bytes, digest: str) -> None:
    """
    Verify the signature for a data string.

    :param cert: signing certificate (X509 object) corresponding to the
        private key which generated the signature.
    :param signature: signature returned by sign function
    :param data: data to be verified
    :param digest: message digest to use
    :return: ``None`` if the signature is correct, raise exception otherwise.

    .. versionadded:: 0.11
    """
    ...
@deprecated("CRL support in pyOpenSSL is deprecated. You should use the APIs in cryptography.")
def dump_crl(type: int, crl: CRL) -> bytes:
    """
    Dump a certificate revocation list to a buffer.

    :param type: The file type (one of ``FILETYPE_PEM``, ``FILETYPE_ASN1``, or
        ``FILETYPE_TEXT``).
    :param CRL crl: The CRL to dump.

    :return: The buffer with the CRL.
    :rtype: bytes
    """
    ...
@deprecated("CRL support in pyOpenSSL is deprecated. You should use the APIs in cryptography.")
def load_crl(type: int, buffer: str | bytes) -> CRL:
    """
    Load Certificate Revocation List (CRL) data from a string *buffer*.
    *buffer* encoded with the type *type*.

    :param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    :param buffer: The buffer the CRL is stored in

    :return: The CRL object
    """
    ...
