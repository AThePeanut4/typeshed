"""Trophic levels"""

from _typeshed import Incomplete

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

__all__ = ["trophic_levels", "trophic_differences", "trophic_incoherence_parameter"]

@_dispatchable
def trophic_levels(G: DiGraph[_Node], weight="weight") -> dict[Incomplete, Incomplete]:
    r"""
    Compute the trophic levels of nodes.

    The trophic level of a node $i$ is

    .. math::

        s_i = 1 + \frac{1}{k^{in}_i} \sum_{j} a_{ij} s_j

    where $k^{in}_i$ is the in-degree of i

    .. math::

        k^{in}_i = \sum_{j} a_{ij}

    and nodes with $k^{in}_i = 0$ have $s_i = 1$ by convention.

    These are calculated using the method outlined in Levine [1]_.

    Parameters
    ----------
    G : DiGraph
        A directed networkx graph

    Returns
    -------
    nodes : dict
        Dictionary of nodes with trophic level as the value.

    References
    ----------
    .. [1] Stephen Levine (1980) J. theor. Biol. 83, 195-207
    """
    ...
@_dispatchable
def trophic_differences(G: DiGraph[_Node], weight="weight") -> dict[Incomplete, Incomplete]:
    """
    Compute the trophic differences of the edges of a directed graph.

    The trophic difference $x_ij$ for each edge is defined in Johnson et al.
    [1]_ as:

    .. math::
        x_ij = s_j - s_i

    Where $s_i$ is the trophic level of node $i$.

    Parameters
    ----------
    G : DiGraph
        A directed networkx graph

    Returns
    -------
    diffs : dict
        Dictionary of edges with trophic differences as the value.

    References
    ----------
    .. [1] Samuel Johnson, Virginia Dominguez-Garcia, Luca Donetti, Miguel A.
        Munoz (2014) PNAS "Trophic coherence determines food-web stability"
    """
    ...
@_dispatchable
def trophic_incoherence_parameter(G: DiGraph[_Node], weight="weight", cannibalism: bool = False) -> float:
    """
    Compute the trophic incoherence parameter of a graph.

    Trophic coherence is defined as the homogeneity of the distribution of
    trophic distances: the more similar, the more coherent. This is measured by
    the standard deviation of the trophic differences and referred to as the
    trophic incoherence parameter $q$ by [1].

    Parameters
    ----------
    G : DiGraph
        A directed networkx graph

    cannibalism: Boolean
        If set to False, self edges are not considered in the calculation

    Returns
    -------
    trophic_incoherence_parameter : float
        The trophic coherence of a graph

    References
    ----------
    .. [1] Samuel Johnson, Virginia Dominguez-Garcia, Luca Donetti, Miguel A.
        Munoz (2014) PNAS "Trophic coherence determines food-web stability"
    """
    ...
