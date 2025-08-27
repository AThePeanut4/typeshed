from collections.abc import Iterable
from typing import ClassVar

from .core import Calendar

class IsoRegistry:
    """
    Registry for all calendars retrievable
    by ISO 3166-2 codes associated with countries
    where they are used as official calendars.

    Two letter codes are favored for any subdivisions.
    """
    STANDARD_MODULES: ClassVar[tuple[str, ...]]
    region_registry: dict[str, type[Calendar]]
    def __init__(self, load_standard_modules: bool | None = True) -> None: ...
    def register(self, iso_code: str, cls: type[Calendar]) -> None:
        """Store the ``cls`` in the region_registry."""
        ...
    def load_module_from_items(self, module_name: str, items: Iterable[str]) -> None:
        """Load all registered classes in the registry"""
        ...
    def get(self, iso_code: str) -> type[Calendar]:
        """
        Retrieve calendar class associated with given ``iso_code``.

        If calendar of subdivision is not registered
        (for subdivision like ISO codes, e.g. GB-ENG)
        returns calendar of containing region
        (e.g. United Kingdom for ISO code GB) if it's available.

        :rtype: Calendar
        """
        ...
    def get_subregions(self, iso_code: str) -> dict[str, type[Calendar]]:
        """
        Returns subregion calendar classes for given region iso_code.

        >>> registry = IsoRegistry()
        >>> # assuming calendars registered are: DE, DE-HH, DE-BE
        >>> registry.get_subregions('DE')
        {'DE-HH': <class 'workalendar.europe.germany.Hamburg'>,
        'DE-BE': <class 'workalendar.europe.germany.Berlin'>}
        :rtype dict
        :return dict where keys are ISO codes strings
        and values are calendar classes
        """
        ...
    def get_calendars(
        self, region_codes: Iterable[str] | None = None, include_subregions: bool | None = False
    ) -> dict[str, type[Calendar]]:
        """
        Returns calendar classes for regions

        :param region_codes list of ISO codes for selected regions. If empty,
                            the function will return all items from the
                            registry.
        :param include_subregions boolean if subregions
        of selected regions should be included in result
        :rtype dict
        :return dict where keys are ISO codes strings
        and values are calendar classes
        """
        ...

registry: IsoRegistry
