"""Library of dtypes (Tensor element types)."""

import dataclasses
from _typeshed import Incomplete

@dataclasses.dataclass(frozen=True)
class HandleData:
    """Holds resource/variant tensor specific data."""
    shape_inference: Incomplete | None = None
    alias_id: int | None = None
