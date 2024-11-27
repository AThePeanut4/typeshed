from _typeshed import Incomplete
from ssl import SSLObject, SSLSocket
from typing import Literal

from cryptography.x509.base import Certificate
from OpenSSL.SSL import Connection

def ocsp_staple_verifier(con: Connection, ocsp_bytes: bytes, expected: bytes | None = None) -> Literal[True]:
    """
    An implemention of a function for set_ocsp_client_callback in PyOpenSSL.

    This function validates that the provide ocsp_bytes response is valid,
    and matches the expected, stapled responses.
    """
    ...

class OCSPVerifier:
    """
    A class to verify ssl sockets for RFC6960/RFC6961. This can be used
    when using direct validation of OCSP responses and certificate revocations.

    @see https://datatracker.ietf.org/doc/html/rfc6960
    @see https://datatracker.ietf.org/doc/html/rfc6961
    """
    SOCK: SSLObject | SSLSocket
    HOST: str
    PORT: int
    CA_CERTS: str | None
    def __init__(self, sock: SSLObject | SSLSocket, host: str, port: int, ca_certs: str | None = None) -> None: ...
    # cryptography.x509.general_name.GeneralName.value is typed as Any
    def components_from_socket(self) -> tuple[Certificate, Incomplete | None, Incomplete]:
        """
        This function returns the certificate, primary issuer, and primary ocsp
        server in the chain for a socket already wrapped with ssl.
        """
        ...
    def components_from_direct_connection(self) -> tuple[Certificate, Incomplete | None, Incomplete]:
        """
        Return the certificate, primary issuer, and primary ocsp server
        from the host defined by the socket. This is useful in cases where
        different certificates are occasionally presented.
        """
        ...
    def build_certificate_url(self, server: str, cert: Certificate, issuer_cert: Certificate) -> str:
        """Return the complete url to the ocsp"""
        ...
    def check_certificate(self, server: str, cert: Certificate, issuer_url: str | bytes) -> Literal[True]:
        """Checks the validitity of an ocsp server for an issuer"""
        ...
    def is_valid(self) -> Literal[True]:
        """
        Returns the validity of the certificate wrapping our socket.
        This first retrieves for validate the certificate, issuer_url,
        and ocsp_server for certificate validate. Then retrieves the
        issuer certificate from the issuer_url, and finally checks
        the validity of OCSP revocation status.
        """
        ...
