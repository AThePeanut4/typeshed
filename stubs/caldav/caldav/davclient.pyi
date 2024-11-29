from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from types import TracebackType
from typing_extensions import Self, TypeAlias
from urllib.parse import ParseResult, SplitResult

from requests.auth import AuthBase
from requests.models import Response
from requests.sessions import _Timeout
from requests.structures import CaseInsensitiveDict

from .lib.url import URL
from .objects import Calendar, DAVObject, Principal

_Element: TypeAlias = Incomplete  # actually lxml.etree._Element

class DAVResponse:
    """
    This class is a response from a DAV request.  It is instantiated from
    the DAVClient class.  End users of the library should not need to
    know anything about this class.  Since we often get XML responses,
    it tries to parse it into `self.tree`
    """
    reason: str
    tree: _Element | None
    status: int
    headers: CaseInsensitiveDict[str]
    objects: dict[str, dict[str, str]]  # only defined after call to find_objects_and_props()
    huge_tree: bool
    def __init__(self, response: Response, davclient: DAVClient | None = None) -> None: ...
    @property
    def raw(self) -> str: ...
    def validate_status(self, status: str) -> None:
        """
        status is a string like "HTTP/1.1 404 Not Found".  200, 207 and
        404 are considered good statuses.  The SOGo caldav server even
        returns "201 created" when doing a sync-report, to indicate
        that a resource was created after the last sync-token.  This
        makes sense to me, but I've only seen it from SOGo, and it's
        not in accordance with the examples in rfc6578.
        """
        ...
    def find_objects_and_props(self) -> None:
        """
        Check the response from the server, check that it is on an expected format,
        find hrefs and props from it and check statuses delivered.

        The parsed data will be put into self.objects, a dict {href:
        {proptag: prop_element}}.  Further parsing of the prop_element
        has to be done by the caller.

        self.sync_token will be populated if found, self.objects will be populated.
        """
        ...
    def expand_simple_props(
        self, props: Iterable[Incomplete] = [], multi_value_props: Iterable[Incomplete] = [], xpath: str | None = None
    ) -> dict[str, dict[str, str]]:
        """
        The find_objects_and_props() will stop at the xml element
        below the prop tag.  This method will expand those props into
        text.

        Executes find_objects_and_props if not run already, then
        modifies and returns self.objects.
        """
        ...

class DAVClient:
    """
    Basic client for webdav, uses the requests lib; gives access to
    low-level operations towards the caldav server.

    Unless you have special needs, you should probably care most about
    the constructor (__init__), the principal method and the calendar method.
    """
    proxy: str | None
    url: URL
    headers: dict[str, str]
    username: str | None
    password: str | None
    auth: AuthBase | None
    timeout: _Timeout | None
    ssl_verify_cert: bool | str
    ssl_cert: str | tuple[str, str] | None
    huge_tree: bool
    def __init__(
        self,
        url: str,
        proxy: str | None = None,
        username: str | None = None,
        password: str | None = None,
        auth: AuthBase | None = None,
        timeout: _Timeout | None = None,
        ssl_verify_cert: bool | str = True,
        ssl_cert: str | tuple[str, str] | None = None,
        headers: dict[str, str] = {},
        huge_tree: bool = False,
    ) -> None:
        """
        Sets up a HTTPConnection object towards the server in the url.
        Parameters:
         * url: A fully qualified url: `scheme://user:pass@hostname:port`
         * proxy: A string defining a proxy server: `hostname:port`
         * username and password should be passed as arguments or in the URL
         * auth, timeout and ssl_verify_cert are passed to requests.request.
         * ssl_verify_cert can be the path of a CA-bundle or False.
         * huge_tree: boolean, enable XMLParser huge_tree to handle big events, beware
           of security issues, see : https://lxml.de/api/lxml.etree.XMLParser-class.html

        The requests library will honor a .netrc-file, if such a file exists
        username and password may be omitted.  Known bug: .netrc is honored
        even if a username/password is given, ref https://github.com/python-caldav/caldav/issues/206
        """
        ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def principal(self, *, url: str | ParseResult | SplitResult | URL | None = None) -> Principal:
        """
        Convenience method, it gives a bit more object-oriented feel to
        write client.principal() than Principal(client).

        This method returns a :class:`caldav.Principal` object, with
        higher-level methods for dealing with the principals
        calendars.
        """
        ...
    def calendar(
        self,
        *,
        url: str | ParseResult | SplitResult | URL | None = ...,
        parent: DAVObject | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        props: Mapping[Incomplete, Incomplete] = ...,
        **extra,
    ) -> Calendar:
        """
        Returns a calendar object.

        Typically, a URL should be given as a named parameter (url)

        No network traffic will be initiated by this method.

        If you don't know the URL of the calendar, use
        client.principal().calendar(...) instead, or
        client.principal().calendars()
        """
        ...
    def check_dav_support(self) -> str | None: ...
    def check_cdav_support(self) -> bool: ...
    def check_scheduling_support(self) -> bool: ...
    def propfind(self, url: str | None = None, props: str = "", depth: int = 0) -> DAVResponse:
        """
        Send a propfind request.

        Parameters:
         * url: url for the root of the propfind.
         * props = (xml request), properties we want
         * depth: maximum recursion depth

        Returns
         * DAVResponse
        """
        ...
    def proppatch(self, url: str, body: str, dummy: None = None) -> DAVResponse:
        """
        Send a proppatch request.

        Parameters:
         * url: url for the root of the propfind.
         * body: XML propertyupdate request
         * dummy: compatibility parameter

        Returns
         * DAVResponse
        """
        ...
    def report(self, url: str, query: str = "", depth: int = 0) -> DAVResponse:
        """
        Send a report request.

        Parameters:
         * url: url for the root of the propfind.
         * query: XML request
         * depth: maximum recursion depth

        Returns
         * DAVResponse
        """
        ...
    def mkcol(self, url: str, body: str, dummy: None = None) -> DAVResponse:
        """
        Send a MKCOL request.

        MKCOL is basically not used with caldav, one should use
        MKCALENDAR instead.  However, some calendar servers MAY allow
        "subcollections" to be made in a calendar, by using the MKCOL
        query.  As for 2020-05, this method is not exercised by test
        code or referenced anywhere else in the caldav library, it's
        included just for the sake of completeness.  And, perhaps this
        DAVClient class can be used for vCards and other WebDAV
        purposes.

        Parameters:
         * url: url for the root of the mkcol
         * body: XML request
         * dummy: compatibility parameter

        Returns
         * DAVResponse
        """
        ...
    def mkcalendar(self, url: str, body: str = "", dummy: None = None) -> DAVResponse:
        """
        Send a mkcalendar request.

        Parameters:
         * url: url for the root of the mkcalendar
         * body: XML request
         * dummy: compatibility parameter

        Returns
         * DAVResponse
        """
        ...
    def put(self, url: str, body: str, headers: Mapping[str, str] = {}) -> DAVResponse:
        """Send a put request."""
        ...
    def post(self, url: str, body: str, headers: Mapping[str, str] = {}) -> DAVResponse:
        """Send a POST request."""
        ...
    def delete(self, url: str) -> DAVResponse:
        """Send a delete request."""
        ...
    def options(self, url: str) -> DAVResponse: ...
    def request(self, url: str, method: str = "GET", body: str = "", headers: Mapping[str, str] = {}) -> DAVResponse:
        """Actually sends the request, and does the authentication"""
        ...
