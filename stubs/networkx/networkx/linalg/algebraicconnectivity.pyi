from networkx.utils.backends import _dispatchable

__all__ = ["algebraic_connectivity", "fiedler_vector", "spectral_ordering", "spectral_bisection"]

class _PCGSolver:
    """
    Preconditioned conjugate gradient method.

    To solve Ax = b:
        M = A.diagonal() # or some other preconditioner
        solver = _PCGSolver(lambda x: A * x, lambda x: M * x)
        x = solver.solve(b)

    The inputs A and M are functions which compute
    matrix multiplication on the argument.
    A - multiply by the matrix A in Ax=b
    M - multiply by M, the preconditioner surrogate for A

    Warning: There is no limit on number of iterations.
    """
    def __init__(self, A, M) -> None: ...
    def solve(self, B, tol): ...

class _LUSolver:
    """
    LU factorization.

    To solve Ax = b:
        solver = _LUSolver(A)
        x = solver.solve(b)

    optional argument `tol` on solve method is ignored but included
    to match _PCGsolver API.
    """
    def __init__(self, A) -> None: ...
    def solve(self, B, tol=None): ...

@_dispatchable
def algebraic_connectivity(
    G, weight: str = "weight", normalized: bool = False, tol: float = 1e-08, method: str = "tracemin_pcg", seed=None
): ...
@_dispatchable
def fiedler_vector(
    G, weight: str = "weight", normalized: bool = False, tol: float = 1e-08, method: str = "tracemin_pcg", seed=None
): ...
@_dispatchable
def spectral_ordering(
    G, weight: str = "weight", normalized: bool = False, tol: float = 1e-08, method: str = "tracemin_pcg", seed=None
): ...
@_dispatchable
def spectral_bisection(
    G, weight: str = "weight", normalized: bool = False, tol: float = 1e-08, method: str = "tracemin_pcg", seed=None
): ...
