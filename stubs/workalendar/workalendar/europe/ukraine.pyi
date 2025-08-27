from typing import ClassVar

from ..core import OrthodoxCalendar

class Ukraine(OrthodoxCalendar):
    """Ukraine"""
    shift_sunday_holidays: ClassVar[bool]
