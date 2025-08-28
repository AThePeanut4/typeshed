from typing import Final, Literal

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

PERIODIC_TERMS_LR_TABLE: Final[list[list[float]]]
PERIODIC_TERMS_B_TABLE: Final[list[list[float]]]

class Moon:
    """Class Moon models Earth's satellite."""
    @staticmethod
    def geocentric_ecliptical_pos(epoch: Epoch) -> tuple[Angle, Angle, float, Angle]:
        """
        This method computes the geocentric ecliptical position (longitude,
        latitude) of the Moon for a given instant, referred to the mean equinox
        of the date, as well as the Moon-Earth distance in kilometers and the
        equatorial horizontal parallax.

        :param epoch: Instant to compute the Moon's position, as an
            py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: Tuple containing:

            * Geocentric longitude of the center of the Moon, as an
              py:class:`Epoch` object.
            * Geocentric latitude of the center of the Moon, as an
              py:class:`Epoch` object.
            * Distance in kilometers between the centers of Earth and Moon, in
              kilometers (float)
            * Equatorial horizontal parallax of the Moon, as an
              py:class:`Epoch` object.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> Lambda, Beta, Delta, ppi = Moon.geocentric_ecliptical_pos(epoch)
        >>> print(round(Lambda, 6))
        133.162655
        >>> print(round(Beta, 6))
        -3.229126
        >>> print(round(Delta, 1))
        368409.7
        >>> print(round(ppi, 5))
        0.99199
        """
        ...
    @staticmethod
    def apparent_ecliptical_pos(epoch: Epoch) -> tuple[Angle, Angle, float, Angle]:
        """
        This method computes the apparent geocentric ecliptical position
        (longitude, latitude) of the Moon for a given instant, referred to the
        mean equinox of the date, as well as the Moon-Earth distance in
        kilometers and the equatorial horizontal parallax.

        :param epoch: Instant to compute the Moon's position, as an
            py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: Tuple containing:

            * Apparent geocentric longitude of the center of the Moon, as an
              py:class:`Epoch` object.
            * Apparent geocentric latitude of the center of the Moon, as an
              py:class:`Epoch` object.
            * Distance in kilometers between the centers of Earth and Moon, in
              kilometers (float)
            * Equatorial horizontal parallax of the Moon, as an
              py:class:`Epoch` object.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> Lambda, Beta, Delta, ppi = Moon.apparent_ecliptical_pos(epoch)
        >>> print(round(Lambda, 5))
        133.16726
        >>> print(round(Beta, 6))
        -3.229126
        >>> print(round(Delta, 1))
        368409.7
        >>> print(round(ppi, 5))
        0.99199
        """
        ...
    @staticmethod
    def apparent_equatorial_pos(epoch: Epoch) -> tuple[Angle, Angle, float, Angle]:
        """
        This method computes the apparent equatorial position (right
        ascension, declination) of the Moon for a given instant, referred to
        the mean equinox of the date, as well as the Moon-Earth distance in
        kilometers and the equatorial horizontal parallax.

        :param epoch: Instant to compute the Moon's position, as an
            py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: Tuple containing:

            * Apparent right ascension of the center of the Moon, as an
              py:class:`Epoch` object.
            * Apparent declination of the center of the Moon, as an
              py:class:`Epoch` object.
            * Distance in kilometers between the centers of Earth and Moon, in
              kilometers (float)
            * Equatorial horizontal parallax of the Moon, as an
              py:class:`Epoch` object.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> ra, dec, Delta, ppi = Moon.apparent_equatorial_pos(epoch)
        >>> print(round(ra, 6))
        134.688469
        >>> print(round(dec, 6))
        13.768367
        >>> print(round(Delta, 1))
        368409.7
        >>> print(round(ppi, 5))
        0.99199
        """
        ...
    @staticmethod
    def longitude_mean_ascending_node(epoch: Epoch) -> Angle:
        """
        This method computes the longitude of the mean ascending node of the
        Moon in degrees, for a given instant, measured from the mean equinox of
        the date.

        :param epoch: Instant to compute the Moon's mean ascending node, as an
            py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: The longitude of the mean ascending node.
        :rtype: py:class:`Angle`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1913, 5, 27.0)
        >>> Omega = Moon.longitude_mean_ascending_node(epoch)
        >>> print(round(Omega, 1))
        0.0
        >>> epoch = Epoch(2043, 9, 10.0)
        >>> Omega = Moon.longitude_mean_ascending_node(epoch)
        >>> print(round(Omega, 1))
        0.0
        >>> epoch = Epoch(1959, 12, 7.0)
        >>> Omega = Moon.longitude_mean_ascending_node(epoch)
        >>> print(round(Omega, 1))
        180.0
        >>> epoch = Epoch(2108, 11, 3.0)
        >>> Omega = Moon.longitude_mean_ascending_node(epoch)
        >>> print(round(Omega, 1))
        180.0
        """
        ...
    @staticmethod
    def longitude_true_ascending_node(epoch: Epoch) -> Angle:
        """
        This method computes the longitude of the true ascending node of the
        Moon in degrees, for a given instant, measured from the mean equinox of
        the date.

        :param epoch: Instant to compute the Moon's true ascending node, as an
            py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: The longitude of the true ascending node.
        :rtype: py:class:`Angle`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1913, 5, 27.0)
        >>> Omega = Moon.longitude_true_ascending_node(epoch)
        >>> print(round(Omega, 4))
        0.8763
        """
        ...
    @staticmethod
    def longitude_mean_perigee(epoch: Epoch) -> Angle:
        """
        This method computes the longitude of the mean perigee of the lunar
        orbitn in degrees, for a given instant, measured from the mean equinox
        of the date.

        :param epoch: Instant to compute the Moon's mean perigee, as an
            py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: The longitude of the mean perigee.
        :rtype: py:class:`Angle`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(2021, 3, 5.0)
        >>> Pi = Moon.longitude_mean_perigee(epoch)
        >>> print(round(Pi, 5))
        224.89194
        """
        ...
    @staticmethod
    def illuminated_fraction_disk(epoch: Epoch) -> float:
        """
        This method computes the approximate illuminated fraction 'k' of the
        disk of the Moon. The method used has a relatively low accuracy, but it
        is enough to the 2nd decimal place.

        :param epoch: Instant to compute the Moon's illuminated fraction of the
            disk, as a py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: The approximate illuminated fraction of the Moon's disk.
        :rtype: float
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> k = Moon.illuminated_fraction_disk(epoch)
        >>> print(round(k, 2))
        0.68
        """
        ...
    @staticmethod
    def position_bright_limb(epoch: Epoch) -> Angle:
        """
        This method computes the position angle of the Moon's bright limb,
        i.e., the position angle of the midpoint of the illuminated limb,
        reckoned eastward from the North Point of the disk (not from the axis
        of rotation of the lunar globe).

        :param epoch: Instant to compute the position angle of the  Moon's
            bright limb, as a py:class:`Epoch` object.
        :type epoch: :py:class:`Epoch`

        :returns: The position angle of the Moon's bright limb.
        :rtype: :py:class:`Angle`
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> xi = Moon.position_bright_limb(epoch)
        >>> print(round(xi, 1))
        285.0
        """
        ...
    @staticmethod
    def moon_phase(epoch: Epoch, target: Literal["new", "first", "full", "last"] = "new") -> Epoch:
        """
        This method computes the time of the phase of the moon closest to
        the provided epoch. The resulting time is expressed in the uniform time
        scale of Dynamical Time (TT).

        :param epoch: Approximate epoch we want to compute the Moon phase for.
        :type year: :py:class:`Epoch`
        :param target: Corresponding phase. It can be "new" (New Moon), "first"
            (First Quarter), "full" (Full Moon) and "last" (Last Quarter). It
            is 'new' by default.
        :type target: str

        :returns: The instant of time when the provided phase happens.
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input values are of wrong type.
        :raises: ValueError if 'target' value is invalid.

        >>> epoch = Epoch(1977, 2, 15.0)
        >>> new_moon = Moon.moon_phase(epoch, target="new")
        >>> y, m, d, h, mi, s = new_moon.get_full_date()
        >>> print("{}/{}/{} {}:{}:{}".format(y, m, d, h, mi, round(s, 0)))
        1977/2/18 3:37:42.0
        >>> epoch = Epoch(2044, 1, 1.0)
        >>> new_moon = Moon.moon_phase(epoch, target="last")
        >>> y, m, d, h, mi, s = new_moon.get_full_date()
        >>> print("{}/{}/{} {}:{}:{}".format(y, m, d, h, mi, round(s)))
        2044/1/21 23:48:17
        """
        ...
    @staticmethod
    def moon_perigee_apogee(epoch: Epoch, target: Literal["perigee", "apogee"] = "perigee") -> tuple[Epoch, Angle]:
        """
        This method computes the approximate times when the distance between
        the Earth and the Moon is a minimum (perigee) or a maximum (apogee).
        The resulting times will be expressed in the uniform time scale of
        Dynamical Time (TT).

        :param epoch: Approximate epoch we want to compute the Moon's perigee
            or apogee for.
        :type year: :py:class:`Epoch`
        :param target: Either 'perigee' or 'apogee'. It's 'perigee' by default.
        :type target: str

        :returns: A tuple containing the instant of time when the perigee or
            apogee happens, as a :py:class:`Epoch` object, and the Moon's
            corresponding equatorial horizontal parallax, as a
            :py:class:`Angle` object.
        :rtype: tuple
        :raises: TypeError if input values are of wrong type.
        :raises: ValueError if 'target' value is invalid.

        >>> epoch = Epoch(1988, 10, 1.0)
        >>> apogee, parallax = Moon.moon_perigee_apogee(epoch, target="apogee")
        >>> y, m, d, h, mi, s = apogee.get_full_date()
        >>> print("{}/{}/{} {}:{}".format(y, m, d, h, mi))
        1988/10/7 20:30
        >>> print("{}".format(parallax.dms_str(n_dec=3)))
        54' 0.679''
        """
        ...
    @staticmethod
    def moon_passage_nodes(epoch: Epoch, target: Literal["ascending", "descending"] = "ascending") -> Epoch:
        """
        This method computes the approximate times when the center of the
        Moon passes through the ascending or descending node of its orbit. The
        resulting times will be expressed in the uniform time scale of
        Dynamical Time (TT).

        :param epoch: Approximate epoch we want to compute the Moon's passage
            through the ascending or descending node.
        :type year: :py:class:`Epoch`
        :param target: Either 'ascending' or 'descending'. It is 'ascending' by
            default.
        :type target: str

        :returns: The instant of time when the Moon passes thhrough the
            ascending or descending node.
        :rtype: :py:class:`Epoch`
        :raises: TypeError if input values are of wrong type.
        :raises: ValueError if 'target' value is invalid.

        >>> epoch = Epoch(1987, 5, 15.0)
        >>> passage = Moon.moon_passage_nodes(epoch, target="ascending")
        >>> y, m, d, h, mi, s = passage.get_full_date()
        >>> mi += s/60.0
        >>> print("{}/{}/{} {}:{}".format(y, m, d, h, round(mi)))
        1987/5/23 6:26
        """
        ...
    @staticmethod
    def moon_maximum_declination(epoch: Epoch, target: Literal["northern", "southern"] = "northern") -> tuple[Epoch, Angle]:
        """
        This method computes the approximate times when the Moon reaches
        its maximum declination (either 'northern' or 'southern'), as well as
        the values of these extreme declinations. The resulting times will be
        expressed in the uniform time scale of Dynamical Time (TT).

        :param epoch: Approximate epoch we want to compute the Moon's maximum
            declination.
        :type year: :py:class:`Epoch`
        :param target: Either 'northern' or 'southern', depending on the
            maximum declination being looked for. It is 'northern' by default.
        :type target: str

        :returns: A tuple containing the instant of time when the maximum
            declination happens, as a :py:class:`Epoch` object, and the angle
            value of such declination, as a :py:class:`Angle` object.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1988, 12, 15.0)
        >>> epo, dec = Moon.moon_maximum_declination(epoch)
        >>> y, m, d, h, mi, s = epo.get_full_date()
        >>> print("{}/{}/{} {}:0{}".format(y, m, d, h, mi))
        1988/12/22 20:01
        >>> print("{}".format(dec.dms_str(n_dec=0)))
        28d 9' 22.0''
        >>> epoch = Epoch(2049, 4, 15.0)
        >>> epo, dec = Moon.moon_maximum_declination(epoch, target='southern')
        >>> y, m, d, h, mi, s = epo.get_full_date()
        >>> print("{}/{}/{} {}:{}".format(y, m, d, h, mi))
        2049/4/21 14:0
        >>> print("{}".format(dec.dms_str(n_dec=0)))
        -22d 8' 18.0''
        >>> epoch = Epoch(-4, 3, 15.0)
        >>> epo, dec = Moon.moon_maximum_declination(epoch, target='northern')
        >>> y, m, d, h, mi, s = epo.get_full_date()
        >>> print("{}/{}/{} {}h".format(y, m, d, h))
        -4/3/16 15h
        >>> print("{}".format(dec.dms_str(n_dec=0)))
        28d 58' 26.0''
        """
        ...
    @staticmethod
    def moon_librations(epoch: Epoch) -> tuple[Angle, Angle, Angle, Angle, Angle, Angle]:
        """
        This method computes the librations in longitude and latitude of the
        moon. There are several librations: The optical librations, that are
        the apparent oscillations in the hemisphere that the Moon turns towards
        the Earth, due to variations in the geometric position of the Earth
        relative to the lunar surface during the course of the orbital motion
        of the Moon. These variations allow to observe about 59% of the surface
        of the Moon from the Earth.

        There is also the physical libration of the Moon, i.e., the libration
        due to the actual rotational motion of the Moon about its mean
        rotation. The physical libration is much smaller than the optical
        libration, and can never be larger than 0.04 degree in both longitude
        and latitude.

        Finally, there is the total libration, which is the sum of the two
        librations mentioned above

        :param epoch: Epoch we want to compute the Moon's librations.
        :type year: :py:class:`Epoch`

        :returns: A tuple containing the optical libration in longitude and in
            latitude, the physical libration also in longitude and latitude,
            and the total librations which is the sum of the previouse ones,
            all of them as :py:class:`Angle` objects.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> lopt, bopt, lphys, bphys, ltot, btot = Moon.moon_librations(epoch)
        >>> print(round(lopt, 3))
        -1.206
        >>> print(round(bopt, 3))
        4.194
        >>> print(round(lphys, 3))
        -0.025
        >>> print(round(bphys, 3))
        0.006
        >>> print(round(ltot, 2))
        -1.23
        >>> print(round(btot, 3))
        4.2
        """
        ...
    @staticmethod
    def moon_position_angle_axis(epoch: Epoch) -> Angle:
        """
        This method computes the position angle of the Moon's axis of
        rotation. The effect of the physical libration is taken into account.

        :param epoch: Epoch we want to compute the position angle of the Moon's
            axis of rotation.
        :type year: :py:class:`Epoch`

        :returns: The position angle of the Moon's axis of rotation, as a
            :py:class:`Angle` object.
        :rtype: tuple
        :raises: TypeError if input value is of wrong type.

        >>> epoch = Epoch(1992, 4, 12.0)
        >>> p = Moon.moon_position_angle_axis(epoch)
        >>> print(round(p, 2))
        15.08
        """
        ...

def main() -> None: ...
