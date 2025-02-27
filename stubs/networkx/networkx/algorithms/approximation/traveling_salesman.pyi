"""
=================================
Travelling Salesman Problem (TSP)
=================================

Implementation of approximate algorithms
for solving and approximating the TSP problem.

Categories of algorithms which are implemented:

- Christofides (provides a 3/2-approximation of TSP)
- Greedy
- Simulated Annealing (SA)
- Threshold Accepting (TA)
- Asadpour Asymmetric Traveling Salesman Algorithm

The Travelling Salesman Problem tries to find, given the weight
(distance) between all points where a salesman has to visit, the
route so that:

- The total distance (cost) which the salesman travels is minimized.
- The salesman returns to the starting point.
- Note that for a complete graph, the salesman visits each point once.

The function `travelling_salesman_problem` allows for incomplete
graphs by finding all-pairs shortest paths, effectively converting
the problem to a complete graph problem. It calls one of the
approximate methods on that problem and then converts the result
back to the original graph using the previously found shortest paths.

TSP is an NP-hard problem in combinatorial optimization,
important in operations research and theoretical computer science.

http://en.wikipedia.org/wiki/Travelling_salesman_problem
"""

from _typeshed import Incomplete
from collections.abc import Callable

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def christofides(G: Graph[_Node], weight: str | None = "weight", tree: Graph[_Node] | None = None): ...
@_dispatchable
def traveling_salesman_problem(
    G: Graph[_Node],
    weight: str = "weight",
    nodes=None,
    cycle: bool = True,
    method: Callable[..., Incomplete] | None = None,
    **kwargs,
): ...
@_dispatchable
def asadpour_atsp(
    G: DiGraph[_Node], weight: str | None = "weight", seed: int | RandomState | None = None, source: str | None = None
): ...
@_dispatchable
def greedy_tsp(G: Graph[_Node], weight: str | None = "weight", source=None): ...
@_dispatchable
def simulated_annealing_tsp(
    G: Graph[_Node],
    init_cycle,
    weight: str | None = "weight",
    source=None,
    temp: int | None = 100,
    move="1-1",
    max_iterations: int | None = 10,
    N_inner: int | None = 100,
    alpha=0.01,
    seed: int | RandomState | None = None,
): ...
@_dispatchable
def threshold_accepting_tsp(
    G: Graph[_Node],
    init_cycle,
    weight: str | None = "weight",
    source=None,
    threshold: int | None = 1,
    move="1-1",
    max_iterations: int | None = 10,
    N_inner: int | None = 100,
    alpha=0.1,
    seed: int | RandomState | None = None,
): ...
