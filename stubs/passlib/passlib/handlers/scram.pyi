"""passlib.handlers.scram - hash for SCRAM credential storage"""

from _typeshed import Incomplete
from typing import ClassVar

import passlib.utils.handlers as uh

class scram(uh.HasRounds, uh.HasRawSalt, uh.HasRawChecksum, uh.GenericHandler):  # type: ignore[misc]
    """
    This class provides a format for storing SCRAM passwords, and follows
    the :ref:`password-hash-api`.

    It supports a variable-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: bytes
    :param salt:
        Optional salt bytes.
        If specified, the length must be between 0-1024 bytes.
        If not specified, a 12 byte salt will be autogenerated
        (this is recommended).

    :type salt_size: int
    :param salt_size:
        Optional number of bytes to use when autogenerating new salts.
        Defaults to 12 bytes, but can be any value between 0 and 1024.

    :type rounds: int
    :param rounds:
        Optional number of rounds to use.
        Defaults to 100000, but must be within ``range(1,1<<32)``.

    :type algs: list of strings
    :param algs:
        Specify list of digest algorithms to use.

        By default each scram hash will contain digests for SHA-1,
        SHA-256, and SHA-512. This can be overridden by specify either be a
        list such as ``["sha-1", "sha-256"]``, or a comma-separated string
        such as ``"sha-1, sha-256"``. Names are case insensitive, and may
        use :mod:`!hashlib` or `IANA <http://www.iana.org/assignments/hash-function-text-names>`_
        hash names.

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include ``rounds``
        that are too small or too large, and ``salt`` strings that are too long.

        .. versionadded:: 1.6

    In addition to the standard :ref:`password-hash-api` methods,
    this class also provides the following methods for manipulating Passlib
    scram hashes in ways useful for pluging into a SCRAM protocol stack:

    .. automethod:: extract_digest_info
    .. automethod:: extract_digest_algs
    .. automethod:: derive_digest
    """
    name: ClassVar[str]
    ident: ClassVar[str]
    default_salt_size: ClassVar[int]
    max_salt_size: ClassVar[int]
    default_rounds: ClassVar[int]
    min_rounds: ClassVar[int]
    max_rounds: ClassVar[int]
    rounds_cost: ClassVar[str]
    default_algs: ClassVar[list[str]]
    algs: Incomplete | None
    @classmethod
    def extract_digest_info(cls, hash, alg):
        """
        return (salt, rounds, digest) for specific hash algorithm.

        :type hash: str
        :arg hash:
            :class:`!scram` hash stored for desired user

        :type alg: str
        :arg alg:
            Name of digest algorithm (e.g. ``"sha-1"``) requested by client.

            This value is run through :func:`~passlib.crypto.digest.norm_hash_name`,
            so it is case-insensitive, and can be the raw SCRAM
            mechanism name (e.g. ``"SCRAM-SHA-1"``), the IANA name,
            or the hashlib name.

        :raises KeyError:
            If the hash does not contain an entry for the requested digest
            algorithm.

        :returns:
            A tuple containing ``(salt, rounds, digest)``,
            where *digest* matches the raw bytes returned by
            SCRAM's :func:`Hi` function for the stored password,
            the provided *salt*, and the iteration count (*rounds*).
            *salt* and *digest* are both raw (unencoded) bytes.
        """
        ...
    @classmethod
    def extract_digest_algs(cls, hash, format: str = "iana"):
        """
        Return names of all algorithms stored in a given hash.

        :type hash: str
        :arg hash:
            The :class:`!scram` hash to parse

        :type format: str
        :param format:
            This changes the naming convention used by the
            returned algorithm names. By default the names
            are IANA-compatible; possible values are ``"iana"`` or ``"hashlib"``.

        :returns:
            Returns a list of digest algorithms; e.g. ``["sha-1"]``
        """
        ...
    @classmethod
    def derive_digest(cls, password, salt, rounds, alg):
        """
        helper to create SaltedPassword digest for SCRAM.

        This performs the step in the SCRAM protocol described as::

            SaltedPassword  := Hi(Normalize(password), salt, i)

        :type password: unicode or utf-8 bytes
        :arg password: password to run through digest

        :type salt: bytes
        :arg salt: raw salt data

        :type rounds: int
        :arg rounds: number of iterations.

        :type alg: str
        :arg alg: name of digest to use (e.g. ``"sha-1"``).

        :returns:
            raw bytes of ``SaltedPassword``
        """
        ...
    @classmethod
    def from_string(cls, hash): ...
    @classmethod
    def using(cls, default_algs: Incomplete | None = None, algs: Incomplete | None = None, **kwds): ...  # type: ignore[override]
    def __init__(self, algs: Incomplete | None = None, **kwds) -> None: ...
    @classmethod
    def verify(cls, secret, hash, full: bool = False): ...  # type: ignore[override]
