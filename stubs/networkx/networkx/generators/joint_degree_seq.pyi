from _typeshed import Incomplete
from collections.abc import Mapping, Sequence

from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

from ..classes.graph import Graph

__all__ = ["is_valid_joint_degree", "is_valid_directed_joint_degree", "joint_degree_graph", "directed_joint_degree_graph"]

@_dispatchable
def is_valid_joint_degree(joint_degrees: Mapping[int, Mapping[int, int]]) -> bool:
    """
    Checks whether the given joint degree dictionary is realizable.

    A *joint degree dictionary* is a dictionary of dictionaries, in
    which entry ``joint_degrees[k][l]`` is an integer representing the
    number of edges joining nodes of degree *k* with nodes of degree
    *l*. Such a dictionary is realizable as a simple graph if and only
    if the following conditions are satisfied.

    - each entry must be an integer,
    - the total number of nodes of degree *k*, computed by
      ``sum(joint_degrees[k].values()) / k``, must be an integer,
    - the total number of edges joining nodes of degree *k* with
      nodes of degree *l* cannot exceed the total number of possible edges,
    - each diagonal entry ``joint_degrees[k][k]`` must be even (this is
      a convention assumed by the :func:`joint_degree_graph` function).


    Parameters
    ----------
    joint_degrees :  dictionary of dictionary of integers
        A joint degree dictionary in which entry ``joint_degrees[k][l]``
        is the number of edges joining nodes of degree *k* with nodes of
        degree *l*.

    Returns
    -------
    bool
        Whether the given joint degree dictionary is realizable as a
        simple graph.

    References
    ----------
    .. [1] M. Gjoka, M. Kurant, A. Markopoulou, "2.5K Graphs: from Sampling
       to Generation", IEEE Infocom, 2013.
    .. [2] I. Stanton, A. Pinar, "Constructing and sampling graphs with a
       prescribed joint degree distribution", Journal of Experimental
       Algorithmics, 2012.
    """
    ...
@_dispatchable
def joint_degree_graph(
    joint_degrees: Mapping[int, Mapping[int, int]], seed: int | RandomState | None = None
) -> Graph[Incomplete]: ...
@_dispatchable
def is_valid_directed_joint_degree(
    in_degrees: Sequence[int], out_degrees: Sequence[int], nkk: Mapping[int, Mapping[int, int]]
) -> bool:
    """
    Checks whether the given directed joint degree input is realizable

    Parameters
    ----------
    in_degrees :  list of integers
        in degree sequence contains the in degrees of nodes.
    out_degrees : list of integers
        out degree sequence contains the out degrees of nodes.
    nkk  :  dictionary of dictionary of integers
        directed joint degree dictionary. for nodes of out degree k (first
        level of dict) and nodes of in degree l (second level of dict)
        describes the number of edges.

    Returns
    -------
    boolean
        returns true if given input is realizable, else returns false.

    Notes
    -----
    Here is the list of conditions that the inputs (in/out degree sequences,
    nkk) need to satisfy for simple directed graph realizability:

    - Condition 0: in_degrees and out_degrees have the same length
    - Condition 1: nkk[k][l]  is integer for all k,l
    - Condition 2: sum(nkk[k])/k = number of nodes with partition id k, is an
                   integer and matching degree sequence
    - Condition 3: number of edges and non-chords between k and l cannot exceed
                   maximum possible number of edges


    References
    ----------
    [1] B. Tillman, A. Markopoulou, C. T. Butts & M. Gjoka,
        "Construction of Directed 2K Graphs". In Proc. of KDD 2017.
    """
    ...
@_dispatchable
def directed_joint_degree_graph(
    in_degrees: Sequence[int],
    out_degrees: Sequence[int],
    nkk: Mapping[int, Mapping[int, int]],
    seed: int | RandomState | None = None,
) -> Graph[Incomplete]: ...
