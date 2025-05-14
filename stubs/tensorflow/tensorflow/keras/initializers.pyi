from collections.abc import Callable
from typing import Any, overload
from typing_extensions import Self, TypeAlias

from tensorflow import Tensor
from tensorflow._aliases import DTypeLike, ShapeLike, TensorCompatible

class Initializer:
    """
    Initializer base class: all Keras initializers inherit from this class.

    Initializers should implement a `__call__()` method with the following
    signature:

    ```python
    def __call__(self, shape, dtype=None, **kwargs):
        # returns a tensor of shape `shape` and dtype `dtype`
        # containing values drawn from a distribution of your choice.
    ```

    Optionally, you can also implement the method `get_config()` and the class
    method `from_config` in order to support serialization, just like with
    any Keras object.

    Here's a simple example: a random normal initializer.

    ```python
    class ExampleRandomNormal(Initializer):
        def __init__(self, mean, stddev):
            self.mean = mean
            self.stddev = stddev

        def __call__(self, shape, dtype=None, **kwargs):
            return keras.random.normal(
                shape, mean=self.mean, stddev=self.stddev, dtype=dtype
            )

        def get_config(self):  # To support serialization
            return {"mean": self.mean, "stddev": self.stddev}
    ```

    Note that we don't have to implement `from_config()` in the example above
    since the constructor arguments of the class the keys in the config returned
    by `get_config()` are the same. In this case, the default `from_config()`
    works fine.
    """
    def __call__(self, shape: ShapeLike, dtype: DTypeLike | None = None) -> Tensor:
        """
        Returns a tensor object initialized as specified by the initializer.

        Args:
            shape: Shape of the tensor.
            dtype: Optional dtype of the tensor.
        """
        ...
    def get_config(self) -> dict[str, Any]:
        """
        Returns the initializer's configuration as a JSON-serializable dict.

        Returns:
            A JSON-serializable Python dict.
        """
        ...
    @classmethod
    def from_config(cls, config: dict[str, Any]) -> Self:
        """
        Instantiates an initializer from a configuration dictionary.

        Example:

        ```python
        initializer = RandomUniform(-1, 1)
        config = initializer.get_config()
        initializer = RandomUniform.from_config(config)
        ```

        Args:
            config: A Python dictionary, the output of `get_config()`.

        Returns:
            An `Initializer` instance.
        """
        ...

class Constant(Initializer):
    """
    Initializer that generates tensors with constant values.

    Only scalar values are allowed.
    The constant value provided must be convertible to the dtype requested
    when calling the initializer.

    Examples:

    >>> # Standalone usage:
    >>> initializer = Constant(10.)
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = Constant(10.)
    >>> layer = Dense(3, kernel_initializer=initializer)

    Args:
        value: A Python scalar.
    """
    def __init__(self, value: TensorCompatible = 0.0) -> None: ...

class GlorotNormal(Initializer):
    """
    The Glorot normal initializer, also called Xavier normal initializer.

    Draws samples from a truncated normal distribution centered on 0 with
    `stddev = sqrt(2 / (fan_in + fan_out))` where `fan_in` is the number of
    input units in the weight tensor and `fan_out` is the number of output units
    in the weight tensor.

    Examples:

    >>> # Standalone usage:
    >>> initializer = GlorotNormal()
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = GlorotNormal()
    >>> layer = Dense(3, kernel_initializer=initializer)

    Args:
        seed: A Python integer or instance of
            `keras.backend.SeedGenerator`.
            Used to make the behavior of the initializer
            deterministic. Note that an initializer seeded with an integer
            or `None` (unseeded) will produce the same random values
            across multiple calls. To get different random values
            across multiple calls, use as seed an instance
            of `keras.backend.SeedGenerator`.

    Reference:

    - [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    """
    def __init__(self, seed: int | None = None) -> None: ...

class GlorotUniform(Initializer):
    """
    The Glorot uniform initializer, also called Xavier uniform initializer.

    Draws samples from a uniform distribution within `[-limit, limit]`, where
    `limit = sqrt(6 / (fan_in + fan_out))` (`fan_in` is the number of input
    units in the weight tensor and `fan_out` is the number of output units).

    Examples:

    >>> # Standalone usage:
    >>> initializer = GlorotUniform()
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = GlorotUniform()
    >>> layer = Dense(3, kernel_initializer=initializer)

    Args:
        seed: A Python integer or instance of
            `keras.backend.SeedGenerator`.
            Used to make the behavior of the initializer
            deterministic. Note that an initializer seeded with an integer
            or `None` (unseeded) will produce the same random values
            across multiple calls. To get different random values
            across multiple calls, use as seed an instance
            of `keras.backend.SeedGenerator`.

    Reference:

    - [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    """
    def __init__(self, seed: int | None = None) -> None: ...

class TruncatedNormal(Initializer):
    """
    Initializer that generates a truncated normal distribution.

    The values generated are similar to values from a
    `RandomNormal` initializer, except that values more
    than two standard deviations from the mean are
    discarded and re-drawn.

    Examples:

    >>> # Standalone usage:
    >>> initializer = TruncatedNormal(mean=0., stddev=1.)
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = TruncatedNormal(mean=0., stddev=1.)
    >>> layer = Dense(3, kernel_initializer=initializer)

    Args:
        mean: A python scalar or a scalar keras tensor. Mean of the random
            values to generate.
        stddev: A python scalar or a scalar keras tensor. Standard deviation of
           the random values to generate.
        seed: A Python integer or instance of
            `keras.backend.SeedGenerator`.
            Used to make the behavior of the initializer
            deterministic. Note that an initializer seeded with an integer
            or `None` (unseeded) will produce the same random values
            across multiple calls. To get different random values
            across multiple calls, use as seed an instance
            of `keras.backend.SeedGenerator`.
    """
    def __init__(self, mean: TensorCompatible = 0.0, stddev: TensorCompatible = 0.05, seed: int | None = None) -> None: ...

class RandomNormal(Initializer):
    """
    Random normal initializer.

    Draws samples from a normal distribution for given parameters.

    Examples:

    >>> # Standalone usage:
    >>> initializer = RandomNormal(mean=0.0, stddev=1.0)
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = RandomNormal(mean=0.0, stddev=1.0)
    >>> layer = Dense(3, kernel_initializer=initializer)

    Args:
        mean: A python scalar or a scalar keras tensor. Mean of the random
            values to generate.
        stddev: A python scalar or a scalar keras tensor. Standard deviation of
           the random values to generate.
        seed: A Python integer or instance of
            `keras.backend.SeedGenerator`.
            Used to make the behavior of the initializer
            deterministic. Note that an initializer seeded with an integer
            or `None` (unseeded) will produce the same random values
            across multiple calls. To get different random values
            across multiple calls, use as seed an instance
            of `keras.backend.SeedGenerator`.
    """
    def __init__(self, mean: TensorCompatible = 0.0, stddev: TensorCompatible = 0.05, seed: int | None = None) -> None: ...

class RandomUniform(Initializer):
    """
    Random uniform initializer.

    Draws samples from a uniform distribution for given parameters.

    Examples:

    >>> # Standalone usage:
    >>> initializer = RandomUniform(minval=0.0, maxval=1.0)
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = RandomUniform(minval=0.0, maxval=1.0)
    >>> layer = Dense(3, kernel_initializer=initializer)

    Args:
        minval: A python scalar or a scalar keras tensor. Lower bound of the
            range of random values to generate (inclusive).
        maxval: A python scalar or a scalar keras tensor. Upper bound of the
            range of random values to generate (exclusive).
        seed: A Python integer or instance of
            `keras.backend.SeedGenerator`.
            Used to make the behavior of the initializer
            deterministic. Note that an initializer seeded with an integer
            or `None` (unseeded) will produce the same random values
            across multiple calls. To get different random values
            across multiple calls, use as seed an instance
            of `keras.backend.SeedGenerator`.
    """
    def __init__(self, minval: TensorCompatible = -0.05, maxval: TensorCompatible = 0.05, seed: int | None = None) -> None: ...

class Zeros(Initializer):
    """
    Initializer that generates tensors initialized to 0.

    Examples:

    >>> # Standalone usage:
    >>> initializer = Zeros()
    >>> values = initializer(shape=(2, 2))

    >>> # Usage in a Keras layer:
    >>> initializer = Zeros()
    >>> layer = Dense(units=3, kernel_initializer=initializer)
    """
    ...

constant = Constant
glorot_normal = GlorotNormal
glorot_uniform = GlorotUniform
truncated_normal = TruncatedNormal
zeros = Zeros

_Initializer: TypeAlias = (  # noqa: Y047
    str | Initializer | type[Initializer] | Callable[[ShapeLike], Tensor] | dict[str, Any] | None
)

@overload
def get(identifier: None) -> None:
    """
    Retrieves a Keras initializer object via an identifier.

    The `identifier` may be the string name of a initializers function or class
    (case-sensitively).

    >>> identifier = 'Ones'
    >>> keras.initializers.get(identifier)
    <...keras.initializers.initializers.Ones...>

    You can also specify `config` of the initializer to this function by passing
    dict containing `class_name` and `config` as an identifier. Also note that
    the `class_name` must map to a `Initializer` class.

    >>> cfg = {'class_name': 'Ones', 'config': {}}
    >>> keras.initializers.get(cfg)
    <...keras.initializers.initializers.Ones...>

    In the case that the `identifier` is a class, this method will return a new
    instance of the class by its constructor.

    You may also pass a callable function with a signature that includes `shape`
    and `dtype=None` as an identifier.

    >>> fn = lambda shape, dtype=None: ops.ones(shape, dtype)
    >>> keras.initializers.get(fn)
    <function <lambda> at ...>

    Alternatively, you can pass a backend tensor or numpy array as the
    `identifier` to define the initializer values directly. Note that when
    calling the initializer, the specified `shape` argument must be the same as
    the shape of the tensor.

    >>> tensor = ops.ones(shape=(5, 5))
    >>> keras.initializers.get(tensor)
    <function get.<locals>.initialize_fn at ...>

    Args:
        identifier: A string, dict, callable function, or tensor specifying
            the initializer. If a string, it should be the name of an
            initializer. If a dict, it should contain the configuration of an
            initializer. Callable functions or predefined tensors are also
            accepted.

    Returns:
        Initializer instance base on the input identifier.
    """
    ...
@overload
def get(identifier: str | Initializer | dict[str, Any] | type[Initializer]) -> Initializer:
    """
    Retrieves a Keras initializer object via an identifier.

    The `identifier` may be the string name of a initializers function or class
    (case-sensitively).

    >>> identifier = 'Ones'
    >>> keras.initializers.get(identifier)
    <...keras.initializers.initializers.Ones...>

    You can also specify `config` of the initializer to this function by passing
    dict containing `class_name` and `config` as an identifier. Also note that
    the `class_name` must map to a `Initializer` class.

    >>> cfg = {'class_name': 'Ones', 'config': {}}
    >>> keras.initializers.get(cfg)
    <...keras.initializers.initializers.Ones...>

    In the case that the `identifier` is a class, this method will return a new
    instance of the class by its constructor.

    You may also pass a callable function with a signature that includes `shape`
    and `dtype=None` as an identifier.

    >>> fn = lambda shape, dtype=None: ops.ones(shape, dtype)
    >>> keras.initializers.get(fn)
    <function <lambda> at ...>

    Alternatively, you can pass a backend tensor or numpy array as the
    `identifier` to define the initializer values directly. Note that when
    calling the initializer, the specified `shape` argument must be the same as
    the shape of the tensor.

    >>> tensor = ops.ones(shape=(5, 5))
    >>> keras.initializers.get(tensor)
    <function get.<locals>.initialize_fn at ...>

    Args:
        identifier: A string, dict, callable function, or tensor specifying
            the initializer. If a string, it should be the name of an
            initializer. If a dict, it should contain the configuration of an
            initializer. Callable functions or predefined tensors are also
            accepted.

    Returns:
        Initializer instance base on the input identifier.
    """
    ...
@overload
def get(identifier: Callable[[ShapeLike], Tensor]) -> Callable[[ShapeLike], Tensor]: ...
def __getattr__(name: str): ...  # incomplete module
