"""Async executor versions of file functions from the os module."""

import sys
from _typeshed import BytesPath, FileDescriptorOrPath, GenericPath, ReadableBuffer, StrOrBytesPath, StrPath
from asyncio.events import AbstractEventLoop
from collections.abc import Sequence
from concurrent.futures import Executor
from os import _ScandirIterator, stat_result
from typing import AnyStr, overload

from aiofiles import ospath
from aiofiles.ospath import wrap as wrap

__all__ = [
    "path",
    "stat",
    "rename",
    "renames",
    "replace",
    "remove",
    "unlink",
    "mkdir",
    "makedirs",
    "rmdir",
    "removedirs",
    "link",
    "symlink",
    "readlink",
    "listdir",
    "scandir",
    "access",
    "wrap",
    "getcwd",
]

if sys.platform != "win32":
    __all__ += ["statvfs", "sendfile"]

path = ospath

async def stat(
    path: FileDescriptorOrPath,
    *,
    dir_fd: int | None = None,
    follow_symlinks: bool = True,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> stat_result: ...
async def rename(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def renames(
    old: StrOrBytesPath, new: StrOrBytesPath, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> None: ...
async def replace(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def remove(
    path: StrOrBytesPath, *, dir_fd: int | None = None, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> None: ...
async def unlink(
    path: StrOrBytesPath, *, dir_fd: int | None = ..., loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> None: ...
async def mkdir(
    path: StrOrBytesPath,
    mode: int = 511,
    *,
    dir_fd: int | None = None,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def makedirs(
    name: StrOrBytesPath,
    mode: int = 511,
    exist_ok: bool = False,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def link(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = ...,
    dst_dir_fd: int | None = ...,
    follow_symlinks: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def symlink(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    target_is_directory: bool = ...,
    *,
    dir_fd: int | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def readlink(
    path: AnyStr, *, dir_fd: int | None = ..., loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> AnyStr: ...
async def rmdir(
    path: StrOrBytesPath, *, dir_fd: int | None = None, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> None: ...
async def removedirs(name: StrOrBytesPath, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...) -> None: ...
@overload
async def scandir(
    path: None = None, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> _ScandirIterator[str]: ...
@overload
async def scandir(
    path: int, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> _ScandirIterator[str]: ...
@overload
async def scandir(
    path: GenericPath[AnyStr], *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> _ScandirIterator[AnyStr]: ...
@overload
async def listdir(
    path: StrPath | None, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> list[str]: ...
@overload
async def listdir(path: BytesPath, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...) -> list[bytes]: ...
@overload
async def listdir(path: int, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...) -> list[str]: ...
async def access(
    path: FileDescriptorOrPath, mode: int, *, dir_fd: int | None = None, effective_ids: bool = False, follow_symlinks: bool = True
) -> bool:
    """
    Use the real uid/gid to test for access to a path.

      path
        Path to be tested; can be string, bytes, or a path-like object.
      mode
        Operating-system mode bitfield.  Can be F_OK to test existence,
        or the inclusive-OR of R_OK, W_OK, and X_OK.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      effective_ids
        If True, access will use the effective uid/gid instead of
        the real uid/gid.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        access will examine the symbolic link itself instead of the file
        the link points to.

    dir_fd, effective_ids, and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.

    Note that most operations will use the effective uid/gid, therefore this
      routine can be used in a suid/sgid environment to test if the invoking user
      has the specified access to the path.
    """
    ...
async def getcwd() -> str:
    """Return a unicode string representing the current working directory."""
    ...

if sys.platform != "win32":
    from os import statvfs_result

    @overload
    async def sendfile(
        out_fd: int,
        in_fd: int,
        offset: int | None,
        count: int,
        *,
        loop: AbstractEventLoop | None = ...,
        executor: Executor | None = ...,
    ) -> int: ...
    @overload
    async def sendfile(
        out_fd: int,
        in_fd: int,
        offset: int,
        count: int,
        headers: Sequence[ReadableBuffer] = ...,
        trailers: Sequence[ReadableBuffer] = ...,
        flags: int = ...,
        *,
        loop: AbstractEventLoop | None = ...,
        executor: Executor | None = ...,
    ) -> int: ...  # FreeBSD and Mac OS X only
    async def statvfs(path: FileDescriptorOrPath) -> statvfs_result: ...  # Unix only
