"""
Deprecated from html5lib 1.1.

See `here <https://github.com/html5lib/html5lib-python/issues/443>`_ for
information about its deprecation; `Bleach <https://github.com/mozilla/bleach>`_
is recommended as a replacement. Please let us know in the aforementioned issue
if Bleach is unsuitable for your needs.
"""

from typing import Any

from . import base

class Filter(base.Filter):
    """Sanitizes token stream of XHTML+MathML+SVG and of inline style attributes"""
    allowed_elements: Any
    allowed_attributes: Any
    allowed_css_properties: Any
    allowed_css_keywords: Any
    allowed_svg_properties: Any
    allowed_protocols: Any
    allowed_content_types: Any
    attr_val_is_uri: Any
    svg_attr_val_allows_ref: Any
    svg_allow_local_href: Any
    def __init__(
        self,
        source,
        allowed_elements=...,
        allowed_attributes=...,
        allowed_css_properties=...,
        allowed_css_keywords=...,
        allowed_svg_properties=...,
        allowed_protocols=...,
        allowed_content_types=...,
        attr_val_is_uri=...,
        svg_attr_val_allows_ref=...,
        svg_allow_local_href=...,
    ) -> None:
        """
        Creates a Filter

        :arg allowed_elements: set of elements to allow--everything else will
            be escaped

        :arg allowed_attributes: set of attributes to allow in
            elements--everything else will be stripped

        :arg allowed_css_properties: set of CSS properties to allow--everything
            else will be stripped

        :arg allowed_css_keywords: set of CSS keywords to allow--everything
            else will be stripped

        :arg allowed_svg_properties: set of SVG properties to allow--everything
            else will be removed

        :arg allowed_protocols: set of allowed protocols for URIs

        :arg allowed_content_types: set of allowed content types for ``data`` URIs.

        :arg attr_val_is_uri: set of attributes that have URI values--values
            that have a scheme not listed in ``allowed_protocols`` are removed

        :arg svg_attr_val_allows_ref: set of SVG attributes that can have
            references

        :arg svg_allow_local_href: set of SVG elements that can have local
            hrefs--these are removed
        """
        ...
    def __iter__(self): ...
    def sanitize_token(self, token): ...
    def allowed_token(self, token): ...
    def disallowed_token(self, token): ...
    def sanitize_css(self, style): ...
