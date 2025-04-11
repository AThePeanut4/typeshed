"""
Header value parser implementing various email-related RFC parsing rules.

The parsing methods defined in this module implement various email related
parsing rules.  Principal among them is RFC 5322, which is the followon
to RFC 2822 and primarily a clarification of the former.  It also implements
RFC 2047 encoded word decoding.

RFC 5322 goes to considerable trouble to maintain backward compatibility with
RFC 822 in the parse phase, while cleaning up the structure on the generation
phase.  This parser supports correct RFC 5322 generation by tagging white space
as folding white space only when folding is allowed in the non-obsolete rule
sets.  Actually, the parser is even more generous when accepting input than RFC
5322 mandates, following the spirit of Postel's Law, which RFC 5322 encourages.
Where possible deviations from the standard are annotated on the 'defects'
attribute of tokens that deviate.

The general structure of the parser follows RFC 5322, and uses its terminology
where there is a direct correspondence.  Where the implementation requires a
somewhat different structure than that used by the formal grammar, new terms
that mimic the closest existing terms are used.  Thus, it really helps to have
a copy of RFC 5322 handy when studying this code.

Input to the parser is a string that has already been unfolded according to
RFC 5322 rules.  According to the RFC this unfolding is the very first step, and
this parser leaves the unfolding step to a higher level message parser, which
will have already detected the line breaks that need unfolding while
determining the beginning and end of each header.

The output of the parser is a TokenList object, which is a list subclass.  A
TokenList is a recursive data structure.  The terminal nodes of the structure
are Terminal objects, which are subclasses of str.  These do not correspond
directly to terminal objects in the formal grammar, but are instead more
practical higher level combinations of true terminals.

All TokenList and Terminal objects have a 'value' attribute, which produces the
semantically meaningful value of that part of the parse subtree.  The value of
all whitespace tokens (no matter how many sub-tokens they may contain) is a
single space, as per the RFC rules.  This includes 'CFWS', which is herein
included in the general class of whitespace tokens.  There is one exception to
the rule that whitespace tokens are collapsed into single spaces in values: in
the value of a 'bare-quoted-string' (a quoted-string with no leading or
trailing whitespace), any whitespace that appeared between the quotation marks
is preserved in the returned value.  Note that in all Terminal strings quoted
pairs are turned into their unquoted values.

All TokenList and Terminal objects also have a string value, which attempts to
be a "canonical" representation of the RFC-compliant form of the substring that
produced the parsed subtree, including minimal use of quoted pair quoting.
Whitespace runs are not collapsed.

Comment tokens also have a 'content' attribute providing the string found
between the parens (including any nested comments) with whitespace preserved.

All TokenList and Terminal objects have a 'defects' attribute which is a
possibly empty list all of the defects found while creating the token.  Defects
may appear on any token in the tree, and a composite list of all defects in the
subtree is available through the 'all_defects' attribute of any node.  (For
Terminal notes x.defects == x.all_defects.)

Each object in a parse tree is called a 'token', and each has a 'token_type'
attribute that gives the name from the RFC 5322 grammar that it represents.
Not all RFC 5322 nodes are produced, and there is one non-RFC 5322 node that
may be produced: 'ptext'.  A 'ptext' is a string of printable ascii characters.
It is returned in place of lists of (ctext/quoted-pair) and
(qtext/quoted-pair).

XXX: provide complete list of token types.
"""

import sys
from collections.abc import Iterable, Iterator
from email.errors import HeaderParseError, MessageDefect
from email.policy import Policy
from re import Pattern
from typing import Any, Final
from typing_extensions import Self

WSP: Final[set[str]]
CFWS_LEADER: Final[set[str]]
SPECIALS: Final[set[str]]
ATOM_ENDS: Final[set[str]]
DOT_ATOM_ENDS: Final[set[str]]
PHRASE_ENDS: Final[set[str]]
TSPECIALS: Final[set[str]]
TOKEN_ENDS: Final[set[str]]
ASPECIALS: Final[set[str]]
ATTRIBUTE_ENDS: Final[set[str]]
EXTENDED_ATTRIBUTE_ENDS: Final[set[str]]
# Added in Python 3.8.20, 3.9.20, 3.10.15, 3.11.10, 3.12.5
NLSET: Final[set[str]]
# Added in Python 3.8.20, 3.9.20, 3.10.15, 3.11.10, 3.12.5
SPECIALSNL: Final[set[str]]

if sys.version_info >= (3, 10):
    # Added in Python 3.10.17, 3.11.12, 3.12.9, 3.13.2 (may still be backported to 3.9)
    def make_quoted_pairs(value: Any) -> str: ...

def quote_string(value: Any) -> str: ...

rfc2047_matcher: Pattern[str]

class TokenList(list[TokenList | Terminal]):
    token_type: str | None
    syntactic_break: bool
    ew_combine_allowed: bool
    defects: list[MessageDefect]
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    @property
    def value(self) -> str: ...
    @property
    def all_defects(self) -> list[MessageDefect]: ...
    def startswith_fws(self) -> bool: ...
    @property
    def as_ew_allowed(self) -> bool:
        """True if all top level tokens of this part may be RFC2047 encoded."""
        ...
    @property
    def comments(self) -> list[str]: ...
    def fold(self, *, policy: Policy) -> str: ...
    def pprint(self, indent: str = "") -> None: ...
    def ppstr(self, indent: str = "") -> str: ...

class WhiteSpaceTokenList(TokenList): ...

class UnstructuredTokenList(TokenList):
    token_type: str

class Phrase(TokenList):
    token_type: str

class Word(TokenList):
    token_type: str

class CFWSList(WhiteSpaceTokenList):
    token_type: str

class Atom(TokenList):
    token_type: str

class Token(TokenList):
    token_type: str
    encode_as_ew: bool

class EncodedWord(TokenList):
    token_type: str
    cte: str | None
    charset: str | None
    lang: str | None

class QuotedString(TokenList):
    token_type: str
    @property
    def content(self) -> str: ...
    @property
    def quoted_value(self) -> str: ...
    @property
    def stripped_value(self) -> str: ...

class BareQuotedString(QuotedString):
    token_type: str

class Comment(WhiteSpaceTokenList):
    token_type: str
    def quote(self, value: Any) -> str: ...
    @property
    def content(self) -> str: ...

class AddressList(TokenList):
    token_type: str
    @property
    def addresses(self) -> list[Address]: ...
    @property
    def mailboxes(self) -> list[Mailbox]: ...
    @property
    def all_mailboxes(self) -> list[Mailbox]: ...

class Address(TokenList):
    token_type: str
    @property
    def display_name(self) -> str: ...
    @property
    def mailboxes(self) -> list[Mailbox]: ...
    @property
    def all_mailboxes(self) -> list[Mailbox]: ...

class MailboxList(TokenList):
    token_type: str
    @property
    def mailboxes(self) -> list[Mailbox]: ...
    @property
    def all_mailboxes(self) -> list[Mailbox]: ...

class GroupList(TokenList):
    token_type: str
    @property
    def mailboxes(self) -> list[Mailbox]: ...
    @property
    def all_mailboxes(self) -> list[Mailbox]: ...

class Group(TokenList):
    token_type: str
    @property
    def mailboxes(self) -> list[Mailbox]: ...
    @property
    def all_mailboxes(self) -> list[Mailbox]: ...
    @property
    def display_name(self) -> str: ...

class NameAddr(TokenList):
    token_type: str
    @property
    def display_name(self) -> str: ...
    @property
    def local_part(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def route(self) -> list[Domain] | None: ...
    @property
    def addr_spec(self) -> str: ...

class AngleAddr(TokenList):
    token_type: str
    @property
    def local_part(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def route(self) -> list[Domain] | None: ...
    @property
    def addr_spec(self) -> str: ...

class ObsRoute(TokenList):
    token_type: str
    @property
    def domains(self) -> list[Domain]: ...

class Mailbox(TokenList):
    token_type: str
    @property
    def display_name(self) -> str: ...
    @property
    def local_part(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def route(self) -> list[str]: ...
    @property
    def addr_spec(self) -> str: ...

class InvalidMailbox(TokenList):
    token_type: str
    @property
    def display_name(self) -> None: ...
    @property
    def local_part(self) -> None: ...
    @property
    def domain(self) -> None: ...
    @property
    def route(self) -> None: ...
    @property
    def addr_spec(self) -> None: ...

class Domain(TokenList):
    token_type: str
    as_ew_allowed: bool
    @property
    def domain(self) -> str: ...

class DotAtom(TokenList):
    token_type: str

class DotAtomText(TokenList):
    token_type: str
    as_ew_allowed: bool

class NoFoldLiteral(TokenList):
    token_type: str
    as_ew_allowed: bool

class AddrSpec(TokenList):
    token_type: str
    as_ew_allowed: bool
    @property
    def local_part(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def addr_spec(self) -> str: ...

class ObsLocalPart(TokenList):
    token_type: str
    as_ew_allowed: bool

class DisplayName(Phrase):
    token_type: str
    @property
    def display_name(self) -> str: ...

class LocalPart(TokenList):
    token_type: str
    as_ew_allowed: bool
    @property
    def local_part(self) -> str: ...

class DomainLiteral(TokenList):
    token_type: str
    as_ew_allowed: bool
    @property
    def domain(self) -> str: ...
    @property
    def ip(self) -> str: ...

class MIMEVersion(TokenList):
    token_type: str
    major: int | None
    minor: int | None

class Parameter(TokenList):
    token_type: str
    sectioned: bool
    extended: bool
    charset: str
    @property
    def section_number(self) -> int: ...
    @property
    def param_value(self) -> str: ...

class InvalidParameter(Parameter):
    token_type: str

class Attribute(TokenList):
    token_type: str
    @property
    def stripped_value(self) -> str: ...

class Section(TokenList):
    token_type: str
    number: int | None

class Value(TokenList):
    token_type: str
    @property
    def stripped_value(self) -> str: ...

class MimeParameters(TokenList):
    token_type: str
    syntactic_break: bool
    @property
    def params(self) -> Iterator[tuple[str, str]]: ...

class ParameterizedHeaderValue(TokenList):
    syntactic_break: bool
    @property
    def params(self) -> Iterable[tuple[str, str]]: ...

class ContentType(ParameterizedHeaderValue):
    token_type: str
    as_ew_allowed: bool
    maintype: str
    subtype: str

class ContentDisposition(ParameterizedHeaderValue):
    token_type: str
    as_ew_allowed: bool
    content_disposition: Any

class ContentTransferEncoding(TokenList):
    token_type: str
    as_ew_allowed: bool
    cte: str

class HeaderLabel(TokenList):
    token_type: str
    as_ew_allowed: bool

class MsgID(TokenList):
    token_type: str
    as_ew_allowed: bool
    def fold(self, policy: Policy) -> str: ...

class MessageID(MsgID):
    token_type: str

class InvalidMessageID(MessageID):
    token_type: str

class Header(TokenList):
    token_type: str

class Terminal(str):
    as_ew_allowed: bool
    ew_combine_allowed: bool
    syntactic_break: bool
    token_type: str
    defects: list[MessageDefect]
    def __new__(cls, value: str, token_type: str) -> Self: ...
    def pprint(self) -> None: ...
    @property
    def all_defects(self) -> list[MessageDefect]: ...
    def pop_trailing_ws(self) -> None: ...
    @property
    def comments(self) -> list[str]: ...
    def __getnewargs__(self) -> tuple[str, str]: ...  # type: ignore[override]

class WhiteSpaceTerminal(Terminal):
    @property
    def value(self) -> str: ...
    def startswith_fws(self) -> bool: ...

class ValueTerminal(Terminal):
    @property
    def value(self) -> ValueTerminal: ...
    def startswith_fws(self) -> bool: ...

class EWWhiteSpaceTerminal(WhiteSpaceTerminal): ...
class _InvalidEwError(HeaderParseError):
    """Invalid encoded word found while parsing headers."""
    ...

DOT: Final[ValueTerminal]
ListSeparator: Final[ValueTerminal]
RouteComponentMarker: Final[ValueTerminal]

def get_fws(value: str) -> tuple[WhiteSpaceTerminal, str]: ...
def get_encoded_word(value: str, terminal_type: str = "vtext") -> tuple[EncodedWord, str]: ...
def get_unstructured(value: str) -> UnstructuredTokenList: ...
def get_qp_ctext(value: str) -> tuple[WhiteSpaceTerminal, str]: ...
def get_qcontent(value: str) -> tuple[ValueTerminal, str]: ...
def get_atext(value: str) -> tuple[ValueTerminal, str]: ...
def get_bare_quoted_string(value: str) -> tuple[BareQuotedString, str]: ...
def get_comment(value: str) -> tuple[Comment, str]: ...
def get_cfws(value: str) -> tuple[CFWSList, str]: ...
def get_quoted_string(value: str) -> tuple[QuotedString, str]: ...
def get_atom(value: str) -> tuple[Atom, str]: ...
def get_dot_atom_text(value: str) -> tuple[DotAtomText, str]: ...
def get_dot_atom(value: str) -> tuple[DotAtom, str]: ...
def get_word(value: str) -> tuple[Any, str]: ...
def get_phrase(value: str) -> tuple[Phrase, str]: ...
def get_local_part(value: str) -> tuple[LocalPart, str]: ...
def get_obs_local_part(value: str) -> tuple[ObsLocalPart, str]: ...
def get_dtext(value: str) -> tuple[ValueTerminal, str]: ...
def get_domain_literal(value: str) -> tuple[DomainLiteral, str]: ...
def get_domain(value: str) -> tuple[Domain, str]: ...
def get_addr_spec(value: str) -> tuple[AddrSpec, str]: ...
def get_obs_route(value: str) -> tuple[ObsRoute, str]: ...
def get_angle_addr(value: str) -> tuple[AngleAddr, str]: ...
def get_display_name(value: str) -> tuple[DisplayName, str]: ...
def get_name_addr(value: str) -> tuple[NameAddr, str]: ...
def get_mailbox(value: str) -> tuple[Mailbox, str]: ...
def get_invalid_mailbox(value: str, endchars: str) -> tuple[InvalidMailbox, str]: ...
def get_mailbox_list(value: str) -> tuple[MailboxList, str]: ...
def get_group_list(value: str) -> tuple[GroupList, str]: ...
def get_group(value: str) -> tuple[Group, str]: ...
def get_address(value: str) -> tuple[Address, str]: ...
def get_address_list(value: str) -> tuple[AddressList, str]: ...
def get_no_fold_literal(value: str) -> tuple[NoFoldLiteral, str]: ...
def get_msg_id(value: str) -> tuple[MsgID, str]: ...
def parse_message_id(value: str) -> MessageID: ...
def parse_mime_version(value: str) -> MIMEVersion: ...
def get_invalid_parameter(value: str) -> tuple[InvalidParameter, str]: ...
def get_ttext(value: str) -> tuple[ValueTerminal, str]: ...
def get_token(value: str) -> tuple[Token, str]: ...
def get_attrtext(value: str) -> tuple[ValueTerminal, str]: ...
def get_attribute(value: str) -> tuple[Attribute, str]: ...
def get_extended_attrtext(value: str) -> tuple[ValueTerminal, str]: ...
def get_extended_attribute(value: str) -> tuple[Attribute, str]: ...
def get_section(value: str) -> tuple[Section, str]: ...
def get_value(value: str) -> tuple[Value, str]: ...
def get_parameter(value: str) -> tuple[Parameter, str]: ...
def parse_mime_parameters(value: str) -> MimeParameters: ...
def parse_content_type_header(value: str) -> ContentType: ...
def parse_content_disposition_header(value: str) -> ContentDisposition: ...
def parse_content_transfer_encoding_header(value: str) -> ContentTransferEncoding: ...
