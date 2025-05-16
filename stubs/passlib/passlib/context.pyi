from _typeshed import StrOrBytesPath, SupportsItems
from typing import Any
from typing_extensions import Self

class CryptPolicy:
    """
    .. deprecated:: 1.6
        This class has been deprecated, and will be removed in Passlib 1.8.
        All of its functionality has been rolled into :class:`CryptContext`.

    This class previously stored the configuration options for the
    CryptContext class. In the interest of interface simplification,
    all of this class' functionality has been rolled into the CryptContext
    class itself.
    The documentation for this class is now focused on  documenting how to
    migrate to the new api. Additionally, where possible, the deprecation
    warnings issued by the CryptPolicy methods will list the replacement call
    that should be used.

    Constructors
    ============
    CryptPolicy objects can be constructed directly using any of
    the keywords accepted by :class:`CryptContext`. Direct uses of the
    :class:`!CryptPolicy` constructor should either pass the keywords
    directly into the CryptContext constructor, or to :meth:`CryptContext.update`
    if the policy object was being used to update an existing context object.

    In addition to passing in keywords directly,
    CryptPolicy objects can be constructed by the following methods:

    .. automethod:: from_path
    .. automethod:: from_string
    .. automethod:: from_source
    .. automethod:: from_sources
    .. automethod:: replace

    Introspection
    =============
    All of the informational methods provided by this class have been deprecated
    by identical or similar methods in the :class:`CryptContext` class:

    .. automethod:: has_schemes
    .. automethod:: schemes
    .. automethod:: iter_handlers
    .. automethod:: get_handler
    .. automethod:: get_options
    .. automethod:: handler_is_deprecated
    .. automethod:: get_min_verify_time

    Exporting
    =========
    .. automethod:: iter_config
    .. automethod:: to_dict
    .. automethod:: to_file
    .. automethod:: to_string

    .. note::
        CryptPolicy are immutable.
        Use the :meth:`replace` method to mutate existing instances.

    .. deprecated:: 1.6
    """
    @classmethod
    def from_path(cls, path, section: str = "passlib", encoding: str = "utf-8"):
        """
        create a CryptPolicy instance from a local file.

        .. deprecated:: 1.6

        Creating a new CryptContext from a file, which was previously done via
        ``CryptContext(policy=CryptPolicy.from_path(path))``, can now be
        done via ``CryptContext.from_path(path)``.
        See :meth:`CryptContext.from_path` for details.

        Updating an existing CryptContext from a file, which was previously done
        ``context.policy = CryptPolicy.from_path(path)``, can now be
        done via ``context.load_path(path)``.
        See :meth:`CryptContext.load_path` for details.
        """
        ...
    @classmethod
    def from_string(cls, source, section: str = "passlib", encoding: str = "utf-8"):
        """
        create a CryptPolicy instance from a string.

        .. deprecated:: 1.6

        Creating a new CryptContext from a string, which was previously done via
        ``CryptContext(policy=CryptPolicy.from_string(data))``, can now be
        done via ``CryptContext.from_string(data)``.
        See :meth:`CryptContext.from_string` for details.

        Updating an existing CryptContext from a string, which was previously done
        ``context.policy = CryptPolicy.from_string(data)``, can now be
        done via ``context.load(data)``.
        See :meth:`CryptContext.load` for details.
        """
        ...
    @classmethod
    def from_source(cls, source, _warn: bool = True):
        """
        create a CryptPolicy instance from some source.

        this method autodetects the source type, and invokes
        the appropriate constructor automatically. it attempts
        to detect whether the source is a configuration string, a filepath,
        a dictionary, or an existing CryptPolicy instance.

        .. deprecated:: 1.6

        Create a new CryptContext, which could previously be done via
        ``CryptContext(policy=CryptPolicy.from_source(source))``, should
        now be done using an explicit method: the :class:`CryptContext`
        constructor itself, :meth:`CryptContext.from_path`,
        or :meth:`CryptContext.from_string`.

        Updating an existing CryptContext, which could previously be done via
        ``context.policy = CryptPolicy.from_source(source)``, should
        now be done using an explicit method: :meth:`CryptContext.update`,
        or :meth:`CryptContext.load`.
        """
        ...
    @classmethod
    def from_sources(cls, sources, _warn: bool = True):
        """
        create a CryptPolicy instance by merging multiple sources.

        each source is interpreted as by :meth:`from_source`,
        and the results are merged together.

        .. deprecated:: 1.6
            Instead of using this method to merge multiple policies together,
            a :class:`CryptContext` instance should be created, and then
            the multiple sources merged together via :meth:`CryptContext.load`.
        """
        ...
    def replace(self, *args, **kwds):
        """
        create a new CryptPolicy, optionally updating parts of the
        existing configuration.

        .. deprecated:: 1.6
            Callers of this method should :meth:`CryptContext.update` or
            :meth:`CryptContext.copy` instead.
        """
        ...
    def __init__(self, *args, **kwds) -> None: ...
    def has_schemes(self): ...
    def iter_handlers(self): ...
    def schemes(self, resolve: bool = False): ...
    def get_handler(self, name=None, category=None, required: bool = False): ...
    def get_min_verify_time(self, category=None): ...
    def get_options(self, name, category=None): ...
    def handler_is_deprecated(self, name, category=None): ...
    def iter_config(self, ini: bool = False, resolve: bool = False): ...
    def to_dict(self, resolve: bool = False): ...
    def to_file(self, stream, section: str = "passlib") -> None: ...
    def to_string(self, section: str = "passlib", encoding=None): ...

class CryptContext:
    """
    Helper for hashing & verifying passwords using multiple algorithms.

    Instances of this class allow applications to choose a specific
    set of hash algorithms which they wish to support, set limits and defaults
    for the rounds and salt sizes those algorithms should use, flag
    which algorithms should be deprecated, and automatically handle
    migrating users to stronger hashes when they log in.

    Basic usage::

        >>> ctx = CryptContext(schemes=[...])

    See the Passlib online documentation for details and full documentation.
    """
    @classmethod
    def from_string(cls, source: str | bytes, section: str = "passlib", encoding: str = "utf-8") -> Self:
        """
        create new CryptContext instance from an INI-formatted string.

        :type source: unicode or bytes
        :arg source:
            string containing INI-formatted content.

        :type section: str
        :param section:
            option name of section to read from, defaults to ``"passlib"``.

        :type encoding: str
        :arg encoding:
            optional encoding used when source is bytes, defaults to ``"utf-8"``.

        :returns:
            new :class:`CryptContext` instance, configured based on the
            parameters in the *source* string.

        Usage example::

            >>> from passlib.context import CryptContext
            >>> context = CryptContext.from_string('''
            ... [passlib]
            ... schemes = sha256_crypt, des_crypt
            ... sha256_crypt__default_rounds = 30000
            ... ''')

        .. versionadded:: 1.6

        .. seealso:: :meth:`to_string`, the inverse of this constructor.
        """
        ...
    @classmethod
    def from_path(cls, path: StrOrBytesPath, section: str = "passlib", encoding: str = "utf-8") -> Self: ...
    def copy(self, **kwds: Any) -> CryptContext: ...
    def using(self, **kwds: Any) -> CryptContext: ...
    def replace(self, **kwds): ...
    def __init__(self, schemes=None, policy=..., _autoload: bool = True, **kwds) -> None: ...
    policy: CryptPolicy
    def load_path(
        self, path: StrOrBytesPath, update: bool = False, section: str = "passlib", encoding: str = "utf-8"
    ) -> None:
        """
        Load new configuration into CryptContext from a local file.

        This function is a wrapper for :meth:`load` which
        loads a configuration string from the local file *path*,
        instead of an in-memory source. Its behavior and options
        are otherwise identical to :meth:`!load` when provided with
        an INI-formatted string.

        .. versionadded:: 1.6
        """
        ...
    def load(
        self,
        source: str | bytes | SupportsItems[str, Any] | CryptContext,
        update: bool = False,
        section: str = "passlib",
        encoding: str = "utf-8",
    ) -> None: ...
    def update(self, *args: Any, **kwds: Any) -> None: ...
    def schemes(self, resolve: bool = False, category=None, unconfigured: bool = False): ...
    def default_scheme(self, category=None, resolve: bool = False, unconfigured: bool = False): ...
    def handler(self, scheme=None, category=None, unconfigured: bool = False): ...
    @property
    def context_kwds(self):
        """
        return :class:`!set` containing union of all :ref:`contextual keywords <context-keywords>`
        supported by the handlers in this context.

        .. versionadded:: 1.6.6
        """
        ...
    def to_dict(self, resolve: bool = False) -> dict[str, Any]:
        """
        Return current configuration as a dictionary.

        :type resolve: bool
        :arg resolve:
            if ``True``, the ``schemes`` key will contain a list of
            a :class:`~passlib.ifc.PasswordHash` objects instead of just
            their names.

        This method dumps the current configuration of the CryptContext
        instance. The key/value pairs should be in the format accepted
        by the :class:`!CryptContext` class constructor, in fact
        ``CryptContext(**myctx.to_dict())`` will create an exact copy of ``myctx``.
        As an example::

            >>> # you can dump the configuration of any crypt context...
            >>> from passlib.apps import ldap_nocrypt_context
            >>> ldap_nocrypt_context.to_dict()
            {'schemes': ['ldap_salted_sha1',
            'ldap_salted_md5',
            'ldap_sha1',
            'ldap_md5',
            'ldap_plaintext']}

        .. versionadded:: 1.6
            This was previously available as ``CryptContext().policy.to_dict()``

        .. seealso:: the :ref:`context-serialization-example` example in the tutorial.
        """
        ...
    def to_string(self, section: str = "passlib") -> str:
        """
        serialize to INI format and return as unicode string.

        :param section:
            name of INI section to output, defaults to ``"passlib"``.

        :returns:
            CryptContext configuration, serialized to a INI unicode string.

        This function acts exactly like :meth:`to_dict`, except that it
        serializes all the contents into a single human-readable string,
        which can be hand edited, and/or stored in a file. The
        output of this method is accepted by :meth:`from_string`,
        :meth:`from_path`, and :meth:`load`. As an example::

            >>> # you can dump the configuration of any crypt context...
            >>> from passlib.apps import ldap_nocrypt_context
            >>> print ldap_nocrypt_context.to_string()
            [passlib]
            schemes = ldap_salted_sha1, ldap_salted_md5, ldap_sha1, ldap_md5, ldap_plaintext

        .. versionadded:: 1.6
            This was previously available as ``CryptContext().policy.to_string()``

        .. seealso:: the :ref:`context-serialization-example` example in the tutorial.
        """
        ...
    mvt_estimate_max_samples: int
    mvt_estimate_min_samples: int
    mvt_estimate_max_time: int
    mvt_estimate_resolution: float
    harden_verify: Any
    min_verify_time: int
    def reset_min_verify_time(self) -> None: ...
    def needs_update(
        self, hash: str | bytes, scheme: str | None = None, category: str | None = None, secret: str | bytes | None = None
    ) -> bool: ...
    def hash_needs_update(self, hash, scheme=None, category=None): ...
    def genconfig(self, scheme=None, category=None, **settings): ...
    def genhash(self, secret, config, scheme=None, category=None, **kwds): ...
    def identify(self, hash, category=None, resolve: bool = False, required: bool = False, unconfigured: bool = False): ...
    def hash(self, secret: str | bytes, scheme: str | None = None, category: str | None = None, **kwds: Any) -> str: ...
    def encrypt(self, *args, **kwds): ...
    def verify(
        self, secret: str | bytes, hash: str | bytes | None, scheme: str | None = None, category: str | None = None, **kwds: Any
    ) -> bool:
        r"""
        verify secret against an existing hash.

        If no scheme is specified, this will attempt to identify
        the scheme based on the contents of the provided hash
        (limited to the schemes configured for this context).
        It will then check whether the password verifies against the hash.

        :type secret: unicode or bytes
        :arg secret:
            the secret to verify

        :type hash: unicode or bytes
        :arg hash:
            hash string to compare to

            if ``None`` is passed in, this will be treated as "never verifying"

        :type scheme: str
        :param scheme:
            Optionally force context to use specific scheme.
            This is usually not needed, as most hashes can be unambiguously
            identified. Scheme must be one of the ones configured
            for this context
            (see the :ref:`schemes <context-schemes-option>` option).

            .. deprecated:: 1.7

                Support for this keyword is deprecated, and will be removed in Passlib 2.0.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>` string.
            This is mainly used when generating new hashes, it has little
            effect when verifying; this keyword is mainly provided for symmetry.

        :param \*\*kwds:
            All additional keywords are passed to the appropriate handler,
            and should match its :attr:`~passlib.ifc.PasswordHash.context_kwds`.

        :returns:
            ``True`` if the password matched the hash, else ``False``.

        :raises ValueError:
            * if the hash did not match any of the configured :meth:`schemes`.

            * if any of the arguments have an invalid value (this includes
              any keywords passed to the underlying hash's
              :meth:`PasswordHash.verify() <passlib.ifc.PasswordHash.verify>` method).

        :raises TypeError:
            * if any of the arguments have an invalid type (this includes
              any keywords passed to the underlying hash's
              :meth:`PasswordHash.verify() <passlib.ifc.PasswordHash.verify>` method).

        .. seealso:: the :ref:`context-basic-example` example in the tutorial
        """
        ...
    def verify_and_update(
        self, secret: str | bytes, hash: str | bytes | None, scheme: str | None = None, category: str | None = None, **kwds: Any
    ) -> tuple[bool, str | None]:
        r"""
        verify password and re-hash the password if needed, all in a single call.

        This is a convenience method which takes care of all the following:
        first it verifies the password (:meth:`~CryptContext.verify`), if this is successfull
        it checks if the hash needs updating (:meth:`~CryptContext.needs_update`), and if so,
        re-hashes the password (:meth:`~CryptContext.hash`), returning the replacement hash.
        This series of steps is a very common task for applications
        which wish to update deprecated hashes, and this call takes
        care of all 3 steps efficiently.

        :type secret: unicode or bytes
        :arg secret:
            the secret to verify

        :type secret: unicode or bytes
        :arg hash:
            hash string to compare to.

            if ``None`` is passed in, this will be treated as "never verifying"

        :type scheme: str
        :param scheme:
            Optionally force context to use specific scheme.
            This is usually not needed, as most hashes can be unambiguously
            identified. Scheme must be one of the ones configured
            for this context
            (see the :ref:`schemes <context-schemes-option>` option).

            .. deprecated:: 1.7

                Support for this keyword is deprecated, and will be removed in Passlib 2.0.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>`.
            If specified, this will cause any category-specific defaults to
            be used if the password has to be re-hashed.

        :param \*\*kwds:
            all additional keywords are passed to the appropriate handler,
            and should match that hash's
            :attr:`PasswordHash.context_kwds <passlib.ifc.PasswordHash.context_kwds>`.

        :returns:
            This function returns a tuple containing two elements:
            ``(verified, replacement_hash)``. The first is a boolean
            flag indicating whether the password verified,
            and the second an optional replacement hash.
            The tuple will always match one of the following 3 cases:

            * ``(False, None)`` indicates the secret failed to verify.
            * ``(True, None)`` indicates the secret verified correctly,
              and the hash does not need updating.
            * ``(True, str)`` indicates the secret verified correctly,
              but the current hash needs to be updated. The :class:`!str`
              will be the freshly generated hash, to replace the old one.

        :raises TypeError, ValueError:
            For the same reasons as :meth:`verify`.

        .. seealso:: the :ref:`context-migration-example` example in the tutorial.
        """
        ...
    def dummy_verify(self, elapsed: int = 0):
        """
        Helper that applications can call when user wasn't found,
        in order to simulate time it would take to hash a password.

        Runs verify() against a dummy hash, to simulate verification
        of a real account password.

        :param elapsed:

            .. deprecated:: 1.7.1

                this option is ignored, and will be removed in passlib 1.8.

        .. versionadded:: 1.7
        """
        ...
    def is_enabled(self, hash: str | bytes) -> bool:
        """
        test if hash represents a usuable password --
        i.e. does not represent an unusuable password such as ``"!"``,
        which is recognized by the :class:`~passlib.hash.unix_disabled` hash.

        :raises ValueError:
            if the hash is not recognized
            (typically solved by adding ``unix_disabled`` to the list of schemes).
        """
        ...
    def disable(self, hash: str | bytes | None = None) -> str:
        """
        return a string to disable logins for user,
        usually by returning a non-verifying string such as ``"!"``.

        :param hash:
            Callers can optionally provide the account's existing hash.
            Some disabled handlers (such as :class:`!unix_disabled`)
            will encode this into the returned value,
            so that it can be recovered via :meth:`enable`.

        :raises RuntimeError:
            if this function is called w/o a disabled hasher
            (such as :class:`~passlib.hash.unix_disabled`) included
            in the list of schemes.

        :returns:
            hash string which will be recognized as valid by the context,
            but is guaranteed to not validate against *any* password.
        """
        ...
    def enable(self, hash: str | bytes) -> str:
        """
        inverse of :meth:`disable` --
        attempts to recover original hash which was converted
        by a :meth:`!disable` call into a disabled hash --
        thus restoring the user's original password.

        :raises ValueError:
            if original hash not present, or if the disabled handler doesn't
            support encoding the original hash (e.g. ``django_disabled``)

        :returns:
            the original hash.
        """
        ...

class LazyCryptContext(CryptContext):
    def __init__(self, schemes=None, **kwds) -> None: ...
    def __getattribute__(self, attr: str) -> Any: ...

__all__ = ["CryptContext", "LazyCryptContext", "CryptPolicy"]
