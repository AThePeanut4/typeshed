from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["rooted_tree_isomorphism", "tree_isomorphism"]

@_dispatchable
def root_trees(t1, root1, t2, root2):
    """
    Create a single digraph dT of free trees t1 and t2
    #   with roots root1 and root2 respectively
    # rename the nodes with consecutive integers
    # so that all nodes get a unique name between both trees

    # our new "fake" root node is 0
    # t1 is numbers from 1 ... n
    # t2 is numbered from n+1 to 2n
    """
    ...
@_dispatchable
def rooted_tree_isomorphism(t1, root1, t2, root2) -> list[tuple[Incomplete, Incomplete]]: ...
@_dispatchable
def tree_isomorphism(t1: Graph[_Node], t2: Graph[_Node]) -> list[tuple[Incomplete, Incomplete]]: ...
