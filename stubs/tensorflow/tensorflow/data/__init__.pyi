"""Public API for tf._api.v2.data namespace"""

from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable, Collection, Iterator as _Iterator, Sequence
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Self, Unpack

import numpy as np
import tensorflow as tf
from tensorflow import TypeSpec
from tensorflow._aliases import ContainerGeneric, ScalarTensorCompatible, TensorCompatible
from tensorflow.data import experimental as experimental
from tensorflow.data.experimental import AUTOTUNE as AUTOTUNE
from tensorflow.dtypes import DType
from tensorflow.io import _CompressionTypes
from tensorflow.python.trackable.base import Trackable

_T1_co = TypeVar("_T1_co", covariant=True)
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")

class Iterator(_Iterator[_T1_co], Trackable, ABC):
    @property
    @abstractmethod
    def element_spec(self) -> ContainerGeneric[TypeSpec[Any]]:
        """
        The type specification of an element of this iterator.

        >>> dataset = tf.data.Dataset.from_tensors(42)
        >>> iterator = iter(dataset)
        >>> iterator.element_spec
        tf.TensorSpec(shape=(), dtype=tf.int32, name=None)

        For more information,
        read [this guide](https://www.tensorflow.org/guide/data#dataset_structure).

        Returns:
          A (nested) structure of `tf.TypeSpec` objects matching the structure of an
          element of this iterator, specifying the type of individual components.
        """
        ...
    @abstractmethod
    def get_next(self) -> _T1_co: ...
    @abstractmethod
    def get_next_as_optional(self) -> tf.experimental.Optional[_T1_co]: ...

class Dataset(ABC, Generic[_T1_co]):
    def apply(self, transformation_func: Callable[[Dataset[_T1_co]], Dataset[_T2]]) -> Dataset[_T2]: ...
    def as_numpy_iterator(self) -> Iterator[np.ndarray[Any, Any]]: ...
    def batch(
        self,
        batch_size: ScalarTensorCompatible,
        drop_remainder: bool = False,
        num_parallel_calls: int | None = None,
        deterministic: bool | None = None,
        name: str | None = None,
    ) -> Dataset[_T1_co]: ...
    def bucket_by_sequence_length(
        self,
        element_length_func: Callable[[_T1_co], ScalarTensorCompatible],
        bucket_boundaries: Sequence[int],
        bucket_batch_sizes: Sequence[int],
        padded_shapes: ContainerGeneric[tf.TensorShape | TensorCompatible] | None = None,
        padding_values: ContainerGeneric[ScalarTensorCompatible] | None = None,
        pad_to_bucket_boundary: bool = False,
        no_padding: bool = False,
        drop_remainder: bool = False,
        name: str | None = None,
    ) -> Dataset[_T1_co]: ...
    def cache(self, filename: str = "", name: str | None = None) -> Dataset[_T1_co]: ...
    def cardinality(self) -> int: ...
    @staticmethod
    def choose_from_datasets(
        datasets: Sequence[Dataset[_T2]], choice_dataset: Dataset[tf.Tensor], stop_on_empty_dataset: bool = True
    ) -> Dataset[_T2]: ...
    def concatenate(self, dataset: Dataset[_T1_co], name: str | None = None) -> Dataset[_T1_co]: ...
    @staticmethod
    def counter(
        start: ScalarTensorCompatible = 0, step: ScalarTensorCompatible = 1, dtype: DType = ..., name: str | None = None
    ) -> Dataset[tf.Tensor]:
        """
        Creates a `Dataset` that counts from `start` in steps of size `step`.

        Unlike `tf.data.Dataset.range`, which stops at some ending number,
        `tf.data.Dataset.counter` produces elements indefinitely.

        >>> dataset = tf.data.experimental.Counter().take(5)
        >>> [a.item() for a in dataset.as_numpy_iterator()]
        [0, 1, 2, 3, 4]
        >>> dataset.element_spec
        TensorSpec(shape=(), dtype=tf.int64, name=None)
        >>> dataset = tf.data.experimental.Counter(dtype=tf.int32)
        >>> dataset.element_spec
        TensorSpec(shape=(), dtype=tf.int32, name=None)
        >>> dataset = tf.data.experimental.Counter(start=2).take(5)
        >>> [a.item() for a in dataset.as_numpy_iterator()]
        [2, 3, 4, 5, 6]
        >>> dataset = tf.data.experimental.Counter(start=2, step=5).take(5)
        >>> [a.item() for a in dataset.as_numpy_iterator()]
        [2, 7, 12, 17, 22]
        >>> dataset = tf.data.experimental.Counter(start=10, step=-1).take(5)
        >>> [a.item() for a in dataset.as_numpy_iterator()]
        [10, 9, 8, 7, 6]

        Args:
          start: (Optional.) The starting value for the counter. Defaults to 0.
          step: (Optional.) The step size for the counter. Defaults to 1.
          dtype: (Optional.) The data type for counter elements. Defaults to
            `tf.int64`.
          name: (Optional.) A name for the tf.data operation.

        Returns:
          A `Dataset` of scalar `dtype` elements.
        """
        ...
    @property
    @abstractmethod
    def element_spec(self) -> ContainerGeneric[TypeSpec[Any]]: ...
    def enumerate(self, start: ScalarTensorCompatible = 0, name: str | None = None) -> Dataset[tuple[int, _T1_co]]: ...
    def filter(self, predicate: Callable[[_T1_co], bool | tf.Tensor], name: str | None = None) -> Dataset[_T1_co]: ...
    def flat_map(self, map_func: Callable[[_T1_co], Dataset[_T2]], name: str | None = None) -> Dataset[_T2]: ...
    # PEP 646 can be used here for a more precise type when better supported.
    @staticmethod
    def from_generator(
        generator: Callable[..., _T2],
        output_types: ContainerGeneric[DType] | None = None,
        output_shapes: ContainerGeneric[tf.TensorShape | Sequence[int | None]] | None = None,
        args: tuple[object, ...] | None = None,
        output_signature: ContainerGeneric[TypeSpec[Any]] | None = None,
        name: str | None = None,
    ) -> Dataset[_T2]:
        """
        Creates a `Dataset` whose elements are generated by `generator`. (deprecated arguments)

        Deprecated: SOME ARGUMENTS ARE DEPRECATED: `(output_shapes, output_types)`. They will be removed in a future version.
        Instructions for updating:
        Use output_signature instead

        Note: The current implementation of `Dataset.from_generator()` uses
        `tf.numpy_function` and inherits the same constraints. In particular, it
        requires the dataset and iterator related operations to be placed
        on a device in the same process as the Python program that called
        `Dataset.from_generator()`. In particular, using `from_generator` will
        preclude the use of tf.data service for scaling out dataset processing.
        The body of `generator` will not be serialized in a `GraphDef`, and you
        should not use this method if you need to serialize your model and restore
        it in a different environment.

        The `generator` argument must be a callable object that returns
        an object that supports the `iter()` protocol (e.g. a generator function).

        The elements generated by `generator` must be compatible with either the
        given `output_signature` argument or with the given `output_types` and
        (optionally) `output_shapes` arguments, whichever was specified.

        The recommended way to call `from_generator` is to use the
        `output_signature` argument. In this case the output will be assumed to
        consist of objects with the classes, shapes and types defined by
        `tf.TypeSpec` objects from `output_signature` argument:

        >>> def gen():
        ...   ragged_tensor = tf.ragged.constant([[1, 2], [3]])
        ...   yield 42, ragged_tensor
        >>>
        >>> dataset = tf.data.Dataset.from_generator(
        ...      gen,
        ...      output_signature=(
        ...          tf.TensorSpec(shape=(), dtype=tf.int32),
        ...          tf.RaggedTensorSpec(shape=(2, None), dtype=tf.int32)))
        >>>
        >>> list(dataset.take(1))
        [(<tf.Tensor: shape=(), dtype=int32, numpy=42>,
        <tf.RaggedTensor [[1, 2], [3]]>)]

        There is also a deprecated way to call `from_generator` by either with
        `output_types` argument alone or together with `output_shapes` argument.
        In this case the output of the function will be assumed to consist of
        `tf.Tensor` objects with the types defined by `output_types` and with the
        shapes which are either unknown or defined by `output_shapes`.

        Note: If `generator` depends on mutable global variables or other external
        state, be aware that the runtime may invoke `generator` multiple times
        (in order to support repeating the `Dataset`) and at any time
        between the call to `Dataset.from_generator()` and the production of the
        first element from the generator. Mutating global variables or external
        state can cause undefined behavior, and we recommend that you explicitly
        cache any external state in `generator` before calling
        `Dataset.from_generator()`.

        Note: While the `output_signature` parameter makes it possible to yield
        `Dataset` elements, the scope of `Dataset.from_generator()` should be
        limited to logic that cannot be expressed through tf.data operations. Using
        tf.data operations within the generator function is an anti-pattern and may
        result in incremental memory growth.

        Args:
          generator: A callable object that returns an object that supports the
            `iter()` protocol. If `args` is not specified, `generator` must take no
            arguments; otherwise it must take as many arguments as there are values
            in `args`.
          output_types: (Optional.) A (nested) structure of `tf.DType` objects
            corresponding to each component of an element yielded by `generator`.
          output_shapes: (Optional.) A (nested) structure of `tf.TensorShape`
            objects corresponding to each component of an element yielded by
            `generator`.
          args: (Optional.) A tuple of `tf.Tensor` objects that will be evaluated
            and passed to `generator` as NumPy-array arguments.
          output_signature: (Optional.) A (nested) structure of `tf.TypeSpec`
            objects corresponding to each component of an element yielded by
            `generator`.
          name: (Optional.) A name for the tf.data operations used by
            `from_generator`.

        Returns:
          Dataset: A `Dataset`.
        """
        ...
    @staticmethod
    def from_tensors(tensors: Any, name: str | None = None) -> Dataset[Any]:
        """
        Creates a `Dataset` with a single element, comprising the given tensors.

        `from_tensors` produces a dataset containing only a single element. To slice
        the input tensor into multiple elements, use `from_tensor_slices` instead.

        >>> dataset = tf.data.Dataset.from_tensors([1, 2, 3])
        >>> list(dataset.as_numpy_iterator())
        [array([1, 2, 3], dtype=int32)]
        >>> dataset = tf.data.Dataset.from_tensors(([1, 2, 3], 'A'))
        >>> list(dataset.as_numpy_iterator())
        [(array([1, 2, 3], dtype=int32), b'A')]

        >>> # You can use `from_tensors` to produce a dataset which repeats
        >>> # the same example many times.
        >>> example = tf.constant([1,2,3])
        >>> dataset = tf.data.Dataset.from_tensors(example).repeat(2)
        >>> list(dataset.as_numpy_iterator())
        [array([1, 2, 3], dtype=int32), array([1, 2, 3], dtype=int32)]

        Note that if `tensors` contains a NumPy array, and eager execution is not
        enabled, the values will be embedded in the graph as one or more
        `tf.constant` operations. For large datasets (> 1 GB), this can waste
        memory and run into byte limits of graph serialization. If `tensors`
        contains one or more large NumPy arrays, consider the alternative described
        in [this
        guide](https://tensorflow.org/guide/data#consuming_numpy_arrays).

        Args:
          tensors: A dataset "element". Supported values are documented
            [here](https://www.tensorflow.org/guide/data#dataset_structure).
          name: (Optional.) A name for the tf.data operation.

        Returns:
          Dataset: A `Dataset`.
        """
        ...
    @staticmethod
    def from_tensor_slices(tensors: TensorCompatible, name: str | None = None) -> Dataset[Any]: ...
    def get_single_element(self, name: str | None = None) -> _T1_co: ...
    def group_by_window(
        self,
        key_func: Callable[[_T1_co], tf.Tensor],
        reduce_func: Callable[[tf.Tensor, Dataset[_T1_co]], Dataset[_T2]],
        window_size: ScalarTensorCompatible | None = None,
        window_size_func: Callable[[tf.Tensor], tf.Tensor] | None = None,
        name: str | None = None,
    ) -> Dataset[_T2]: ...
    def ignore_errors(self, log_warning: bool = False, name: str | None = None) -> Dataset[_T1_co]: ...
    def interleave(
        self,
        map_func: Callable[[_T1_co], Dataset[_T2]],
        cycle_length: int | None = None,
        block_length: int | None = None,
        num_parallel_calls: int | None = None,
        deterministic: bool | None = None,
        name: str | None = None,
    ) -> Dataset[_T2]: ...
    def __iter__(self) -> Iterator[_T1_co]: ...
    @staticmethod
    def list_files(
        file_pattern: str | Sequence[str] | TensorCompatible,
        shuffle: bool | None = None,
        seed: int | None = None,
        name: str | None = None,
    ) -> Dataset[str]:
        """
        A dataset of all files matching one or more glob patterns.

        The `file_pattern` argument should be a small number of glob patterns.
        If your filenames have already been globbed, use
        `Dataset.from_tensor_slices(filenames)` instead, as re-globbing every
        filename with `list_files` may result in poor performance with remote
        storage systems.

        Note: The default behavior of this method is to return filenames in
        a non-deterministic random shuffled order. Pass a `seed` or `shuffle=False`
        to get results in a deterministic order.

        Example:
          If we had the following files on our filesystem:

            - /path/to/dir/a.txt
            - /path/to/dir/b.py
            - /path/to/dir/c.py

          If we pass "/path/to/dir/*.py" as the directory, the dataset
          would produce:

            - /path/to/dir/b.py
            - /path/to/dir/c.py

        Args:
          file_pattern: A string, a list of strings, or a `tf.Tensor` of string type
            (scalar or vector), representing the filename glob (i.e. shell wildcard)
            pattern(s) that will be matched.
          shuffle: (Optional.) If `True`, the file names will be shuffled randomly.
            Defaults to `True`.
          seed: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the random
            seed that will be used to create the distribution. See
            `tf.random.set_seed` for behavior.
          name: Optional. A name for the tf.data operations used by `list_files`.

        Returns:
         Dataset: A `Dataset` of strings corresponding to file names.
        """
        ...
    @staticmethod
    def load(
        path: str,
        element_spec: ContainerGeneric[tf.TypeSpec[Any]] | None = None,
        compression: _CompressionTypes = None,
        reader_func: Callable[[Dataset[Dataset[Any]]], Dataset[Any]] | None = None,
        wait: bool = False,
    ) -> Dataset[Any]:
        """
        Loads a previously saved dataset.

        Example usage:

        >>> import tempfile
        >>> path = os.path.join(tempfile.gettempdir(), "saved_data")
        >>> # Save a dataset
        >>> dataset = tf.data.Dataset.range(2)
        >>> tf.data.Dataset.save(dataset, path)
        >>> new_dataset = tf.data.Dataset.load(path)
        >>> for elem in new_dataset:
        ...   print(elem)
        tf.Tensor(0, shape=(), dtype=int64)
        tf.Tensor(1, shape=(), dtype=int64)


        If the default option of sharding the saved dataset was used, the element
        order of the saved dataset will be preserved when loading it.

        The `reader_func` argument can be used to specify a custom order in which
        elements should be loaded from the individual shards. The `reader_func` is
        expected to take a single argument -- a dataset of datasets, each containing
        elements of one of the shards -- and return a dataset of elements. For
        example, the order of shards can be shuffled when loading them as follows:

        ```python
        def custom_reader_func(datasets):
          datasets = datasets.shuffle(NUM_SHARDS)
          return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)

        dataset = tf.data.Dataset.load(
            path="/path/to/data", ..., reader_func=custom_reader_func)
        ```

        Args:
          path: Required. A path pointing to a previously saved dataset.
          element_spec: Optional. A nested structure of `tf.TypeSpec` objects
            matching the structure of an element of the saved dataset and specifying
            the type of individual element components. If not provided, the nested
            structure of `tf.TypeSpec` saved with the saved dataset is used. Note
            that this argument is required in graph mode.
          compression: Optional. The algorithm to use to decompress the data when
            reading it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`.
          reader_func: Optional. A function to control how to read data from shards.
            If present, the function will be traced and executed as graph
            computation.
          wait: If `True`, for snapshots written with `distributed_save`, it reads
            the snapshot while it is being written. For snapshots written with
            regular `save`, it waits for the snapshot until it's finished. The
            default is `False` for backward compatibility. Users of
            `distributed_save` are recommended to set it to `True`.

        Returns:
          A `tf.data.Dataset` instance.

        Raises:
          FileNotFoundError: If `element_spec` is not specified and the saved nested
            structure of `tf.TypeSpec` can not be located with the saved dataset.
          ValueError: If `element_spec` is not specified and the method is executed
            in graph mode.
        """
        ...
    # PEP 646 could be used here for a more precise type when better supported.
    def map(
        self,
        map_func: Callable[..., _T2],
        num_parallel_calls: int | None = None,
        deterministic: bool | None = None,
        synchronous: bool | None = None,
        use_unbounded_threadpool: bool = False,
        name: str | None = None,
    ) -> Dataset[_T2]:
        """
        Maps `map_func` across the elements of this dataset.

        This transformation applies `map_func` to each element of this dataset, and
        returns a new dataset containing the transformed elements, in the same
        order as they appeared in the input. `map_func` can be used to change both
        the values and the structure of a dataset's elements. Supported structure
        constructs are documented
        [here](https://www.tensorflow.org/guide/data#dataset_structure).

        For example, `map` can be used for adding 1 to each element, or projecting a
        subset of element components.

        >>> dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]
        >>> dataset = dataset.map(lambda x: x + 1)
        >>> [a.item() for a in dataset.as_numpy_iterator()]
        [2, 3, 4, 5, 6]

        The input signature of `map_func` is determined by the structure of each
        element in this dataset.

        >>> dataset = Dataset.range(5)
        >>> # `map_func` takes a single argument of type `tf.Tensor` with the same
        >>> # shape and dtype.
        >>> result = dataset.map(lambda x: x + 1)

        >>> # Each element is a tuple containing two `tf.Tensor` objects.
        >>> elements = [(1, "foo"), (2, "bar"), (3, "baz")]
        >>> dataset = tf.data.Dataset.from_generator(
        ...     lambda: elements, (tf.int32, tf.string))
        >>> # `map_func` takes two arguments of type `tf.Tensor`. This function
        >>> # projects out just the first component.
        >>> result = dataset.map(lambda x_int, y_str: x_int)
        >>> [a.item() for a in result.as_numpy_iterator()]
        [1, 2, 3]

        >>> # Each element is a dictionary mapping strings to `tf.Tensor` objects.
        >>> elements =  ([{"a": 1, "b": "foo"},
        ...               {"a": 2, "b": "bar"},
        ...               {"a": 3, "b": "baz"}])
        >>> dataset = tf.data.Dataset.from_generator(
        ...     lambda: elements, {"a": tf.int32, "b": tf.string})
        >>> # `map_func` takes a single argument of type `dict` with the same keys
        >>> # as the elements.
        >>> result = dataset.map(lambda d: str(d["a"]) + d["b"])

        The value or values returned by `map_func` determine the structure of each
        element in the returned dataset.

        >>> dataset = tf.data.Dataset.range(3)
        >>> # `map_func` returns two `tf.Tensor` objects.
        >>> def g(x):
        ...   return tf.constant(37.0), tf.constant(["Foo", "Bar", "Baz"])
        >>> result = dataset.map(g)
        >>> result.element_spec
        (TensorSpec(shape=(), dtype=tf.float32, name=None), TensorSpec(shape=(3,), dtype=tf.string, name=None))
        >>> # Python primitives, lists, and NumPy arrays are implicitly converted to
        >>> # `tf.Tensor`.
        >>> def h(x):
        ...   return 37.0, ["Foo", "Bar"], np.array([1.0, 2.0], dtype=np.float64)
        >>> result = dataset.map(h)
        >>> result.element_spec
        (TensorSpec(shape=(), dtype=tf.float32, name=None), TensorSpec(shape=(2,), dtype=tf.string, name=None), TensorSpec(shape=(2,), dtype=tf.float64, name=None))
        >>> # `map_func` can return nested structures.
        >>> def i(x):
        ...   return (37.0, [42, 16]), "foo"
        >>> result = dataset.map(i)
        >>> result.element_spec
        ((TensorSpec(shape=(), dtype=tf.float32, name=None),
          TensorSpec(shape=(2,), dtype=tf.int32, name=None)),
         TensorSpec(shape=(), dtype=tf.string, name=None))

        `map_func` can accept as arguments and return any type of dataset element.

        Note that irrespective of the context in which `map_func` is defined (eager
        vs. graph), tf.data traces the function and executes it as a graph. To use
        Python code inside of the function you have a few options:

        1) Rely on AutoGraph to convert Python code into an equivalent graph
        computation. The downside of this approach is that AutoGraph can convert
        some but not all Python code.

        2) Use `tf.py_function`, which allows you to write arbitrary Python code but
        will generally result in worse performance than 1). For example:

        >>> d = tf.data.Dataset.from_tensor_slices(['hello', 'world'])
        >>> # transform a string tensor to upper case string using a Python function
        >>> def upper_case_fn(t: tf.Tensor):
        ...   return t.numpy().decode('utf-8').upper()
        >>> d = d.map(lambda x: tf.py_function(func=upper_case_fn,
        ...           inp=[x], Tout=tf.string))
        >>> list(d.as_numpy_iterator())
        [b'HELLO', b'WORLD']

        3) Use `tf.numpy_function`, which also allows you to write arbitrary
        Python code. Note that `tf.py_function` accepts `tf.Tensor` whereas
        `tf.numpy_function` accepts numpy arrays and returns only numpy arrays.
        For example:

        >>> d = tf.data.Dataset.from_tensor_slices(['hello', 'world'])
        >>> def upper_case_fn(t: np.ndarray):
        ...   return t.decode('utf-8').upper()
        >>> d = d.map(lambda x: tf.numpy_function(func=upper_case_fn,
        ...           inp=[x], Tout=tf.string))
        >>> list(d.as_numpy_iterator())
        [b'HELLO', b'WORLD']

        Note that the use of `tf.numpy_function` and `tf.py_function`
        in general precludes the possibility of executing user-defined
        transformations in parallel (because of Python GIL).

        Performance can often be improved by setting `num_parallel_calls` so that
        `map` will use multiple threads to process elements. If deterministic order
        isn't required, it can also improve performance to set
        `deterministic=False`.

        >>> dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]
        >>> dataset = dataset.map(lambda x: x + 1,
        ...     num_parallel_calls=tf.data.AUTOTUNE,
        ...     deterministic=False)

        The order of elements yielded by this transformation is deterministic if
        `deterministic=True`. If `map_func` contains stateful operations and
        `num_parallel_calls > 1`, the order in which that state is accessed is
        undefined, so the values of output elements may not be deterministic
        regardless of the `deterministic` flag value.

        Args:
          map_func: A function mapping a dataset element to another dataset element.
          num_parallel_calls: (Optional.) A `tf.int64` scalar `tf.Tensor`,
            representing the number elements to process asynchronously in parallel.
            If the value `tf.data.AUTOTUNE` is used, then the number of parallel
            calls is set dynamically based on available CPU. If not specified, the
            `tf.data.Options.experimental_optimization.map_parallelization` option
            (`True` by default) controls whether the map will run as with
            `tf.data.AUTOTUNE` or run sequentially.
          deterministic: (Optional.) When `num_parallel_calls` is specified, if this
            boolean is specified (`True` or `False`), it controls the order in which
            the transformation produces elements. If set to `False`, the
            transformation is allowed to yield elements out of order to trade
            determinism for performance. If not specified, the
            `tf.data.Options.deterministic` option (`True` by default) controls the
            behavior.
          synchronous: (Optional.) Whether to force the map transformation to run
            synchronously. This only matters when
            `options.experimental_optimization.map_parallelization=True`. That
            option would normally change the map to run with
            `num_parallel_calls=tf.data.AUTOTUNE`, but if `synchronous=True` is
            specified, the map will not be parallelized at all. This is useful for
            saving memory, since even setting `num_parallel_calls=1` will cause one
            batch to be buffered, while with `synchronous=True` the map
            transformation doesn't buffer anything.
          use_unbounded_threadpool: (Optional.) By default, map functions run in a
            limited threadpool based on the number of cores on the machine. This
            efficient for CPU-heavy processing, but if the map function performs IO
            it is better to use an unbounded threadpool by setting it to `True`. It
            is `False` by default.
          name: (Optional.) A name for the tf.data operation.

        Returns:
          A new `Dataset` with the transformation applied as described above.
        """
        ...
    def options(self) -> Options:
        """
        Returns the options for this dataset and its inputs.

        Returns:
          A `tf.data.Options` object representing the dataset options.
        """
        ...
    def padded_batch(
        self,
        batch_size: ScalarTensorCompatible,
        padded_shapes: ContainerGeneric[tf.TensorShape | TensorCompatible] | None = None,
        padding_values: ContainerGeneric[ScalarTensorCompatible] | None = None,
        drop_remainder: bool = False,
        name: str | None = None,
    ) -> Dataset[_T1_co]: ...
    def prefetch(self, buffer_size: ScalarTensorCompatible, name: str | None = None) -> Dataset[_T1_co]: ...
    def ragged_batch(
        self,
        batch_size: ScalarTensorCompatible,
        drop_remainder: bool = False,
        row_splits_dtype: DType = ...,
        name: str | None = None,
    ) -> Dataset[tf.RaggedTensor]:
        """
        Combines consecutive elements of this dataset into `tf.RaggedTensor`s.

        Like `tf.data.Dataset.batch`, the components of the resulting element will
        have an additional outer dimension, which will be `batch_size` (or
        `N % batch_size` for the last element if `batch_size` does not divide the
        number of input elements `N` evenly and `drop_remainder` is `False`). If
        your program depends on the batches having the same outer dimension, you
        should set the `drop_remainder` argument to `True` to prevent the smaller
        batch from being produced.

        Unlike `tf.data.Dataset.batch`, the input elements to be batched may have
        different shapes:

        *  If an input element is a `tf.Tensor` whose static `tf.TensorShape` is
        fully defined, then it is batched as normal.
        *  If an input element is a `tf.Tensor` whose static `tf.TensorShape`
        contains one or more axes with unknown size (i.e., `shape[i]=None`), then
        the output will contain a `tf.RaggedTensor` that is ragged up to any of such
        dimensions.
        *  If an input element is a `tf.RaggedTensor` or any other type, then it is
        batched as normal.

        Example:

        >>> dataset = tf.data.Dataset.range(6)
        >>> dataset = dataset.map(lambda x: tf.range(x))
        >>> dataset.element_spec.shape
        TensorShape([None])
        >>> dataset = dataset.ragged_batch(2)
        >>> for batch in dataset:
        ...   print(batch)
        <tf.RaggedTensor [[], [0]]>
        <tf.RaggedTensor [[0, 1], [0, 1, 2]]>
        <tf.RaggedTensor [[0, 1, 2, 3], [0, 1, 2, 3, 4]]>

        Args:
          batch_size: A `tf.int64` scalar `tf.Tensor`, representing the number of
            consecutive elements of this dataset to combine in a single batch.
          drop_remainder: (Optional.) A `tf.bool` scalar `tf.Tensor`, representing
            whether the last batch should be dropped in the case it has fewer than
            `batch_size` elements; the default behavior is not to drop the smaller
            batch.
          row_splits_dtype: The dtype that should be used for the `row_splits` of
            any new ragged tensors.  Existing `tf.RaggedTensor` elements do not have
            their row_splits dtype changed.
          name: (Optional.) A string indicating a name for the `tf.data` operation.

        Returns:
          A new `Dataset` with the transformation applied as described above.
        """
        ...
    @staticmethod
    def random(
        seed: int | None = None, rerandomize_each_iteration: bool | None = None, name: str | None = None
    ) -> Dataset[tf.Tensor]:
        """
        Creates a `Dataset` of pseudorandom values.

        The dataset generates a sequence of uniformly distributed integer values.

        `rerandomize_each_iteration` controls whether the sequence of random number
        generated should be re-randomized for each epoch. The default value is False
        where the dataset generates the same sequence of random numbers for each
        epoch.

        >>> ds1 = tf.data.Dataset.random(seed=4).take(10)
        >>> ds2 = tf.data.Dataset.random(seed=4).take(10)
        >>> print(list(ds1.as_numpy_iterator())==list(ds2.as_numpy_iterator()))
        True

        >>> ds3 = tf.data.Dataset.random(seed=4).take(10)
        >>> ds3_first_epoch = list(ds3.as_numpy_iterator())
        >>> ds3_second_epoch = list(ds3.as_numpy_iterator())
        >>> print(ds3_first_epoch == ds3_second_epoch)
        True

        >>> ds4 = tf.data.Dataset.random(
        ...     seed=4, rerandomize_each_iteration=True).take(10)
        >>> ds4_first_epoch = list(ds4.as_numpy_iterator())
        >>> ds4_second_epoch = list(ds4.as_numpy_iterator())
        >>> print(ds4_first_epoch == ds4_second_epoch)
        False

        Args:
          seed: (Optional) If specified, the dataset produces a deterministic
            sequence of values.
          rerandomize_each_iteration: (Optional) If set to False, the dataset
          generates the same sequence of random numbers for each epoch. If set to
          True, it generates a different deterministic sequence of random numbers
          for each epoch. It is defaulted to False if left unspecified.
          name: (Optional.) A name for the tf.data operation.

        Returns:
          Dataset: A `Dataset`.
        """
        ...
    @staticmethod
    @overload
    def range(stop: ScalarTensorCompatible, /, output_type: DType = ..., name: str | None = None) -> Dataset[tf.Tensor]:
        """
        Creates a `Dataset` of a step-separated range of values.

        >>> ds = Dataset.range(5)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [0, 1, 2, 3, 4]
        >>> ds = Dataset.range(2, 5)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [2, 3, 4]
        >>> ds = Dataset.range(1, 5, 2)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [1, 3]
        >>> ds = Dataset.range(1, 5, -2)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        []
        >>> ds = Dataset.range(5, 1)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        []
        >>> ds = Dataset.range(5, 1, -2)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [5, 3]
        >>> ds = Dataset.range(2, 5, output_type=tf.int32)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [2, 3, 4]
        >>> ds = Dataset.range(1, 5, 2, output_type=tf.float32)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [1.0, 3.0]

        Args:
          *args: follows the same semantics as python's range.
            len(args) == 1 -> start = 0, stop = args[0], step = 1.
            len(args) == 2 -> start = args[0], stop = args[1], step = 1.
            len(args) == 3 -> start = args[0], stop = args[1], step = args[2].
          **kwargs:
            - output_type: Its expected dtype. (Optional, default: `tf.int64`).
            - name: (Optional.) A name for the tf.data operation.

        Returns:
          Dataset: A `RangeDataset`.

        Raises:
          ValueError: if len(args) == 0.
        """
        ...
    @staticmethod
    @overload
    def range(
        start: ScalarTensorCompatible,
        stop: ScalarTensorCompatible,
        step: ScalarTensorCompatible = 1,
        /,
        output_type: DType = ...,
        name: str | None = None,
    ) -> Dataset[tf.Tensor]:
        """
        Creates a `Dataset` of a step-separated range of values.

        >>> ds = Dataset.range(5)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [0, 1, 2, 3, 4]
        >>> ds = Dataset.range(2, 5)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [2, 3, 4]
        >>> ds = Dataset.range(1, 5, 2)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [1, 3]
        >>> ds = Dataset.range(1, 5, -2)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        []
        >>> ds = Dataset.range(5, 1)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        []
        >>> ds = Dataset.range(5, 1, -2)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [5, 3]
        >>> ds = Dataset.range(2, 5, output_type=tf.int32)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [2, 3, 4]
        >>> ds = Dataset.range(1, 5, 2, output_type=tf.float32)
        >>> [a.item() for a in ds.as_numpy_iterator()]
        [1.0, 3.0]

        Args:
          *args: follows the same semantics as python's range.
            len(args) == 1 -> start = 0, stop = args[0], step = 1.
            len(args) == 2 -> start = args[0], stop = args[1], step = 1.
            len(args) == 3 -> start = args[0], stop = args[1], step = args[2].
          **kwargs:
            - output_type: Its expected dtype. (Optional, default: `tf.int64`).
            - name: (Optional.) A name for the tf.data operation.

        Returns:
          Dataset: A `RangeDataset`.

        Raises:
          ValueError: if len(args) == 0.
        """
        ...
    def rebatch(
        self, batch_size: ScalarTensorCompatible, drop_remainder: bool = False, name: str | None = None
    ) -> Dataset[_T1_co]: ...
    def reduce(self, initial_state: _T2, reduce_func: Callable[[_T2, _T1_co], _T2], name: str | None = None) -> _T2: ...
    def rejection_resample(
        self,
        class_func: Callable[[_T1_co], ScalarTensorCompatible],
        target_dist: TensorCompatible,
        initial_dist: TensorCompatible | None = None,
        seed: int | None = None,
        name: str | None = None,
    ) -> Dataset[_T1_co]: ...
    def repeat(self, count: ScalarTensorCompatible | None = None, name: str | None = None) -> Dataset[_T1_co]: ...
    @staticmethod
    def sample_from_datasets(
        datasets: Sequence[Dataset[_T1_co]],
        weights: TensorCompatible | None = None,
        seed: int | None = None,
        stop_on_empty_dataset: bool = False,
        rerandomize_each_iteration: bool | None = None,
    ) -> Dataset[_T1_co]: ...
    # Incomplete as tf.train.CheckpointOptions not yet covered.
    def save(
        self,
        path: str,
        compression: _CompressionTypes = None,
        shard_func: Callable[[_T1_co], int] | None = None,
        checkpoint_args: Incomplete | None = None,
    ) -> None:
        """
        Saves the content of the given dataset.

          Example usage:

          >>> import tempfile
          >>> path = os.path.join(tempfile.gettempdir(), "saved_data")
          >>> # Save a dataset
          >>> dataset = tf.data.Dataset.range(2)
          >>> dataset.save(path)
          >>> new_dataset = tf.data.Dataset.load(path)
          >>> for elem in new_dataset:
          ...   print(elem)
          tf.Tensor(0, shape=(), dtype=int64)
          tf.Tensor(1, shape=(), dtype=int64)

          The saved dataset is saved in multiple file "shards". By default, the
          dataset output is divided to shards in a round-robin fashion but custom
          sharding can be specified via the `shard_func` function. For example, you
          can save the dataset to using a single shard as follows:

          ```python
          dataset = make_dataset()
          def custom_shard_func(element):
            return np.int64(0)
          dataset.save(
              path="/path/to/data", ..., shard_func=custom_shard_func)
          ```

          To enable checkpointing, pass in `checkpoint_args` to the `save` method
          as follows:

          ```python
          dataset = tf.data.Dataset.range(100)
          save_dir = "..."
          checkpoint_prefix = "..."
          step_counter = tf.Variable(0, trainable=False)
          checkpoint_args = {
            "checkpoint_interval": 50,
            "step_counter": step_counter,
            "directory": checkpoint_prefix,
            "max_to_keep": 20,
          }
          dataset.save(dataset, save_dir, checkpoint_args=checkpoint_args)
          ```

          NOTE: The directory layout and file format used for saving the dataset is
          considered an implementation detail and may change. For this reason,
          datasets saved through `tf.data.Dataset.save` should only be consumed
          through `tf.data.Dataset.load`, which is guaranteed to be
          backwards compatible.

        Args:
         path: Required. A directory to use for saving the dataset.
         compression: Optional. The algorithm to use to compress data when writing
              it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`.
         shard_func: Optional. A function to control the mapping of dataset
              elements to file shards. The function is expected to map elements of
              the input dataset to int64 shard IDs. If present, the function will be
              traced and executed as graph computation.
         checkpoint_args: Optional args for checkpointing which will be passed into
              the `tf.train.CheckpointManager`. If `checkpoint_args` are not
              specified, then checkpointing will not be performed. The `save()`
              implementation creates a `tf.train.Checkpoint` object internally, so
              users should not set the `checkpoint` argument in `checkpoint_args`.

        Returns:
          An operation which when executed performs the save. When writing
          checkpoints, returns None. The return value is useful in unit tests.

        Raises:
          ValueError if `checkpoint` is passed into `checkpoint_args`.
        """
        ...
    def scan(
        self, initial_state: _T2, scan_func: Callable[[_T2, _T1_co], tuple[_T2, _T3]], name: str | None = None
    ) -> Dataset[_T3]: ...
    def shard(
        self, num_shards: ScalarTensorCompatible, index: ScalarTensorCompatible, name: str | None = None
    ) -> Dataset[_T1_co]: ...
    def shuffle(
        self,
        buffer_size: ScalarTensorCompatible,
        seed: int | None = None,
        reshuffle_each_iteration: bool = True,
        name: str | None = None,
    ) -> Dataset[_T1_co]: ...
    def skip(self, count: ScalarTensorCompatible, name: str | None = None) -> Dataset[_T1_co]: ...
    def snapshot(
        self,
        path: str,
        compression: _CompressionTypes = "AUTO",
        reader_func: Callable[[Dataset[Dataset[_T1_co]]], Dataset[_T1_co]] | None = None,
        shard_func: Callable[[_T1_co], ScalarTensorCompatible] | None = None,
        name: str | None = None,
    ) -> Dataset[_T1_co]: ...
    def sparse_batch(
        self, batch_size: ScalarTensorCompatible, row_shape: tf.TensorShape | TensorCompatible, name: str | None = None
    ) -> Dataset[tf.SparseTensor]: ...
    def take(self, count: ScalarTensorCompatible, name: str | None = None) -> Dataset[_T1_co]: ...
    def take_while(self, predicate: Callable[[_T1_co], ScalarTensorCompatible], name: str | None = None) -> Dataset[_T1_co]: ...
    def unbatch(self, name: str | None = None) -> Dataset[_T1_co]: ...
    def unique(self, name: str | None = None) -> Dataset[_T1_co]: ...
    def window(
        self,
        size: ScalarTensorCompatible,
        shift: ScalarTensorCompatible | None = None,
        stride: ScalarTensorCompatible = 1,
        drop_remainder: bool = False,
        name: str | None = None,
    ) -> Dataset[Dataset[_T1_co]]: ...
    def with_options(self, options: Options, name: str | None = None) -> Dataset[_T1_co]: ...
    @overload
    @staticmethod
    def zip(
        *args: Dataset[Any] | Collection[Dataset[Any]] | ContainerGeneric[Dataset[Any]], name: str | None = None
    ) -> Dataset[tuple[Any, ...]]:
        """
        Creates a `Dataset` by zipping together the given datasets.

        This method has similar semantics to the built-in `zip()` function
        in Python, with the main difference being that the `datasets`
        argument can be a (nested) structure of `Dataset` objects. The supported
        nesting mechanisms are documented
        [here] (https://www.tensorflow.org/guide/data#dataset_structure).

        >>> # The datasets or nested structure of datasets `*args` argument
        >>> # determines the structure of elements in the resulting dataset.
        >>> a = tf.data.Dataset.range(1, 4)  # ==> [ 1, 2, 3 ]
        >>> b = tf.data.Dataset.range(4, 7)  # ==> [ 4, 5, 6 ]
        >>> ds = tf.data.Dataset.zip(a, b)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(1, 4), (2, 5), (3, 6)]
        >>> ds = tf.data.Dataset.zip(b, a)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(4, 1), (5, 2), (6, 3)]
        >>>
        >>> # The `datasets` argument may contain an arbitrary number of datasets.
        >>> c = tf.data.Dataset.range(7, 13).batch(2)  # ==> [ [7, 8],
        ...                                            #       [9, 10],
        ...                                            #       [11, 12] ]
        >>> ds = tf.data.Dataset.zip(a, b, c)
        >>> for i, j, k in ds.as_numpy_iterator():
        ...   print(i.item(), j.item(), k)
        1 4 [7 8]
        2 5 [ 9 10]
        3 6 [11 12]
        >>>
        >>> # The number of elements in the resulting dataset is the same as
        >>> # the size of the smallest dataset in `datasets`.
        >>> d = tf.data.Dataset.range(13, 15)  # ==> [ 13, 14 ]
        >>> ds = tf.data.Dataset.zip(a, d)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(1, 13), (2, 14)]

        Args:
          *args: Datasets or nested structures of datasets to zip together. This
            can't be set if `datasets` is set.
          datasets: A (nested) structure of datasets. This can't be set if `*args`
            is set. Note that this exists only for backwards compatibility and it is
            preferred to use *args.
          name: (Optional.) A name for the tf.data operation.

        Returns:
          A new `Dataset` with the transformation applied as described above.
        """
        ...
    @overload
    @staticmethod
    def zip(*args: Unpack[tuple[Dataset[_T2], Dataset[_T3]]], name: str | None = None) -> Dataset[tuple[_T2, _T3]]:
        """
        Creates a `Dataset` by zipping together the given datasets.

        This method has similar semantics to the built-in `zip()` function
        in Python, with the main difference being that the `datasets`
        argument can be a (nested) structure of `Dataset` objects. The supported
        nesting mechanisms are documented
        [here] (https://www.tensorflow.org/guide/data#dataset_structure).

        >>> # The datasets or nested structure of datasets `*args` argument
        >>> # determines the structure of elements in the resulting dataset.
        >>> a = tf.data.Dataset.range(1, 4)  # ==> [ 1, 2, 3 ]
        >>> b = tf.data.Dataset.range(4, 7)  # ==> [ 4, 5, 6 ]
        >>> ds = tf.data.Dataset.zip(a, b)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(1, 4), (2, 5), (3, 6)]
        >>> ds = tf.data.Dataset.zip(b, a)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(4, 1), (5, 2), (6, 3)]
        >>>
        >>> # The `datasets` argument may contain an arbitrary number of datasets.
        >>> c = tf.data.Dataset.range(7, 13).batch(2)  # ==> [ [7, 8],
        ...                                            #       [9, 10],
        ...                                            #       [11, 12] ]
        >>> ds = tf.data.Dataset.zip(a, b, c)
        >>> for i, j, k in ds.as_numpy_iterator():
        ...   print(i.item(), j.item(), k)
        1 4 [7 8]
        2 5 [ 9 10]
        3 6 [11 12]
        >>>
        >>> # The number of elements in the resulting dataset is the same as
        >>> # the size of the smallest dataset in `datasets`.
        >>> d = tf.data.Dataset.range(13, 15)  # ==> [ 13, 14 ]
        >>> ds = tf.data.Dataset.zip(a, d)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(1, 13), (2, 14)]

        Args:
          *args: Datasets or nested structures of datasets to zip together. This
            can't be set if `datasets` is set.
          datasets: A (nested) structure of datasets. This can't be set if `*args`
            is set. Note that this exists only for backwards compatibility and it is
            preferred to use *args.
          name: (Optional.) A name for the tf.data operation.

        Returns:
          A new `Dataset` with the transformation applied as described above.
        """
        ...
    @overload
    @staticmethod
    def zip(
        *, datasets: tuple[Dataset[_T2], Dataset[_T3]] | None = None, name: str | None = None
    ) -> Dataset[tuple[_T2, _T3]]:
        """
        Creates a `Dataset` by zipping together the given datasets.

        This method has similar semantics to the built-in `zip()` function
        in Python, with the main difference being that the `datasets`
        argument can be a (nested) structure of `Dataset` objects. The supported
        nesting mechanisms are documented
        [here] (https://www.tensorflow.org/guide/data#dataset_structure).

        >>> # The datasets or nested structure of datasets `*args` argument
        >>> # determines the structure of elements in the resulting dataset.
        >>> a = tf.data.Dataset.range(1, 4)  # ==> [ 1, 2, 3 ]
        >>> b = tf.data.Dataset.range(4, 7)  # ==> [ 4, 5, 6 ]
        >>> ds = tf.data.Dataset.zip(a, b)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(1, 4), (2, 5), (3, 6)]
        >>> ds = tf.data.Dataset.zip(b, a)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(4, 1), (5, 2), (6, 3)]
        >>>
        >>> # The `datasets` argument may contain an arbitrary number of datasets.
        >>> c = tf.data.Dataset.range(7, 13).batch(2)  # ==> [ [7, 8],
        ...                                            #       [9, 10],
        ...                                            #       [11, 12] ]
        >>> ds = tf.data.Dataset.zip(a, b, c)
        >>> for i, j, k in ds.as_numpy_iterator():
        ...   print(i.item(), j.item(), k)
        1 4 [7 8]
        2 5 [ 9 10]
        3 6 [11 12]
        >>>
        >>> # The number of elements in the resulting dataset is the same as
        >>> # the size of the smallest dataset in `datasets`.
        >>> d = tf.data.Dataset.range(13, 15)  # ==> [ 13, 14 ]
        >>> ds = tf.data.Dataset.zip(a, d)
        >>> [(i.item(), j.item()) for i, j in ds.as_numpy_iterator()]
        [(1, 13), (2, 14)]

        Args:
          *args: Datasets or nested structures of datasets to zip together. This
            can't be set if `datasets` is set.
          datasets: A (nested) structure of datasets. This can't be set if `*args`
            is set. Note that this exists only for backwards compatibility and it is
            preferred to use *args.
          name: (Optional.) A name for the tf.data operation.

        Returns:
          A new `Dataset` with the transformation applied as described above.
        """
        ...
    def __len__(self) -> int:
        """
        Returns the length of the dataset if it is known and finite.

        This method requires that you are running in eager mode, and that the
        length of the dataset is known and non-infinite. When the length may be
        unknown or infinite, or if you are running in graph mode, use
        `tf.data.Dataset.cardinality` instead.

        Returns:
          An integer representing the length of the dataset.

        Raises:
          RuntimeError: If the dataset length is unknown or infinite, or if eager
            execution is not enabled.
        """
        ...
    def __nonzero__(self) -> bool: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class Options:
    """
    Represents options for `tf.data.Dataset`.

    A `tf.data.Options` object can be, for instance, used to control which static
    optimizations to apply to the input pipeline graph or whether to use
    performance modeling to dynamically tune the parallelism of operations such as
    `tf.data.Dataset.map` or `tf.data.Dataset.interleave`.

    The options are set for the entire dataset and are carried over to datasets
    created through tf.data transformations.

    The options can be set by constructing an `Options` object and using the
    `tf.data.Dataset.with_options(options)` transformation, which returns a
    dataset with the options set.

    >>> dataset = tf.data.Dataset.range(42)
    >>> options = tf.data.Options()
    >>> options.deterministic = False
    >>> dataset = dataset.with_options(options)
    >>> print(dataset.options().deterministic)
    False

    Note: A known limitation of the `tf.data.Options` implementation is that the
    options are not preserved across tf.function boundaries. In particular, to
    set options for a dataset that is iterated within a tf.function, the options
    need to be set within the same tf.function.
    """
    autotune: Incomplete
    deterministic: bool
    experimental_deterministic: bool
    experimental_distribute: Incomplete
    experimental_external_state_policy: Incomplete
    experimental_optimization: Incomplete
    experimental_slack: bool
    experimental_symbolic_checkpoint: bool
    experimental_threading: Incomplete
    threading: Incomplete
    def merge(self, options: Options) -> Self:
        """
        Merges itself with the given `tf.data.Options`.

        If this object and the `options` to merge set an option differently, a
        warning is generated and this object's value is updated with the `options`
        object's value.

        Args:
          options: The `tf.data.Options` to merge with.

        Returns:
          New `tf.data.Options` object which is the result of merging self with
          the input `tf.data.Options`.
        """
        ...

class TFRecordDataset(Dataset[tf.Tensor]):
    """
    A `Dataset` comprising records from one or more TFRecord files.

    This dataset loads TFRecords from the files as bytes, exactly as they were
    written.`TFRecordDataset` does not do any parsing or decoding on its own.
    Parsing and decoding can be done by applying `Dataset.map` transformations
    after the `TFRecordDataset`.

    A minimal example is given below:

    >>> import tempfile
    >>> example_path = os.path.join(tempfile.gettempdir(), "example.tfrecords")
    >>> np.random.seed(0)

    >>> # Write the records to a file.
    ... with tf.io.TFRecordWriter(example_path) as file_writer:
    ...   for _ in range(4):
    ...     x, y = np.random.random(), np.random.random()
    ...
    ...     record_bytes = tf.train.Example(features=tf.train.Features(feature={
    ...         "x": tf.train.Feature(float_list=tf.train.FloatList(value=[x])),
    ...         "y": tf.train.Feature(float_list=tf.train.FloatList(value=[y])),
    ...     })).SerializeToString()
    ...     file_writer.write(record_bytes)

    >>> # Read the data back out.
    >>> def decode_fn(record_bytes):
    ...   return tf.io.parse_single_example(
    ...       # Data
    ...       record_bytes,
    ...
    ...       # Schema
    ...       {"x": tf.io.FixedLenFeature([], dtype=tf.float32),
    ...        "y": tf.io.FixedLenFeature([], dtype=tf.float32)}
    ...   )

    >>> for batch in tf.data.TFRecordDataset([example_path]).map(decode_fn):
    ...   print("x = {x:.4f},  y = {y:.4f}".format(**batch))
    x = 0.5488,  y = 0.7152
    x = 0.6028,  y = 0.5449
    x = 0.4237,  y = 0.6459
    x = 0.4376,  y = 0.8918
    """
    def __init__(
        self,
        filenames: TensorCompatible | Dataset[str],
        compression_type: _CompressionTypes = None,
        buffer_size: int | None = None,
        num_parallel_reads: int | None = None,
        name: str | None = None,
    ) -> None:
        """
        Creates a `TFRecordDataset` to read one or more TFRecord files.

        Each element of the dataset will contain a single TFRecord.

        Args:
          filenames: A `tf.string` tensor or `tf.data.Dataset` containing one or
            more filenames.
          compression_type: (Optional.) A `tf.string` scalar evaluating to one of
            `""` (no compression), `"ZLIB"`, or `"GZIP"`.
          buffer_size: (Optional.) A `tf.int64` scalar representing the number of
            bytes in the read buffer. If your input pipeline is I/O bottlenecked,
            consider setting this parameter to a value 1-100 MBs. If `None`, a
            sensible default for both local and remote file systems is used.
          num_parallel_reads: (Optional.) A `tf.int64` scalar representing the
            number of files to read in parallel. If greater than one, the records of
            files read in parallel are outputted in an interleaved order. If your
            input pipeline is I/O bottlenecked, consider setting this parameter to a
            value greater than one to parallelize the I/O. If `None`, files will be
            read sequentially.
          name: (Optional.) A name for the tf.data operation.

        Raises:
          TypeError: If any argument does not have the expected type.
          ValueError: If any argument does not have the expected shape.
        """
        ...
    @property
    def element_spec(self) -> tf.TensorSpec: ...

def __getattr__(name: str) -> Incomplete: ...
