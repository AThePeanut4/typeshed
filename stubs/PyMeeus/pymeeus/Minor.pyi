from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

class Minor:
    """Class Minor models minor celestial bodies."""
    def __init__(self, q: float, e: float, i: Angle, omega: Angle, w: Angle, t: Epoch) -> None:
        """
        Minor constructor.

        The Minor object is initialized with this constructor, setting the
        orbital values and computing some internal parameters. This constructor
        is build upon the 'set()' method.

        :param q: Perihelion distance, in Astronomical Units
        :type q: float
        :param e: Eccentricity of the orbit
        :type e: float
        :param i: Inclination of the orbit, as an Angle object
        :type i: :py:class:`Angle`
        :param omega: Longitude of the ascending node, as an Angle object
        :type omega: :py:class:`Angle`
        :param w: Argument of the perihelion, as an Angle object
        :type w: :py:class:`Angle`
        :param t: Epoch of passage by perihelion, as an Epoch object
        :type t: :py:class:`Epoch`

        :raises: TypeError if input value is of wrong type.
        """
        ...
    def set(self, q: float, e: float, i: Angle, omega: Angle, w: Angle, t: Epoch) -> None:
        """
        Method used to set the orbital values and set some internal
        parameters.

        :param q: Perihelion distance, in Astronomical Units
        :type q: float
        :param e: Eccentricity of the orbit
        :type e: float
        :param i: Inclination of the orbit, as an Angle object
        :type i: :py:class:`Angle`
        :param omega: Longitude of the ascending node, as an Angle object
        :type omega: :py:class:`Angle`
        :param w: Argument of the perihelion, as an Angle object
        :type w: :py:class:`Angle`
        :param t: Epoch of passage by perihelion, as an Epoch object
        :type t: :py:class:`Epoch`

        :raises: TypeError if input value is of wrong type.
        """
        ...
    def geocentric_position(self, epoch: Epoch) -> tuple[Angle, Angle, Angle]:
        """
        This method computes the geocentric position of a minor celestial
        body (right ascension and declination) for the given epoch, and
        referred to the standard equinox J2000.0. Additionally, it also
        computes the elongation angle to the Sun.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing the right ascension, the declination and
            the elongation angle to the Sun, as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> a = 2.2091404
        >>> e = 0.8502196
        >>> q = a * (1.0 - e)
        >>> i = Angle(11.94524)
        >>> omega = Angle(334.75006)
        >>> w = Angle(186.23352)
        >>> t = Epoch(1990, 10, 28.54502)
        >>> minor = Minor(q, e, i, omega, w, t)
        >>> epoch = Epoch(1990, 10, 6.0)
        >>> ra, dec, p = minor.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        10h 34' 13.7''
        >>> print(dec.dms_str(n_dec=0))
        19d 9' 32.0''
        >>> print(round(p, 2))
        40.51
        >>> t = Epoch(1998, 4, 14.4358)
        >>> q = 1.487469
        >>> e = 1.0
        >>> i = Angle(0.0)
        >>> omega = Angle(0.0)
        >>> w = Angle(0.0)
        >>> minor = Minor(q, e, i, omega, w, t)
        >>> epoch = Epoch(1998, 8, 5.0)
        >>> ra, dec, p = minor.geocentric_position(epoch)
        >>> print(ra.ra_str(n_dec=1))
        5h 45' 34.5''
        >>> print(dec.dms_str(n_dec=0))
        23d 23' 53.0''
        >>> print(round(p, 2))
        45.73
        """
        ...
    def heliocentric_ecliptical_position(self, epoch: Epoch) -> tuple[Angle, Angle]:
        """
        This method computes the heliocentric position of a minor celestial
        body, providing the result in ecliptical coordinates.

        :param epoch: Epoch to compute geocentric position, as an Epoch object
        :type epoch: :py:class:`Epoch`

        :returns: A tuple containing longitude and latitude, as Angle objects
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> a = 2.2091404
        >>> e = 0.8502196
        >>> q = a * (1.0 - e)
        >>> i = Angle(11.94524)
        >>> omega = Angle(334.75006)
        >>> w = Angle(186.23352)
        >>> t = Epoch(1990, 10, 28.54502)
        >>> epoch = Epoch(1990, 10, 6.0)
        >>> minor = Minor(q, e, i, omega, w, t)
        >>> lon, lat = minor.heliocentric_ecliptical_position(epoch)
        >>> print(lon.dms_str(n_dec=1))
        66d 51' 57.8''
        >>> print(lat.dms_str(n_dec=1))
        11d 56' 14.4''
        """
        ...

def main() -> None: ...
