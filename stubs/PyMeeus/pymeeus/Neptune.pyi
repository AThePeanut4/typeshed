from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Neptune:
    """Class Neptune models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool | None = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Neptune for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Neptune position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param tofk5: Whether or not the small correction to convert to the FK5
            system will be applied or not
        :type tofk5: bool

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(2018, 10, 27.0)
        >>> l, b, r = Neptune.geometric_heliocentric_position(epoch)
        >>> print(round(l.to_positive(), 4))
        345.3776
        >>> print(round(b, 4))
        -0.9735
        >>> print(round(r, 5))
        29.93966
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Neptune for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Neptune position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.
        """
        ...
    @staticmethod
    def orbital_elements_mean_equinox(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Neptune for the mean
        equinox of the date for a given epoch.

        :param epoch: Epoch to compute orbital elements, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the following six orbital elements:
            - Mean longitude of the planet (Angle)
            - Semimajor axis of the orbit (float, astronomical units)
            - eccentricity of the orbit (float)
            - inclination on the plane of the ecliptic (Angle)
            - longitude of the ascending node (Angle)
            - argument of the perihelion (Angle)
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(2065, 6, 24.0)
        >>> l, a, e, i, ome, arg = Neptune.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        88.321947
        >>> print(round(a, 8))
        30.11038676
        >>> print(round(e, 7))
        0.0094597
        >>> print(round(i, 6))
        1.763855
        >>> print(round(ome, 5))
        132.46986
        >>> print(round(arg, 6))
        -83.415521
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Neptune for the
        standard equinox J2000.0 for a given epoch.

        :param epoch: Epoch to compute orbital elements, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the following six orbital elements:
            - Mean longitude of the planet (Angle)
            - Semimajor axis of the orbit (float, astronomical units)
            - eccentricity of the orbit (float)
            - inclination on the plane of the ecliptic (Angle)
            - longitude of the ascending node (Angle)
            - argument of the perihelion (Angle)
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(2065, 6, 24.0)
        >>> l, a, e, i, ome, arg = Neptune.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        87.407029
        >>> print(round(a, 8))
        30.11038676
        >>> print(round(e, 7))
        0.0094597
        >>> print(round(i, 6))
        1.770101
        >>> print(round(ome, 5))
        131.74402
        >>> print(round(arg, 6))
        -83.6046
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Neptune (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Neptune.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        19h 17' 14.5''
        >>> print(dec.dms_str(n_dec=1))
        -21d 34' 15.1''
        >>> print(elon.dms_str(n_dec=1))
        19d 44' 59.6''
        """
        ...
    @staticmethod
    def conjunction(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the conjunction closest to the
        given epoch.

        :param epoch: Epoch close to the desired conjunction
        :type epoch: :py:class:`Epoch`

        :returns: The time when the conjunction happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1993, 10, 1.0)
        >>> conj = Neptune.conjunction(epoch)
        >>> y, m, d = conj.get_date()
        >>> print(y)
        1994
        >>> print(m)
        1
        >>> print(round(d, 4))
        11.3057
        """
        ...
    @staticmethod
    def opposition(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the opposition closest to the given
        epoch.

        :param epoch: Epoch close to the desired opposition
        :type epoch: :py:class:`Epoch`

        :returns: The time when the opposition happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1846, 8, 1)
        >>> oppo = Neptune.opposition(epoch)
        >>> y, m, d = oppo.get_date()
        >>> print(y)
        1846
        >>> print(m)
        8
        >>> print(round(d, 4))
        20.1623
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float) -> float:
        """
        This function computes the approximate magnitude of Neptune.

        :param sun_dist: Distance from Neptune to Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance Neptune to Earth, in Astronomical Units
        :type earth_dist: float

        :returns: Neptune's magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.
        """
        ...

def main() -> None: ...
