"""passlib.handlers.sha2_crypt - SHA256-Crypt / SHA512-Crypt"""

from typing import ClassVar
from typing_extensions import Self

import passlib.utils.handlers as uh

class _SHA2_Common(uh.HasManyBackends, uh.HasRounds, uh.HasSalt, uh.GenericHandler):  # type: ignore[misc]
    """class containing common code shared by sha256_crypt & sha512_crypt"""
    checksum_chars: ClassVar[str]
    max_salt_size: ClassVar[int]
    salt_chars: ClassVar[str]
    min_rounds: ClassVar[int]
    max_rounds: ClassVar[int]
    rounds_cost: ClassVar[str]
    implicit_rounds: bool
    def __init__(self, implicit_rounds: bool | None = None, **kwds) -> None: ...
    @classmethod
    def from_string(cls, hash: str | bytes) -> Self: ...  # type: ignore[override]
    backends: ClassVar[tuple[str, ...]]

class sha256_crypt(_SHA2_Common):
    """
    This class implements the SHA256-Crypt password hash, and follows the :ref:`password-hash-api`.

    It supports a variable-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, one will be autogenerated (this is recommended).
        If specified, it must be 0-16 characters, drawn from the regexp range ``[./0-9A-Za-z]``.

    :type rounds: int
    :param rounds:
        Optional number of rounds to use.
        Defaults to 535000, must be between 1000 and 999999999, inclusive.

        .. note::
            per the official specification, when the rounds parameter is set to 5000,
            it may be omitted from the hash string.

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include ``rounds``
        that are too small or too large, and ``salt`` strings that are too long.

        .. versionadded:: 1.6

    ..
        commented out, currently only supported by :meth:`hash`, and not via :meth:`using`:

        :type implicit_rounds: bool
        :param implicit_rounds:
            this is an internal option which generally doesn't need to be touched.

            this flag determines whether the hash should omit the rounds parameter
            when encoding it to a string; this is only permitted by the spec for rounds=5000,
            and the flag is ignored otherwise. the spec requires the two different
            encodings be preserved as they are, instead of normalizing them.
    """
    name: ClassVar[str]
    ident: ClassVar[str]
    checksum_size: ClassVar[int]
    default_rounds: ClassVar[int]

class sha512_crypt(_SHA2_Common):
    """
    This class implements the SHA512-Crypt password hash, and follows the :ref:`password-hash-api`.

    It supports a variable-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, one will be autogenerated (this is recommended).
        If specified, it must be 0-16 characters, drawn from the regexp range ``[./0-9A-Za-z]``.

    :type rounds: int
    :param rounds:
        Optional number of rounds to use.
        Defaults to 656000, must be between 1000 and 999999999, inclusive.

        .. note::
            per the official specification, when the rounds parameter is set to 5000,
            it may be omitted from the hash string.

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include ``rounds``
        that are too small or too large, and ``salt`` strings that are too long.

        .. versionadded:: 1.6

    ..
        commented out, currently only supported by :meth:`hash`, and not via :meth:`using`:

        :type implicit_rounds: bool
        :param implicit_rounds:
            this is an internal option which generally doesn't need to be touched.

            this flag determines whether the hash should omit the rounds parameter
            when encoding it to a string; this is only permitted by the spec for rounds=5000,
            and the flag is ignored otherwise. the spec requires the two different
            encodings be preserved as they are, instead of normalizing them.
    """
    name: ClassVar[str]
    ident: ClassVar[str]
    checksum_size: ClassVar[int]
    default_rounds: ClassVar[int]
