"""
Parse four ``Accept*`` headers used in server-driven content negotiation.

The four headers are ``Accept``, ``Accept-Charset``, ``Accept-Encoding`` and
``Accept-Language``.
"""

from _typeshed import SupportsItems
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any, Literal, NamedTuple, Protocol, TypeVar, overload
from typing_extensions import Self, TypeAlias

from webob._types import AsymmetricPropertyWithDelete

_T = TypeVar("_T")
_ListOrTuple: TypeAlias = list[_T] | tuple[_T, ...]
_ParsedAccept: TypeAlias = tuple[str, float, list[tuple[str, str]], list[str | tuple[str, str]]]

class _SupportsStr(Protocol):
    def __str__(self) -> str: ...  # noqa: Y029

_AnyAcceptHeader: TypeAlias = AcceptValidHeader | AcceptInvalidHeader | AcceptNoHeader
_AnyAcceptCharsetHeader: TypeAlias = AcceptCharsetValidHeader | AcceptCharsetInvalidHeader | AcceptCharsetNoHeader
_AnyAcceptEncodingHeader: TypeAlias = AcceptEncodingValidHeader | AcceptEncodingInvalidHeader | AcceptEncodingNoHeader
_AnyAcceptLanguageHeader: TypeAlias = AcceptLanguageValidHeader | AcceptLanguageInvalidHeader | AcceptLanguageNoHeader

_AcceptProperty: TypeAlias = AsymmetricPropertyWithDelete[
    _AnyAcceptHeader,
    (
        _AnyAcceptHeader
        | SupportsItems[str, float | tuple[float, str]]
        | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
        | _SupportsStr
        | str
        | None
    ),
]
_AcceptCharsetProperty: TypeAlias = AsymmetricPropertyWithDelete[
    _AnyAcceptCharsetHeader,
    (
        _AnyAcceptCharsetHeader
        | SupportsItems[str, float]
        | _ListOrTuple[str | tuple[str, float] | list[Any]]
        | _SupportsStr
        | str
        | None
    ),
]
_AcceptEncodingProperty: TypeAlias = AsymmetricPropertyWithDelete[
    _AnyAcceptEncodingHeader,
    (
        _AnyAcceptEncodingHeader
        | SupportsItems[str, float]
        | _ListOrTuple[str | tuple[str, float] | list[Any]]
        | _SupportsStr
        | str
        | None
    ),
]
_AcceptLanguageProperty: TypeAlias = AsymmetricPropertyWithDelete[
    _AnyAcceptLanguageHeader,
    (
        _AnyAcceptLanguageHeader
        | SupportsItems[str, float]
        | _ListOrTuple[str | tuple[str, float] | list[Any]]
        | _SupportsStr
        | str
        | None
    ),
]

class AcceptOffer(NamedTuple):
    """
    A pre-parsed offer tuple represeting a value in the format
    ``type/subtype;param0=value0;param1=value1``.

    :ivar type: The media type's root category.
    :ivar subtype: The media type's subtype.
    :ivar params: A tuple of 2-tuples containing parameter names and values.
    """
    type: str
    subtype: str
    params: tuple[tuple[str, str], ...]

class Accept:
    """
    Represent an ``Accept`` header.

    Base class for :class:`AcceptValidHeader`, :class:`AcceptNoHeader`, and
    :class:`AcceptInvalidHeader`.
    """
    @classmethod
    def parse(cls, value: str) -> Iterator[_ParsedAccept]:
        r"""
        Parse an ``Accept`` header.

        :param value: (``str``) header value
        :return: If `value` is a valid ``Accept`` header, returns an iterator
                 of (*media_range*, *qvalue*, *media_type_params*,
                 *extension_params*) tuples, as parsed from the header from
                 left to right.

                 | *media_range* is the media range, including any media type
                   parameters. The media range is returned in a canonicalised
                   form (except the case of the characters are unchanged):
                   unnecessary spaces around the semicolons before media type
                   parameters are removed; the parameter values are returned in
                   a form where only the '``\``' and '``"``' characters are
                   escaped, and the values are quoted with double quotes only
                   if they need to be quoted.

                 | *qvalue* is the quality value of the media range.

                 | *media_type_params* is the media type parameters, as a list
                   of (parameter name, value) tuples.

                 | *extension_params* is the extension parameters, as a list
                   where each item is either a parameter string or a (parameter
                   name, value) tuple.
        :raises ValueError: if `value` is an invalid header
        """
        ...
    @classmethod
    def parse_offer(cls, offer: str | AcceptOffer) -> AcceptOffer:
        """
        Parse an offer into its component parts.

        :param offer: A media type or range in the format
                      ``type/subtype[;params]``.
        :return: A named tuple containing ``(*type*, *subtype*, *params*)``.

                 | *params* is a list containing ``(*parameter name*, *value*)``
                   values.

        :raises ValueError: If the offer does not match the required format.
        """
        ...

class AcceptValidHeader(Accept):
    """
    Represent a valid ``Accept`` header.

    A valid header is one that conforms to :rfc:`RFC 7231, section 5.3.2
    <7231#section-5.3.2>`.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptValidHeader.__add__`).
    """
    @property
    def header_value(self) -> str:
        """(``str`` or ``None``) The header value."""
        ...
    @property
    def parsed(self) -> list[_ParsedAccept]: ...
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    def __add__(
        self,
        other: (
            _AnyAcceptHeader
            | SupportsItems[str, float | tuple[float, str]]
            | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def __bool__(self) -> Literal[True]: ...
    def __contains__(self, offer: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __radd__(
        self,
        other: (
            _AnyAcceptHeader
            | SupportsItems[str, float | tuple[float, str]]
            | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def accept_html(self) -> bool: ...
    @property
    def accepts_html(self) -> bool: ...
    def acceptable_offers(self, offers: Sequence[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None:
        """
        Return the best match from the sequence of media type `offers`.

        .. warning::

           This is currently maintained for backward compatibility, and will be
           deprecated in the future.

           :meth:`AcceptValidHeader.best_match` uses its own algorithm (one not
           specified in :rfc:`RFC 7231 <7231>`) to determine what is a best
           match. The algorithm has many issues, and does not conform to
           :rfc:`RFC 7231 <7231>`.

        Each media type in `offers` is checked against each non-``q=0`` range
        in the header. If the two are a match according to WebOb's old
        criterion for a match, the quality value of the match is the qvalue of
        the media range from the header multiplied by the server quality value
        of the offer (if the server quality value is not supplied, it is 1).

        The offer in the match with the highest quality value is the best
        match. If there is more than one match with the highest qvalue, the
        match where the media range has a lower number of '*'s is the best
        match. If the two have the same number of '*'s, the one that shows up
        first in `offers` is the best match.

        :param offers: (iterable)

                       | Each item in the iterable may be a ``str`` media type,
                         or a (media type, server quality value) ``tuple`` or
                         ``list``. (The two may be mixed in the iterable.)

        :param default_match: (optional, any type) the value to be returned if
                              there is no match

        :return: (``str``, or the type of `default_match`)

                 | The offer that is the best match. If there is no match, the
                   value of `default_match` is returned.

        This uses the old criterion of a match in
        :meth:`AcceptValidHeader._old_match`, which is not as specified in
        :rfc:`RFC 7231, section 5.3.2 <7231#section-5.3.2>`. It does not
        correctly take into account media type parameters:

            >>> instance = AcceptValidHeader('text/html')
            >>> instance.best_match(offers=['text/html;p=1']) is None
            True

        or media ranges with ``q=0`` in the header::

            >>> instance = AcceptValidHeader('text/*, text/html;q=0')
            >>> instance.best_match(offers=['text/html'])
            'text/html'

            >>> instance = AcceptValidHeader('text/html;q=0, */*')
            >>> instance.best_match(offers=['text/html'])
            'text/html'

        (See the docstring for :meth:`AcceptValidHeader._old_match` for other
        problems with the old criterion for matching.)

        Another issue is that this method considers the best matching range for
        an offer to be the matching range with the highest quality value,
        (where quality values are tied, the most specific media range is
        chosen); whereas :rfc:`RFC 7231, section 5.3.2 <7231#section-5.3.2>`
        specifies that we should consider the best matching range for a media
        type offer to be the most specific matching range.::

            >>> instance = AcceptValidHeader('text/html;q=0.5, text/*')
            >>> instance.best_match(offers=['text/html', 'text/plain'])
            'text/html'
        """
        ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str:
        """
        Return the best match from the sequence of media type `offers`.

        .. warning::

           This is currently maintained for backward compatibility, and will be
           deprecated in the future.

           :meth:`AcceptValidHeader.best_match` uses its own algorithm (one not
           specified in :rfc:`RFC 7231 <7231>`) to determine what is a best
           match. The algorithm has many issues, and does not conform to
           :rfc:`RFC 7231 <7231>`.

        Each media type in `offers` is checked against each non-``q=0`` range
        in the header. If the two are a match according to WebOb's old
        criterion for a match, the quality value of the match is the qvalue of
        the media range from the header multiplied by the server quality value
        of the offer (if the server quality value is not supplied, it is 1).

        The offer in the match with the highest quality value is the best
        match. If there is more than one match with the highest qvalue, the
        match where the media range has a lower number of '*'s is the best
        match. If the two have the same number of '*'s, the one that shows up
        first in `offers` is the best match.

        :param offers: (iterable)

                       | Each item in the iterable may be a ``str`` media type,
                         or a (media type, server quality value) ``tuple`` or
                         ``list``. (The two may be mixed in the iterable.)

        :param default_match: (optional, any type) the value to be returned if
                              there is no match

        :return: (``str``, or the type of `default_match`)

                 | The offer that is the best match. If there is no match, the
                   value of `default_match` is returned.

        This uses the old criterion of a match in
        :meth:`AcceptValidHeader._old_match`, which is not as specified in
        :rfc:`RFC 7231, section 5.3.2 <7231#section-5.3.2>`. It does not
        correctly take into account media type parameters:

            >>> instance = AcceptValidHeader('text/html')
            >>> instance.best_match(offers=['text/html;p=1']) is None
            True

        or media ranges with ``q=0`` in the header::

            >>> instance = AcceptValidHeader('text/*, text/html;q=0')
            >>> instance.best_match(offers=['text/html'])
            'text/html'

            >>> instance = AcceptValidHeader('text/html;q=0, */*')
            >>> instance.best_match(offers=['text/html'])
            'text/html'

        (See the docstring for :meth:`AcceptValidHeader._old_match` for other
        problems with the old criterion for matching.)

        Another issue is that this method considers the best matching range for
        an offer to be the matching range with the highest quality value,
        (where quality values are tied, the most specific media range is
        chosen); whereas :rfc:`RFC 7231, section 5.3.2 <7231#section-5.3.2>`
        specifies that we should consider the best matching range for a media
        type offer to be the most specific matching range.::

            >>> instance = AcceptValidHeader('text/html;q=0.5, text/*')
            >>> instance.best_match(offers=['text/html', 'text/plain'])
            'text/html'
        """
        ...
    def quality(self, offer: str) -> float | None:
        """
        Return quality value of given offer, or ``None`` if there is no match.

        .. warning::

           This is currently maintained for backward compatibility, and will be
           deprecated in the future.

        :param offer: (``str``) media type offer
        :return: (``float`` or ``None``)

                 | The highest quality value from the media range(s) that match
                   the `offer`, or ``None`` if there is no match.

        This uses the old criterion of a match in
        :meth:`AcceptValidHeader._old_match`, which is not as specified in
        :rfc:`RFC 7231, section 5.3.2 <7231#section-5.3.2>`. It does not
        correctly take into account media type parameters:

            >>> instance = AcceptValidHeader('text/html')
            >>> instance.quality('text/html;p=1') is None
            True

        or media ranges with ``q=0`` in the header::

            >>> instance = AcceptValidHeader('text/*, text/html;q=0')
            >>> instance.quality('text/html')
            1.0
            >>> AcceptValidHeader('text/html;q=0, */*').quality('text/html')
            1.0

        (See the docstring for :meth:`AcceptValidHeader._old_match` for other
        problems with the old criterion for matching.)

        Another issue is that this method considers the best matching range for
        an offer to be the matching range with the highest quality value,
        whereas :rfc:`RFC 7231, section 5.3.2 <7231#section-5.3.2>` specifies
        that we should consider the best matching range for a media type offer
        to be the most specific matching range.::

            >>> instance = AcceptValidHeader('text/html;q=0.5, text/*')
            >>> instance.quality('text/html')
            1.0
        """
        ...

class _AcceptInvalidOrNoHeader(Accept):
    def __bool__(self) -> Literal[False]: ...
    def __contains__(self, offer: str) -> Literal[True]: ...
    def __iter__(self) -> Iterator[str]: ...
    def accept_html(self) -> bool: ...
    @property
    def accepts_html(self) -> bool: ...
    def acceptable_offers(self, offers: Sequence[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None:
        """
        Return the best match from the sequence of language tag `offers`.

        This is the ``.best_match()`` method for when the header is invalid or
        not found in the request, corresponding to
        :meth:`AcceptValidHeader.best_match`.

        .. warning::

           This is currently maintained for backward compatibility, and will be
           deprecated in the future (see the documentation for
           :meth:`AcceptValidHeader.best_match`).

        When the header is invalid, or there is no `Accept` header in the
        request, all `offers` are considered acceptable, so the best match is
        the media type in `offers` with the highest server quality value (if
        the server quality value is not supplied for a media type, it is 1).

        If more than one media type in `offers` have the same highest server
        quality value, then the one that shows up first in `offers` is the best
        match.

        :param offers: (iterable)

                       | Each item in the iterable may be a ``str`` media type,
                         or a (media type, server quality value) ``tuple`` or
                         ``list``. (The two may be mixed in the iterable.)

        :param default_match: (optional, any type) the value to be returned if
                              `offers` is empty.

        :return: (``str``, or the type of `default_match`)

                 | The offer that has the highest server quality value.  If
                   `offers` is empty, the value of `default_match` is returned.
        """
        ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str:
        """
        Return the best match from the sequence of language tag `offers`.

        This is the ``.best_match()`` method for when the header is invalid or
        not found in the request, corresponding to
        :meth:`AcceptValidHeader.best_match`.

        .. warning::

           This is currently maintained for backward compatibility, and will be
           deprecated in the future (see the documentation for
           :meth:`AcceptValidHeader.best_match`).

        When the header is invalid, or there is no `Accept` header in the
        request, all `offers` are considered acceptable, so the best match is
        the media type in `offers` with the highest server quality value (if
        the server quality value is not supplied for a media type, it is 1).

        If more than one media type in `offers` have the same highest server
        quality value, then the one that shows up first in `offers` is the best
        match.

        :param offers: (iterable)

                       | Each item in the iterable may be a ``str`` media type,
                         or a (media type, server quality value) ``tuple`` or
                         ``list``. (The two may be mixed in the iterable.)

        :param default_match: (optional, any type) the value to be returned if
                              `offers` is empty.

        :return: (``str``, or the type of `default_match`)

                 | The offer that has the highest server quality value.  If
                   `offers` is empty, the value of `default_match` is returned.
        """
        ...
    def quality(self, offer: str) -> float:
        """
        Return quality value of given offer, or ``None`` if there is no match.

        This is the ``.quality()`` method for when the header is invalid or not
        found in the request, corresponding to
        :meth:`AcceptValidHeader.quality`.

        .. warning::

           This is currently maintained for backward compatibility, and will be
           deprecated in the future (see the documentation for
           :meth:`AcceptValidHeader.quality`).

        :param offer: (``str``) media type offer
        :return: (``float``) ``1.0``.

        When the ``Accept`` header is invalid or not in the request, all offers
        are equally acceptable, so 1.0 is always returned.
        """
        ...

class AcceptNoHeader(_AcceptInvalidOrNoHeader):
    """
    Represent when there is no ``Accept`` header in the request.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptNoHeader.__add__`).
    """
    @property
    def header_value(self) -> None: ...
    @property
    def parsed(self) -> None: ...
    def __init__(self) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __add__(self, other: AcceptValidHeader | Literal[""]) -> AcceptValidHeader: ...
    @overload
    def __add__(self, other: AcceptNoHeader | AcceptInvalidHeader | None) -> Self: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptHeader
            | SupportsItems[str, float | tuple[float, str]]
            | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptValidHeader: ...
    @overload
    def __radd__(self, other: AcceptValidHeader | Literal[""]) -> AcceptValidHeader: ...
    @overload
    def __radd__(self, other: AcceptNoHeader | AcceptInvalidHeader | None) -> Self: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptHeader
            | SupportsItems[str, float | tuple[float, str]]
            | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptValidHeader: ...

class AcceptInvalidHeader(_AcceptInvalidOrNoHeader):
    """
    Represent an invalid ``Accept`` header.

    An invalid header is one that does not conform to
    :rfc:`7231#section-5.3.2`.

    :rfc:`7231` does not provide any guidance on what should happen if the
    ``Accept`` header has an invalid value. This implementation disregards the
    header, and treats it as if there is no ``Accept`` header in the request.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptInvalidHeader.__add__`).
    """
    @property
    def header_value(self) -> str: ...
    @property
    def parsed(self) -> None: ...
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __add__(self, other: AcceptValidHeader | Literal[""]) -> AcceptValidHeader: ...
    @overload
    def __add__(self, other: AcceptInvalidHeader | AcceptNoHeader | None) -> AcceptNoHeader: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptHeader
            | SupportsItems[str, float | tuple[float, str]]
            | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptValidHeader | AcceptNoHeader: ...
    @overload
    def __radd__(self, other: AcceptValidHeader | Literal[""]) -> AcceptValidHeader: ...
    @overload
    def __radd__(self, other: AcceptInvalidHeader | AcceptNoHeader | None) -> AcceptNoHeader: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptHeader
            | SupportsItems[str, float | tuple[float, str]]
            | _ListOrTuple[str | tuple[str, float, str] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptValidHeader | AcceptNoHeader: ...

@overload
def create_accept_header(header_value: AcceptValidHeader | Literal[""]) -> AcceptValidHeader: ...
@overload
def create_accept_header(header_value: AcceptInvalidHeader) -> AcceptInvalidHeader: ...
@overload
def create_accept_header(header_value: None | AcceptNoHeader) -> AcceptNoHeader: ...
@overload
def create_accept_header(header_value: str) -> AcceptValidHeader | AcceptInvalidHeader: ...
@overload
def create_accept_header(header_value: _AnyAcceptHeader | str | None) -> _AnyAcceptHeader: ...
def accept_property() -> _AcceptProperty: ...

class AcceptCharset:
    """
    Represent an ``Accept-Charset`` header.

    Base class for :class:`AcceptCharsetValidHeader`,
    :class:`AcceptCharsetNoHeader`, and :class:`AcceptCharsetInvalidHeader`.
    """
    @classmethod
    def parse(cls, value: str) -> Iterator[tuple[str, float]]:
        """
        Parse an ``Accept-Charset`` header.

        :param value: (``str``) header value
        :return: If `value` is a valid ``Accept-Charset`` header, returns an
                 iterator of (charset, quality value) tuples, as parsed from
                 the header from left to right.
        :raises ValueError: if `value` is an invalid header
        """
        ...

class AcceptCharsetValidHeader(AcceptCharset):
    """
    Represent a valid ``Accept-Charset`` header.

    A valid header is one that conforms to :rfc:`RFC 7231, section 5.3.3
    <7231#section-5.3.3>`.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptCharsetValidHeader.__add__`).
    """
    @property
    def header_value(self) -> str:
        """(``str``) The header value."""
        ...
    @property
    def parsed(self) -> list[tuple[str, float]]: ...
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    def __add__(
        self,
        other: (
            _AnyAcceptCharsetHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def __bool__(self) -> Literal[True]: ...
    def __contains__(self, offer: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __radd__(
        self,
        other: (
            _AnyAcceptCharsetHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def acceptable_offers(self, offers: Sequence[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str: ...
    def quality(self, offer: str) -> float | None: ...

class _AcceptCharsetInvalidOrNoHeader(AcceptCharset):
    def __bool__(self) -> Literal[False]: ...
    def __contains__(self, offer: str) -> Literal[True]: ...
    def __iter__(self) -> Iterator[str]: ...
    def acceptable_offers(self, offers: Iterable[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str: ...
    def quality(self, offer: str) -> float | None: ...

class AcceptCharsetNoHeader(_AcceptCharsetInvalidOrNoHeader):
    """
    Represent when there is no ``Accept-Charset`` header in the request.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptCharsetNoHeader.__add__`).
    """
    @property
    def header_value(self) -> None: ...
    @property
    def parsed(self) -> None: ...
    def __init__(self) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __add__(self, other: AcceptCharsetValidHeader) -> AcceptCharsetValidHeader: ...
    @overload
    def __add__(self, other: AcceptCharsetInvalidHeader | AcceptCharsetNoHeader | Literal[""] | None) -> Self: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptCharsetHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptCharsetValidHeader: ...
    @overload
    def __radd__(self, other: AcceptCharsetValidHeader) -> AcceptCharsetValidHeader: ...
    @overload
    def __radd__(self, other: AcceptCharsetInvalidHeader | AcceptCharsetNoHeader | Literal[""] | None) -> Self: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptCharsetHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptCharsetValidHeader: ...

class AcceptCharsetInvalidHeader(_AcceptCharsetInvalidOrNoHeader):
    """
    Represent an invalid ``Accept-Charset`` header.

    An invalid header is one that does not conform to
    :rfc:`7231#section-5.3.3`. As specified in the RFC, an empty header is an
    invalid ``Accept-Charset`` header.

    :rfc:`7231` does not provide any guidance on what should happen if the
    ``Accept-Charset`` header has an invalid value. This implementation
    disregards the header, and treats it as if there is no ``Accept-Charset``
    header in the request.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptCharsetInvalidHeader.__add__`).
    """
    @property
    def header_value(self) -> str: ...
    @property
    def parsed(self) -> None: ...
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __add__(self, other: AcceptCharsetValidHeader) -> AcceptCharsetValidHeader: ...
    @overload
    def __add__(
        self, other: AcceptCharsetInvalidHeader | AcceptCharsetNoHeader | Literal[""] | None
    ) -> AcceptCharsetNoHeader: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptCharsetHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptCharsetValidHeader | AcceptCharsetNoHeader: ...
    @overload
    def __radd__(self, other: AcceptCharsetValidHeader) -> AcceptCharsetValidHeader: ...
    @overload
    def __radd__(
        self, other: AcceptCharsetInvalidHeader | AcceptCharsetNoHeader | Literal[""] | None
    ) -> AcceptCharsetNoHeader: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptCharsetHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptCharsetValidHeader | AcceptCharsetNoHeader: ...

@overload
def create_accept_charset_header(header_value: AcceptCharsetValidHeader | Literal[""]) -> AcceptCharsetValidHeader: ...
@overload
def create_accept_charset_header(header_value: AcceptCharsetInvalidHeader) -> AcceptCharsetInvalidHeader: ...
@overload
def create_accept_charset_header(header_value: AcceptCharsetNoHeader | None) -> AcceptCharsetNoHeader: ...
@overload
def create_accept_charset_header(header_value: str) -> AcceptCharsetValidHeader | AcceptCharsetInvalidHeader: ...
@overload
def create_accept_charset_header(header_value: _AnyAcceptCharsetHeader | str | None) -> _AnyAcceptCharsetHeader: ...
def accept_charset_property() -> _AcceptCharsetProperty: ...

class AcceptEncoding:
    """
    Represent an ``Accept-Encoding`` header.

    Base class for :class:`AcceptEncodingValidHeader`,
    :class:`AcceptEncodingNoHeader`, and :class:`AcceptEncodingInvalidHeader`.
    """
    @classmethod
    def parse(cls, value: str) -> Iterator[tuple[str, float]]:
        """
        Parse an ``Accept-Encoding`` header.

        :param value: (``str``) header value
        :return: If `value` is a valid ``Accept-Encoding`` header, returns an
                 iterator of (codings, quality value) tuples, as parsed from
                 the header from left to right.
        :raises ValueError: if `value` is an invalid header
        """
        ...

class AcceptEncodingValidHeader(AcceptEncoding):
    """
    Represent a valid ``Accept-Encoding`` header.

    A valid header is one that conforms to :rfc:`RFC 7231, section 5.3.4
    <7231#section-5.3.4>`.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptEncodingValidHeader.__add__`).
    """
    @property
    def header_value(self) -> str:
        """(``str`` or ``None``) The header value."""
        ...
    @property
    def parsed(self) -> list[tuple[str, float]]: ...
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    def __add__(
        self,
        other: (
            _AnyAcceptEncodingHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def __bool__(self) -> Literal[True]: ...
    def __contains__(self, offer: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __radd__(
        self,
        other: (
            _AnyAcceptEncodingHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def acceptable_offers(self, offers: Sequence[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str: ...
    def quality(self, offer: str) -> float | None: ...

class _AcceptEncodingInvalidOrNoHeader(AcceptEncoding):
    def __bool__(self) -> Literal[False]: ...
    def __contains__(self, offer: str) -> Literal[True]: ...
    def __iter__(self) -> Iterator[str]: ...
    def acceptable_offers(self, offers: Iterable[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str: ...
    def quality(self, offer: str) -> float | None: ...

class AcceptEncodingNoHeader(_AcceptEncodingInvalidOrNoHeader):
    """
    Represent when there is no ``Accept-Encoding`` header in the request.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptEncodingNoHeader.__add__`).
    """
    @property
    def header_value(self) -> None: ...
    @property
    def parsed(self) -> None: ...
    def __init__(self) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __add__(self, other: AcceptEncodingValidHeader | Literal[""]) -> AcceptEncodingValidHeader: ...
    @overload
    def __add__(self, other: AcceptEncodingInvalidHeader | AcceptEncodingNoHeader | None) -> Self: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptEncodingHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptEncodingValidHeader: ...
    @overload
    def __radd__(self, other: AcceptEncodingValidHeader | Literal[""]) -> AcceptEncodingValidHeader: ...
    @overload
    def __radd__(self, other: AcceptEncodingInvalidHeader | AcceptEncodingNoHeader | None) -> Self: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptEncodingHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptEncodingValidHeader: ...

class AcceptEncodingInvalidHeader(_AcceptEncodingInvalidOrNoHeader):
    """
    Represent an invalid ``Accept-Encoding`` header.

    An invalid header is one that does not conform to
    :rfc:`7231#section-5.3.4`.

    :rfc:`7231` does not provide any guidance on what should happen if the
    ``Accept-Encoding`` header has an invalid value. This implementation
    disregards the header, and treats it as if there is no ``Accept-Encoding``
    header in the request.

    This object should not be modified. To add to the header, we can use the
    addition operators (``+`` and ``+=``), which return a new object (see the
    docstring for :meth:`AcceptEncodingInvalidHeader.__add__`).
    """
    @property
    def header_value(self) -> str: ...
    @property
    def parsed(self) -> None: ...
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __add__(self, other: AcceptEncodingValidHeader | Literal[""]) -> AcceptEncodingValidHeader: ...
    @overload
    def __add__(self, other: AcceptEncodingInvalidHeader | AcceptEncodingNoHeader | None) -> AcceptEncodingNoHeader: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptEncodingHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptEncodingValidHeader | AcceptEncodingNoHeader: ...
    @overload
    def __radd__(self, other: AcceptEncodingValidHeader | Literal[""]) -> AcceptEncodingValidHeader: ...
    @overload
    def __radd__(self, other: AcceptEncodingInvalidHeader | AcceptEncodingNoHeader | None) -> AcceptEncodingNoHeader: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptEncodingHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptEncodingValidHeader | AcceptEncodingNoHeader: ...

@overload
def create_accept_encoding_header(header_value: AcceptEncodingValidHeader | Literal[""]) -> AcceptEncodingValidHeader: ...
@overload
def create_accept_encoding_header(header_value: AcceptEncodingInvalidHeader) -> AcceptEncodingInvalidHeader: ...
@overload
def create_accept_encoding_header(header_value: AcceptEncodingNoHeader | None) -> AcceptEncodingNoHeader: ...
@overload
def create_accept_encoding_header(header_value: str) -> AcceptEncodingValidHeader | AcceptEncodingInvalidHeader: ...
@overload
def create_accept_encoding_header(header_value: _AnyAcceptEncodingHeader | str | None) -> _AnyAcceptEncodingHeader: ...
def accept_encoding_property() -> _AcceptEncodingProperty: ...

class AcceptLanguage:
    """
    Represent an ``Accept-Language`` header.

    Base class for :class:`AcceptLanguageValidHeader`,
    :class:`AcceptLanguageNoHeader`, and :class:`AcceptLanguageInvalidHeader`.
    """
    @classmethod
    def parse(cls, value: str) -> Iterator[tuple[str, float]]:
        """
        Parse an ``Accept-Language`` header.

        :param value: (``str``) header value
        :return: If `value` is a valid ``Accept-Language`` header, returns an
                 iterator of (language range, quality value) tuples, as parsed
                 from the header from left to right.
        :raises ValueError: if `value` is an invalid header
        """
        ...

class AcceptLanguageValidHeader(AcceptLanguage):
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    @property
    def header_value(self) -> str:
        """(``str`` or ``None``) The header value."""
        ...
    @property
    def parsed(self) -> list[tuple[str, float]]: ...
    def __add__(
        self,
        other: (
            _AnyAcceptLanguageHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def __bool__(self) -> Literal[True]: ...
    def __contains__(self, offer: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __radd__(
        self,
        other: (
            _AnyAcceptLanguageHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self: ...
    def basic_filtering(self, language_tags: Sequence[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str: ...
    @overload
    def lookup(
        self, language_tags: Sequence[str], default_range: str | None, default_tag: str, default: None = None
    ) -> str | None: ...
    @overload
    def lookup(
        self, language_tags: Sequence[str], *, default_range: str | None = None, default_tag: str, default: None = None
    ) -> str | None: ...
    @overload
    def lookup(
        self, language_tags: Sequence[str], default_range: str | None, default_tag: None, default: _T | Callable[[], _T]
    ) -> _T | str | None: ...
    @overload
    def lookup(
        self, language_tags: Sequence[str], default_range: str | None, default_tag: str, default: _T | Callable[[], _T]
    ) -> _T | str: ...
    @overload
    def lookup(
        self,
        language_tags: Sequence[str],
        *,
        default_range: str | None = None,
        default_tag: None = None,
        default: _T | Callable[[], _T],
    ) -> _T | str | None: ...
    @overload
    def lookup(
        self, language_tags: Sequence[str], *, default_range: str | None = None, default_tag: str, default: _T | Callable[[], _T]
    ) -> _T | str: ...
    def quality(self, offer: str) -> float | None: ...

class _AcceptLanguageInvalidOrNoHeader(AcceptLanguage):
    def __bool__(self) -> Literal[False]: ...
    def __contains__(self, offer: str) -> Literal[True]: ...
    def __iter__(self) -> Iterator[str]: ...
    def basic_filtering(self, language_tags: Iterable[str]) -> list[tuple[str, float]]: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: None = None) -> str | None: ...
    @overload
    def best_match(self, offers: Iterable[str | tuple[str, float] | list[Any]], default_match: str) -> str: ...
    @overload
    def lookup(self, language_tags: object, default_range: object, default_tag: str, default: object = None) -> str: ...
    @overload
    def lookup(
        self, language_tags: object = None, *, default_range: object = None, default_tag: str, default: object = None
    ) -> str: ...
    @overload
    def lookup(self, language_tags: object, default_range: object, default_tag: None, default: _T | Callable[[], _T]) -> _T: ...
    @overload
    def lookup(
        self,
        language_tags: object = None,
        *,
        default_range: object = None,
        default_tag: None = None,
        default: _T | Callable[[], _T],
    ) -> _T: ...
    def quality(self, offer: str) -> float | None: ...

class AcceptLanguageNoHeader(_AcceptLanguageInvalidOrNoHeader):
    def __init__(self) -> None: ...
    def copy(self) -> Self: ...
    @property
    def header_value(self) -> None: ...
    @property
    def parsed(self) -> None: ...
    @overload
    def __add__(self, other: AcceptLanguageValidHeader) -> AcceptLanguageValidHeader: ...
    @overload
    def __add__(self, other: AcceptLanguageInvalidHeader | AcceptLanguageNoHeader | Literal[""] | None) -> Self: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptLanguageHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptLanguageValidHeader: ...
    @overload
    def __radd__(self, other: AcceptLanguageValidHeader) -> AcceptLanguageValidHeader: ...
    @overload
    def __radd__(self, other: AcceptLanguageInvalidHeader | AcceptLanguageNoHeader | Literal[""] | None) -> Self: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptLanguageHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> Self | AcceptLanguageValidHeader: ...

class AcceptLanguageInvalidHeader(_AcceptLanguageInvalidOrNoHeader):
    def __init__(self, header_value: str) -> None: ...
    def copy(self) -> Self: ...
    @property
    def header_value(self) -> str: ...
    @property
    def parsed(self) -> None: ...
    @overload
    def __add__(self, other: AcceptLanguageValidHeader) -> AcceptLanguageValidHeader: ...
    @overload
    def __add__(
        self, other: AcceptLanguageInvalidHeader | AcceptLanguageNoHeader | Literal[""] | None
    ) -> AcceptLanguageNoHeader: ...
    @overload
    def __add__(
        self,
        other: (
            _AnyAcceptLanguageHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptLanguageValidHeader | AcceptLanguageNoHeader: ...
    @overload
    def __radd__(self, other: AcceptLanguageValidHeader) -> AcceptLanguageValidHeader: ...
    @overload
    def __radd__(
        self, other: AcceptLanguageInvalidHeader | AcceptLanguageNoHeader | Literal[""] | None
    ) -> AcceptLanguageNoHeader: ...
    @overload
    def __radd__(
        self,
        other: (
            _AnyAcceptLanguageHeader
            | SupportsItems[str, float]
            | _ListOrTuple[str | tuple[str, float] | list[Any]]
            | _SupportsStr
            | str
            | None
        ),
    ) -> AcceptLanguageValidHeader | AcceptLanguageNoHeader: ...

@overload
def create_accept_language_header(header_value: AcceptLanguageValidHeader | Literal[""]) -> AcceptLanguageValidHeader: ...
@overload
def create_accept_language_header(header_value: AcceptLanguageNoHeader | None) -> AcceptLanguageNoHeader: ...
@overload
def create_accept_language_header(header_value: AcceptLanguageInvalidHeader) -> AcceptLanguageInvalidHeader: ...
@overload
def create_accept_language_header(header_value: str) -> AcceptLanguageValidHeader | AcceptLanguageInvalidHeader: ...
@overload
def create_accept_language_header(header_value: _AnyAcceptLanguageHeader | str | None) -> _AnyAcceptLanguageHeader: ...
def accept_language_property() -> _AcceptLanguageProperty: ...
