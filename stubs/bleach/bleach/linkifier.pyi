from collections.abc import Container, Iterable, Iterator, Sequence
from re import Pattern
from typing import Any, Final
from typing_extensions import TypeAlias

from html5lib.filters.base import Filter
from html5lib.treewalkers.base import TreeWalker

from .callbacks import _Callback, _HTMLAttrs

DEFAULT_CALLBACKS: Final[list[_Callback]]
TLDS: Final[list[str]]

def build_url_re(tlds: Iterable[str] = ..., protocols: Iterable[str] = ...) -> Pattern[str]:
    """
    Builds the url regex used by linkifier

    If you want a different set of tlds or allowed protocols, pass those in
    and stomp on the existing ``url_re``::

        from bleach import linkifier

        my_url_re = linkifier.build_url_re(my_tlds_list, my_protocols)

        linker = LinkifyFilter(url_re=my_url_re)
    """
    ...

URL_RE: Final[Pattern[str]]
PROTO_RE: Final[Pattern[str]]

def build_email_re(tlds: Iterable[str] = ...) -> Pattern[str]:
    """
    Builds the email regex used by linkifier

    If you want a different set of tlds, pass those in and stomp on the existing ``email_re``::

        from bleach import linkifier

        my_email_re = linkifier.build_email_re(my_tlds_list)

        linker = LinkifyFilter(email_re=my_url_re)
    """
    ...

EMAIL_RE: Final[Pattern[str]]

class Linker:
    """
    Convert URL-like strings in an HTML fragment to links

    This function converts strings that look like URLs, domain names and email
    addresses in text that may be an HTML fragment to links, while preserving:

    1. links already in the string
    2. urls found in attributes
    3. email addresses

    linkify does a best-effort approach and tries to recover from bad
    situations due to crazy text.
    """
    def __init__(
        self,
        callbacks: Iterable[_Callback] = ...,
        skip_tags: Container[str] | None = None,
        parse_email: bool = False,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
        recognized_tags: Container[str] | None = ...,
    ) -> None:
        """
        Creates a Linker instance

        :arg list callbacks: list of callbacks to run when adjusting tag attributes;
            defaults to ``bleach.linkifier.DEFAULT_CALLBACKS``

        :arg set skip_tags: set of tags that you don't want to linkify the
            contents of; for example, you could set this to ``{'pre'}`` to skip
            linkifying contents of ``pre`` tags; ``None`` means you don't
            want linkify to skip any tags

        :arg bool parse_email: whether or not to linkify email addresses

        :arg url_re: url matching regex

        :arg email_re: email matching regex

        :arg set recognized_tags: the set of tags that linkify knows about;
            everything else gets escaped

        :returns: linkified text as unicode
        """
        ...
    def linkify(self, text: str) -> str:
        """
        Linkify specified text

        :arg str text: the text to add links to

        :returns: linkified text as unicode

        :raises TypeError: if ``text`` is not a text type
        """
        ...

# TODO: `_Token` might be converted into `TypedDict`
# or `html5lib` token might be reused
_Token: TypeAlias = dict[str, Any]

class LinkifyFilter(Filter):
    """
    html5lib filter that linkifies text

    This will do the following:

    * convert email addresses into links
    * convert urls into links
    * edit existing links by running them through callbacks--the default is to
      add a ``rel="nofollow"``

    This filter can be used anywhere html5lib filters can be used.
    """
    callbacks: Iterable[_Callback]
    skip_tags: Container[str]
    parse_email: bool
    url_re: Pattern[str]
    email_re: Pattern[str]
    def __init__(
        self,
        source: TreeWalker,
        callbacks: Iterable[_Callback] | None = ...,
        skip_tags: Container[str] | None = None,
        parse_email: bool = False,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
    ) -> None: ...
    def apply_callbacks(self, attrs: _HTMLAttrs, is_new: bool) -> _HTMLAttrs | None: ...
    def extract_character_data(self, token_list: Iterable[_Token]) -> str: ...
    def handle_email_addresses(self, src_iter: Iterable[_Token]) -> Iterator[_Token]: ...
    def strip_non_url_bits(self, fragment: str) -> tuple[str, str, str]: ...
    def handle_links(self, src_iter: Iterable[_Token]) -> Iterator[_Token]: ...
    def handle_a_tag(self, token_buffer: Sequence[_Token]) -> Iterator[_Token]: ...
    def extract_entities(self, token: _Token) -> Iterator[_Token]: ...
    def __iter__(self) -> Iterator[_Token]: ...
