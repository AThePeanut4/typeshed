from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

PLUTO_ARGUMENT: Final[list[tuple[float, float, float]]]
PLUTO_LONGITUDE: Final[list[tuple[float, float]]]
PLUTO_LATITUDE: Final[list[tuple[float, float]]]
PLUTO_RADIUS_VECTOR: Final[list[tuple[float, float]]]

class Pluto:
    """Class Pluto models that minor planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Pluto for a given epoch.

        :param epoch: Epoch to compute Pluto position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the 1885-2099 range.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> l, b, r = Pluto.geometric_heliocentric_position(epoch)
        >>> print(round(l, 5))
        232.74071
        >>> print(round(b, 5))
        14.58782
        >>> print(round(r, 6))
        29.711111
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle]:
        """
        This method computes the geocentric position of Pluto (right
        ascension and declination) for the given epoch, for the standard
        equinox J2000.0.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension and the declination as
            Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the 1885-2099 range.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> ra, dec = Pluto.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        15h 31' 43.7''
        >>> print(dec.dms_str(n_dec=0))
        -4d 27' 29.0''
        """
        ...

def main() -> None: ...
