from _typeshed import Incomplete

__all__ = ["DOCUMENT", "DOCTYPE", "TEXT", "ELEMENT", "COMMENT", "ENTITY", "UNKNOWN", "TreeWalker", "NonRecursiveTreeWalker"]

DOCUMENT: int
DOCTYPE: int
TEXT: int
ELEMENT: int
COMMENT: int
ENTITY: int
UNKNOWN: str
spaceCharacters: str

class TreeWalker:
    """
    Walks a tree yielding tokens

    Tokens are dicts that all have a ``type`` field specifying the type of the
    token.
    """
    tree: Incomplete
    def __init__(self, tree) -> None:
        """
        Creates a TreeWalker

        :arg tree: the tree to walk
        """
        ...
    def __iter__(self): ...
    def error(self, msg):
        """
        Generates an error token with the given message

        :arg msg: the error message

        :returns: SerializeError token
        """
        ...
    def emptyTag(self, namespace, name, attrs, hasChildren: bool = False) -> None:
        """
        Generates an EmptyTag token

        :arg namespace: the namespace of the token--can be ``None``

        :arg name: the name of the element

        :arg attrs: the attributes of the element as a dict

        :arg hasChildren: whether or not to yield a SerializationError because
            this tag shouldn't have children

        :returns: EmptyTag token
        """
        ...
    def startTag(self, namespace, name, attrs):
        """
        Generates a StartTag token

        :arg namespace: the namespace of the token--can be ``None``

        :arg name: the name of the element

        :arg attrs: the attributes of the element as a dict

        :returns: StartTag token
        """
        ...
    def endTag(self, namespace, name):
        """
        Generates an EndTag token

        :arg namespace: the namespace of the token--can be ``None``

        :arg name: the name of the element

        :returns: EndTag token
        """
        ...
    def text(self, data) -> None:
        """
        Generates SpaceCharacters and Characters tokens

        Depending on what's in the data, this generates one or more
        ``SpaceCharacters`` and ``Characters`` tokens.

        For example:

            >>> from html5lib.treewalkers.base import TreeWalker
            >>> # Give it an empty tree just so it instantiates
            >>> walker = TreeWalker([])
            >>> list(walker.text(''))
            []
            >>> list(walker.text('  '))
            [{u'data': '  ', u'type': u'SpaceCharacters'}]
            >>> list(walker.text(' abc '))  # doctest: +NORMALIZE_WHITESPACE
            [{u'data': ' ', u'type': u'SpaceCharacters'},
            {u'data': u'abc', u'type': u'Characters'},
            {u'data': u' ', u'type': u'SpaceCharacters'}]

        :arg data: the text data

        :returns: one or more ``SpaceCharacters`` and ``Characters`` tokens
        """
        ...
    def comment(self, data):
        """
        Generates a Comment token

        :arg data: the comment

        :returns: Comment token
        """
        ...
    def doctype(self, name, publicId=None, systemId=None):
        """
        Generates a Doctype token

        :arg name:

        :arg publicId:

        :arg systemId:

        :returns: the Doctype token
        """
        ...
    def entity(self, name):
        """
        Generates an Entity token

        :arg name: the entity name

        :returns: an Entity token
        """
        ...
    def unknown(self, nodeType):
        """Handles unknown node types"""
        ...

class NonRecursiveTreeWalker(TreeWalker):
    def getNodeDetails(self, node) -> None: ...
    def getFirstChild(self, node) -> None: ...
    def getNextSibling(self, node) -> None: ...
    def getParentNode(self, node) -> None: ...
    def __iter__(self): ...
