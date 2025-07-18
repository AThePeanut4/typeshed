"""
Utilities for generating random numbers, random sequences, and
random selections.
"""

__all__ = [
    "powerlaw_sequence",
    "zipf_rv",
    "cumulative_distribution",
    "discrete_sequence",
    "random_weighted_sample",
    "weighted_choice",
]

def powerlaw_sequence(n, exponent: float = 2.0, seed=None):
    """Return sample sequence of length n from a power law distribution."""
    ...
def zipf_rv(alpha, xmin: int = 1, seed=None) -> int:
    r"""
    Returns a random value chosen from the Zipf distribution.

    The return value is an integer drawn from the probability distribution

    .. math::

        p(x)=\frac{x^{-\alpha}}{\zeta(\alpha, x_{\min})},

    where $\zeta(\alpha, x_{\min})$ is the Hurwitz zeta function.

    Parameters
    ----------
    alpha : float
      Exponent value of the distribution
    xmin : int
      Minimum value
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    x : int
      Random value from Zipf distribution

    Raises
    ------
    ValueError:
      If xmin < 1 or
      If alpha <= 1

    Notes
    -----
    The rejection algorithm generates random values for a the power-law
    distribution in uniformly bounded expected time dependent on
    parameters.  See [1]_ for details on its operation.

    Examples
    --------
    >>> nx.utils.zipf_rv(alpha=2, xmin=3, seed=42)
    8

    References
    ----------
    .. [1] Luc Devroye, Non-Uniform Random Variate Generation,
       Springer-Verlag, New York, 1986.
    """
    ...
def cumulative_distribution(distribution):
    """Returns normalized cumulative distribution from discrete distribution."""
    ...
def discrete_sequence(n, distribution=None, cdistribution=None, seed=None):
    """
    Return sample sequence of length n from a given discrete distribution
    or discrete cumulative distribution.

    One of the following must be specified.

    distribution = histogram of values, will be normalized

    cdistribution = normalized discrete cumulative distribution
    """
    ...
def random_weighted_sample(mapping, k, seed=None):
    """
    Returns k items without replacement from a weighted sample.

    The input is a dictionary of items with weights as values.
    """
    ...
def weighted_choice(mapping, seed=None):
    """
    Returns a single element from a weighted sample.

    The input is a dictionary of items with weights as values.
    """
    ...
