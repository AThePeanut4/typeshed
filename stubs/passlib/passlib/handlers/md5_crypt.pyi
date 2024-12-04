"""passlib.handlers.md5_crypt - md5-crypt algorithm"""

from typing import ClassVar

import passlib.utils.handlers as uh

class _MD5_Common(uh.HasSalt, uh.GenericHandler):
    """common code for md5_crypt and apr_md5_crypt"""
    checksum_size: ClassVar[int]
    checksum_chars: ClassVar[str]
    max_salt_size: ClassVar[int]
    salt_chars: ClassVar[str]
    @classmethod
    def from_string(cls, hash): ...

class md5_crypt(uh.HasManyBackends, _MD5_Common):
    """
    This class implements the MD5-Crypt password hash, and follows the :ref:`password-hash-api`.

    It supports a variable-length salt.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, one will be autogenerated (this is recommended).
        If specified, it must be 0-8 characters, drawn from the regexp range ``[./0-9A-Za-z]``.

    :type salt_size: int
    :param salt_size:
        Optional number of characters to use when autogenerating new salts.
        Defaults to 8, but can be any value between 0 and 8.
        (This is mainly needed when generating Cisco-compatible hashes,
        which require ``salt_size=4``).

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include
        ``salt`` strings that are too long.

        .. versionadded:: 1.6
    """
    name: ClassVar[str]
    ident: ClassVar[str]
    backends: ClassVar[tuple[str, ...]]

class apr_md5_crypt(_MD5_Common):
    """
    This class implements the Apr-MD5-Crypt password hash, and follows the :ref:`password-hash-api`.

    It supports a variable-length salt.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, one will be autogenerated (this is recommended).
        If specified, it must be 0-8 characters, drawn from the regexp range ``[./0-9A-Za-z]``.

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include
        ``salt`` strings that are too long.

        .. versionadded:: 1.6
    """
    name: ClassVar[str]
    ident: ClassVar[str]
