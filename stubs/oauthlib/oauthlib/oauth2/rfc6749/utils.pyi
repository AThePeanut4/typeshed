"""
oauthlib.utils
~~~~~~~~~~~~~~

This module contains utility methods used by various parts of the OAuth 2 spec.
"""

def list_to_scope(scope):
    """Convert a list of scopes to a space separated string."""
    ...
def scope_to_list(scope):
    """Convert a space separated string to a list of scopes."""
    ...
def params_from_uri(uri): ...
def host_from_uri(uri):
    """
    Extract hostname and port from URI.

    Will use default port for HTTP and HTTPS if none is present in the URI.
    """
    ...
def escape(u):
    """
    Escape a string in an OAuth-compatible fashion.

    TODO: verify whether this can in fact be used for OAuth 2
    """
    ...
def generate_age(issue_time):
    """Generate a age parameter for MAC authentication draft 00."""
    ...
def is_secure_transport(uri):
    """Check if the uri is over ssl."""
    ...
