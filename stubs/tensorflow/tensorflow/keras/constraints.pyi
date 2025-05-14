from collections.abc import Callable
from typing import Any, overload

from tensorflow import Tensor

class Constraint:
    """
    Base class for weight constraints.

    A `Constraint` instance works like a stateless function.
    Users who subclass this
    class should override the `__call__()` method, which takes a single
    weight parameter and return a projected version of that parameter
    (e.g. normalized or clipped). Constraints can be used with various Keras
    layers via the `kernel_constraint` or `bias_constraint` arguments.

    Here's a simple example of a non-negative weight constraint:

    >>> class NonNegative(keras.constraints.Constraint):
    ...
    ...  def __call__(self, w):
    ...    return w * ops.cast(ops.greater_equal(w, 0.), dtype=w.dtype)

    >>> weight = ops.convert_to_tensor((-1.0, 1.0))
    >>> NonNegative()(weight)
    [0.,  1.]

    Usage in a layer:

    >>> keras.layers.Dense(4, kernel_constraint=NonNegative())
    """
    def get_config(self) -> dict[str, Any]:
        """
        Returns a Python dict of the object config.

        A constraint config is a Python dictionary (JSON-serializable) that can
        be used to reinstantiate the same object.

        Returns:
            Python dict containing the configuration of the constraint object.
        """
        ...
    def __call__(self, w: Tensor, /) -> Tensor:
        """
        Applies the constraint to the input weight variable.

        By default, the inputs weight variable is not modified.
        Users should override this method to implement their own projection
        function.

        Args:
            w: Input weight variable.

        Returns:
            Projected variable (by default, returns unmodified inputs).
        """
        ...

@overload
def get(identifier: None) -> None:
    """Retrieve a Keras constraint object via an identifier."""
    ...
@overload
def get(identifier: str | dict[str, Any] | Constraint) -> Constraint:
    """Retrieve a Keras constraint object via an identifier."""
    ...
@overload
def get(identifier: Callable[[Tensor], Tensor]) -> Callable[[Tensor], Tensor]: ...
def __getattr__(name: str): ...  # incomplete module
