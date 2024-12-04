"""
Subpackages related to graph-minor problems.

In graph theory, an undirected graph H is called a minor of the graph G if H
can be formed from G by deleting edges and vertices and by contracting edges
[1]_.

References
----------
.. [1] https://en.wikipedia.org/wiki/Graph_minor
"""

from networkx.algorithms.minors.contraction import (
    contracted_edge as contracted_edge,
    contracted_nodes as contracted_nodes,
    equivalence_classes as equivalence_classes,
    identified_nodes as identified_nodes,
    quotient_graph as quotient_graph,
)
