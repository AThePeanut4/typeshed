from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

VSOP87_L: Final[list[list[list[float]]]]
VSOP87_B: Final[list[list[list[float]]]]
VSOP87_R: Final[list[list[list[float]]]]
VSOP87_L_J2000: Final[list[list[list[float]]]]
VSOP87_B_J2000: Final[list[list[list[float]]]]
ORBITAL_ELEM: Final[list[list[float]]]
ORBITAL_ELEM_J2000: Final[list[list[float]]]

class Ellipsoid:
    """
    Class Ellipsoid is useful to encapsulate the most important parameters of
    a given reference ellipsoid.
    """
    def __init__(self, a: float, f: float, omega: float) -> None:
        """
        Ellipsoid constructor.

        :param a: Semi-major or equatorial radius, in meters
        :type a: float
        :param f: Flattening
        :type f: float
        :param omega: Angular velocity of the Earth, in rad/s
        :type omega: float
        """
        ...
    def b(self) -> float:
        """
        Method to return the semi-minor radius.

        :returns: Semi-minor radius, in meters
        :rtype: float

        >>> a = Ellipsoid(6378140.0, 0.0033528132, 7.292e-5)
        >>> round(a.b(), 3)
        6356755.288
        """
        ...
    def e(self) -> float:
        """
        Method to return the eccentricity of the Earth's meridian.

        :returns: Eccentricity of the Earth's meridian
        :rtype: float

        >>> a = Ellipsoid(6378140.0, 0.0033528132, 7.292e-5)
        >>> round(a.e(), 8)
        0.08181922
        """
        ...

IAU76: Final[Ellipsoid]
WGS84: Final[Ellipsoid]

class Earth:
    """
    Class Earth models the figure of the Earth surface and, with the help of a
    configurable reference ellipsoid, provides a set of handy method to compute
    different parameters, like the distance between two points on the surface.

    Please note that here we depart a little bit from Meeus' book because the
    Earth class uses the **World Geodetic System 1984 (WGS84)** as the default
    reference ellipsoid, instead of the International Astronomical Union 1974,
    which Meeus uses. This change is done because WGS84 is regarded as more
    modern.
    """
    def __init__(self, ellipsoid: Ellipsoid = ...) -> None:
        """
        Earth constructor.

        It takes a reference ellipsoid as input. If not provided, the ellipsoid
        used is the WGS84 by default.

        :param ellipsoid: Reference ellipsoid to be used. WGS84 by default.
        :type radians: :class:`Ellipsoid`

        :returns: Earth object.
        :rtype: :py:class:`Earth`
        :raises: TypeError if input value is of wrong type.
        """
        ...
    def set(self, ellipsoid: Ellipsoid) -> None:
        """
        Method used to define an Earth object.

        It takes a reference ellipsoid as input. If not provided, the ellipsoid
        used is the WGS84 by default.

        :param ellipsoid: Reference ellipsoid to be used. WGS84 by default.
        :type radians: :class:`Ellipsoid`

        :returns: None
        :rtype: None
        :raises: TypeError if input value is of wrong type.
        """
        ...
    def rho(self, latitude: float | Angle) -> float:
        """
        Method to compute the rho term, which is the observer distance to
        the center of the Earth, when the observer is at sea level. In this
        case, the Earth's equatorial radius is taken as unity.

        :param latitude: Geodetical or geographical latitude of the observer,
            in degrees
        :type latitude: int, float, :class:`Angle`

        :returns: Rho: Distance to the center of the Earth from sea level. It
            is a ratio with respect to Earth equatorial radius.
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> e = Earth(ellipsoid=IAU76)
        >>> round(e.rho(0.0), 1)
        1.0
        """
        ...
    def rho_sinphi(self, latitude: float | Angle, height: float) -> float:
        """
        Method to compute the rho*sin(phi') term, needed in the calculation
        of diurnal parallaxes, eclipses and occulatitions.

        :param latitude: Geodetical or geographical latitude of the observer,
            in degrees
        :type latitude: int, float, :class:`Angle`
        :param height: Height of the observer above the sea level, in meters
        :type height: int, float

        :returns: rho*sin(phi') term
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> lat = Angle(33, 21, 22.0)
        >>> e = Earth(ellipsoid=IAU76)
        >>> round(e.rho_sinphi(lat, 1706), 6)
        0.546861
        """
        ...
    def rho_cosphi(self, latitude: float | Angle, height: float) -> float:
        """
        Method to compute the rho*cos(phi') term, needed in the calculation
        of diurnal parallaxes, eclipses and occulatitions.

        :param latitude: Geodetical or geographical latitude of the observer,
            in degrees
        :type latitude: int, float, :class:`Angle`
        :param height: Height of the observer above the sea level, in meters
        :type height: int, float

        :returns: rho*cos(phi') term
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> lat = Angle(33, 21, 22.0)
        >>> e = Earth(ellipsoid=IAU76)
        >>> round(e.rho_cosphi(lat, 1706), 6)
        0.836339
        """
        ...
    def rp(self, latitude: float | Angle) -> float:
        """
        Method to compute the radius of the parallel circle at the given
        latitude.

        :param latitude: Geodetical or geographical latitude of the observer,
            in degrees
        :type latitude: int, float, :class:`Angle`

        :returns: Radius of the parallel circle at given latitude, in meters
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> e = Earth(ellipsoid=IAU76)
        >>> round(e.rp(42.0), 1)
        4747001.2
        """
        ...
    def linear_velocity(self, latitude: float | Angle) -> float:
        """
        Method to compute the linear velocity of a point at latitude, due
        to the rotation of the Earth.

        :param latitude: Geodetical or geographical latitude of the observer,
            in degrees
        :type latitude: int, float, :class:`Angle`

        :returns: Linear velocity of a point at latitude, in meters per second
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> e = Earth(ellipsoid=IAU76)
        >>> round(e.linear_velocity(42.0), 2)
        346.16
        """
        ...
    def rm(self, latitude: float | Angle) -> float:
        """
        Method to compute the radius of curvature of the Earth's meridian
        at the given latitude.

        :param latitude: Geodetical or geographical latitude of the observer,
            in degrees
        :type latitude: int, float, :class:`Angle`

        :returns: Radius of curvature of the Earth's meridian at the given
            latitude, in meters
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> e = Earth(ellipsoid=IAU76)
        >>> round(e.rm(42.0), 1)
        6364033.3
        """
        ...
    def distance(
        self, lon1: float | Angle, lat1: float | Angle, lon2: float | Angle, lat2: float | Angle
    ) -> tuple[float, float]:
        """
        This method computes the distance between two points on the Earth's
        surface using the method from H. Andoyer.

        .. note:: We will consider that positions 'East' and 'South' are
            negative.

        :param lon1: Longitude of the first point, in degrees
        :type lon1: int, float, :class:`Angle`
        :param lat1: Geodetical or geographical latitude of the first point,
            in degrees
        :type lat1: int, float, :class:`Angle`
        :param lon2: Longitude of the second point, in degrees
        :type lon2: int, float, :class:`Angle`
        :param lat2: Geodetical or geographical latitude of the second point,
            in degrees
        :type lat2: int, float, :class:`Angle`

        :returns: Tuple with distance between the two points along Earth's
            surface, and approximate error, in meters
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> e = Earth(ellipsoid=IAU76)
        >>> lon1 = Angle(-2, 20, 14.0)
        >>> lat1 = Angle(48, 50, 11.0)
        >>> lon2 = Angle(77, 3, 56.0)
        >>> lat2 = Angle(38, 55, 17.0)
        >>> dist, error = e.distance(lon1, lat1, lon2, lat2)
        >>> round(dist, 0)
        6181628.0
        >>> error
        69.0
        >>> lon1 = Angle(-2.09)
        >>> lat1 = Angle(41.3)
        >>> lon2 = Angle(73.99)
        >>> lat2 = Angle(40.75)
        >>> dist, error = e.distance(lon1, lat1, lon2, lat2)
        >>> round(dist, 0)
        6176760.0
        >>> error
        69.0
        """
        ...
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch, tofk5: bool = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of the
        Earth for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Earth position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param tofk5: Whether or not the small correction to convert to the FK5
            system will be applied or not
        :type tofk5: bool

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> l, b, r = Earth.geometric_heliocentric_position(epoch, tofk5=False)
        >>> print(round(l.to_positive(), 6))
        19.907297
        >>> print(b.dms_str(n_dec=3))
        -0.744''
        >>> print(round(r, 8))
        0.99760852
        """
        ...
    @staticmethod
    def apparent_heliocentric_position(epoch: Epoch, nutation: bool = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent heliocentric position of the
        Earth for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Earth position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param nutation: Whether the nutation correction will be applied
        :type nutation: bool

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> lon, lat, r = Earth.apparent_heliocentric_position(epoch)
        >>> print(round(lon.to_positive(), 6))
        19.905986
        >>> print(lat.dms_str(n_dec=3))
        -0.721''
        >>> print(round(r, 8))
        0.99760852
        """
        ...
    @staticmethod
    def geometric_heliocentric_position_j2000(epoch: Epoch, tofk5: bool = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric heliocentric position of the
        Earth for a given epoch, using the VSOP87 theory, referred to the
        equinox J2000.0.

        :param epoch: Epoch to compute Earth position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param tofk5: Whether or not the small correction to convert to the FK5
            system will be applied or not
        :type tofk5: bool

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
        This method computes the orbital elements of Earth for the mean
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
        >>> l, a, e, i, ome, arg = Earth.orbital_elements_mean_equinox(epoch)
        >>> print(round(l, 6))
        272.716028
        >>> print(round(a, 8))
        1.00000102
        >>> print(round(e, 7))
        0.0166811
        >>> print(round(i, 6))
        0.0
        >>> print(round(ome, 5))
        174.71534
        >>> print(round(arg, 6))
        -70.651889
        """
        ...
    @staticmethod
    def orbital_elements_j2000(epoch: Epoch) -> tuple[Angle, float, float, Angle, Angle, Angle]:
        """
        This method computes the orbital elements of Earth for the
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
        >>> l, a, e, i, ome, arg = Earth.orbital_elements_j2000(epoch)
        >>> print(round(l, 6))
        271.801199
        >>> print(round(a, 8))
        1.00000102
        >>> print(round(e, 7))
        0.0166811
        >>> print(round(i, 6))
        0.008544
        >>> print(round(ome, 5))
        174.71534
        >>> print(round(arg, 6))
        -71.566717
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

        >>> epoch = Epoch(1989, 11, 20.0)
        >>> e = Earth.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        1990
        >>> print(m)
        1
        >>> print(d)
        4
        >>> print(h)
        17
        >>> epoch = Epoch(2000, 4, 1.0)
        >>> e = Earth.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2000
        >>> print(m)
        7
        >>> print(d)
        3
        >>> print(h)
        23
        >>> print(mi)
        51
        >>> epoch = Epoch(2003, 3, 10.0)
        >>> e = Earth.perihelion_aphelion(epoch)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2003
        >>> print(m)
        1
        >>> print(d)
        4
        >>> print(h)
        5
        >>> print(mi)
        1
        >>> epoch = Epoch(2009, 5, 1.0)
        >>> e = Earth.perihelion_aphelion(epoch, perihelion=False)
        >>> y, m, d, h, mi, s = e.get_full_date()
        >>> print(y)
        2009
        >>> print(m)
        7
        >>> print(d)
        4
        >>> print(h)
        1
        >>> print(mi)
        41
        """
        ...
    @staticmethod
    def passage_nodes(epoch: Epoch, ascending: bool = True) -> tuple[Epoch, float]:
        """
        This function computes the time of passage by the nodes (ascending
        or descending) of Earth, nearest to the given epoch.

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
        >>> time, r = Earth.passage_nodes(epoch)
        >>> year, month, day = time.get_date()
        >>> print(year)
        2019
        >>> print(month)
        3
        >>> print(round(day, 1))
        15.0
        >>> print(round(r, 4))
        0.9945
        """
        ...
    @staticmethod
    def parallax_correction(
        right_ascension: Angle, declination: Angle, latitude: Angle, distance: float, hour_angle: Angle, height: float = 0.0
    ) -> tuple[Angle, Angle]:
        """
        This function computes the parallaxes in right ascension and
        declination in order to obtain the topocentric values.

        :param right_ascension: Geocentric right ascension, as an
            :py:class:`Angle` object
        :type right_ascension: :py:class:`Angle`
        :param declination: Geocentric declination, as an
            :py:class:`Angle` object
        :type declination: :py:class:`Angle`
        :param latitude: Latitude of the observation point
        :type latitude: :py:class:`Angle`
        :param distance: Distance from the celestial object to the Earth, in
            Astronomical Units
        :type distance: float
        :param hour_angle: Geocentric hour angle of the celestial object, as an
            :py:class:`Angle`
        :type hour_angle: :py:class:`Angle`
        :param heigth: Height of observation point above sea level, in meters
        :type height: float

        :returns: Tuple containing the topocentric right ascension and
            declination
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> right_ascension = Angle(22, 38, 7.25, ra=True)
        >>> declination = Angle(-15, 46, 15.9)
        >>> latitude = Angle(33, 21, 22)
        >>> distance = 0.37276
        >>> hour_angle = Angle(288.7958)
        >>> topo_ra, topo_dec = Earth.parallax_correction(right_ascension,                                                           declination,                                                           latitude, distance,                                                           hour_angle)
        >>> print(topo_ra.ra_str(n_dec=2))
        22h 38' 8.54''
        >>> print(topo_dec.dms_str(n_dec=1))
        -15d 46' 30.0''
        """
        ...
    @staticmethod
    def parallax_ecliptical(
        longitude: Angle,
        latitude: Angle,
        semidiameter: Angle,
        obs_lat: Angle,
        obliquity: Angle,
        sidereal_time: Angle,
        distance: float,
        height: float = 0.0,
    ) -> tuple[Angle, Angle, Angle]:
        """
        This function computes the topocentric coordinates of a celestial
        body (Moon or planet) directly from its geocentric values in ecliptical
        coordinates.

        :param longitude: Geocentric ecliptical longitude as an
            :py:class:`Angle`
        :type longitude: :py:class:`Angle`
        :param latitude: Geocentric ecliptical latitude as an :py:class:`Angle`
        :type latitude: :py:class:`Angle`
        :param semidiameter: Geocentric semidiameter as an :py:class:`Angle`
        :type semidiameter: :py:class:`Angle`
        :param obs_lat: Latitude of the observation point
        :type obs_lat: :py:class:`Angle`
        :param obliquity: Obliquity of the eliptic, as an :py:class:`Angle`
        :type obliquity: :py:class:`Angle`
        :param sidereal_time: Local sidereal time, as an :py:class:`Angle`
        :type sidereal_time: :py:class:`Angle`
        :param distance: Distance from the celestial object to the Earth, in
            Astronomical Units
        :type distance: float
        :param heigth: Height of observation point above sea level, in meters
        :type height: float

        :returns: Tuple containing the topocentric longitude, latitude and
            semidiameter
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> longitude = Angle(181, 46, 22.5)
        >>> latitude = Angle(2, 17, 26.2)
        >>> semidiameter = Angle(0, 16, 15.5)
        >>> obs_lat = Angle(50, 5, 7.8)
        >>> obliquity = Angle(23, 28, 0.8)
        >>> sidereal_time = Angle(209, 46, 7.9)
        >>> distance = 0.0024650163
        >>> topo_lon, topo_lat, topo_diam =                 Earth.parallax_ecliptical(longitude, latitude, semidiameter,                                           obs_lat, obliquity, sidereal_time,                                           distance)
        >>> print(topo_lon.dms_str(n_dec=1))
        181d 48' 5.0''
        >>> print(topo_lat.dms_str(n_dec=1))
        1d 29' 7.1''
        >>> print(topo_diam.dms_str(n_dec=1))
        16' 25.5''
        """
        ...

def main() -> None: ...
