"""
Functions for working with filesystem paths.

The :func:`expandpath` function expands the tilde to $HOME and environment
variables to their values.

The :func:`augpath` function creates variants of an existing path without
having to spend multiple lines of code splitting it up and stitching it back
together.

The :func:`shrinkuser` function replaces your home directory with a tilde.
"""

from _typeshed import StrPath

def augpath(
    path: StrPath,
    suffix: str = "",
    prefix: str = "",
    ext: str | None = None,
    base: str | None = None,
    dpath: str | None = None,
    multidot: bool = False,
) -> str:
    """
    Augment a path by modifying its components.

    Creates a new path with a different extension, basename, directory, prefix,
    and/or suffix.

    A prefix is inserted before the basename. A suffix is inserted
    between the basename and the extension. The basename and extension can be
    replaced with a new one. Essentially a path is broken down into components
    (dpath, base, ext), and then recombined as (dpath, prefix, base, suffix,
    ext) after replacing any specified component.

    Args:
        path (str | PathLike): a path to augment
        suffix (str, default=''): placed between the basename and extension
        prefix (str, default=''): placed in front of the basename
        ext (str, default=None): if specified, replaces the extension
        base (str, default=None): if specified, replaces the basename without
            extension
        dpath (str | PathLike, default=None): if specified, replaces the
            directory
        multidot (bool, default=False): Allows extensions to contain multiple
            dots. Specifically, if False, everything after the last dot in the
            basename is the extension. If True, everything after the first dot
            in the basename is the extension.

    Returns:
        str: augmented path

    Example:
        >>> path = 'foo.bar'
        >>> suffix = '_suff'
        >>> prefix = 'pref_'
        >>> ext = '.baz'
        >>> newpath = augpath(path, suffix, prefix, ext=ext, base='bar')
        >>> print('newpath = %s' % (newpath,))
        newpath = pref_bar_suff.baz

    Example:
        >>> augpath('foo.bar')
        'foo.bar'
        >>> augpath('foo.bar', ext='.BAZ')
        'foo.BAZ'
        >>> augpath('foo.bar', suffix='_')
        'foo_.bar'
        >>> augpath('foo.bar', prefix='_')
        '_foo.bar'
        >>> augpath('foo.bar', base='baz')
        'baz.bar'
        >>> augpath('foo.tar.gz', ext='.zip', multidot=True)
        'foo.zip'
        >>> augpath('foo.tar.gz', ext='.zip', multidot=False)
        'foo.tar.zip'
        >>> augpath('foo.tar.gz', suffix='_new', multidot=True)
        'foo_new.tar.gz'
    """
    ...
def shrinkuser(path: StrPath, home: str = "~") -> str:
    """
    Inverse of :func:`os.path.expanduser`.

    Args:
        path (str | PathLike): path in system file structure
        home (str, default='~'): symbol used to replace the home path.
            Defaults to '~', but you might want to use '$HOME' or
            '%USERPROFILE%' instead.

    Returns:
        str: path: shortened path replacing the home directory with a tilde

    Example:
        >>> path = expanduser('~')
        >>> assert path != '~'
        >>> assert shrinkuser(path) == '~'
        >>> assert shrinkuser(path + '1') == path + '1'
        >>> assert shrinkuser(path + '/1') == join('~', '1')
        >>> assert shrinkuser(path + '/1', '$HOME') == join('$HOME', '1')
    """
    ...
def expandpath(path: StrPath) -> str:
    """
    Shell-like expansion of environment variables and tilde home directory.

    Args:
        path (str | PathLike): the path to expand

    Returns:
        str : expanded path

    Example:
        >>> import os
        >>> os.environ['SPAM'] = 'eggs'
        >>> assert expandpath('~/$SPAM') == expanduser('~/eggs')
        >>> assert expandpath('foo') == 'foo'
    """
    ...

__all__ = ["augpath", "shrinkuser", "expandpath"]
