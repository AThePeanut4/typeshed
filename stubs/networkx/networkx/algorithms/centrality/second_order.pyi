"""
Copyright (c) 2015 – Thomson Licensing, SAS

Redistribution and use in source and binary forms, with or without
modification, are permitted (subject to the limitations in the
disclaimer below) provided that the following conditions are met:

* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

* Neither the name of Thomson Licensing, or Technicolor, nor the names
of its contributors may be used to endorse or promote products derived
from this software without specific prior written permission.

NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE
GRANTED BY THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT
HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["second_order_centrality"]

@_dispatchable
def second_order_centrality(G: Graph[_Node], weight: str | None = "weight") -> dict[Incomplete, float]:
    """
    Compute the second order centrality for nodes of G.

    The second order centrality of a given node is the standard deviation of
    the return times to that node of a perpetual random walk on G:

    Parameters
    ----------
    G : graph
      A NetworkX connected and undirected graph.

    weight : string or None, optional (default="weight")
        The name of an edge attribute that holds the numerical value
        used as a weight. If None then each edge has weight 1.

    Returns
    -------
    nodes : dictionary
       Dictionary keyed by node with second order centrality as the value.

    Examples
    --------
    >>> G = nx.star_graph(10)
    >>> soc = nx.second_order_centrality(G)
    >>> print(sorted(soc.items(), key=lambda x: x[1])[0][0])  # pick first id
    0

    Raises
    ------
    NetworkXException
        If the graph G is empty, non connected or has negative weights.

    See Also
    --------
    betweenness_centrality

    Notes
    -----
    Lower values of second order centrality indicate higher centrality.

    The algorithm is from Kermarrec, Le Merrer, Sericola and Trédan [1]_.

    This code implements the analytical version of the algorithm, i.e.,
    there is no simulation of a random walk process involved. The random walk
    is here unbiased (corresponding to eq 6 of the paper [1]_), thus the
    centrality values are the standard deviations for random walk return times
    on the transformed input graph G (equal in-degree at each nodes by adding
    self-loops).

    Complexity of this implementation, made to run locally on a single machine,
    is O(n^3), with n the size of G, which makes it viable only for small
    graphs.

    References
    ----------
    .. [1] Anne-Marie Kermarrec, Erwan Le Merrer, Bruno Sericola, Gilles Trédan
       "Second order centrality: Distributed assessment of nodes criticity in
       complex networks", Elsevier Computer Communications 34(5):619-628, 2011.
    """
    ...
