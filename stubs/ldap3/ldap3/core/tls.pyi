""""""

from _typeshed import Incomplete

use_ssl_context: bool

class Tls:
    """
    tls/ssl configuration for Server object
    Starting from python 2.7.9 and python 3.4 uses the SSLContext object
    that tries to read the CAs defined at system level
    ca_certs_path and ca_certs_data are valid only when using SSLContext
    local_private_key_password is valid only when using SSLContext
    ssl_options is valid only when using SSLContext
    sni is the server name for Server Name Indication (when available)
    """
    ssl_options: Incomplete
    validate: Incomplete
    ca_certs_file: Incomplete
    ca_certs_path: Incomplete
    ca_certs_data: Incomplete
    private_key_password: Incomplete
    version: Incomplete
    private_key_file: Incomplete
    certificate_file: Incomplete
    valid_names: Incomplete
    ciphers: Incomplete
    sni: Incomplete
    def __init__(
        self,
        local_private_key_file=None,
        local_certificate_file=None,
        validate=...,
        version=None,
        ssl_options=None,
        ca_certs_file=None,
        valid_names=None,
        ca_certs_path=None,
        ca_certs_data=None,
        local_private_key_password=None,
        ciphers=None,
        sni=None,
    ) -> None: ...
    def wrap_socket(self, connection, do_handshake: bool = False) -> None:
        """Adds TLS to the connection socket"""
        ...
    def start_tls(self, connection): ...

def check_hostname(sock, server_name, additional_names) -> None: ...
