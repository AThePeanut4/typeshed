from collections.abc import Callable, Iterable
from typing import TypeVar

from redis.backoff import AbstractBackoff

_T = TypeVar("_T")

class Retry:
    """Retry a specific number of times after a failure"""
    def __init__(self, backoff: AbstractBackoff, retries: int, supported_errors: tuple[type[Exception], ...] = ...) -> None:
        """
        Initialize a `Retry` object with a `Backoff` object
        that retries a maximum of `retries` times.
        `retries` can be negative to retry forever.
        You can specify the types of supported errors which trigger
        a retry with the `supported_errors` parameter.
        """
        ...
    def update_supported_errors(self, specified_errors: Iterable[type[Exception]]) -> None:
        """Updates the supported errors with the specified error types"""
        ...
    def call_with_retry(self, do: Callable[[], _T], fail: Callable[[Exception], object]) -> _T:
        """
        Execute an operation that might fail and returns its result, or
        raise the exception that was thrown depending on the `Backoff` object.
        `do`: the operation to call. Expects no argument.
        `fail`: the failure handler, expects the last error that was thrown
        """
        ...
