from _typeshed import Incomplete
from collections.abc import Sequence

from networkx.utils.backends import _dispatchable

__all__ = ["combinatorial_embedding_to_pos"]

@_dispatchable
def combinatorial_embedding_to_pos(embedding, fully_triangulate: bool = False) -> dict[Incomplete, Incomplete]: ...
def set_position(parent, tree, remaining_nodes, delta_x, y_coordinate, pos): ...
def get_canonical_ordering(embedding, outer_face: Sequence[Incomplete]) -> list[Incomplete]: ...
def triangulate_face(embedding, v1, v2): ...
def triangulate_embedding(embedding, fully_triangulate: bool = True): ...
def make_bi_connected(
    embedding, starting_node, outgoing_node, edges_counted: set[tuple[Incomplete, Incomplete]]
) -> list[Incomplete]:
    """
    Triangulate a face and make it 2-connected

    This method also adds all edges on the face to `edges_counted`.

    Parameters
    ----------
    embedding: nx.PlanarEmbedding
        The embedding that defines the faces
    starting_node : node
        A node on the face
    outgoing_node : node
        A node such that the half edge (starting_node, outgoing_node) belongs
        to the face
    edges_counted: set
        Set of all half-edges that belong to a face that have been visited

    Returns
    -------
    face_nodes: list
        A list of all nodes at the border of this face
    """
    ...
