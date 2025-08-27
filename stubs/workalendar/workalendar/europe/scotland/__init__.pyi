"""
Scotland specific module.

The main source of information is:
https://en.wikipedia.org/wiki/Public_and_bank_holidays_in_Scotland

Note on "inheritance":

* Carnoustie and Monifieth area is a subdivision of Angus
* Lanark is part of South Lanarkshire

FIXME:

* Galashiels is part of the Scottish Borders
* Hawick is part of the Scottish Borders
* Kilmarnock is probably part of AyrShire (?)
* Lanark is part of South Lanarkshire
* Linlithgow... part of N/A
* Lochaber... part of N/A
* ...
"""

import datetime
from typing import ClassVar

from ...core import WesternCalendar
from .mixins import (
    AutumnHolidayFirstMondayOctober,
    AutumnHolidayLastMondaySeptember,
    AutumnHolidaySecondMondayOctober,
    AutumnHolidayThirdMondayOctober,
    AyrGoldCup,
    BattleStirlingBridge,
    FairHolidayFirstMondayAugust,
    FairHolidayFirstMondayJuly,
    FairHolidayFourthFridayJuly,
    FairHolidayLastMondayJuly,
    FairHolidayLastMondayJune,
    FairHolidaySecondMondayJuly,
    FairHolidayThirdMondayJuly,
    LateSummer,
    SpringHolidayFirstMondayApril,
    SpringHolidayFirstMondayJune,
    SpringHolidayLastMondayMay,
    SpringHolidaySecondMondayApril,
    SpringHolidayTuesdayAfterFirstMondayMay,
    VictoriaDayFirstMondayJune,
    VictoriaDayFourthMondayMay,
    VictoriaDayLastMondayMay,
)

class Scotland(WesternCalendar):
    """Scotland"""
    include_spring_holiday: ClassVar[bool]
    spring_holiday_label: ClassVar[str]
    include_fair_holiday: ClassVar[bool]
    include_autumn_holiday: ClassVar[bool]
    include_saint_andrew: ClassVar[bool]
    include_victoria_day: ClassVar[bool]
    def __init__(self, *args, **kwargs) -> None: ...
    def get_may_day(self, year: int) -> tuple[datetime.date, str]:
        """May Day is the first Monday in May"""
        ...
    def get_spring_holiday(self, year: int) -> tuple[datetime.date, str]:
        """
        Return spring holiday date and label.

        You need to implement it as soon as the flag `include_spring_holiday`
        is True.
        """
        ...
    def get_fair_holiday(self, year: int) -> tuple[datetime.date, str]:
        """
        Return fair holiday date and label.

        You need to implement it as soon as the flag `include_fair_holiday`
        is True.
        """
        ...
    def get_autumn_holiday(self, year: int) -> tuple[datetime.date, str]:
        """
        Return autumn holiday date and label.

        You need to implement it as soon as the flag `include_autumn_holiday`
        is True.
        """
        ...
    def get_victoria_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Return Victoria day date and label.

        You need to implement it as soon as the flag `include_victoria_day`
        is True.
        """
        ...

class Aberdeen(FairHolidaySecondMondayJuly, AutumnHolidayLastMondaySeptember, Scotland):
    """Aberdeen"""
    ...
class Angus(SpringHolidaySecondMondayApril, AutumnHolidayLastMondaySeptember, Scotland):
    """Angus"""
    ...
class Arbroath(FairHolidayThirdMondayJuly, Scotland):
    """Arbroath"""
    ...
class Ayr(SpringHolidayLastMondayMay, AyrGoldCup, Scotland):
    """Ayr"""
    ...
class CarnoustieMonifieth(SpringHolidayFirstMondayApril, AutumnHolidayFirstMondayOctober, Scotland):
    """Carnoustie & Monifieth"""
    ...
class Clydebank(SpringHolidayTuesdayAfterFirstMondayMay, Scotland):
    """Clydebank"""
    ...
class DumfriesGalloway(Scotland):
    """Dumfries & Galloway"""
    ...
class Dundee(
    SpringHolidayFirstMondayApril, VictoriaDayLastMondayMay, FairHolidayLastMondayJuly, AutumnHolidayFirstMondayOctober, Scotland
):
    """Dundee"""
    ...
class EastDunbartonshire(SpringHolidayLastMondayMay, FairHolidayThirdMondayJuly, AutumnHolidayLastMondaySeptember, Scotland):
    """East Dunbartonshire"""
    ...
class Edinburgh(Scotland):
    """Edinburgh"""
    ...
class Elgin(SpringHolidaySecondMondayApril, FairHolidayLastMondayJune, LateSummer, AutumnHolidayThirdMondayOctober, Scotland):
    """Elgin"""
    ...
class Falkirk(FairHolidayFirstMondayJuly, BattleStirlingBridge, Scotland):
    """Falkirk"""
    ...
class Fife(VictoriaDayFirstMondayJune, FairHolidayThirdMondayJuly, AutumnHolidayThirdMondayOctober, Scotland):
    """Fife"""
    ...
class Galashiels(SpringHolidayFirstMondayJune, Scotland):
    """Galashiels"""
    ...
class Glasgow(SpringHolidayLastMondayMay, FairHolidayThirdMondayJuly, AutumnHolidayLastMondaySeptember, Scotland):
    """Glasgow"""
    ...
class Hawick(Scotland):
    """Hawick"""
    ...
class Inverclyde(LateSummer, Scotland):
    """Inverclyde"""
    ...
class Inverness(SpringHolidayFirstMondayApril, FairHolidayFirstMondayJuly, AutumnHolidayFirstMondayOctober, Scotland):
    """Inverness"""
    ...
class Kilmarnock(AyrGoldCup, Scotland):
    """Kilmarnock"""
    ...
class Lanark(Scotland):
    """Lanark"""
    ...
class Linlithgow(Scotland):
    """Linlithgow"""
    ...
class Lochaber(Scotland):
    """Lochaber"""
    ...
class NorthLanarkshire(SpringHolidayLastMondayMay, FairHolidayThirdMondayJuly, AutumnHolidayLastMondaySeptember, Scotland):
    """North Lanarkshire"""
    ...
class Paisley(VictoriaDayLastMondayMay, FairHolidayFirstMondayAugust, AutumnHolidayLastMondaySeptember, Scotland):
    """Paisley"""
    ...
class Perth(
    SpringHolidayFirstMondayApril, VictoriaDayFourthMondayMay, BattleStirlingBridge, AutumnHolidayFirstMondayOctober, Scotland
):
    """Perth"""
    ...
class ScottishBorders(SpringHolidayFirstMondayApril, FairHolidayFourthFridayJuly, AutumnHolidaySecondMondayOctober, Scotland):
    """Scottish Borders"""
    ...
class SouthLanarkshire(SpringHolidayLastMondayMay, FairHolidayThirdMondayJuly, AutumnHolidayLastMondaySeptember, Scotland):
    """South Lanarkshire"""
    ...
class Stirling(SpringHolidayTuesdayAfterFirstMondayMay, BattleStirlingBridge, Scotland):
    """Stirling"""
    ...
class WestDunbartonshire(AutumnHolidayLastMondaySeptember, Scotland):
    """West Dunbartonshire"""
    ...
