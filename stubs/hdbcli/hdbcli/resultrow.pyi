from collections.abc import Iterator, Sequence
from typing import Any, overload

class ResultRow:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    column_names: tuple[str, ...]
    column_values: tuple[Any, ...]

    def __len__(self) -> int:
        """Return len(self)."""
        ...
    @overload
    def __getitem__(self, index: int) -> Any:
        """Return self[key]."""
        ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[Any]:
        """Return self[key]."""
        ...
    def __iter__(self) -> Iterator[Any]:
        """Implement iter(self)."""
        ...
    # __next__, __delitem__, __setitem__ are technically defined but lead always to an error
