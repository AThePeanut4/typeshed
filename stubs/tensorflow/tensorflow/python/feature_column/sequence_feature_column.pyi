"""
This API defines FeatureColumn for sequential input.

NOTE: This API is a work in progress and will likely be changing frequently.
"""

from collections.abc import Callable
from typing_extensions import Self

import tensorflow as tf
from tensorflow._aliases import ShapeLike
from tensorflow.python.feature_column.feature_column_v2 import SequenceDenseColumn, _ExampleSpec, _FeatureColumn

# Strangely at runtime most of Sequence feature columns are defined in feature_column_v2 except
# for this one.
class SequenceNumericColumn(SequenceDenseColumn):
    """Represents sequences of numeric data."""
    key: str
    shape: ShapeLike
    default_value: float
    dtype: tf.DType
    normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None

    def __new__(
        _cls,
        key: str,
        shape: ShapeLike,
        default_value: float,
        dtype: tf.DType,
        normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None,
    ) -> Self:
        """Create new instance of SequenceNumericColumn(key, shape, default_value, dtype, normalizer_fn)"""
        ...
    @property
    def name(self) -> str:
        """See `FeatureColumn` base class."""
        ...
    @property
    def parse_example_spec(self) -> _ExampleSpec:
        """See `FeatureColumn` base class."""
        ...
    @property
    def parents(self) -> list[_FeatureColumn | str]:
        """See 'FeatureColumn` base class."""
        ...
