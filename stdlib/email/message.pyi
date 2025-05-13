"""Basic message object for the email package object model."""

from _typeshed import MaybeNone
from collections.abc import Generator, Iterator, Sequence
from email import _ParamsType, _ParamType
from email.charset import Charset
from email.contentmanager import ContentManager
from email.errors import MessageDefect
from email.policy import Policy
from typing import Any, Generic, Literal, Protocol, TypeVar, overload
from typing_extensions import Self, TypeAlias

__all__ = ["Message", "EmailMessage"]

_T = TypeVar("_T")
# Type returned by Policy.header_fetch_parse, often str or Header.
_HeaderT_co = TypeVar("_HeaderT_co", covariant=True, default=str)
_HeaderParamT_contra = TypeVar("_HeaderParamT_contra", contravariant=True, default=str)
# Represents headers constructed by HeaderRegistry. Those are sub-classes
# of BaseHeader and another header type.
_HeaderRegistryT_co = TypeVar("_HeaderRegistryT_co", covariant=True, default=Any)
_HeaderRegistryParamT_contra = TypeVar("_HeaderRegistryParamT_contra", contravariant=True, default=Any)

_PayloadType: TypeAlias = Message | str
_EncodedPayloadType: TypeAlias = Message | bytes
_MultipartPayloadType: TypeAlias = list[_PayloadType]
_CharsetType: TypeAlias = Charset | str | None

class _SupportsEncodeToPayload(Protocol):
    def encode(self, encoding: str, /) -> _PayloadType | _MultipartPayloadType | _SupportsDecodeToPayload: ...

class _SupportsDecodeToPayload(Protocol):
    def decode(self, encoding: str, errors: str, /) -> _PayloadType | _MultipartPayloadType: ...

class Message(Generic[_HeaderT_co, _HeaderParamT_contra]):
    # The policy attributes and arguments in this class and its subclasses
    # would ideally use Policy[Self], but this is not possible.
    policy: Policy[Any]  # undocumented
    preamble: str | None
    epilogue: str | None
    defects: list[MessageDefect]
    def __init__(self, policy: Policy[Any] = ...) -> None: ...
    def is_multipart(self) -> bool:
        """Return True if the message consists of multiple parts."""
        ...
    def set_unixfrom(self, unixfrom: str) -> None: ...
    def get_unixfrom(self) -> str | None: ...
    def attach(self, payload: _PayloadType) -> None:
        """
        Add the given payload to the current payload.

        The current payload will always be a list of objects after this method
        is called.  If you want to set the payload to a scalar object, use
        set_payload() instead.
        """
        ...
    # `i: int` without a multipart payload results in an error
    # `| MaybeNone` acts like `| Any`: can be None for cleared or unset payload, but annoying to check
    @overload  # multipart
    def get_payload(self, i: int, decode: Literal[True]) -> None:
        """
        Return a reference to the payload.

        The payload will either be a list object or a string.  If you mutate
        the list object, you modify the message's payload in place.  Optional
        i returns that index into the payload.

        Optional decode is a flag indicating whether the payload should be
        decoded or not, according to the Content-Transfer-Encoding header
        (default is False).

        When True and the message is not a multipart, the payload will be
        decoded if this header's value is `quoted-printable' or `base64'.  If
        some other encoding is used, or the header is missing, or if the
        payload has bogus data (i.e. bogus base64 or uuencoded data), the
        payload is returned as-is.

        If the message is a multipart and the decode flag is True, then None
        is returned.
        """
        ...
    @overload  # multipart
    def get_payload(self, i: int, decode: Literal[False] = False) -> _PayloadType | MaybeNone:
        """
        Return a reference to the payload.

        The payload will either be a list object or a string.  If you mutate
        the list object, you modify the message's payload in place.  Optional
        i returns that index into the payload.

        Optional decode is a flag indicating whether the payload should be
        decoded or not, according to the Content-Transfer-Encoding header
        (default is False).

        When True and the message is not a multipart, the payload will be
        decoded if this header's value is `quoted-printable' or `base64'.  If
        some other encoding is used, or the header is missing, or if the
        payload has bogus data (i.e. bogus base64 or uuencoded data), the
        payload is returned as-is.

        If the message is a multipart and the decode flag is True, then None
        is returned.
        """
        ...
    @overload  # either
    def get_payload(self, i: None = None, decode: Literal[False] = False) -> _PayloadType | _MultipartPayloadType | MaybeNone:
        """
        Return a reference to the payload.

        The payload will either be a list object or a string.  If you mutate
        the list object, you modify the message's payload in place.  Optional
        i returns that index into the payload.

        Optional decode is a flag indicating whether the payload should be
        decoded or not, according to the Content-Transfer-Encoding header
        (default is False).

        When True and the message is not a multipart, the payload will be
        decoded if this header's value is `quoted-printable' or `base64'.  If
        some other encoding is used, or the header is missing, or if the
        payload has bogus data (i.e. bogus base64 or uuencoded data), the
        payload is returned as-is.

        If the message is a multipart and the decode flag is True, then None
        is returned.
        """
        ...
    @overload  # not multipart
    def get_payload(self, i: None = None, *, decode: Literal[True]) -> _EncodedPayloadType | MaybeNone:
        """
        Return a reference to the payload.

        The payload will either be a list object or a string.  If you mutate
        the list object, you modify the message's payload in place.  Optional
        i returns that index into the payload.

        Optional decode is a flag indicating whether the payload should be
        decoded or not, according to the Content-Transfer-Encoding header
        (default is False).

        When True and the message is not a multipart, the payload will be
        decoded if this header's value is `quoted-printable' or `base64'.  If
        some other encoding is used, or the header is missing, or if the
        payload has bogus data (i.e. bogus base64 or uuencoded data), the
        payload is returned as-is.

        If the message is a multipart and the decode flag is True, then None
        is returned.
        """
        ...
    @overload  # not multipart, IDEM but w/o kwarg
    def get_payload(self, i: None, decode: Literal[True]) -> _EncodedPayloadType | MaybeNone:
        """
        Return a reference to the payload.

        The payload will either be a list object or a string.  If you mutate
        the list object, you modify the message's payload in place.  Optional
        i returns that index into the payload.

        Optional decode is a flag indicating whether the payload should be
        decoded or not, according to the Content-Transfer-Encoding header
        (default is False).

        When True and the message is not a multipart, the payload will be
        decoded if this header's value is `quoted-printable' or `base64'.  If
        some other encoding is used, or the header is missing, or if the
        payload has bogus data (i.e. bogus base64 or uuencoded data), the
        payload is returned as-is.

        If the message is a multipart and the decode flag is True, then None
        is returned.
        """
        ...
    # If `charset=None` and payload supports both `encode` AND `decode`,
    # then an invalid payload could be passed, but this is unlikely
    # Not[_SupportsEncodeToPayload]
    @overload
    def set_payload(
        self, payload: _SupportsDecodeToPayload | _PayloadType | _MultipartPayloadType, charset: None = None
    ) -> None:
        """
        Set the payload to the given value.

        Optional charset sets the message's default character set.  See
        set_charset() for details.
        """
        ...
    @overload
    def set_payload(
        self,
        payload: _SupportsEncodeToPayload | _SupportsDecodeToPayload | _PayloadType | _MultipartPayloadType,
        charset: Charset | str,
    ) -> None:
        """
        Set the payload to the given value.

        Optional charset sets the message's default character set.  See
        set_charset() for details.
        """
        ...
    def set_charset(self, charset: _CharsetType) -> None:
        """
        Set the charset of the payload to a given character set.

        charset can be a Charset instance, a string naming a character set, or
        None.  If it is a string it will be converted to a Charset instance.
        If charset is None, the charset parameter will be removed from the
        Content-Type field.  Anything else will generate a TypeError.

        The message will be assumed to be of type text/* encoded with
        charset.input_charset.  It will be converted to charset.output_charset
        and encoded properly, if needed, when generating the plain text
        representation of the message.  MIME headers (MIME-Version,
        Content-Type, Content-Transfer-Encoding) will be added as needed.
        """
        ...
    def get_charset(self) -> _CharsetType:
        """
        Return the Charset instance associated with the message's payload.
        
        """
        ...
    def __len__(self) -> int:
        """Return the total number of headers, including duplicates."""
        ...
    def __contains__(self, name: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    # Same as `get` with `failobj=None`, but with the expectation that it won't return None in most scenarios
    # This is important for protocols using __getitem__, like SupportsKeysAndGetItem
    # Morally, the return type should be `AnyOf[_HeaderType, None]`,
    # so using "the Any trick" instead.
    def __getitem__(self, name: str) -> _HeaderT_co | MaybeNone: ...
    def __setitem__(self, name: str, val: _HeaderParamT_contra) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[_HeaderT_co]: ...
    def items(self) -> list[tuple[str, _HeaderT_co]]: ...
    @overload
    def get(self, name: str, failobj: None = None) -> _HeaderT_co | None: ...
    @overload
    def get(self, name: str, failobj: _T) -> _HeaderT_co | _T: ...
    @overload
    def get_all(self, name: str, failobj: None = None) -> list[_HeaderT_co] | None: ...
    @overload
    def get_all(self, name: str, failobj: _T) -> list[_HeaderT_co] | _T: ...
    def add_header(self, _name: str, _value: str, **_params: _ParamsType) -> None: ...
    def replace_header(self, _name: str, _value: _HeaderParamT_contra) -> None: ...
    def get_content_type(self) -> str: ...
    def get_content_maintype(self) -> str: ...
    def get_content_subtype(self) -> str: ...
    def get_default_type(self) -> str: ...
    def set_default_type(self, ctype: str) -> None: ...
    @overload
    def get_params(
        self, failobj: None = None, header: str = "content-type", unquote: bool = True
    ) -> list[tuple[str, str]] | None:
        """
        Return the message's Content-Type parameters, as a list.

        The elements of the returned list are 2-tuples of key/value pairs, as
        split on the `=' sign.  The left hand side of the `=' is the key,
        while the right hand side is the value.  If there is no `=' sign in
        the parameter the value is the empty string.  The value is as
        described in the get_param() method.

        Optional failobj is the object to return if there is no Content-Type
        header.  Optional header is the header to search instead of
        Content-Type.  If unquote is True, the value is unquoted.
        """
        ...
    @overload
    def get_params(self, failobj: _T, header: str = "content-type", unquote: bool = True) -> list[tuple[str, str]] | _T:
        """
        Return the message's Content-Type parameters, as a list.

        The elements of the returned list are 2-tuples of key/value pairs, as
        split on the `=' sign.  The left hand side of the `=' is the key,
        while the right hand side is the value.  If there is no `=' sign in
        the parameter the value is the empty string.  The value is as
        described in the get_param() method.

        Optional failobj is the object to return if there is no Content-Type
        header.  Optional header is the header to search instead of
        Content-Type.  If unquote is True, the value is unquoted.
        """
        ...
    @overload
    def get_param(
        self, param: str, failobj: None = None, header: str = "content-type", unquote: bool = True
    ) -> _ParamType | None:
        """
        Return the parameter value if found in the Content-Type header.

        Optional failobj is the object to return if there is no Content-Type
        header, or the Content-Type header has no such parameter.  Optional
        header is the header to search instead of Content-Type.

        Parameter keys are always compared case insensitively.  The return
        value can either be a string, or a 3-tuple if the parameter was RFC
        2231 encoded.  When it's a 3-tuple, the elements of the value are of
        the form (CHARSET, LANGUAGE, VALUE).  Note that both CHARSET and
        LANGUAGE can be None, in which case you should consider VALUE to be
        encoded in the us-ascii charset.  You can usually ignore LANGUAGE.
        The parameter value (either the returned string, or the VALUE item in
        the 3-tuple) is always unquoted, unless unquote is set to False.

        If your application doesn't care whether the parameter was RFC 2231
        encoded, it can turn the return value into a string as follows:

            rawparam = msg.get_param('foo')
            param = email.utils.collapse_rfc2231_value(rawparam)
        """
        ...
    @overload
    def get_param(self, param: str, failobj: _T, header: str = "content-type", unquote: bool = True) -> _ParamType | _T:
        """
        Return the parameter value if found in the Content-Type header.

        Optional failobj is the object to return if there is no Content-Type
        header, or the Content-Type header has no such parameter.  Optional
        header is the header to search instead of Content-Type.

        Parameter keys are always compared case insensitively.  The return
        value can either be a string, or a 3-tuple if the parameter was RFC
        2231 encoded.  When it's a 3-tuple, the elements of the value are of
        the form (CHARSET, LANGUAGE, VALUE).  Note that both CHARSET and
        LANGUAGE can be None, in which case you should consider VALUE to be
        encoded in the us-ascii charset.  You can usually ignore LANGUAGE.
        The parameter value (either the returned string, or the VALUE item in
        the 3-tuple) is always unquoted, unless unquote is set to False.

        If your application doesn't care whether the parameter was RFC 2231
        encoded, it can turn the return value into a string as follows:

            rawparam = msg.get_param('foo')
            param = email.utils.collapse_rfc2231_value(rawparam)
        """
        ...
    def del_param(self, param: str, header: str = "content-type", requote: bool = True) -> None:
        """
        Remove the given parameter completely from the Content-Type header.

        The header will be re-written in place without the parameter or its
        value. All values will be quoted as necessary unless requote is
        False.  Optional header specifies an alternative to the Content-Type
        header.
        """
        ...
    def set_type(self, type: str, header: str = "Content-Type", requote: bool = True) -> None:
        """
        Set the main type and subtype for the Content-Type header.

        type must be a string in the form "maintype/subtype", otherwise a
        ValueError is raised.

        This method replaces the Content-Type header, keeping all the
        parameters in place.  If requote is False, this leaves the existing
        header's quoting as is.  Otherwise, the parameters will be quoted (the
        default).

        An alternative header can be specified in the header argument.  When
        the Content-Type header is set, we'll always also add a MIME-Version
        header.
        """
        ...
    @overload
    def get_filename(self, failobj: None = None) -> str | None:
        """
        Return the filename associated with the payload if present.

        The filename is extracted from the Content-Disposition header's
        `filename' parameter, and it is unquoted.  If that header is missing
        the `filename' parameter, this method falls back to looking for the
        `name' parameter.
        """
        ...
    @overload
    def get_filename(self, failobj: _T) -> str | _T:
        """
        Return the filename associated with the payload if present.

        The filename is extracted from the Content-Disposition header's
        `filename' parameter, and it is unquoted.  If that header is missing
        the `filename' parameter, this method falls back to looking for the
        `name' parameter.
        """
        ...
    @overload
    def get_boundary(self, failobj: None = None) -> str | None:
        """
        Return the boundary associated with the payload if present.

        The boundary is extracted from the Content-Type header's `boundary'
        parameter, and it is unquoted.
        """
        ...
    @overload
    def get_boundary(self, failobj: _T) -> str | _T:
        """
        Return the boundary associated with the payload if present.

        The boundary is extracted from the Content-Type header's `boundary'
        parameter, and it is unquoted.
        """
        ...
    def set_boundary(self, boundary: str) -> None:
        """
        Set the boundary parameter in Content-Type to 'boundary'.

        This is subtly different than deleting the Content-Type header and
        adding a new one with a new boundary parameter via add_header().  The
        main difference is that using the set_boundary() method preserves the
        order of the Content-Type header in the original message.

        HeaderParseError is raised if the message has no Content-Type header.
        """
        ...
    @overload
    def get_content_charset(self) -> str | None:
        """
        Return the charset parameter of the Content-Type header.

        The returned string is always coerced to lower case.  If there is no
        Content-Type header, or if that header has no charset parameter,
        failobj is returned.
        """
        ...
    @overload
    def get_content_charset(self, failobj: _T) -> str | _T:
        """
        Return the charset parameter of the Content-Type header.

        The returned string is always coerced to lower case.  If there is no
        Content-Type header, or if that header has no charset parameter,
        failobj is returned.
        """
        ...
    @overload
    def get_charsets(self, failobj: None = None) -> list[str | None]:
        """
        Return a list containing the charset(s) used in this message.

        The returned list of items describes the Content-Type headers'
        charset parameter for this message and all the subparts in its
        payload.

        Each item will either be a string (the value of the charset parameter
        in the Content-Type header of that part) or the value of the
        'failobj' parameter (defaults to None), if the part does not have a
        main MIME type of "text", or the charset is not defined.

        The list will contain one string for each part of the message, plus
        one for the container message (i.e. self), so that a non-multipart
        message will still return a list of length 1.
        """
        ...
    @overload
    def get_charsets(self, failobj: _T) -> list[str | _T]:
        """
        Return a list containing the charset(s) used in this message.

        The returned list of items describes the Content-Type headers'
        charset parameter for this message and all the subparts in its
        payload.

        Each item will either be a string (the value of the charset parameter
        in the Content-Type header of that part) or the value of the
        'failobj' parameter (defaults to None), if the part does not have a
        main MIME type of "text", or the charset is not defined.

        The list will contain one string for each part of the message, plus
        one for the container message (i.e. self), so that a non-multipart
        message will still return a list of length 1.
        """
        ...
    def walk(self) -> Generator[Self, None, None]:
        """
        Walk over the message tree, yielding each subpart.

        The walk is performed in depth-first order.  This method is a
        generator.
        """
        ...
    def get_content_disposition(self) -> str | None:
        """
        Return the message's content-disposition if it exists, or None.

        The return values can be either 'inline', 'attachment' or None
        according to the rfc2183.
        """
        ...
    def as_string(self, unixfrom: bool = False, maxheaderlen: int = 0, policy: Policy[Any] | None = None) -> str:
        """
        Return the entire formatted message as a string.

        Optional 'unixfrom', when true, means include the Unix From_ envelope
        header.  For backward compatibility reasons, if maxheaderlen is
        not specified it defaults to 0, so you must override it explicitly
        if you want a different maxheaderlen.  'policy' is passed to the
        Generator instance used to serialize the message; if it is not
        specified the policy associated with the message instance is used.

        If the message object contains binary data that is not encoded
        according to RFC standards, the non-compliant data will be replaced by
        unicode "unknown character" code points.
        """
        ...
    def as_bytes(self, unixfrom: bool = False, policy: Policy[Any] | None = None) -> bytes:
        """
        Return the entire formatted message as a bytes object.

        Optional 'unixfrom', when true, means include the Unix From_ envelope
        header.  'policy' is passed to the BytesGenerator instance used to
        serialize the message; if not specified the policy associated with
        the message instance is used.
        """
        ...
    def __bytes__(self) -> bytes:
        """
        Return the entire formatted message as a bytes object.
        
        """
        ...
    def set_param(
        self,
        param: str,
        value: str,
        header: str = "Content-Type",
        requote: bool = True,
        charset: str | None = None,
        language: str = "",
        replace: bool = False,
    ) -> None:
        """
        Set a parameter in the Content-Type header.

        If the parameter already exists in the header, its value will be
        replaced with the new value.

        If header is Content-Type and has not yet been defined for this
        message, it will be set to "text/plain" and the new parameter and
        value will be appended as per RFC 2045.

        An alternate header can be specified in the header argument, and all
        parameters will be quoted as necessary unless requote is False.

        If charset is specified, the parameter will be encoded according to RFC
        2231.  Optional language specifies the RFC 2231 language, defaulting
        to the empty string.  Both charset and language should be strings.
        """
        ...
    # The following two methods are undocumented, but a source code comment states that they are public API
    def set_raw(self, name: str, value: _HeaderParamT_contra) -> None: ...
    def raw_items(self) -> Iterator[tuple[str, _HeaderT_co]]: ...

class MIMEPart(Message[_HeaderRegistryT_co, _HeaderRegistryParamT_contra]):
    def __init__(self, policy: Policy[Any] | None = None) -> None: ...
    def get_body(self, preferencelist: Sequence[str] = ("related", "html", "plain")) -> MIMEPart[_HeaderRegistryT_co] | None: ...
    def attach(self, payload: Self) -> None: ...  # type: ignore[override]
    # The attachments are created via type(self) in the attach method. It's theoretically
    # possible to sneak other attachment types into a MIMEPart instance, but could cause
    # cause unforseen consequences.
    def iter_attachments(self) -> Iterator[Self]: ...
    def iter_parts(self) -> Iterator[MIMEPart[_HeaderRegistryT_co]]: ...
    def get_content(self, *args: Any, content_manager: ContentManager | None = None, **kw: Any) -> Any: ...
    def set_content(self, *args: Any, content_manager: ContentManager | None = None, **kw: Any) -> None: ...
    def make_related(self, boundary: str | None = None) -> None: ...
    def make_alternative(self, boundary: str | None = None) -> None: ...
    def make_mixed(self, boundary: str | None = None) -> None: ...
    def add_related(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def add_alternative(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def add_attachment(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def clear(self) -> None: ...
    def clear_content(self) -> None: ...
    def as_string(self, unixfrom: bool = False, maxheaderlen: int | None = None, policy: Policy[Any] | None = None) -> str:
        """
        Return the entire formatted message as a string.

        Optional 'unixfrom', when true, means include the Unix From_ envelope
        header.  maxheaderlen is retained for backward compatibility with the
        base Message class, but defaults to None, meaning that the policy value
        for max_line_length controls the header maximum length.  'policy' is
        passed to the Generator instance used to serialize the message; if it
        is not specified the policy associated with the message instance is
        used.
        """
        ...
    def is_attachment(self) -> bool: ...

class EmailMessage(MIMEPart): ...
