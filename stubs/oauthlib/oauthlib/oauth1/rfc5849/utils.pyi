"""
oauthlib.utils
~~~~~~~~~~~~~~

This module contains utility methods used by various parts of the OAuth
spec.
"""

UNICODE_ASCII_CHARACTER_SET: str

def filter_params(target):
    """
    Decorator which filters params to remove non-oauth_* parameters

    Assumes the decorated method takes a params dict or list of tuples as its
    first argument.
    """
    ...
def filter_oauth_params(params):
    """Removes all non oauth parameters from a dict or a list of params."""
    ...
def escape(u):
    """
    Escape a unicode string in an OAuth-compatible fashion.

    Per `section 3.6`_ of the spec.

    .. _`section 3.6`: https://tools.ietf.org/html/rfc5849#section-3.6
    """
    ...
def unescape(u): ...
def parse_keqv_list(l):
    """A unicode-safe version of urllib2.parse_keqv_list"""
    ...
def parse_http_list(u):
    """A unicode-safe version of urllib2.parse_http_list"""
    ...
def parse_authorization_header(authorization_header):
    """Parse an OAuth authorization header into a list of 2-tuples"""
    ...
