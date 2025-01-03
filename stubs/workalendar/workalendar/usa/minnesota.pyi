from typing import ClassVar

from .core import UnitedStates

class Minnesota(UnitedStates):
    """Minnesota"""
    include_thanksgiving_friday: ClassVar[bool]
    include_columbus_day: ClassVar[bool]
