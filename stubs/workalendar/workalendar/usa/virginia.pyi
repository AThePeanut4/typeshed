"""
Virginia module

You may or may want not to treat the Day before Thanksgiving as a non-working
day by implementing the following class:

.. code::

    from workalenda.usa import Virginia as VirginiaBase

    class Virginia(VirginiaBase):
        include_thanksgiving_wednesday = False
"""

from typing import ClassVar

from .core import UnitedStates

class Virginia(UnitedStates):
    include_thanksgiving_wednesday: ClassVar[bool]
