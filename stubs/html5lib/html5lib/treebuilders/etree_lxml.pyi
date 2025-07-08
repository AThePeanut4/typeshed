"""
Module for supporting the lxml.etree library. The idea here is to use as much
of the native library as possible, without using fragile hacks like custom element
names that break between releases. The downside of this is that we cannot represent
all possible trees; specifically the following are known to cause problems:

Text or comments as siblings of the root element
Docypes with no name

When any of these things occur, we emit a DataLossWarning
"""

import re
from _typeshed import Incomplete

from . import base

fullTree: bool
tag_regexp: re.Pattern[str]
comment_type: Incomplete

class DocumentType:
    name: Incomplete
    publicId: Incomplete
    systemId: Incomplete
    def __init__(self, name, publicId, systemId) -> None: ...

class Document:
    def __init__(self) -> None: ...
    def appendChild(self, element) -> None: ...
    @property
    def childNodes(self): ...

def testSerializer(element) -> str: ...
def tostring(element) -> str:
    """Serialize an element and its child nodes to a string"""
    ...

class TreeBuilder(base.TreeBuilder):
    documentClass: Incomplete
    doctypeClass: Incomplete
    elementClass: Incomplete
    commentClass: Incomplete
    fragmentClass: Incomplete
    implementation: Incomplete
    namespaceHTMLElements: Incomplete
    def __init__(self, namespaceHTMLElements, fullTree: bool = False): ...
    insertComment: Incomplete
    initial_comments: Incomplete
    doctype: Incomplete
    def reset(self) -> None: ...
    def testSerializer(self, element): ...
    def getDocument(self): ...
    def getFragment(self): ...
    def insertDoctype(self, token) -> None: ...
    def insertCommentInitial(self, data, parent=None) -> None: ...
    def insertCommentMain(self, data, parent=None) -> None: ...
    document: Incomplete
    def insertRoot(self, token) -> None: ...
