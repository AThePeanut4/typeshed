"""Text-based visual representations of graphs"""

from _typeshed import Incomplete
from collections.abc import Generator
from typing import ClassVar

__all__ = ["generate_network_text", "write_network_text"]

class BaseGlyphs:
    @classmethod
    def as_dict(cls) -> dict[str, str]: ...

class AsciiBaseGlyphs(BaseGlyphs):
    empty: ClassVar[str]
    newtree_last: ClassVar[str]
    newtree_mid: ClassVar[str]
    endof_forest: ClassVar[str]
    within_forest: ClassVar[str]
    within_tree: ClassVar[str]

class AsciiDirectedGlyphs(AsciiBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

class AsciiUndirectedGlyphs(AsciiBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

class UtfBaseGlyphs(BaseGlyphs):
    empty: ClassVar[str]
    newtree_last: ClassVar[str]
    newtree_mid: ClassVar[str]
    endof_forest: ClassVar[str]
    within_forest: ClassVar[str]
    within_tree: ClassVar[str]

class UtfDirectedGlyphs(UtfBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

class UtfUndirectedGlyphs(UtfBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

def generate_network_text(
    graph, with_labels: bool = True, sources=None, max_depth=None, ascii_only: bool = False, vertical_chains: bool = False
) -> Generator[Incomplete, None, Incomplete]: ...
def write_network_text(
    graph,
    path=None,
    with_labels: bool = True,
    sources=None,
    max_depth=None,
    ascii_only: bool = False,
    end: str = "\n",
    vertical_chains=False,
) -> None:
    """
    Creates a nice text representation of a graph

    This works via a depth-first traversal of the graph and writing a line for
    each unique node encountered. Non-tree edges are written to the right of
    each node, and connection to a non-tree edge is indicated with an ellipsis.
    This representation works best when the input graph is a forest, but any
    graph can be represented.

    Parameters
    ----------
    graph : nx.DiGraph | nx.Graph
        Graph to represent

    path : string or file or callable or None
       Filename or file handle for data output.
       if a function, then it will be called for each generated line.
       if None, this will default to "sys.stdout.write"

    with_labels : bool | str
        If True will use the "label" attribute of a node to display if it
        exists otherwise it will use the node value itself. If given as a
        string, then that attribute name will be used instead of "label".
        Defaults to True.

    sources : List
        Specifies which nodes to start traversal from. Note: nodes that are not
        reachable from one of these sources may not be shown. If unspecified,
        the minimal set of nodes needed to reach all others will be used.

    max_depth : int | None
        The maximum depth to traverse before stopping. Defaults to None.

    ascii_only : Boolean
        If True only ASCII characters are used to construct the visualization

    end : string
        The line ending character

    vertical_chains : Boolean
        If True, chains of nodes will be drawn vertically when possible.

    Examples
    --------
    >>> graph = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
    >>> nx.write_network_text(graph)
    ╙── 0
        ├─╼ 1
        │   ├─╼ 3
        │   └─╼ 4
        └─╼ 2
            ├─╼ 5
            └─╼ 6

    >>> # A near tree with one non-tree edge
    >>> graph.add_edge(5, 1)
    >>> nx.write_network_text(graph)
    ╙── 0
        ├─╼ 1 ╾ 5
        │   ├─╼ 3
        │   └─╼ 4
        └─╼ 2
            ├─╼ 5
            │   └─╼  ...
            └─╼ 6

    >>> graph = nx.cycle_graph(5)
    >>> nx.write_network_text(graph)
    ╙── 0
        ├── 1
        │   └── 2
        │       └── 3
        │           └── 4 ─ 0
        └──  ...

    >>> graph = nx.cycle_graph(5, nx.DiGraph)
    >>> nx.write_network_text(graph, vertical_chains=True)
    ╙── 0 ╾ 4
        ╽
        1
        ╽
        2
        ╽
        3
        ╽
        4
        └─╼  ...

    >>> nx.write_network_text(graph, vertical_chains=True, ascii_only=True)
    +-- 0 <- 4
        !
        1
        !
        2
        !
        3
        !
        4
        L->  ...

    >>> graph = nx.generators.barbell_graph(4, 2)
    >>> nx.write_network_text(graph, vertical_chains=False)
    ╙── 4
        ├── 5
        │   └── 6
        │       ├── 7
        │       │   ├── 8 ─ 6
        │       │   │   └── 9 ─ 6, 7
        │       │   └──  ...
        │       └──  ...
        └── 3
            ├── 0
            │   ├── 1 ─ 3
            │   │   └── 2 ─ 0, 3
            │   └──  ...
            └──  ...
    >>> nx.write_network_text(graph, vertical_chains=True)
    ╙── 4
        ├── 5
        │   │
        │   6
        │   ├── 7
        │   │   ├── 8 ─ 6
        │   │   │   │
        │   │   │   9 ─ 6, 7
        │   │   └──  ...
        │   └──  ...
        └── 3
            ├── 0
            │   ├── 1 ─ 3
            │   │   │
            │   │   2 ─ 0, 3
            │   └──  ...
            └──  ...

    >>> graph = nx.complete_graph(5, create_using=nx.Graph)
    >>> nx.write_network_text(graph)
    ╙── 0
        ├── 1
        │   ├── 2 ─ 0
        │   │   ├── 3 ─ 0, 1
        │   │   │   └── 4 ─ 0, 1, 2
        │   │   └──  ...
        │   └──  ...
        └──  ...

    >>> graph = nx.complete_graph(3, create_using=nx.DiGraph)
    >>> nx.write_network_text(graph)
    ╙── 0 ╾ 1, 2
        ├─╼ 1 ╾ 2
        │   ├─╼ 2 ╾ 0
        │   │   └─╼  ...
        │   └─╼  ...
        └─╼  ...
    """
    ...
