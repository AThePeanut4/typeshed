"""
oauthlib.parameters
~~~~~~~~~~~~~~~~~~~

This module contains methods related to `section 3.5`_ of the OAuth 1.0a spec.

.. _`section 3.5`: https://tools.ietf.org/html/rfc5849#section-3.5
"""

from _typeshed import Incomplete

def prepare_headers(params, headers: Incomplete | None = ..., realm: Incomplete | None = ...): ...
def prepare_form_encoded_body(oauth_params, body): ...
def prepare_request_uri_query(oauth_params, uri): ...
