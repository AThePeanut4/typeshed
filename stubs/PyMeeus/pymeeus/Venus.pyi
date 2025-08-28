from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Venus:
    """Class Venus models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool | None = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Venus for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Venus position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param tofk5: Whether or not the small correction to convert to the FK5
            system will be applied or not
        :type tofk5: bool

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> l, b, r = Venus.geometric_heliocentric_position(epoch, tofk5=False)
        >>> print(round(l, 5))
        26.11412
        >>> print(round(b, 4))
        -2.6206
        >>> print(round(r, 6))
        0.724602
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Venus for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Venus position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.
        """
        ...
    @staticmethod
    def orbital_elements_mean_equinox(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Venus for the mean
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
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(2065, 6, 24.0)
        >>> l, a, e, i, ome, arg = Venus.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        338.646306
        >>> print(round(a, 8))
        0.72332982
        >>> print(round(e, 7))
        0.0067407
        >>> print(round(i, 6))
        3.395319
        >>> print(round(ome, 5))
        77.27012
        >>> print(round(arg, 6))
        55.211257
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Venus for the standard
        equinox J2000.0 for a given epoch.

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
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(2065, 6, 24.0)
        >>> l, a, e, i, ome, arg = Venus.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        337.731227
        >>> print(round(a, 8))
        0.72332982
        >>> print(round(e, 7))
        0.0067407
        >>> print(round(i, 6))
        3.394087
        >>> print(round(ome, 5))
        76.49782
        >>> print(round(arg, 6))
        55.068476
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Venus (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Venus.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        21h 4' 41.5''
        >>> print(dec.dms_str(n_dec=1))
        -18d 53' 16.8''
        >>> print(elon.dms_str(n_dec=1))
        44d 46' 8.9''
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

        >>> epoch = Epoch(1882, 12, 1.0)
        >>> conjunction = Venus.inferior_conjunction(epoch)
        >>> y, m, d = conjunction.get_date()
        >>> print(y)
        1882
        >>> print(m)
        12
        >>> print(round(d, 1))
        6.7
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
        >>> conjunction = Venus.superior_conjunction(epoch)
        >>> y, m, d = conjunction.get_date()
        >>> print(y)
        1994
        >>> print(m)
        1
        >>> print(round(d, 2))
        17.05
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

        >>> epoch = Epoch(2019, 1, 1.0)
        >>> time, elongation = Venus.western_elongation(epoch)
        >>> y, m, d = time.get_date()
        >>> print(y)
        2019
        >>> print(m)
        1
        >>> print(round(d, 4))
        6.1895
        >>> print(round(elongation, 4))
        46.9571
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

        >>> epoch = Epoch(2019, 10, 1.0)
        >>> time, elongation = Venus.eastern_elongation(epoch)
        >>> y, m, d = time.get_date()
        >>> print(y)
        2020
        >>> print(m)
        3
        >>> print(round(d, 4))
        24.9179
        >>> print(round(elongation, 4))
        46.078
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

        :returns: Time when the 1st station in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(2018, 12, 1.0)
        >>> sta1 = Venus.station_longitude_1(epoch)
        >>> y, m, d = sta1.get_date()
        >>> print(y)
        2018
        >>> print(m)
        10
        >>> print(round(d, 4))
        5.7908
        """
        ...
    @staticmethod
    def station_longitude_2(epoch: Epoch) -> Epoch:
        """
        This method computes the time of the 1st station in longitude
        (i.e. when the planet is stationary and begins to move eastward -
        prograde - among the starts) closest to the given epoch.

        :param epoch: Epoch close to the desired inferior conjunction
        :type epoch: :py:class:`Epoch`

        :returns: Time when the 2nd station in longitude happens, as an Epoch
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.
        :raises: ValueError if input epoch outside the -2000/4000 range.

        >>> epoch = Epoch(2018, 12, 1.0)
        >>> sta2 = Venus.station_longitude_2(epoch)
        >>> y, m, d = sta2.get_date()
        >>> print(y)
        2018
        >>> print(m)
        11
        >>> print(round(d, 4))
        16.439
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

        >>> epoch = Epoch(1978, 10, 15.0)
        >>> e = Venus.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        1978
        >>> print(m)
        12
        >>> print(d)
        31
        >>> print(h)
        4
        >>> epoch = Epoch(1979, 2, 1.0)
        >>> e = Venus.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        1979
        >>> print(m)
        4
        >>> print(d)
        22
        >>> print(h)
        12
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Venus, nearest to the given epoch.

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

        >>> epoch = Epoch(1979, 1, 1)
        >>> time, r = Venus.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        1978
        >>> print(month)
        11
        >>> print(round(day, 1))
        27.4
        >>> print(round(r, 4))
        0.7205
        """
        ...
    @staticmethod
    def illuminated_fraction(epoch: Epoch) -> float:
        """
        This function computes an approximation of the illuminated fraction
        of Venus disk, as seen from Earth.

        :param epoch: Epoch to compute the illuminated fraction
        :type epoch: :py:class:`Epoch`

        :returns: Illuminated fraction of Venus disk
        :rtype: float
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 12, 20)
        >>> k = Venus.illuminated_fraction(epoch)
        >>> print(round(k, 2))
        0.64
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float, phase_angle: float | Angle) -> float:
        """
        This function computes the approximate magnitude of Venus.

        :param sun_dist: Distance from Venus to the Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance from Venus to Earth, in Astronomical Units
        :type earth_dist: float
        :param phase_angle: Venus phase angle
        :type phase_angle: float, :py:class:`Angle`

        :returns: Venus' magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.

        >>> sun_dist = 0.724604
        >>> earth_dist = 0.910947
        >>> phase_angle = Angle(72.96)
        >>> m = Venus.magnitude(sun_dist, earth_dist, phase_angle)
        >>> print(m)
        -3.8
        """
        ...

def main() -> None: ...
