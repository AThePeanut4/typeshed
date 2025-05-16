from typing import Any

class UnknownBackendError(ValueError):
    """
    Error raised if multi-backend handler doesn't recognize backend name.
    Inherits from :exc:`ValueError`.

    .. versionadded:: 1.7
    """
    hasher: Any
    backend: Any
    def __init__(self, hasher, backend) -> None: ...

class MissingBackendError(RuntimeError):
    """
    Error raised if multi-backend handler has no available backends;
    or if specifically requested backend is not available.

    :exc:`!MissingBackendError` derives
    from :exc:`RuntimeError`, since it usually indicates
    lack of an external library or OS feature.
    This is primarily raised by handlers which depend on
    external libraries (which is currently just
    :class:`~passlib.hash.bcrypt`).
    """
    ...
class InternalBackendError(RuntimeError):
    """
    Error raised if something unrecoverable goes wrong with backend call;
    such as if ``crypt.crypt()`` returning a malformed hash.

    .. versionadded:: 1.7.3
    """
    ...
class PasswordValueError(ValueError):
    """
    Error raised if a password can't be hashed / verified for various reasons.
    This exception derives from the builtin :exc:`!ValueError`.

    May be thrown directly when password violates internal invariants of hasher
    (e.g. some don't support NULL characters).  Hashers may also throw more specific subclasses,
    such as :exc:`!PasswordSizeError`.

    .. versionadded:: 1.7.3
    """
    ...

class PasswordSizeError(PasswordValueError):
    """
    Error raised if a password exceeds the maximum size allowed
    by Passlib (by default, 4096 characters); or if password exceeds
    a hash-specific size limitation.

    This exception derives from :exc:`PasswordValueError` (above).

    Many password hash algorithms take proportionately larger amounts of time and/or
    memory depending on the size of the password provided. This could present
    a potential denial of service (DOS) situation if a maliciously large
    password is provided to an application. Because of this, Passlib enforces
    a maximum size limit, but one which should be *much* larger
    than any legitimate password. :exc:`PasswordSizeError` derives
    from :exc:`!ValueError`.

    .. note::
        Applications wishing to use a different limit should set the
        ``PASSLIB_MAX_PASSWORD_SIZE`` environmental variable before
        Passlib is loaded. The value can be any large positive integer.

    .. attribute:: max_size

        indicates the maximum allowed size.

    .. versionadded:: 1.6
    """
    max_size: Any
    def __init__(self, max_size, msg=None) -> None: ...

class PasswordTruncateError(PasswordSizeError):
    def __init__(self, cls, msg=None) -> None: ...

class PasslibSecurityError(RuntimeError):
    """
    Error raised if critical security issue is detected
    (e.g. an attempt is made to use a vulnerable version of a bcrypt backend).

    .. versionadded:: 1.6.3
    """
    ...

class TokenError(ValueError):
    def __init__(self, msg=None, *args, **kwds) -> None: ...

class MalformedTokenError(TokenError):
    """
    Error raised by :mod:`passlib.totp` when a token isn't formatted correctly
    (contains invalid characters, wrong number of digits, etc)
    """
    ...
class InvalidTokenError(TokenError):
    """
    Error raised by :mod:`passlib.totp` when a token is formatted correctly,
    but doesn't match any tokens within valid range.
    """
    ...

class UsedTokenError(TokenError):
    """
    Error raised by :mod:`passlib.totp` if a token is reused.
    Derives from :exc:`TokenError`.

    .. autoattribute:: expire_time

    .. versionadded:: 1.7
    """
    expire_time: Any
    def __init__(self, *args, **kwds) -> None: ...

class UnknownHashError(ValueError):
    """
    Error raised by :class:`~passlib.crypto.lookup_hash` if hash name is not recognized.
    This exception derives from :exc:`!ValueError`.

    As of version 1.7.3, this may also be raised if hash algorithm is known,
    but has been disabled due to FIPS mode (message will include phrase "disabled for fips").

    As of version 1.7.4, this may be raised if a :class:`~passlib.context.CryptContext`
    is unable to identify the algorithm used by a password hash.

    .. versionadded:: 1.7

    .. versionchanged: 1.7.3
        added 'message' argument.

    .. versionchanged:: 1.7.4
        altered call signature.
    """
    value: Any
    message: Any
    def __init__(self, message=None, value=None) -> None: ...

class PasslibWarning(UserWarning):
    """
    base class for Passlib's user warnings,
    derives from the builtin :exc:`UserWarning`.

def type_name(value): ...
def ExpectedTypeError(value, expected, param): ...
def ExpectedStringError(value, param): ...
def MissingDigestError(handler=None): ...
def NullPasswordError(handler=None): ...
def InvalidHashError(handler=None): ...
def MalformedHashError(handler=None, reason=None): ...
def ZeroPaddedRoundsError(handler=None): ...
def ChecksumSizeError(handler, raw: bool = False): ...

ENABLE_DEBUG_ONLY_REPR: bool

def debug_only_repr(value, param: str = "hash"):
    """
    helper used to display sensitive data (hashes etc) within error messages.
    currently returns placeholder test UNLESS unittests are running,
    in which case the real value is displayed.

    mainly useful to prevent hashes / secrets from being exposed in production tracebacks;
    while still being visible from test failures.

    NOTE: api subject to change, may formalize this more in the future.
    """
    ...
def CryptBackendError(handler, config, hash, source: str = "crypt.crypt()") -> None:
    """
    helper to generate standard message when ``crypt.crypt()`` returns invalid result.
    takes care of automatically masking contents of config & hash outside of UTs.
    """
    ...
