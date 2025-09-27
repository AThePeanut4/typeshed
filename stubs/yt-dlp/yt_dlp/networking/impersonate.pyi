from abc import ABC
from dataclasses import dataclass
from typing import Any
from typing_extensions import Self

from .common import Request, RequestHandler

@dataclass(order=True, frozen=True)
class ImpersonateTarget:
    """
    A target for browser impersonation.

    Parameters:
    @param client: the client to impersonate
    @param version: the client version to impersonate
    @param os: the client OS to impersonate
    @param os_version: the client OS version to impersonate

    Note: None is used to indicate to match any.
    """
    client: str | None = ...
    version: str | None = ...
    os: str | None = ...
    os_version: str | None = ...

    def __post_init__(self) -> None: ...
    def __contains__(self, target: Self) -> bool: ...
    @classmethod
    def from_str(cls, target: str) -> Self: ...

class ImpersonateRequestHandler(RequestHandler, ABC):
    _SUPPORTED_IMPERSONATE_TARGET_MAP: dict[ImpersonateTarget, Any]  # Copied from source.

    def __init__(
        self,
        *,
        impersonate: ImpersonateTarget | None = None,
        # All keyword arguments are ignored (passed to RequestHandler as **kwargs but RequestHandler.__init__() has **_ and does
        # not use it).
        **kwargs: Any,
    ) -> None: ...
    @property
    def supported_targets(cls) -> tuple[ImpersonateTarget, ...]: ...
    def is_supported_target(self, target: ImpersonateTarget) -> bool: ...

def impersonate_preference(rh: RequestHandler, request: Request) -> int: ...
