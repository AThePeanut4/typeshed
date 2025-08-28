from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Jupiter:
    """Class Jupiter models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool | None = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Jupiter for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Jupiter position, as an Epoch object
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
        >>> l, b, r = Jupiter.geometric_heliocentric_position(epoch)
        >>> print(round(l.to_positive(), 4))
        241.5873
        >>> print(round(b, 4))
        0.8216
        >>> print(round(r, 5))
        5.36848
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Jupiter for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Jupiter position, as an Epoch object
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
        This method computes the orbital elements of Jupiter for the mean
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
        >>> l, a, e, i, ome, arg = Jupiter.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        222.433723
        >>> print(round(a, 8))
        5.20260333
        >>> print(round(e, 7))
        0.0486046
        >>> print(round(i, 6))
        1.29967
        >>> print(round(ome, 5))
        101.13309
        >>> print(round(arg, 6))
        -85.745532
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Jupiter for the
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
        >>> l, a, e, i, ome, arg = Jupiter.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        221.518802
        >>> print(round(a, 8))
        5.20260333
        >>> print(round(e, 7))
        0.0486046
        >>> print(round(i, 6))
        1.30198
        >>> print(round(ome, 5))
        100.58051
        >>> print(round(arg, 6))
        -86.107875
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Jupiter (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Jupiter.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        12h 47' 9.6''
        >>> print(dec.dms_str(n_dec=1))
        -3d 41' 55.3''
        >>> print(elon.dms_str(n_dec=1))
        76d 2' 26.0''
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
        >>> conj = Jupiter.conjunction(epoch)
        >>> y, m, d = conj.get_date()
        >>> print(y)
        1993
        >>> print(m)
        10
        >>> print(round(d, 4))
        18.3341
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

        >>> epoch = Epoch(-6, 9, 1.0)
        >>> oppo = Jupiter.opposition(epoch)
        >>> y, m, d = oppo.get_date()
        >>> print(y)
        -6
        >>> print(m)
        9
        >>> print(round(d, 4))
        15.2865
        """
        ...
    @staticmethod
    def station_longitude_1(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the 1st station in longitude
        (i.e. when the planet is stationary and begins to move westward -
        retrograde - among the starts) closest to the given epoch.

        :param epoch: Epoch close to the desired opposition
        :type epoch: :py:class:`Epoch`

        :returns: Time when the 1st station in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(2018, 11, 1.0)
        >>> sta1 = Jupiter.station_longitude_1(epoch)
        >>> y, m, d = sta1.get_date()
        >>> print(y)
        2018
        >>> print(m)
        3
        >>> print(round(d, 4))
        9.1288
        """
        ...
    @staticmethod
    def station_longitude_2(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the 2nd station in longitude
        (i.e. when the planet is stationary and begins to move eastward -
        prograde - among the starts) closest to the given epoch.

        :param epoch: Epoch close to the desired opposition
        :type epoch: :py:class:`Epoch`

        :returns: Time when the 1st station in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(2018, 11, 1.0)
        >>> sta2 = Jupiter.station_longitude_2(epoch)
        >>> y, m, d = sta2.get_date()
        >>> print(y)
        2018
        >>> print(m)
        7
        >>> print(round(d, 4))
        10.6679
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

        >>> epoch = Epoch(2019, 2, 23.0)
        >>> e = Jupiter.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2023
        >>> print(m)
        1
        >>> print(d)
        20
        >>> print(h)
        11
        >>> epoch = Epoch(1981, 6, 1.0)
        >>> e = Jupiter.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        1981
        >>> print(m)
        7
        >>> print(d)
        28
        >>> print(h)
        6
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Jupiter, nearest to the given epoch.

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
        >>> time, r = Jupiter.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        2025
        >>> print(month)
        9
        >>> print(round(day, 1))
        15.6
        >>> print(round(r, 4))
        5.1729
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float) -> float:
        """
        This function computes the approximate magnitude of Jupiter.

        :param sun_dist: Distance from Jupiter to Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance Jupiter to Earth, in Astronomical Units
        :type earth_dist: float

        :returns: Jupiter's magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.
        """
        ...

def main() -> None: ...
