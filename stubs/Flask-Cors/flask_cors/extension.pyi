from collections.abc import Callable, Iterable
from datetime import timedelta
from logging import Logger
from typing import Any

import flask

LOG: Logger

class CORS:
    """
    Initializes Cross Origin Resource sharing for the application. The
    arguments are identical to `cross_origin`, with the addition of a
    `resources` parameter. The resources parameter defines a series of regular
    expressions for resource paths to match and optionally, the associated
    options to be applied to the particular resource. These options are
    identical to the arguments to `cross_origin`.

    The settings for CORS are determined in the following order

    1. Resource level settings (e.g when passed as a dictionary)
    2. Keyword argument settings
    3. App level configuration settings (e.g. CORS_*)
    4. Default settings

    Note: as it is possible for multiple regular expressions to match a
    resource path, the regular expressions are first sorted by length,
    from longest to shortest, in order to attempt to match the most
    specific regular expression. This allows the definition of a
    number of specific resource options, with a wildcard fallback
    for all other resources.

    :param resources:
        The series of regular expression and (optionally) associated CORS
        options to be applied to the given resource path.

        If the argument is a dictionary, it's keys must be regular expressions,
        and the values must be a dictionary of kwargs, identical to the kwargs
        of this function.

        If the argument is a list, it is expected to be a list of regular
        expressions, for which the app-wide configured options are applied.

        If the argument is a string, it is expected to be a regular expression
        for which the app-wide configured options are applied.

        Default : Match all and apply app-level configuration

    :type resources: dict, iterable or string

    :param origins:
        The origin, or list of origins to allow requests from.
        The origin(s) may be regular expressions, case-sensitive strings,
        or else an asterisk.

        ..  note::

            origins must include the schema and the port (if not port 80),
            e.g.,
            `CORS(app, origins=["http://localhost:8000", "https://example.com"])`.

        Default : '*'
    :type origins: list, string or regex

    :param methods:
        The method or list of methods which the allowed origins are allowed to
        access for non-simple requests.

        Default : [GET, HEAD, POST, OPTIONS, PUT, PATCH, DELETE]
    :type methods: list or string

    :param expose_headers:
        The header or list which are safe to expose to the API of a CORS API
        specification.

        Default : None
    :type expose_headers: list or string

    :param allow_headers:
        The header or list of header field names which can be used when this
        resource is accessed by allowed origins. The header(s) may be regular
        expressions, case-sensitive strings, or else an asterisk.

        Default : '*', allow all headers
    :type allow_headers: list, string or regex

    :param supports_credentials:
        Allows users to make authenticated requests. If true, injects the
        `Access-Control-Allow-Credentials` header in responses. This allows
        cookies and credentials to be submitted across domains.

        :note: This option cannot be used in conjunction with a '*' origin

        Default : False
    :type supports_credentials: bool

    :param max_age:
        The maximum time for which this CORS request maybe cached. This value
        is set as the `Access-Control-Max-Age` header.

        Default : None
    :type max_age: timedelta, integer, string or None

    :param send_wildcard: If True, and the origins parameter is `*`, a wildcard
        `Access-Control-Allow-Origin` header is sent, rather than the
        request's `Origin` header.

        Default : False
    :type send_wildcard: bool

    :param vary_header:
        If True, the header Vary: Origin will be returned as per the W3
        implementation guidelines.

        Setting this header when the `Access-Control-Allow-Origin` is
        dynamically generated (e.g. when there is more than one allowed
        origin, and an Origin than '*' is returned) informs CDNs and other
        caches that the CORS headers are dynamic, and cannot be cached.

        If False, the Vary header will never be injected or altered.

        Default : True
    :type vary_header: bool

    :param allow_private_network:
        If True, the response header `Access-Control-Allow-Private-Network`
        will be set with the value 'true' whenever the request header
        `Access-Control-Request-Private-Network` has a value 'true'.

        If False, the response header `Access-Control-Allow-Private-Network`
        will be set with the value 'false' whenever the request header
        `Access-Control-Request-Private-Network` has a value of 'true'.

        If the request header `Access-Control-Request-Private-Network` is
        not present or has a value other than 'true', the response header
        `Access-Control-Allow-Private-Network` will not be set.

        Default : True
    :type allow_private_network: bool
    """
    def __init__(
        self,
        app: flask.Flask | flask.Blueprint | None = None,
        *,
        resources: dict[str, dict[str, Any]] | list[str] | str | None = ...,
        origins: str | list[str] | None = ...,
        methods: str | list[str] | None = ...,
        expose_headers: str | list[str] | None = ...,
        allow_headers: str | list[str] | None = ...,
        supports_credentials: bool | None = ...,
        max_age: timedelta | int | str | None = ...,
        send_wildcard: bool | None = ...,
        vary_header: bool | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def init_app(
        self,
        app: flask.Flask,
        *,
        resources: dict[str, dict[str, Any]] | list[str] | str = ...,
        origins: str | list[str] = ...,
        methods: str | list[str] = ...,
        expose_headers: str | list[str] = ...,
        allow_headers: str | list[str] = ...,
        supports_credentials: bool = ...,
        max_age: timedelta | int | str | None = ...,
        send_wildcard: bool = ...,
        vary_header: bool = ...,
        **kwargs: Any,
    ) -> None: ...

def make_after_request_function(resources: Iterable[tuple[str, dict[str, Any]]]) -> Callable[..., Any]: ...
