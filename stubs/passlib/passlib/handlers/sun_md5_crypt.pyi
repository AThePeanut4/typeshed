"""
passlib.handlers.sun_md5_crypt - Sun's Md5 Crypt, used on Solaris

.. warning::

    This implementation may not reproduce
    the original Solaris behavior in some border cases.
    See documentation for details.
"""

from typing import ClassVar
from typing_extensions import Self

import passlib.utils.handlers as uh

class sun_md5_crypt(uh.HasRounds, uh.HasSalt, uh.GenericHandler):  # type: ignore[misc]
    """
    This class implements the Sun-MD5-Crypt password hash, and follows the :ref:`password-hash-api`.

    It supports a variable-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, a salt will be autogenerated (this is recommended).
        If specified, it must be drawn from the regexp range ``[./0-9A-Za-z]``.

    :type salt_size: int
    :param salt_size:
        If no salt is specified, this parameter can be used to specify
        the size (in characters) of the autogenerated salt.
        It currently defaults to 8.

    :type rounds: int
    :param rounds:
        Optional number of rounds to use.
        Defaults to 34000, must be between 0 and 4294963199, inclusive.

    :type bare_salt: bool
    :param bare_salt:
        Optional flag used to enable an alternate salt digest behavior
        used by some hash strings in this scheme.
        This flag can be ignored by most users.
        Defaults to ``False``.
        (see :ref:`smc-bare-salt` for details).

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include ``rounds``
        that are too small or too large, and ``salt`` strings that are too long.

        .. versionadded:: 1.6
    """
    name: ClassVar[str]
    checksum_chars: ClassVar[str]
    checksum_size: ClassVar[int]
    default_salt_size: ClassVar[int]
    max_salt_size: ClassVar[int | None]
    salt_chars: ClassVar[str]
    default_rounds: ClassVar[int]
    min_rounds: ClassVar[int]
    max_rounds: ClassVar[int]
    rounds_cost: ClassVar[str]
    ident_values: ClassVar[tuple[str, ...]]
    bare_salt: bool
    def __init__(self, bare_salt: bool = False, **kwds) -> None: ...
    @classmethod
    def identify(cls, hash): ...
    @classmethod
    def from_string(cls, hash: str | bytes) -> Self: ...  # type: ignore[override]
    def to_string(self, _withchk: bool = True) -> str: ...

__all__ = ["sun_md5_crypt"]
