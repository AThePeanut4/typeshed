"""
West Virginia

Christmas Eve and New Years Eve are considered as half-holidays. By default,
they're not included as "non-working days". If for your personal use you want
to include them, you may just have to create a class like this:

.. code::

    class WestVirginiaIncludeEves(WestVirginia):
        west_virginia_include_christmas_eve = True
        west_virginia_include_nye = True
"""

from typing import ClassVar

from .core import UnitedStates

class WestVirginia(UnitedStates):
    """West Virginia"""
    west_virginia_include_christmas_eve: ClassVar[bool]
    west_virginia_include_nye: ClassVar[bool]
