from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Mercury:
    """Class Mercury models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool | None = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Mercury for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Mercury position, as an Epoch object
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
        >>> l, b, r = Mercury.geometric_heliocentric_position(epoch)
        >>> print(round(l.to_positive(), 4))
        287.4887
        >>> print(round(b, 4))
        -6.0086
        >>> print(round(r, 5))
        0.45113
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Mercury for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Mercury position, as an Epoch object
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
        This method computes the orbital elements of Mercury for the mean
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
        >>> l, a, e, i, ome, arg = Mercury.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        203.494701
        >>> print(round(a, 8))
        0.38709831
        >>> print(round(e, 7))
        0.2056451
        >>> print(round(i, 6))
        7.006171
        >>> print(round(ome, 5))
        49.10765
        >>> print(round(arg, 6))
        29.367732
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Mercury for the
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
        >>> l, a, e, i, ome, arg = Mercury.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        202.579453
        >>> print(round(a, 8))
        0.38709831
        >>> print(round(e, 7))
        0.2056451
        >>> print(round(i, 6))
        7.001089
        >>> print(round(ome, 5))
        48.24873
        >>> print(round(arg, 6))
        29.311401
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Mercury (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Mercury.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        16h 33' 59.3''
        >>> print(dec.dms_str(n_dec=1))
        -20d 53' 31.6''
        >>> print(elon.dms_str(n_dec=1))
        18d 24' 29.8''
        """
        ...
    @staticmethod
    def inferior_conjunction(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the inferior conjunction closest to
        the given epoch.

        :param epoch: Epoch close to the desired inferior conjunction
        :type epoch: :py:class:`Epoch`

        :returns: The time when the inferior conjunction happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1993, 10, 1.0)
        >>> conjunction = Mercury.inferior_conjunction(epoch)
        >>> y, m, d = conjunction.get_date()
        >>> print(y)
        1993
        >>> print(m)
        11
        >>> print(round(d, 4))
        6.1449
        >>> epoch = Epoch(1631, 10, 1.0)
        >>> conjunction = Mercury.inferior_conjunction(epoch)
        >>> y, m, d = conjunction.get_date()
        >>> print(y)
        1631
        >>> print(m)
        11
        >>> print(round(d, 3))
        7.306
        """
        ...
    @staticmethod
    def superior_conjunction(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the superior conjunction closest to
        the given epoch.

        :param epoch: Epoch close to the desired superior conjunction
        :type epoch: :py:class:`Epoch`

        :returns: The time when the superior conjunction happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1993, 10, 1.0)
        >>> conjunction = Mercury.superior_conjunction(epoch)
        >>> y, m, d = conjunction.get_date()
        >>> print(y)
        1993
        >>> print(m)
        8
        >>> print(round(d, 4))
        29.3301
        """
        ...
    @staticmethod
    def western_elongation(epoch: Epoch) -> tuple[Epoch, Angle]:
        """
        This method computes the time of the western elongation closest to
        the given epoch, as well as the corresponding maximum elongation angle.

        :param epoch: Epoch close to the desired western elongation
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the time when the western elongation happens, as
            an Epoch, and the maximum elongation angle, as an Angle
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1993, 11, 1.0)
        >>> time, elongation = Mercury.western_elongation(epoch)
        >>> y, m, d = time.get_date()
        >>> print(y)
        1993
        >>> print(m)
        11
        >>> print(round(d, 4))
        22.6386
        >>> print(round(elongation, 4))
        19.7506
        """
        ...
    @staticmethod
    def eastern_elongation(epoch: Epoch) -> tuple[Epoch, Angle]:
        """
        This method computes the time of the eastern elongation closest to
        the given epoch, as well as the corresponding maximum elongation angle.

        :param epoch: Epoch close to the desired eastern elongation
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the time when the eastern elongation happens, as
            an Epoch, and the maximum elongation angle, as an Angle
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1990, 8, 1.0)
        >>> time, elongation = Mercury.eastern_elongation(epoch)
        >>> y, m, d = time.get_date()
        >>> print(y)
        1990
        >>> print(m)
        8
        >>> print(round(d, 4))
        11.8514
        >>> print(round(elongation, 4))
        27.4201
        """
        ...
    @staticmethod
    def station_longitude_1(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the 1st station in longitude
        (i.e. when the planet is stationary and begins to move westward -
        retrograde - among the starts) closest to the given epoch.

        :param epoch: Epoch close to the desired inferior conjunction
        :type epoch: :py:class:`Epoch`

        :returns: Time when the 1st statin in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1993, 10, 1.0)
        >>> sta1 = Mercury.station_longitude_1(epoch)
        >>> y, m, d = sta1.get_date()
        >>> print(y)
        1993
        >>> print(m)
        10
        >>> print(round(d, 4))
        25.9358
        """
        ...
    @staticmethod
    def station_longitude_2(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the 2nd station in longitude
        (i.e. when the planet is stationary and begins to move eastward -
        prograde - among the starts) closest to the given epoch.

        :param epoch: Epoch close to the desired inferior conjunction
        :type epoch: :py:class:`Epoch`

        :returns: Time when the 2nd station in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1993, 10, 1.0)
        >>> sta2 = Mercury.station_longitude_2(epoch)
        >>> y, m, d = sta2.get_date()
        >>> print(y)
        1993
        >>> print(m)
        11
        >>> print(round(d, 4))
        15.0724
        """
        ...
    @staticmethod
    def perihelion_aphelion(epoch: Epoch, perihelion: bool | None = True) -> Epoch:
        """
        This method computes the time of Perihelion (or Aphelion) closer to
        a given epoch.

        :param epoch: Epoch close to the desired Perihelion (or Aphelion)
        :type epoch: :py:class:`Epoch`
        :param peihelion: If True, the epoch of the closest Perihelion is
            computed, if False, the epoch of the closest Aphelion is found.
        :type bool:

        :returns: The epoch of the desired Perihelion (or Aphelion)
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(2000, 1, 1.0)
        >>> e = Mercury.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2000
        >>> print(m)
        2
        >>> print(d)
        15
        >>> print(h)
        18
        >>> epoch = Epoch(2000, 3, 1.0)
        >>> e = Mercury.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2000
        >>> print(m)
        3
        >>> print(d)
        30
        >>> print(h)
        17
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Mercury, nearest to the given epoch.

        :param epoch: Epoch closest to the node passage
        :type epoch: :py:class:`Epoch`
        :param ascending: Whether the time of passage by the ascending (True)
            or descending (False) node will be computed
        :type ascending: bool

        :returns: Tuple containing:
            - Time of passage through the node (:py:class:`Epoch`)
            - Radius vector when passing through the node (in AU, float)
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(2019, 1, 1)
        >>> time, r = Mercury.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        2018
        >>> print(month)
        11
        >>> print(round(day, 1))
        24.7
        >>> print(round(r, 4))
        0.3143
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float, phase_angle: float | Angle) -> float:
        """
        This function computes the approximate magnitude of Mercury.

        :param sun_dist: Distance from Mercury to Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance Mercury to Earth, in Astronomical Units
        :type earth_dist: float
        :param phase_angle: Mercury phase angle
        :type phase_angle: float, :py:class:`Angle`

        :returns: Mercury's magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.
        """
        ...

def main() -> None: ...
