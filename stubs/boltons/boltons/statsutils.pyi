from _typeshed import ConvertibleToFloat, Incomplete
from collections.abc import Callable, Iterable, Iterator
from typing import Any, Literal, overload
from typing_extensions import Self

class _StatsProperty:
    name: str
    func: Callable[..., Any]
    internal_name: str
    __doc__: str | None
    def __init__(self, name: str, func: Callable[..., Any]) -> None: ...
    @overload
    def __get__(self, obj: None, objtype: object = None) -> Self: ...
    @overload
    def __get__(self, obj: Stats, objtype: object = None) -> float: ...

class Stats:
    """
    The ``Stats`` type is used to represent a group of unordered
    statistical datapoints for calculations such as mean, median, and
    variance.

    Args:

        data (list): List or other iterable containing numeric values.
        default (float): A value to be returned when a given
            statistical measure is not defined. 0.0 by default, but
            ``float('nan')`` is appropriate for stricter applications.
        use_copy (bool): By default Stats objects copy the initial
            data into a new list to avoid issues with
            modifications. Pass ``False`` to disable this behavior.
        is_sorted (bool): Presorted data can skip an extra sorting
            step for a little speed boost. Defaults to False.
    """
    data: list[float]
    default: float
    @overload
    def __init__(self, data: list[float], default: float = 0.0, *, use_copy: Literal[False], is_sorted: bool = False) -> None: ...
    @overload
    def __init__(self, data: list[float], default: float, use_copy: Literal[False], is_sorted: bool = False) -> None: ...
    @overload
    def __init__(
        self, data: Iterable[float], default: float = 0.0, use_copy: Literal[True] = True, is_sorted: bool = False
    ) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[float]: ...
    def clear_cache(self) -> None:
        """
        ``Stats`` objects automatically cache intermediary calculations
        that can be reused. For instance, accessing the ``std_dev``
        attribute after the ``variance`` attribute will be
        significantly faster for medium-to-large datasets.

        If you modify the object by adding additional data points,
        call this function to have the cached statistics recomputed.
        """
        ...
    count: _StatsProperty
    mean: _StatsProperty
    max: _StatsProperty
    min: _StatsProperty
    median: _StatsProperty
    iqr: _StatsProperty
    trimean: _StatsProperty
    variance: _StatsProperty
    std_dev: _StatsProperty
    median_abs_dev: _StatsProperty
    mad: _StatsProperty
    rel_std_dev: _StatsProperty
    skewness: _StatsProperty
    kurtosis: _StatsProperty
    pearson_type: _StatsProperty
    def get_quantile(self, q: ConvertibleToFloat) -> float: ...
    def get_zscore(self, value: float) -> float: ...
    def trim_relative(self, amount: float = 0.15) -> None: ...
    def get_histogram_counts(self, bins: int | list[float] | None = None, **kw) -> list[tuple[float, int]]: ...
    def format_histogram(self, bins: int | list[float] | None = None, **kw) -> str: ...
    def describe(
        self, quantiles: Iterable[float] | None = None, format: str | None = None
    ) -> dict[str, float] | list[tuple[str, float]] | str: ...

def describe(
    data: Iterable[float], quantiles: Iterable[float] | None = None, format: str | None = None
) -> dict[str, float] | list[tuple[str, float]] | str: ...

mean: Incomplete
median: Incomplete
iqr: Incomplete
trimean: Incomplete
variance: Incomplete
std_dev: Incomplete
median_abs_dev: Incomplete
rel_std_dev: Incomplete
skewness: Incomplete
kurtosis: Incomplete
pearson_type: Incomplete

def format_histogram_counts(
    bin_counts: list[float], width: int | None = None, format_bin: Callable[..., Any] | None = None
) -> str:
    """
    The formatting logic behind :meth:`Stats.format_histogram`, which
    takes the output of :meth:`Stats.get_histogram_counts`, and passes
    them to this function.

    Args:
        bin_counts (list): A list of bin values to counts.
        width (int): Number of character columns in the text output,
            defaults to 80 or console width in Python 3.3+.
        format_bin (callable): Used to convert bin values into string
            labels.
    """
    ...
