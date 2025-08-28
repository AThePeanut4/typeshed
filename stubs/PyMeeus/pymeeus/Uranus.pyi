from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Uranus:
    """Class Uranus models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool | None = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Uranus for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Uranus position, as an Epoch object
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
        >>> l, b, r = Uranus.geometric_heliocentric_position(epoch)
        >>> print(round(l.to_positive(), 4))
        30.5888
        >>> print(round(b, 4))
        -0.5315
        >>> print(round(r, 5))
        19.86964
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Uranus for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Uranus position, as an Epoch object
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
        This method computes the orbital elements of Uranus for the mean
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
        >>> l, a, e, i, ome, arg = Uranus.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        235.517526
        >>> print(round(a, 8))
        19.21844604
        >>> print(round(e, 7))
        0.0463634
        >>> print(round(i, 6))
        0.77372
        >>> print(round(ome, 5))
        74.34776
        >>> print(round(arg, 6))
        99.630865
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Uranus for the
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
        >>> l, a, e, i, ome, arg = Uranus.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        234.602641
        >>> print(round(a, 8))
        19.21844604
        >>> print(round(e, 7))
        0.0463634
        >>> print(round(i, 6))
        0.772094
        >>> print(round(ome, 5))
        74.05468
        >>> print(round(arg, 6))
        99.009058
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Uranus (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Uranus.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        19h 13' 48.7''
        >>> print(dec.dms_str(n_dec=1))
        -22d 46' 13.0''
        >>> print(elon.dms_str(n_dec=1))
        18d 44' 18.7''
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
        >>> conj = Uranus.conjunction(epoch)
        >>> y, m, d = conj.get_date()
        >>> print(y)
        1994
        >>> print(m)
        1
        >>> print(round(d, 4))
        12.7365
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

        >>> epoch = Epoch(1780, 12, 1.0)
        >>> oppo = Uranus.opposition(epoch)
        >>> y, m, d = oppo.get_date()
        >>> print(y)
        1780
        >>> print(m)
        12
        >>> print(round(d, 4))
        17.5998
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

        .. note:: The solution provided by this method may have several days of
            error.

        >>> epoch = Epoch(1880, 1, 1.0)
        >>> e = Uranus.perihelion_aphelion(epoch)
        >>> y, m, d = e.get_date()
        >>> print(y)
        1882
        >>> print(m)
        3
        >>> print(int(d))
        18
        >>> epoch = Epoch(2090, 1, 1.0)
        >>> e = Uranus.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d = e.get_date()
        >>> print(y)
        2092
        >>> print(m)
        11
        >>> print(int(d))
        22
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Uranus, nearest to the given epoch.

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
        >>> time, r = Uranus.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        2028
        >>> print(month)
        8
        >>> print(round(day, 1))
        23.2
        >>> print(round(r, 4))
        19.3201
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float) -> float:
        """
        This function computes the approximate magnitude of Uranus.

        :param sun_dist: Distance from Uranus to Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance from Uranus to Earth, in Astronomical Units
        :type earth_dist: float

        :returns: Uranus's magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.
        """
        ...

def main() -> None: ...
