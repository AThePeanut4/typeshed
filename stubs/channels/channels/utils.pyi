from collections.abc import Awaitable, Callable
from typing import Any, Protocol, type_check_only
from typing_extensions import TypeAlias

from asgiref.typing import ASGIApplication, ASGIReceiveCallable

def name_that_thing(thing: object) -> str:
    """Returns either the function/class path or just the object's repr"""
    ...
async def await_many_dispatch(
    consumer_callables: list[Callable[[], Awaitable[ASGIReceiveCallable]]], dispatch: Callable[[dict[str, Any]], Awaitable[None]]
) -> None:
    """
    Given a set of consumer callables, awaits on them all and passes results
    from them to the dispatch awaitable as they come in.
    """
    ...

# Defines a generic ASGI middleware protocol.
# All arguments are typed as `Any` to maximize compatibility with third-party ASGI middleware
# that may not strictly follow type conventions or use more specific signatures.
@type_check_only
class _MiddlewareProtocol(Protocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def __call__(self, scope: Any, receive: Any, send: Any) -> Any: ...

_ChannelApplication: TypeAlias = _MiddlewareProtocol | ASGIApplication  # noqa: Y047
