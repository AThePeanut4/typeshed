from enum import Enum

class Reservoir:
    """
    Centralized thread-safe reservoir which holds fixed sampling
    quota, borrowed count and TTL.
    """
    def __init__(self) -> None: ...
    def borrow_or_take(self, now, can_borrow):
        """
        Decide whether to borrow or take one quota from
        the reservoir. Return ``False`` if it can neither
        borrow nor take. This method is thread-safe.
        """
        ...
    def load_quota(self, quota, TTL, interval) -> None:
        """
        Load new quota with a TTL. If the input is None,
        the reservoir will continue using old quota until it
        expires or has a non-None quota/TTL in a future load.
        """
        ...
    @property
    def quota(self): ...
    @property
    def TTL(self): ...

class ReservoirDecision(Enum):
    """
    An Enum of decisions the reservoir could make based on
    assigned quota with TTL and the current timestamp/usage.
    """
    TAKE = "take"
    BORROW = "borrow"
    NO = "no"
