from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Mars:
    """Class Mars models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool | None = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Mars for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Mars position, as an Epoch object
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
        >>> l, b, r = Mars.geometric_heliocentric_position(epoch)
        >>> print(round(l.to_positive(), 4))
        2.0015
        >>> print(round(b, 4))
        -1.3683
        >>> print(round(r, 5))
        1.39306
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Mars for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Mars position, as an Epoch object
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
        This method computes the orbital elements of Mars for the mean
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
        >>> l, a, e, i, ome, arg = Mars.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        288.855211
        >>> print(round(a, 8))
        1.52367934
        >>> print(round(e, 7))
        0.0934599
        >>> print(round(i, 6))
        1.849338
        >>> print(round(ome, 5))
        50.06365
        >>> print(round(arg, 6))
        287.202108
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Mars for the
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
        >>> l, a, e, i, ome, arg = Mars.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        287.94027
        >>> print(round(a, 8))
        1.52367934
        >>> print(round(e, 7))
        0.0934599
        >>> print(round(i, 6))
        1.844381
        >>> print(round(ome, 5))
        49.36464
        >>> print(round(arg, 6))
        286.98617
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Mars (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Mars.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        7h 48' 35.4''
        >>> print(dec.dms_str(n_dec=1))
        24d 35' 33.9''
        >>> print(elon.dms_str(n_dec=1))
        153d 35' 1.6''
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
        >>> conj = Mars.conjunction(epoch)
        >>> y, m, d = conj.get_date()
        >>> print(y)
        1993
        >>> print(m)
        12
        >>> print(round(d, 4))
        27.0898
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

        >>> epoch = Epoch(2729, 10, 1.0)
        >>> oppo = Mars.opposition(epoch)
        >>> y, m, d = oppo.get_date()
        >>> print(y)
        2729
        >>> print(m)
        9
        >>> print(round(d, 4))
        9.1412
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

        >>> epoch = Epoch(1997, 3, 1.0)
        >>> sta1 = Mars.station_longitude_1(epoch)
        >>> y, m, d = sta1.get_date()
        >>> print(y)
        1997
        >>> print(m)
        2
        >>> print(round(d, 4))
        6.033
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

        :returns: Time when the 2nd station in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(1997, 3, 1.0)
        >>> sta2 = Mars.station_longitude_2(epoch)
        >>> y, m, d = sta2.get_date()
        >>> print(y)
        1997
        >>> print(m)
        4
        >>> print(round(d, 4))
        27.7553
        """
        ...
    @staticmethod
    def perihelion_aphelion(epoch: Epoch, perihelion: bool = True) -> Epoch:
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
        >>> e = Mars.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2018
        >>> print(m)
        9
        >>> print(d)
        16
        >>> print(h)
        12
        >>> epoch = Epoch(2032, 1, 1.0)
        >>> e = Mars.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2032
        >>> print(m)
        10
        >>> print(d)
        24
        >>> print(h)
        22
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Mars, nearest to the given epoch.

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
        >>> time, r = Mars.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        2019
        >>> print(month)
        1
        >>> print(round(day, 1))
        15.2
        >>> print(round(r, 4))
        1.4709
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float, phase_angle: float | Angle) -> float:
        """
        This function computes the approximate magnitude of Mars.

        :param sun_dist: Distance from Mars to the Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance from Mars to Earth, in Astronomical Units
        :type earth_dist: float
        :param phase_angle: Mars phase angle
        :type phase_angle: float, :py:class:`Angle`

        :returns: Mars' magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.
        """
        ...

def main() -> None: ...
