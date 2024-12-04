"""
DEPRECATED Example code for lxml.etree protection

The code has NO protection against decompression bombs.
"""

import threading
from _typeshed import Incomplete

# Not bothering with types here as lxml support is supposed to be dropped in a future version
# of defusedxml

LXML3: Incomplete
__origin__: str
tostring: Incomplete

# Should be imported from lxml.etree.ElementBase, but lxml lacks types
class _ElementBase: ...

class RestrictedElement(_ElementBase):
    """A restricted Element class that filters out instances of some classes"""
    blacklist: Incomplete
    def __iter__(self): ...
    def iterchildren(self, tag: Incomplete | None = ..., reversed: bool = ...): ...
    def iter(self, tag: Incomplete | None = ..., *tags): ...
    def iterdescendants(self, tag: Incomplete | None = ..., *tags): ...
    def itersiblings(self, tag: Incomplete | None = ..., preceding: bool = ...): ...
    def getchildren(self): ...
    def getiterator(self, tag: Incomplete | None = ...): ...

class GlobalParserTLS(threading.local):
    """Thread local context for custom parser instances"""
    parser_config: Incomplete
    element_class: Incomplete
    def createDefaultParser(self): ...
    def setDefaultParser(self, parser) -> None: ...
    def getDefaultParser(self): ...

getDefaultParser: Incomplete

def check_docinfo(elementtree, forbid_dtd: bool = ..., forbid_entities: bool = ...) -> None:
    """
    Check docinfo of an element tree for DTD and entity declarations

    The check for entity declarations needs lxml 3 or newer. lxml 2.x does
    not support dtd.iterentities().
    """
    ...
def parse(
    source,
    parser: Incomplete | None = ...,
    base_url: Incomplete | None = ...,
    forbid_dtd: bool = ...,
    forbid_entities: bool = ...,
): ...
def fromstring(
    text, parser: Incomplete | None = ..., base_url: Incomplete | None = ..., forbid_dtd: bool = ..., forbid_entities: bool = ...
): ...

XML = fromstring

def iterparse(*args, **kwargs) -> None: ...
