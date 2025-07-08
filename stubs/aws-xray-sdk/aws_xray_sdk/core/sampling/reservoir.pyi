from enum import Enum

class Reservoir:
    """
    Centralized thread-safe reservoir which holds fixed sampling
    quota, borrowed count and TTL.
    """
    def __init__(self) -> None: ...
    def borrow_or_take(self, now: int, can_borrow: bool | None) -> ReservoirDecision | None: ...
    def load_quota(self, quota: int | None, TTL: int | None, interval: int | None) -> None: ...
    @property
    def quota(self) -> int | None: ...
    @property
    def TTL(self) -> int | None: ...

class ReservoirDecision(Enum):
    """
    An Enum of decisions the reservoir could make based on
    assigned quota with TTL and the current timestamp/usage.
    """
    TAKE = "take"
    BORROW = "borrow"
    NO = "no"
