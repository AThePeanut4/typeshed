"""
This package contains modules for standard tree transforms available
to Docutils components. Tree transforms serve a variety of purposes:

- To tie up certain syntax-specific "loose ends" that remain after the
  initial parsing of the input plaintext. These transforms are used to
  supplement a limited syntax.

- To automate the internal linking of the document tree (hyperlink
  references, footnote references, etc.).

- To extract useful information from the document tree. These
  transforms may be used to construct (for example) indexes and tables
  of contents.

Each transform is an optional step that a Docutils component may
choose to perform on the parsed document.
"""

from _typeshed import Incomplete

from docutils.nodes import Node, document

class Transform:
    """Docutils transform component abstract base class."""
    def __init__(self, document: document, startnode: Node | None = None):
        """Initial setup for in-place document transforms."""
        ...
    def __getattr__(self, name: str, /) -> Incomplete: ...

class Transformer:
    """
    Store "transforms" and apply them to the document tree.

    Collect lists of `Transform` instances and "unknown_reference_resolvers"
    from Docutils components (`TransformSpec` instances).
    Apply collected "transforms" to the document tree.

    Also keeps track of components by component type name.

    https://docutils.sourceforge.io/docs/peps/pep-0258.html#transformer
    """
    def __init__(self, document: document): ...
    def add_transform(self, transform_class: type[Transform], priority: int | None = None, **kwargs) -> None:
        """
        Store a single transform.  Use `priority` to override the default.
        `kwargs` is a dictionary whose contents are passed as keyword
        arguments to the `apply` method of the transform.  This can be used to
        pass application-specific data to the transform instance.
        """
        ...
    def __getattr__(self, name: str, /) -> Incomplete: ...

def __getattr__(name: str) -> Incomplete: ...
