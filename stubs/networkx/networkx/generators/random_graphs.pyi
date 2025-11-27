"""Generators for random graphs."""

from _typeshed import Incomplete
from typing_extensions import deprecated

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = [
    "fast_gnp_random_graph",
    "gnp_random_graph",
    "dense_gnm_random_graph",
    "gnm_random_graph",
    "erdos_renyi_graph",
    "binomial_graph",
    "newman_watts_strogatz_graph",
    "watts_strogatz_graph",
    "connected_watts_strogatz_graph",
    "random_regular_graph",
    "barabasi_albert_graph",
    "dual_barabasi_albert_graph",
    "extended_barabasi_albert_graph",
    "powerlaw_cluster_graph",
    "random_lobster",
    "random_lobster_graph",
    "random_shell_graph",
    "random_powerlaw_tree",
    "random_powerlaw_tree_sequence",
    "random_kernel_graph",
]

@_dispatchable
def fast_gnp_random_graph(n, p, seed=None, directed: bool = False, *, create_using=None): ...
@_dispatchable
def gnp_random_graph(n, p, seed=None, directed: bool = False, *, create_using=None): ...

binomial_graph = gnp_random_graph
erdos_renyi_graph = gnp_random_graph

@_dispatchable
def dense_gnm_random_graph(n, m, seed=None, *, create_using=None): ...
@_dispatchable
def gnm_random_graph(n, m, seed=None, directed: bool = False, *, create_using=None): ...
@_dispatchable
def newman_watts_strogatz_graph(n, k, p, seed=None, *, create_using=None): ...
@_dispatchable
def watts_strogatz_graph(n, k, p, seed=None, *, create_using=None): ...
@_dispatchable
def connected_watts_strogatz_graph(n, k, p, tries: int = 100, seed=None, *, create_using=None): ...
@_dispatchable
def random_regular_graph(d, n, seed=None, *, create_using=None): ...
@_dispatchable
def barabasi_albert_graph(n, m, seed=None, initial_graph=None, *, create_using=None) -> Graph[Incomplete]: ...
@_dispatchable
def dual_barabasi_albert_graph(n, m1, m2, p, seed=None, initial_graph=None, *, create_using=None) -> Graph[Incomplete]: ...
@_dispatchable
def extended_barabasi_albert_graph(n, m, p, q, seed=None, *, create_using=None) -> Graph[Incomplete]: ...
@_dispatchable
def powerlaw_cluster_graph(n, m, p, seed=None, *, create_using=None): ...
@_dispatchable
def random_lobster_graph(n, p1, p2, seed=None, *, create_using=None): ...
@_dispatchable
@deprecated("`random_lobster` is a deprecated alias for `random_lobster_graph`. Use `random_lobster_graph` instead.")
def random_lobster(n, p1, p2, seed=None, *, create_using=None): ...
@_dispatchable
def random_shell_graph(constructor, seed=None, *, create_using=None): ...
@_dispatchable
def random_powerlaw_tree(n, gamma: float = 3, seed=None, tries: int = 100, *, create_using=None): ...
@_dispatchable
def random_powerlaw_tree_sequence(n, gamma: float = 3, seed=None, tries: int = 100):
    """
    Returns a degree sequence for a tree with a power law distribution.

    Parameters
    ----------
    n : int,
        The number of nodes.
    gamma : float
        Exponent of the power law.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.
    tries : int
        Number of attempts to adjust the sequence to make it a tree.

    Raises
    ------
    NetworkXError
        If no valid sequence is found within the maximum number of
        attempts.

    Notes
    -----
    A trial power law degree sequence is chosen and then elements are
    swapped with new elements from a power law distribution until
    the sequence makes a tree (by checking, for example, that the number of
    edges is one smaller than the number of nodes).
    """
    ...
@_dispatchable
def random_kernel_graph(n, kernel_integral, kernel_root=None, seed=None, *, create_using=None): ...
