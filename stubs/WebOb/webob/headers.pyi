from _typeshed.wsgi import WSGIEnvironment
from collections.abc import Iterator, MutableMapping

from webob.multidict import MultiDict

class ResponseHeaders(MultiDict[str, str]):
    """
    Dictionary view on the response headerlist.
    Keys are normalized for case and whitespace.
    """
    ...

class EnvironHeaders(MutableMapping[str, str]):
    """
    An object that represents the headers as present in a
    WSGI environment.

    This object is a wrapper (with no internal state) for a WSGI
    request object, representing the CGI-style HTTP_* keys as a
    dictionary.  Because a CGI environment can only hold one value for
    each key, this dictionary is single-valued (unlike outgoing
    headers).
    """
    environ: WSGIEnvironment
    def __init__(self, environ: WSGIEnvironment) -> None: ...
    def __getitem__(self, hname: str) -> str: ...
    def __setitem__(self, hname: str, value: str) -> None: ...
    def __delitem__(self, hname: str) -> None: ...
    def keys(self) -> list[str]: ...  # type: ignore[override]
    def __contains__(self, hname: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
