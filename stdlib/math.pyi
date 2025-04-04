"""
This module provides access to the mathematical functions
defined by the C standard.
"""

import sys
from _typeshed import SupportsMul, SupportsRMul
from collections.abc import Iterable
from typing import Any, Final, Literal, Protocol, SupportsFloat, SupportsIndex, TypeVar, overload
from typing_extensions import TypeAlias

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

e: Final[float]
pi: Final[float]
inf: Final[float]
nan: Final[float]
tau: Final[float]

def acos(x: _SupportsFloatOrIndex, /) -> float:
    """
    Return the arc cosine (measured in radians) of x.

    The result is between 0 and pi.
    """
    ...
def acosh(x: _SupportsFloatOrIndex, /) -> float:
    """Return the inverse hyperbolic cosine of x."""
    ...
def asin(x: _SupportsFloatOrIndex, /) -> float:
    """
    Return the arc sine (measured in radians) of x.

    The result is between -pi/2 and pi/2.
    """
    ...
def asinh(x: _SupportsFloatOrIndex, /) -> float:
    """Return the inverse hyperbolic sine of x."""
    ...
def atan(x: _SupportsFloatOrIndex, /) -> float:
    """
    Return the arc tangent (measured in radians) of x.

    The result is between -pi/2 and pi/2.
    """
    ...
def atan2(y: _SupportsFloatOrIndex, x: _SupportsFloatOrIndex, /) -> float:
    """
    Return the arc tangent (measured in radians) of y/x.

    Unlike atan(y/x), the signs of both x and y are considered.
    """
    ...
def atanh(x: _SupportsFloatOrIndex, /) -> float:
    """Return the inverse hyperbolic tangent of x."""
    ...

if sys.version_info >= (3, 11):
    def cbrt(x: _SupportsFloatOrIndex, /) -> float:
        """Return the cube root of x."""
        ...

class _SupportsCeil(Protocol[_T_co]):
    def __ceil__(self) -> _T_co: ...

@overload
def ceil(x: _SupportsCeil[_T], /) -> _T:
    """
    Return the ceiling of x as an Integral.

    This is the smallest integer >= x.
    """
    ...
@overload
def ceil(x: _SupportsFloatOrIndex, /) -> int:
    """
    Return the ceiling of x as an Integral.

    This is the smallest integer >= x.
    """
    ...
def comb(n: SupportsIndex, k: SupportsIndex, /) -> int:
    """
    Number of ways to choose k items from n items without repetition and without order.

    Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
    to zero when k > n.

    Also called the binomial coefficient because it is equivalent
    to the coefficient of k-th term in polynomial expansion of the
    expression (1 + x)**n.

    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.
    """
    ...
def copysign(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float:
    """
    Return a float with the magnitude (absolute value) of x but the sign of y.

    On platforms that support signed zeros, copysign(1.0, -0.0)
    returns -1.0.
    """
    ...
def cos(x: _SupportsFloatOrIndex, /) -> float:
    """Return the cosine of x (measured in radians)."""
    ...
def cosh(x: _SupportsFloatOrIndex, /) -> float:
    """Return the hyperbolic cosine of x."""
    ...
def degrees(x: _SupportsFloatOrIndex, /) -> float:
    """Convert angle x from radians to degrees."""
    ...
def dist(p: Iterable[_SupportsFloatOrIndex], q: Iterable[_SupportsFloatOrIndex], /) -> float:
    """
    Return the Euclidean distance between two points p and q.

    The points should be specified as sequences (or iterables) of
    coordinates.  Both inputs must have the same dimension.

    Roughly equivalent to:
        sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    """
    ...
def erf(x: _SupportsFloatOrIndex, /) -> float:
    """Error function at x."""
    ...
def erfc(x: _SupportsFloatOrIndex, /) -> float:
    """Complementary error function at x."""
    ...
def exp(x: _SupportsFloatOrIndex, /) -> float:
    """Return e raised to the power of x."""
    ...

if sys.version_info >= (3, 11):
    def exp2(x: _SupportsFloatOrIndex, /) -> float:
        """Return 2 raised to the power of x."""
        ...

def expm1(x: _SupportsFloatOrIndex, /) -> float:
    """
    Return exp(x)-1.

    This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    """
    ...
def fabs(x: _SupportsFloatOrIndex, /) -> float:
    """Return the absolute value of the float x."""
    ...
def factorial(x: SupportsIndex, /) -> int:
    """
    Find n!.

    Raise a ValueError if x is negative or non-integral.
    """
    ...

class _SupportsFloor(Protocol[_T_co]):
    def __floor__(self) -> _T_co: ...

@overload
def floor(x: _SupportsFloor[_T], /) -> _T:
    """
    Return the floor of x as an Integral.

    This is the largest integer <= x.
    """
    ...
@overload
def floor(x: _SupportsFloatOrIndex, /) -> int: ...
def fmod(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...
def frexp(x: _SupportsFloatOrIndex, /) -> tuple[float, int]: ...
def fsum(seq: Iterable[_SupportsFloatOrIndex], /) -> float: ...
def gamma(x: _SupportsFloatOrIndex, /) -> float: ...
def gcd(*integers: SupportsIndex) -> int: ...
def hypot(*coordinates: _SupportsFloatOrIndex) -> float: ...
def isclose(
    a: _SupportsFloatOrIndex,
    b: _SupportsFloatOrIndex,
    *,
    rel_tol: _SupportsFloatOrIndex = 1e-09,
    abs_tol: _SupportsFloatOrIndex = 0.0,
) -> bool: ...
def isinf(x: _SupportsFloatOrIndex, /) -> bool: ...
def isfinite(x: _SupportsFloatOrIndex, /) -> bool: ...
def isnan(x: _SupportsFloatOrIndex, /) -> bool: ...
def isqrt(n: SupportsIndex, /) -> int: ...
def lcm(*integers: SupportsIndex) -> int: ...
def ldexp(x: _SupportsFloatOrIndex, i: int, /) -> float: ...
def lgamma(x: _SupportsFloatOrIndex, /) -> float: ...
def log(x: _SupportsFloatOrIndex, base: _SupportsFloatOrIndex = ...) -> float: ...
def log10(x: _SupportsFloatOrIndex, /) -> float: ...
def log1p(x: _SupportsFloatOrIndex, /) -> float: ...
def log2(x: _SupportsFloatOrIndex, /) -> float: ...
def modf(x: _SupportsFloatOrIndex, /) -> tuple[float, float]: ...

if sys.version_info >= (3, 12):
    def nextafter(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /, *, steps: SupportsIndex | None = None) -> float:
        """
        Return the floating-point value the given number of steps after x towards y.

        If steps is not specified or is None, it defaults to 1.

        Raises a TypeError, if x or y is not a double, or if steps is not an integer.
        Raises ValueError if steps is negative.
        """
        ...

else:
    def nextafter(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...

def perm(n: SupportsIndex, k: SupportsIndex | None = None, /) -> int:
    """
    Number of ways to choose k items from n items without repetition and with order.

    Evaluates to n! / (n - k)! when k <= n and evaluates
    to zero when k > n.

    If k is not specified or is None, then k defaults to n
    and the function returns n!.

    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.
    """
    ...
def pow(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float:
    """Return x**y (x to the power of y)."""
    ...

_PositiveInteger: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
_NegativeInteger: TypeAlias = Literal[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]
_LiteralInteger = _PositiveInteger | _NegativeInteger | Literal[0]  # noqa: Y026  # TODO: Use TypeAlias once mypy bugs are fixed

_MultiplicableT1 = TypeVar("_MultiplicableT1", bound=SupportsMul[Any, Any])
_MultiplicableT2 = TypeVar("_MultiplicableT2", bound=SupportsMul[Any, Any])

class _SupportsProdWithNoDefaultGiven(SupportsMul[Any, Any], SupportsRMul[int, Any], Protocol): ...

_SupportsProdNoDefaultT = TypeVar("_SupportsProdNoDefaultT", bound=_SupportsProdWithNoDefaultGiven)

# This stub is based on the type stub for `builtins.sum`.
# Like `builtins.sum`, it cannot be precisely represented in a type stub
# without introducing many false positives.
# For more details on its limitations and false positives, see #13572.
# Instead, just like `builtins.sum`, we explicitly handle several useful cases.
@overload
def prod(iterable: Iterable[bool | _LiteralInteger], /, *, start: int = 1) -> int:
    """
    Calculate the product of all the elements in the input iterable.

    The default start value for the product is 1.

    When the iterable is empty, return the start value.  This function is
    intended specifically for use with numeric values and may reject
    non-numeric types.
    """
    ...
@overload
def prod(iterable: Iterable[_SupportsProdNoDefaultT], /) -> _SupportsProdNoDefaultT | Literal[1]:
    """
    Calculate the product of all the elements in the input iterable.

    The default start value for the product is 1.

    When the iterable is empty, return the start value.  This function is
    intended specifically for use with numeric values and may reject
    non-numeric types.
    """
    ...
@overload
def prod(iterable: Iterable[_MultiplicableT1], /, *, start: _MultiplicableT2) -> _MultiplicableT1 | _MultiplicableT2:
    """
    Calculate the product of all the elements in the input iterable.

    The default start value for the product is 1.

    When the iterable is empty, return the start value.  This function is
    intended specifically for use with numeric values and may reject
    non-numeric types.
    """
    ...
def radians(x: _SupportsFloatOrIndex, /) -> float:
    """Convert angle x from degrees to radians."""
    ...
def remainder(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float:
    """
    Difference between x and the closest integer multiple of y.

    Return x - n*y where n*y is the closest integer multiple of y.
    In the case where x is exactly halfway between two multiples of
    y, the nearest even value of n is used. The result is always exact.
    """
    ...
def sin(x: _SupportsFloatOrIndex, /) -> float:
    """Return the sine of x (measured in radians)."""
    ...
def sinh(x: _SupportsFloatOrIndex, /) -> float:
    """Return the hyperbolic sine of x."""
    ...

if sys.version_info >= (3, 12):
    def sumprod(p: Iterable[float], q: Iterable[float], /) -> float:
        """
        Return the sum of products of values from two iterables p and q.

        Roughly equivalent to:

            sum(itertools.starmap(operator.mul, zip(p, q, strict=True)))

        For float and mixed int/float inputs, the intermediate products
        and sums are computed with extended precision.
        """
        ...

def sqrt(x: _SupportsFloatOrIndex, /) -> float:
    """Return the square root of x."""
    ...
def tan(x: _SupportsFloatOrIndex, /) -> float:
    """Return the tangent of x (measured in radians)."""
    ...
def tanh(x: _SupportsFloatOrIndex, /) -> float:
    """Return the hyperbolic tangent of x."""
    ...

# Is different from `_typeshed.SupportsTrunc`, which is not generic
class _SupportsTrunc(Protocol[_T_co]):
    def __trunc__(self) -> _T_co: ...

def trunc(x: _SupportsTrunc[_T], /) -> _T: ...
def ulp(x: _SupportsFloatOrIndex, /) -> float: ...

if sys.version_info >= (3, 13):
    def fma(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, z: _SupportsFloatOrIndex, /) -> float:
        """
        Fused multiply-add operation.

        Compute (x * y) + z with a single round.
        """
        ...
