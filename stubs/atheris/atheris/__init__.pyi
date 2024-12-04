"""Atheris is a coverage-guided Python fuzzing engine."""

from collections.abc import Callable

def Setup(
    args: list[str],
    test_one_input: Callable[[bytes], None],
    **kwargs: bool | Callable[[bytes, int, int], str | bytes] | Callable[[bytes, bytes, int, int], str | bytes] | None,
) -> list[str]:
    """Setup(arg0: List[str], arg1: Callable[[bytes], None], **kwargs) -> List[str]"""
    ...
def Fuzz() -> None:
    """Fuzz() -> None"""
    ...
def Mutate(data: bytes, max_size: int) -> bytes:
    """Mutate(arg0: bytes, arg1: int) -> bytes"""
    ...
