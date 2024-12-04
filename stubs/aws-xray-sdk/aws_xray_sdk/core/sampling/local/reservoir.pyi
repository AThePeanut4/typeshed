from typing import Any

class Reservoir:
    """
    Keeps track of the number of sampled segments within
    a single second. This class is implemented to be
    thread-safe to achieve accurate sampling.
    """
    traces_per_sec: Any
    used_this_sec: int
    this_sec: Any
    def __init__(self, traces_per_sec: int = 0) -> None:
        """
        :param int traces_per_sec: number of guranteed
            sampled segments.
        """
        ...
    def take(self):
        """
        Returns True if there are segments left within the
        current second, otherwise return False.
        """
        ...
