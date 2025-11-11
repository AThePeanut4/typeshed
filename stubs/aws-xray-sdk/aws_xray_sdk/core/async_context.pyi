from asyncio.events import AbstractEventLoop
from asyncio.tasks import Task, _TaskCompatibleCoro
from typing import Any, TypeVar

from .context import Context as _Context

_T_co = TypeVar("_T_co", covariant=True)

class AsyncContext(_Context):
    """
    Async Context for storing segments.

    Inherits nearly everything from the main Context class.
    Replaces threading.local with a task based local storage class,
    Also overrides clear_trace_entities
    """
    def __init__(
        self, context_missing: str = "LOG_ERROR", loop: AbstractEventLoop | None = None, use_task_factory: bool = True
    ) -> None: ...
    def clear_trace_entities(self) -> None:
        """Clear all trace_entities stored in the task local context."""
        ...

class TaskLocalStorage:
    """Simple task local storage"""
    def __init__(self, loop: AbstractEventLoop | None = None) -> None: ...
    # Sets unknown items on the current task's context attribute
    def __setattr__(self, name: str, value: Any) -> None: ...
    # Returns unknown items from the current tasks context attribute
    def __getattribute__(self, item: str) -> Any | None: ...
    def clear(self) -> None: ...

def task_factory(loop: AbstractEventLoop | None, coro: _TaskCompatibleCoro[_T_co]) -> Task[_T_co]:
    """
    Task factory function

    Fuction closely mirrors the logic inside of
    asyncio.BaseEventLoop.create_task. Then if there is a current
    task and the current task has a context then share that context
    with the new task
    """
    ...
