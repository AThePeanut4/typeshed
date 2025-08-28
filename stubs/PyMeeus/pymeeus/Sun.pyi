from typing import Literal

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

class Sun:
    """Class Sun handles the parameters related to the Sun."""
    def __init__(self) -> None:
        """
        Sun constructor.

        :returns: Sun object.
        :rtype: :py:class:`Sun`
        """
        ...
    @staticmethod
    def true_longitude_coarse(epoch: Epoch) -> tuple[Angle, float]:
        """
        This method provides the Sun's true longitude with a relatively low
        accuracy of about 0.01 degree.

        :param epoch: Epoch to compute the position of the Sun
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the true (ecliptical) longitude (as an
            Angle object) and the radius vector in astronomical units.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 10, 13)
        >>> true_lon, r = Sun.true_longitude_coarse(epoch)
        >>> print(true_lon.dms_str(n_dec=0))
        199d 54' 36.0''
        >>> print(round(r, 5))
        0.99766
        """
        ...
    @staticmethod
    def apparent_longitude_coarse(epoch: Epoch) -> tuple[Angle, float]:
        """
        This method provides the Sun's apparent longitude with a relatively
        low accuracy of about 0.01 degree.

        :param epoch: Epoch to compute the position of the Sun
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the sun_apparent (ecliptical) longitude
            (as an Angle object) and the radius vector in astronomical units.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 10, 13)
        >>> app_lon, r = Sun.apparent_longitude_coarse(epoch)
        >>> print(app_lon.dms_str(n_dec=0))
        199d 54' 32.0''
        >>> print(round(r, 5))
        0.99766
        """
        ...
    @staticmethod
    def apparent_rightascension_declination_coarse(epoch: Epoch) -> tuple[Angle, Angle, float]:
        """
        This method provides the Sun's apparent right ascension and
        declination with a relatively low accuracy of about 0.01 degree.

        :param epoch: Epoch to compute the position of the Sun
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension and the declination
            (as Angle objects) and the radius vector in astronomical units.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epo = Epoch(1992, 10, 13)
        >>> ra, delta, r = Sun.apparent_rightascension_declination_coarse(epo)
        >>> print(ra.ra_str(n_dec=1))
        13h 13' 31.4''
        >>> print(delta.dms_str(n_dec=0))
        -7d 47' 6.0''
        >>> print(round(r, 5))
        0.99766
        """
        ...
    @staticmethod
    def geometric_geocentric_position(epoch: Epoch, tofk5: bool = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the geometric geocentric position of the Sun
        for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Sun position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param tofk5: Whether or not the small correction to convert to the FK5
            system will be applied or not
        :type tofk5: bool

        :returns: A tuple with the geocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> l, b, r = Sun.geometric_geocentric_position(epoch, tofk5=False)
        >>> print(round(l.to_positive(), 6))
        199.907297
        >>> print(b.dms_str(n_dec=3))
        0.744''
        >>> print(round(r, 8))
        0.99760852
        """
        ...
    @staticmethod
    def apparent_geocentric_position(epoch: Epoch, nutation: bool = True) -> tuple[Angle, Angle, float]:
        """
        This method computes the apparent geocentric position of the Sun
        for a given epoch, using the VSOP87 theory.

        :param epoch: Epoch to compute Sun position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param nutation: Whether the nutation correction will be applied
        :type epoch: bool

        :returns: A tuple with the heliocentric longitude and latitude (as
            :py:class:`Angle` objects), and the radius vector (as a float,
            in astronomical units), in that order
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> lon, lat, r = Sun.apparent_geocentric_position(epoch)
        >>> print(lon.to_positive().dms_str(n_dec=3))
        199d 54' 21.548''
        >>> print(lat.dms_str(n_dec=3))
        0.721''
        >>> print(round(r, 8))
        0.99760852
        """
        ...
    @staticmethod
    def rectangular_coordinates_mean_equinox(epoch: Epoch) -> tuple[float, float, float]:
        """
        This method computes the rectangular geocentric equatorial
        coordinates (X, Y, Z) of the Sun, referred to the mean equinox of the
        date. The X axis is directed towards the vernal equinox (longitude 0),
        the Y axis lies in the plane of the equator and is directed towards
        longitude 90, and the Z axis is directed towards the north celestial
        pole.

        :param epoch: Epoch to compute Sun position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the X, Y, Z values in astronomical units
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> x, y, z = Sun.rectangular_coordinates_mean_equinox(epoch)
        >>> print(round(x, 7))
        -0.9379963
        >>> print(round(y, 6))
        -0.311654
        >>> print(round(z, 7))
        -0.1351207
        """
        ...
    @staticmethod
    def rectangular_coordinates_j2000(epoch: Epoch) -> tuple[float, float, float]:
        """
        This method computes the rectangular geocentric equatorial
        coordinates (X, Y, Z) of the Sun, referred to the standard equinox of
        J2000.0. The X axis is directed towards the vernal equinox (longitude
        0), the Y axis lies in the plane of the equator and is directed towards
        longitude 90, and the Z axis is directed towards the north celestial
        pole.

        :param epoch: Epoch to compute Sun position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the X, Y, Z values in astronomical units
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> x, y, z = Sun.rectangular_coordinates_j2000(epoch)
        >>> print(round(x, 8))
        -0.93740485
        >>> print(round(y, 8))
        -0.3131474
        >>> print(round(z, 8))
        -0.13577045
        """
        ...
    @staticmethod
    def rectangular_coordinates_b1950(epoch: Epoch) -> tuple[float, float, float]:
        """
        This method computes the rectangular geocentric equatorial
        coordinates (X, Y, Z) of the Sun, referred to the mean equinox of
        B1950.0. The X axis is directed towards the vernal equinox (longitude
        0), the Y axis lies in the plane of the equator and is directed towards
        longitude 90, and the Z axis is directed towards the north celestial
        pole.

        :param epoch: Epoch to compute Sun position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple with the X, Y, Z values in astronomical units
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> x, y, z = Sun.rectangular_coordinates_b1950(epoch)
        >>> print(round(x, 8))
        -0.94149557
        >>> print(round(y, 8))
        -0.30259922
        >>> print(round(z, 8))
        -0.11578695
        """
        ...
    @staticmethod
    def rectangular_coordinates_equinox(epoch: Epoch, equinox_epoch: Epoch) -> tuple[float, float, float]:
        """
        This method computes the rectangular geocentric equatorial
        coordinates (X, Y, Z) of the Sun, referred to an arbitrary mean
        equinox. The X axis is directed towards the vernal equinox (longitude
        0), the Y axis lies in the plane of the equator and is directed towards
        longitude 90, and the Z axis is directed towards the north celestial
        pole.

        :param epoch: Epoch to compute Sun position, as an Epoch object
        :type epoch: :py:class:`Epoch`
        :param equinox_epoch: Epoch corresponding to the mean equinox
        :type equinox_epoch: :py:class:`Epoch`

        :returns: A tuple with the X, Y, Z values in astronomical units
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> e_equinox = Epoch(2467616.0)
        >>> x, y, z = Sun.rectangular_coordinates_equinox(epoch, e_equinox)
        >>> print(round(x, 8))
        -0.93368986
        >>> print(round(y, 8))
        -0.32235085
        >>> print(round(z, 8))
        -0.13977098
        """
        ...
    @staticmethod
    def get_equinox_solstice(year: int, target: Literal["spring", "summer", "autumn", "winter"] = "spring") -> Epoch:
        """
        This method computes the times of the equinoxes or the solstices.

        :param year: Year we want to compute the equinox or solstice for
        :type year: int
        :param target: Corresponding equinox or solstice. It can be "spring",
            "summer", "autumn", "winter"
        :type target: str

        :returns: The instant of time when the equinox or solstice happens
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input values are of wrong type.
        :raises: ValueError if 'target' value is invalid.

        >>> epoch = Sun.get_equinox_solstice(1962, target="summer")
        >>> y, m, d, h, mi, s = epoch.get_full_date()
        >>> print("{}/{}/{} {}:{}:{}".format(y, m, d, h, mi, round(s, 0)))
        1962/6/21 21:24:42.0
        """
        ...
    @staticmethod
    def equation_of_time(epoch: Epoch) -> tuple[int, float]:
        """
        This method computes the equation of time for a given epoch,
        understood as the difference between apparent and mean time, or the
        difference between the hour angle of the true Sun and the mean Sun.

        :param epoch: Epoch to compute the equation of time, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: Difference between apparent and mean time, as a tuple, in
            minutes (int) and seconds (float) of time
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.

        >>> epoch = Epoch(1992, 10, 13.0)
        >>> m, s = Sun.equation_of_time(epoch)
        >>> print(m)
        13
        >>> print(round(s, 1))
        42.6
        """
        ...
    @staticmethod
    def ephemeris_physical_observations(epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method uses Carrington's formulas to compute the following
        quantities:

        - P  : position angle of the northern extremity of the axis of rotation
        - B0 : heliographic latitude of the center of the solar disk
        - L0 : heliographic longitude of the center of the solar disk

        :param epoch: Epoch to compute the parameters
        :type epoch: :py:class:`Epoch`

        :returns: Parameters P, B0 and L0, in a tuple
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 10, 13)
        >>> p, b0, l0 = Sun.ephemeris_physical_observations(epoch)
        >>> print(round(p, 2))
        26.27
        >>> print(round(b0, 2))
        5.99
        >>> print(round(l0, 2))
        238.63
        """
        ...
    @staticmethod
    def beginning_synodic_rotation(number: int) -> Epoch:
        """
        This method calculates the epoch when the Carrington's synodic
        rotation No. 'number' starts.

        :param number: Number of Carrington's synodic rotation
        :type number: int

        :returns: Epoch when the provided rotation starts
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Sun.beginning_synodic_rotation(1699)
        >>> print(round(epoch(), 3))
        2444480.723
        """
        ...

def main() -> None: ...
