"""Public API for tf._api.v2.experimental namespace"""

from _typeshed import Incomplete
from abc import ABC
from typing import Generic, TypeVar

_T_co = TypeVar("_T_co", covariant=True)

class Optional(ABC, Generic[_T_co]):
    """
    Represents a value that may or may not be present.

    A `tf.experimental.Optional` can represent the result of an operation that may
    fail as a value, rather than raising an exception and halting execution. For
    example, `tf.data.Iterator.get_next_as_optional()` returns a
    `tf.experimental.Optional` that either contains the next element of an
    iterator if one exists, or an "empty" value that indicates the end of the
    sequence has been reached.

    `tf.experimental.Optional` can only be used with values that are convertible
    to `tf.Tensor` or `tf.CompositeTensor`.

    One can create a `tf.experimental.Optional` from a value using the
    `from_value()` method:

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.has_value())
    tf.Tensor(True, shape=(), dtype=bool)
    >>> print(optional.get_value())
    tf.Tensor(42, shape=(), dtype=int32)

    or without a value using the `empty()` method:

    >>> optional = tf.experimental.Optional.empty(
    ...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
    >>> print(optional.has_value())
    tf.Tensor(False, shape=(), dtype=bool)
    """
    def __getattr__(self, name: str) -> Incomplete: ...

def __getattr__(name: str) -> Incomplete: ...
