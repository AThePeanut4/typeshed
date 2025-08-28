from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Saturn:
    """Class Saturn models that planet."""
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of planet
        Saturn for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Saturn position, as an Epoch object
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
        >>> l, b, r = Saturn.geometric_heliocentric_position(epoch)
        >>> print(round(l.to_positive(), 4))
        279.5108
        >>> print(round(b, 4))
        0.6141
        >>> print(round(r, 5))
        10.06266
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of planet
        Saturn for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Saturn position, as an Epoch object
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
        This method computes the orbital elements of Saturn for the mean
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
        >>> l, a, e, i, ome, arg = Saturn.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        131.196871
        >>> print(round(a, 8))
        9.55490779
        >>> print(round(e, 7))
        0.0553209
        >>> print(round(i, 6))
        2.486426
        >>> print(round(ome, 5))
        114.23974
        >>> print(round(arg, 6))
        -19.896331
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Saturn for the
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
        >>> l, a, e, i, ome, arg = Saturn.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        130.28188
        >>> print(round(a, 8))
        9.55490779
        >>> print(round(e, 7))
        0.0553209
        >>> print(round(i, 6))
        2.490529
        >>> print(round(ome, 5))
        113.49736
        >>> print(round(arg, 6))
        -20.068943
        """
        ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of Saturn (right
        ascension and declination) for the given epoch, as well as the
        elongation angle.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 20.0)
        >>> ra, dec, elon = Saturn.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        21h 11' 41.8''
        >>> print(dec.dms_str(n_dec=1))
        -17d 15' 40.8''
        >>> print(elon.dms_str(n_dec=1))
        46d 51' 47.7''
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

        >>> epoch = Epoch(2125, 6, 1.0)
        >>> conj = Saturn.conjunction(epoch)
        >>> y, m, d = conj.get_date()
        >>> print(y)
        2125
        >>> print(m)
        8
        >>> print(round(d, 4))
        26.4035
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
        >>> oppo = Saturn.opposition(epoch)
        >>> y, m, d = oppo.get_date()
        >>> print(y)
        -6
        >>> print(m)
        9
        >>> print(round(d, 4))
        14.3709
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
        >>> sta1 = Saturn.station_longitude_1(epoch)
        >>> y, m, d = sta1.get_date()
        >>> print(y)
        2018
        >>> print(m)
        4
        >>> print(round(d, 4))
        17.9433
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

        >>> epoch = Epoch(2018, 11, 1.0)
        >>> sta2 = Saturn.station_longitude_2(epoch)
        >>> y, m, d = sta2.get_date()
        >>> print(y)
        2018
        >>> print(m)
        9
        >>> print(round(d, 4))
        6.4175
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

        >>> epoch = Epoch(1944, 1, 1.0)
        >>> e = Saturn.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        1944
        >>> print(m)
        9
        >>> print(d)
        8
        >>> print(h)
        1
        >>> epoch = Epoch(2047, 1, 1.0)
        >>> e = Saturn.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2047
        >>> print(m)
        7
        >>> print(d)
        15
        >>> print(h)
        0
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Saturn, nearest to the given epoch.

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
        >>> time, r = Saturn.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        2034
        >>> print(month)
        5
        >>> print(round(day, 1))
        30.2
        >>> print(round(r, 4))
        9.0546
        """
        ...
    @staticmethod
    def magnitude(sun_dist: float, earth_dist: float, delta_U: float | Angle, B: float | Angle) -> float:
        """
        This function computes the approximate magnitude of Saturn.

        :param sun_dist: Distance from Saturn to the Sun, in Astronomical Units
        :type sun_dist: float
        :param earth_dist: Distance from Saturn to Earth, in Astronomical Units
        :type earth_dist: float
        :param delta_U: Difference between the Saturnicentric longitudes of the
            Sun and the Earth, measured in the plane of the ring, in degrees
        :type delta_U: float, :py:class:`Angle`
        :param B: Saturnicentric latitude of the Earth refered to the plane of
            the ring, positive towards the north, in degrees
        :type B: float, :py:class:`Angle`

        :returns: Saturn's magnitude
        :rtype: float
        :raises: TypeError if input values are of wrong type.

        .. note::
            In order to obtain ``delta_U`` and ``B``, please see method
            ``ring_parameters()``.

        >>> sun_dist = 9.867882
        >>> earth_dist = 10.464606
        >>> delta_U = Angle(16.442)
        >>> B = Angle(4.198)
        >>> m = Saturn.magnitude(sun_dist, earth_dist, delta_U, B)
        >>> print(m)
        1.9
        """
        ...
    @staticmethod
    def ring_inclination(epoch: Epoch) -> Angle:
        """
        This function computes the inclination of the plane of Saturn's
        ring, referred to the ecliptic and mean equinox of the date.

        :param epoch: Epoch to compute the ring inclination
        :type epoch: :py:class:`Epoch`

        :returns: Inclination of the ring referred to the ecliptic and mean
            equinox of the date
        :rtype: :py:class:`Angle`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 16.00068)
        >>> i = Saturn.ring_inclination(epoch)
        >>> print(round(i, 6))
        28.076131
        """
        ...
    @staticmethod
    def ring_logitude_ascending_node(epoch: Epoch) -> Angle:
        """
        This function computes the longitude of the ascending node of the
        plane of Saturn's ring, referred to the ecliptic and mean equinox of
        the date.

        :param epoch: Epoch to compute the ring longitude of ascending node
        :type epoch: :py:class:`Epoch`

        :returns: Longitude of the ascending node of the ring, referred to the
            ecliptic and mean equinox of the date
        :rtype: :py:class:`Angle`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 12, 16.00068)
        >>> omega = Saturn.ring_logitude_ascending_node(epoch)
        >>> print(round(omega, 6))
        169.410243
        """
        ...
    @staticmethod
    def ring_parameters(epoch: Epoch) -> tuple[Angle, Angle, Angle, Angle, float, float]:
        """
        This function computes the parameters related to Saturn's ring, like
        geocentric position angle of the semiminor axis, the size of the major
        and minor axes of the outer edge, etc.

        :param epoch: Epoch closest to the node passage
        :type epoch: :py:class:`Epoch`

        :returns: Tuple containing:

            * Saturnicentic latitude of the Earth referred to the plane
              of the ring (B), positive towards the north (:py:class:`Angle`).
            * Saturnicentric latitude of the Sun referred to the plane
              of the ring (B'), positive towards the north (:py:class:`Angle`).
            * Geocentric position angle of the northern semiminor axis
              of the apparent ellipse of the ring (P), measured from the north
              towards the east. This is also the position angle of the north
              pole of rotation of the planet (:py:class:`Angle`).
            * Difference between the Saturnicentric longitudes of the Sun and
              the Earth (delta_U), measured in the plane of the ring
              (:py:class:`Angle`).
            * The size of major axis of the outer edge of the outer
              ring ('a'), in arcseconds (float).
            * The size of minor axis of the outer edge of the outer
              ring ('b'), in arcseconds (float).

        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        .. note:: Factors by which the axes 'a' and 'b' of the outer edge of
            the outer ring are to be multiplied to obtain the axes of:

            * Inner edge of outer ring: 0.8801
            * Outer edge of inner ring: 0.8599
            * Inner edge of inner ring: 0.6650
            * Inner edge of dusky ring: 0.5486

        >>> epoch = Epoch(1992, 12, 16.00068)
        >>> B, Bprime, P, delta_U, a, b = Saturn.ring_parameters(epoch)
        >>> print(round(B, 3))
        16.442
        >>> print(round(Bprime, 3))
        14.679
        >>> print(round(P, 3))
        6.741
        >>> print(round(delta_U, 3))
        4.198
        >>> print(round(a, 2))
        35.87
        >>> print(round(b, 2))
        10.15
        """
        ...

def main() -> None: ...
