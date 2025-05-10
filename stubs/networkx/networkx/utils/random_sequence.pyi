"""
Utilities for generating random numbers, random sequences, and
random selections.
"""

from _typeshed import Incomplete

__all__ = [
    "powerlaw_sequence",
    "zipf_rv",
    "cumulative_distribution",
    "discrete_sequence",
    "random_weighted_sample",
    "weighted_choice",
]

def powerlaw_sequence(n, exponent: float = 2.0, seed: Incomplete | None = None): ...
def zipf_rv(alpha, xmin: int = 1, seed: Incomplete | None = None): ...
def cumulative_distribution(distribution): ...
def discrete_sequence(
    n, distribution: Incomplete | None = None, cdistribution: Incomplete | None = None, seed: Incomplete | None = None
):
    """
    Return sample sequence of length n from a given discrete distribution
    or discrete cumulative distribution.

    One of the following must be specified.

    distribution = histogram of values, will be normalized

    cdistribution = normalized discrete cumulative distribution
    """
    ...
def random_weighted_sample(mapping, k, seed: Incomplete | None = None):
    """
    Returns k items without replacement from a weighted sample.

    The input is a dictionary of items with weights as values.
    """
    ...
def weighted_choice(mapping, seed: Incomplete | None = None):
    """
    Returns a single element from a weighted sample.

    The input is a dictionary of items with weights as values.
    """
    ...
