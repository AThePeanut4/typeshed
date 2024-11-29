"""Implementation for Retry strategy during HTTP requests."""

from _typeshed import Incomplete
from collections.abc import Callable

from urllib3 import Retry

logger: Incomplete

class WritesRetry(Retry):
    """
    Writes retry configuration.

    The next delay is computed as random value between range
        `retry_interval * exponential_base^(attempts-1)` and `retry_interval * exponential_base^(attempts)

    Example:
        for retry_interval=5, exponential_base=2, max_retry_delay=125, total=5
        retry delays are random distributed values within the ranges of
        [5-10, 10-20, 20-40, 40-80, 80-125]
    """
    jitter_interval: Incomplete
    total: Incomplete
    retry_interval: Incomplete
    max_retry_delay: Incomplete
    max_retry_time: Incomplete
    exponential_base: Incomplete
    retry_timeout: Incomplete
    retry_callback: Incomplete
    def __init__(
        self,
        jitter_interval: int = 0,
        max_retry_delay: int = 125,
        exponential_base: int = 2,
        max_retry_time: int = 180,
        total: int = 5,
        retry_interval: int = 5,
        retry_callback: Callable[[Exception], int] | None = None,
        **kw,
    ) -> None:
        """
        Initialize defaults.

        :param int jitter_interval: random milliseconds when retrying writes
        :param num max_retry_delay: maximum delay when retrying write in seconds
        :param int max_retry_time: maximum total retry timeout in seconds,
                                   attempt after this timout throws MaxRetryError
        :param int total: maximum number of retries
        :param num retry_interval: initial first retry delay range in seconds
        :param int exponential_base: base for the exponential retry delay,
        :param Callable[[Exception], int] retry_callback: the callable ``callback`` to run after retryable
                                                          error occurred.
                                                          The callable must accept one argument:
                                                                - `Exception`: an retryable error
        """
        ...
    def new(self, **kw):
        """Initialize defaults."""
        ...
    def is_retry(self, method, status_code, has_retry_after: bool = False):
        """is_retry doesn't require retry_after header. If there is not Retry-After we will use backoff."""
        ...
    def get_backoff_time(self):
        """Variant of exponential backoff with initial and max delay and a random jitter delay."""
        ...
    def get_retry_after(self, response):
        """Get the value of Retry-After header and append random jitter delay."""
        ...
    def increment(
        self,
        method: Incomplete | None = None,
        url: Incomplete | None = None,
        response: Incomplete | None = None,
        error: Incomplete | None = None,
        _pool: Incomplete | None = None,
        _stacktrace: Incomplete | None = None,
    ):
        """Return a new Retry object with incremented retry counters."""
        ...
