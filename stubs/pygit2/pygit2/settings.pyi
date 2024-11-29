"""Settings mapping."""

import pygit2.enums

class SearchPathList:
    def __getitem__(self, key: int) -> str: ...
    def __setitem__(self, key: int, value: bytes | str) -> None: ...

class Settings:
    """Library-wide settings interface."""
    def __init__(self) -> None:
        """Initialize global pygit2 and libgit2 settings."""
        ...
    @property
    def search_path(self) -> SearchPathList:
        """
        Configuration file search path.

        This behaves like an array whose indices correspond to ConfigLevel values.
        The local search path cannot be changed.
        """
        ...
    @property
    def mwindow_size(self) -> int:
        """Get or set the maximum mmap window size"""
        ...
    @mwindow_size.setter
    def mwindow_size(self, value: int) -> None:
        """Get or set the maximum mmap window size"""
        ...
    @property
    def mwindow_mapped_limit(self) -> int:
        """
        Get or set the maximum memory that will be mapped in total by the
        library
        """
        ...
    @mwindow_mapped_limit.setter
    def mwindow_mapped_limit(self, value: int) -> None:
        """
        Get or set the maximum memory that will be mapped in total by the
        library
        """
        ...
    @property
    def cached_memory(self) -> tuple[int, int]:
        """
        Get the current bytes in cache and the maximum that would be
        allowed in the cache.
        """
        ...
    def enable_caching(self, value: bool = True) -> None:
        """
        Enable or disable caching completely.

        Because caches are repository-specific, disabling the cache
        cannot immediately clear all cached objects, but each cache will
        be cleared on the next attempt to update anything in it.
        """
        ...
    def disable_pack_keep_file_checks(self, value: bool = True) -> None:
        """
        This will cause .keep file existence checks to be skipped when
        accessing packfiles, which can help performance with remote
        filesystems.
        """
        ...
    def cache_max_size(self, value: int) -> None:
        """
        Set the maximum total data size that will be cached in memory
        across all repositories before libgit2 starts evicting objects
        from the cache.  This is a soft limit, in that the library might
        briefly exceed it, but will start aggressively evicting objects
        from cache when that happens.  The default cache size is 256MB.
        """
        ...
    def cache_object_limit(self, object_type: pygit2.enums.ObjectType, value: int) -> None:
        """
        Set the maximum data size for the given type of object to be
        considered eligible for caching in memory.  Setting to value to
        zero means that that type of object will not be cached.
        Defaults to 0 for enums.ObjectType.BLOB (i.e. won't cache blobs)
        and 4k for COMMIT, TREE, and TAG.
        """
        ...
    @property
    def ssl_cert_file(self) -> bytes | str:
        """TLS certificate file path."""
        ...
    @ssl_cert_file.setter
    def ssl_cert_file(self, value: bytes | str) -> None:
        """TLS certificate file path."""
        ...
    @ssl_cert_file.deleter
    def ssl_cert_file(self) -> None:
        """TLS certificate file path."""
        ...
    @property
    def ssl_cert_dir(self) -> bytes | str:
        """TLS certificates lookup directory path."""
        ...
    @ssl_cert_dir.setter
    def ssl_cert_dir(self, value: bytes | str) -> None:
        """TLS certificates lookup directory path."""
        ...
    @ssl_cert_dir.deleter
    def ssl_cert_dir(self) -> None:
        """TLS certificates lookup directory path."""
        ...
    def set_ssl_cert_locations(self, cert_file: bytes | str, cert_dir: bytes | str) -> None:
        """
        Set the SSL certificate-authority locations.

        - `cert_file` is the location of a file containing several
          certificates concatenated together.
        - `cert_dir` is the location of a directory holding several
          certificates, one per file.

        Either parameter may be `NULL`, but not both.
        """
        ...
