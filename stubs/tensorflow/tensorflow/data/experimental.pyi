from collections.abc import Callable, Sequence
from typing import Final, TypeVar

from tensorflow import Tensor
from tensorflow._aliases import TensorCompatible
from tensorflow.data import Dataset

AUTOTUNE: Final = -1
INFINITE_CARDINALITY: Final = -1
SHARD_HINT: Final = -1
UNKNOWN_CARDINALITY: Final = -2

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

def parallel_interleave(
    map_func: Callable[[_T1], Dataset[_T2]],
    cycle_length: int,
    block_length: int = 1,
    sloppy: bool | None = False,
    buffer_output_elements: int | None = None,
    prefetch_input_elements: int | None = None,
) -> Callable[[Dataset[_T1]], Dataset[_T2]]:
    """
    A parallel version of the `Dataset.interleave()` transformation. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use `tf.data.Dataset.interleave(map_func, cycle_length, block_length, num_parallel_calls=tf.data.AUTOTUNE)` instead. If sloppy execution is desired, use `tf.data.Options.deterministic`.

    `parallel_interleave()` maps `map_func` across its input to produce nested
    datasets, and outputs their elements interleaved. Unlike
    `tf.data.Dataset.interleave`, it gets elements from `cycle_length` nested
    datasets in parallel, which increases the throughput, especially in the
    presence of stragglers. Furthermore, the `sloppy` argument can be used to
    improve performance, by relaxing the requirement that the outputs are produced
    in a deterministic order, and allowing the implementation to skip over nested
    datasets whose elements are not readily available when requested.

    Example usage:

    ```python
    # Preprocess 4 files concurrently.
    filenames = tf.data.Dataset.list_files("/path/to/data/train*.tfrecords")
    dataset = filenames.apply(
        tf.data.experimental.parallel_interleave(
            lambda filename: tf.data.TFRecordDataset(filename),
            cycle_length=4))
    ```

    WARNING: If `sloppy` is `True`, the order of produced elements is not
    deterministic.

    Args:
      map_func: A function mapping a nested structure of tensors to a `Dataset`.
      cycle_length: The number of input `Dataset`s to interleave from in parallel.
      block_length: The number of consecutive elements to pull from an input
        `Dataset` before advancing to the next input `Dataset`.
      sloppy: A boolean controlling whether determinism should be traded for
        performance by allowing elements to be produced out of order.  If `sloppy`
        is `None`, the `tf.data.Options.deterministic` dataset option (`True` by
        default) is used to decide whether to enforce a deterministic order.
      buffer_output_elements: The number of elements each iterator being
        interleaved should buffer (similar to the `.prefetch()` transformation for
        each interleaved iterator).
      prefetch_input_elements: The number of input elements to transform to
        iterators before they are needed for interleaving.

    Returns:
      A `Dataset` transformation function, which can be passed to
      `tf.data.Dataset.apply`.
    """
    ...
def enable_debug_mode() -> None:
    """
    Enables debug mode for tf.data.

    Example usage with pdb module:
    ```
    import tensorflow as tf
    import pdb

    tf.data.experimental.enable_debug_mode()

    def func(x):
      # Python 3.7 and older requires `pdb.Pdb(nosigint=True).set_trace()`
      pdb.set_trace()
      x = x + 1
      return x

    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    dataset = dataset.map(func)

    for item in dataset:
      print(item)
    ```

    The effect of debug mode is two-fold:

    1) Any transformations that would introduce asynchrony, parallelism, or
    non-determinism to the input pipeline execution will be forced to execute
    synchronously, sequentially, and deterministically.

    2) Any user-defined functions passed into tf.data transformations such as
    `map` will be wrapped in `tf.py_function` so that their body is executed
    "eagerly" as a Python function as opposed to a traced TensorFlow graph, which
    is the default behavior. Note that even when debug mode is enabled, the
    user-defined function is still traced  to infer the shape and type of its
    outputs; as a consequence, any `print` statements or breakpoints will be
    triggered once during the tracing before the actual execution of the input
    pipeline.

    NOTE: As the debug mode setting affects the construction of the tf.data input
    pipeline, it should be enabled before any tf.data definitions.

    Raises:
      ValueError: When invoked from graph mode.
    """
    ...
def cardinality(dataset: Dataset[object]) -> Tensor:
    """
    Returns the cardinality of `dataset`, if known.

    The operation returns the cardinality of `dataset`. The operation may return
    `tf.data.experimental.INFINITE_CARDINALITY` if `dataset` contains an infinite
    number of elements or `tf.data.experimental.UNKNOWN_CARDINALITY` if the
    analysis fails to determine the number of elements in `dataset` (e.g. when the
    dataset source is a file).

    >>> dataset = tf.data.Dataset.range(42)
    >>> print(tf.data.experimental.cardinality(dataset).numpy())
    42
    >>> dataset = dataset.repeat()
    >>> cardinality = tf.data.experimental.cardinality(dataset)
    >>> print((cardinality == tf.data.experimental.INFINITE_CARDINALITY).numpy())
    True
    >>> dataset = dataset.filter(lambda x: True)
    >>> cardinality = tf.data.experimental.cardinality(dataset)
    >>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
    True

    Args:
      dataset: A `tf.data.Dataset` for which to determine cardinality.

    Returns:
      A scalar `tf.int64` `Tensor` representing the cardinality of `dataset`. If
      the cardinality is infinite or unknown, the operation returns the named
      constant `INFINITE_CARDINALITY` and `UNKNOWN_CARDINALITY` respectively.
    """
    ...
def sample_from_datasets(
    datasets: Sequence[Dataset[_T1]],
    weights: TensorCompatible | None = None,
    seed: int | None = None,
    stop_on_empty_dataset: bool = False,
) -> Dataset[_T1]: ...
def __getattr__(name: str): ...  # incomplete module
