"""
Module for supporting the lxml.etree library. The idea here is to use as much
of the native library as possible, without using fragile hacks like custom element
names that break between releases. The downside of this is that we cannot represent
all possible trees; specifically the following are known to cause problems:

Text or comments as siblings of the root element
Docypes with no name

When any of these things occur, we emit a DataLossWarning
"""

from _typeshed import Incomplete
from typing import Any

from . import base

fullTree: bool
tag_regexp: Any
comment_type: Any

class DocumentType:
    name: Any
    publicId: Any
    systemId: Any
    def __init__(self, name, publicId, systemId) -> None: ...

class Document:
    def __init__(self) -> None: ...
    def appendChild(self, element) -> None: ...
    @property
    def childNodes(self): ...

def testSerializer(element): ...
def tostring(element):
    """Serialize an element and its child nodes to a string"""
    ...

class TreeBuilder(base.TreeBuilder):
    documentClass: Any
    doctypeClass: Any
    elementClass: Any
    commentClass: Any
    fragmentClass: Any
    implementation: Any
    namespaceHTMLElements: Any
    def __init__(self, namespaceHTMLElements, fullTree: bool = False): ...
    insertComment: Any
    initial_comments: Any
    doctype: Any
    def reset(self) -> None: ...
    def testSerializer(self, element): ...
    def getDocument(self): ...
    def getFragment(self): ...
    def insertDoctype(self, token) -> None: ...
    def insertCommentInitial(self, data, parent: Incomplete | None = None) -> None: ...
    def insertCommentMain(self, data, parent: Incomplete | None = None) -> None: ...
    document: Any
    def insertRoot(self, token) -> None: ...
