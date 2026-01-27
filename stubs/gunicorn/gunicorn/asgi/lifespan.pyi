"""
ASGI lifespan protocol manager.

Manages startup and shutdown events for ASGI applications,
enabling frameworks like FastAPI to run initialization and
cleanup code.
"""

from _typeshed import Incomplete

from gunicorn.glogging import Logger as GLogger

from .._types import _ASGIAppType

class LifespanManager:
    """
    Manages ASGI lifespan events (startup/shutdown).

    The lifespan protocol allows ASGI applications to run code at
    startup and shutdown. This is essential for applications that
    need to initialize database connections, caches, or other
    resources.

    ASGI lifespan messages:
    - Server sends: {"type": "lifespan.startup"}
    - App responds: {"type": "lifespan.startup.complete"} or
                    {"type": "lifespan.startup.failed", "message": "..."}
    - Server sends: {"type": "lifespan.shutdown"}
    - App responds: {"type": "lifespan.shutdown.complete"}
    """
    app: _ASGIAppType
    logger: GLogger
    state: dict[Incomplete, Incomplete]

    def __init__(self, app: _ASGIAppType, logger: GLogger, state: dict[Incomplete, Incomplete] | None = None) -> None:
        """
        Initialize the lifespan manager.

        Args:
            app: ASGI application callable
            logger: Logger instance
            state: Shared state dict for the application
        """
        ...
    async def startup(self) -> None:
        """
        Run lifespan startup and wait for completion.

        Raises:
            RuntimeError: If startup fails or app doesn't support lifespan
        """
        ...
    async def shutdown(self) -> None:
        """
        Signal shutdown and wait for completion.

        This should be called during graceful shutdown.
        """
        ...
