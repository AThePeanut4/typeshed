from _typeshed import Incomplete
from typing import Any

Marker: Any
listElementsMap: Any

class Node:
    """Represents an item in the tree"""
    name: Any
    parent: Any
    value: Any
    attributes: Any
    childNodes: Any
    def __init__(self, name) -> None:
        """
        Creates a Node

        :arg name: The tag name associated with the node
        """
        ...
    def appendChild(self, node) -> None:
        """
        Insert node as a child of the current node

        :arg node: the node to insert
        """
        ...
    def insertText(self, data, insertBefore: Incomplete | None = None) -> None:
        """
        Insert data as text in the current node, positioned before the
        start of node insertBefore or to the end of the node's text.

        :arg data: the data to insert

        :arg insertBefore: True if you want to insert the text before the node
            and False if you want to insert it after the node
        """
        ...
    def insertBefore(self, node, refNode) -> None:
        """
        Insert node as a child of the current node, before refNode in the
        list of child nodes. Raises ValueError if refNode is not a child of
        the current node

        :arg node: the node to insert

        :arg refNode: the child node to insert the node before
        """
        ...
    def removeChild(self, node) -> None:
        """
        Remove node from the children of the current node

        :arg node: the child node to remove
        """
        ...
    def reparentChildren(self, newParent) -> None:
        """
        Move all the children of the current node to newParent.
        This is needed so that trees that don't store text as nodes move the
        text in the correct way

        :arg newParent: the node to move all this node's children to
        """
        ...
    def cloneNode(self) -> None:
        """
        Return a shallow copy of the current node i.e. a node with the same
        name and attributes but with no parent or child nodes
        """
        ...
    def hasContent(self) -> None:
        """
        Return true if the node has children or text, false otherwise
        
        """
        ...

class ActiveFormattingElements(list[Any]):
    def append(self, node) -> None: ...
    def nodesEqual(self, node1, node2): ...

class TreeBuilder:
    """
    Base treebuilder implementation

    * documentClass - the class to use for the bottommost node of a document
    * elementClass - the class to use for HTML Elements
    * commentClass - the class to use for comments
    * doctypeClass - the class to use for doctypes
    """
    documentClass: Any
    elementClass: Any
    commentClass: Any
    doctypeClass: Any
    fragmentClass: Any
    defaultNamespace: str
    def __init__(self, namespaceHTMLElements) -> None:
        """
        Create a TreeBuilder

        :arg namespaceHTMLElements: whether or not to namespace HTML elements
        """
        ...
    openElements: Any
    activeFormattingElements: Any
    headPointer: Any
    formPointer: Any
    insertFromTable: bool
    document: Any
    def reset(self) -> None: ...
    def elementInScope(self, target, variant: Incomplete | None = None): ...
    def reconstructActiveFormattingElements(self) -> None: ...
    def clearActiveFormattingElements(self) -> None: ...
    def elementInActiveFormattingElements(self, name):
        """
        Check if an element exists between the end of the active
        formatting elements and the last marker. If it does, return it, else
        return false
        """
        ...
    def insertRoot(self, token) -> None: ...
    def insertDoctype(self, token) -> None: ...
    def insertComment(self, token, parent: Incomplete | None = None) -> None: ...
    def createElement(self, token):
        """Create an element but don't insert it anywhere"""
        ...
    def insertElementNormal(self, token): ...
    def insertElementTable(self, token):
        """Create an element and insert it into the tree"""
        ...
    def insertText(self, data, parent: Incomplete | None = None) -> None:
        """Insert text data."""
        ...
    def getTableMisnestedNodePosition(self):
        """
        Get the foster parent element, and sibling to insert before
        (or None) when inserting a misnested table node
        """
        ...
    def generateImpliedEndTags(self, exclude: Incomplete | None = None) -> None: ...
    def getDocument(self):
        """Return the final tree"""
        ...
    def getFragment(self):
        """Return the final fragment"""
        ...
    def testSerializer(self, node) -> None:
        """
        Serialize the subtree of node in the format required by unit tests

        :arg node: the node from which to start serializing
        """
        ...
