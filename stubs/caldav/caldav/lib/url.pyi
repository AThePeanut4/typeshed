from typing import overload
from urllib.parse import ParseResult, SplitResult

class URL:
    """
    This class is for wrapping URLs into objects.  It's used
    internally in the library, end users should not need to know
    anything about this class.  All methods that accept URLs can be
    fed either with a URL object, a string or a urlparse.ParsedURL
    object.

    Addresses may be one out of three:

    1) a path relative to the DAV-root, i.e. "someuser/calendar" may
    refer to
    "http://my.davical-server.example.com/caldav.php/someuser/calendar".

    2) an absolute path, i.e. "/caldav.php/someuser/calendar"

    3) a fully qualified URL, i.e.
    "http://someuser:somepass@my.davical-server.example.com/caldav.php/someuser/calendar".
    Remark that hostname, port, user, pass is typically given when
    instantiating the DAVClient object and cannot be overridden later.

    As of 2013-11, some methods in the caldav library expected strings
    and some expected urlParseResult objects, some expected
    fully qualified URLs and most expected absolute paths.  The purpose
    of this class is to ensure consistency and at the same time
    maintaining backward compatibility.  Basically, all methods should
    accept any kind of URL.
    """
    def __init__(self, url: str | ParseResult | SplitResult) -> None: ...
    def __bool__(self) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @overload
    @classmethod
    def objectify(cls, url: None) -> None: ...
    @overload
    @classmethod
    def objectify(cls, url: URL | str | ParseResult | SplitResult) -> URL: ...
    def __getattr__(self, attr: str): ...
    def __unicode__(self) -> str: ...
    def strip_trailing_slash(self) -> URL: ...
    def is_auth(self) -> bool: ...
    def unauth(self) -> URL: ...
    def canonical(self) -> URL:
        """
        a canonical URL ... remove authentication details, make sure there
        are no double slashes, and to make sure the URL is always the same,
        run it through the urlparser, and make sure path is properly quoted
        """
        ...
    def join(self, path: object) -> URL:
        """
        assumes this object is the base URL or base path.  If the path
        is relative, it should be appended to the base.  If the path
        is absolute, it should be added to the connection details of
        self.  If the path already contains connection details and the
        connection details differ from self, raise an error.
        """
        ...

@overload
def make(url: None) -> None:
    """Backward compatibility"""
    ...
@overload
def make(url: URL | str | ParseResult | SplitResult) -> URL:
    """Backward compatibility"""
    ...
