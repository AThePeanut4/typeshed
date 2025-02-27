from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, Literal, overload

import numpy as np
from numpy.typing import ArrayLike, NDArray

BFIndex: Incomplete

class Index:
    ef: int
    num_threads: int

    @overload
    def __init__(self, params: dict[str, Any]) -> None:
        """
        __init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: hnswlib.Index, params: dict) -> None

        2. __init__(self: hnswlib.Index, index: hnswlib.Index) -> None

        3. __init__(self: hnswlib.Index, space: str, dim: int) -> None
        """
        ...
    @overload
    def __init__(self, index: Index) -> None:
        """
        __init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: hnswlib.Index, params: dict) -> None

        2. __init__(self: hnswlib.Index, index: hnswlib.Index) -> None

        3. __init__(self: hnswlib.Index, space: str, dim: int) -> None
        """
        ...
    @overload
    def __init__(self, space: Literal["l2", "ip", "cosine"], dim: int) -> None: ...
    def add_items(
        self, data: ArrayLike, ids: ArrayLike | None = None, num_threads: int = -1, replace_deleted: bool = False
    ) -> None: ...
    def get_current_count(self) -> int: ...
    def get_ids_list(self) -> list[int]: ...
    @overload
    def get_items(self, ids: ArrayLike | None = ..., return_type: Literal["list"] = ...) -> list[float]: ...
    @overload
    def get_items(self, ids: ArrayLike | None = ..., return_type: Literal["numpy"] = ...) -> NDArray[np.float32]: ...
    @overload
    def get_items(
        self, ids: ArrayLike | None = None, return_type: Literal["numpy", "list"] = "numpy"
    ) -> NDArray[np.float32] | list[float]: ...
    def get_max_elements(self) -> int: ...
    def index_file_size(self) -> int: ...
    def init_index(
        self,
        max_elements: int,
        M: int = 16,
        ef_construction: int = 200,
        random_seed: int = 100,
        allow_replace_delete: bool = False,
    ) -> None:
        """init_index(self: hnswlib.Index, max_elements: int, M: int = 16, ef_construction: int = 200, random_seed: int = 100, allow_replace_deleted: bool = False) -> None"""
        ...
    def knn_query(
        self, data: ArrayLike, k: int = 1, num_threads: int = -1, filter: Callable[[int], bool] | None = None
    ) -> tuple[NDArray[np.uint64], NDArray[np.float32]]: ...
    def load_index(self, path_to_index: str, max_elements: int = 0, allow_replace_delete: bool = False) -> None: ...
    def mark_deleted(self, label: int) -> None: ...
    def resize_index(self, new_size: int) -> None: ...
    def save_index(self, path_to_index: str) -> None: ...
    def set_ef(self, ef: int) -> None: ...
    def set_num_threads(self, num_threads: int) -> None: ...
    def unmark_deleted(self, label: int) -> None: ...
    @property
    def M(self) -> int: ...
    @property
    def dim(self) -> int: ...
    @property
    def ef_construction(self) -> int: ...
    @property
    def element_count(self) -> int: ...
    @property
    def max_elements(self) -> int: ...
    @property
    def space(self) -> str: ...
