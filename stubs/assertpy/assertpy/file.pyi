from _typeshed import StrPath, SupportsRead
from typing_extensions import Self

__tracebackhide__: bool

def contents_of(file: SupportsRead[str] | StrPath, encoding: str = "utf-8") -> str: ...

class FileMixin:
    """File assertions mixin."""
    def exists(self) -> Self:
        """
        Asserts that val is a path and that it exists.

        Examples:
            Usage::

                assert_that('myfile.txt').exists()
                assert_that('mydir').exists()

        Returns:
            AssertionBuilder: returns this instance to chain to the next assertion

        Raises:
            AssertionError: if val does **not** exist
        """
        ...
    def does_not_exist(self) -> Self:
        """
        Asserts that val is a path and that it does *not* exist.

        Examples:
            Usage::

                assert_that('missing.txt').does_not_exist()
                assert_that('missing_dir').does_not_exist()

        Returns:
            AssertionBuilder: returns this instance to chain to the next assertion

        Raises:
            AssertionError: if val **does** exist
        """
        ...
    def is_file(self) -> Self:
        """
        Asserts that val is a *file* and that it exists.

        Examples:
            Usage::

                assert_that('myfile.txt').is_file()

        Returns:
            AssertionBuilder: returns this instance to chain to the next assertion

        Raises:
            AssertionError: if val does **not** exist, or is **not** a file
        """
        ...
    def is_directory(self) -> Self:
        """
        Asserts that val is a *directory* and that it exists.

        Examples:
            Usage::

                assert_that('mydir').is_directory()

        Returns:
            AssertionBuilder: returns this instance to chain to the next assertion

        Raises:
            AssertionError: if val does **not** exist, or is **not** a directory
        """
        ...
    def is_named(self, filename: str) -> Self:
        """
        Asserts that val is an existing path to a file and that file is named filename.

        Args:
            filename: the expected filename

        Examples:
            Usage::

                assert_that('/path/to/mydir/myfile.txt').is_named('myfile.txt')

        Returns:
            AssertionBuilder: returns this instance to chain to the next assertion

        Raises:
            AssertionError: if val does **not** exist, or is **not** a file, or is **not** named the given filename
        """
        ...
    def is_child_of(self, parent: str) -> Self:
        """
        Asserts that val is an existing path to a file and that file is a child of parent.

        Args:
            parent: the expected parent directory

        Examples:
            Usage::

                assert_that('/path/to/mydir/myfile.txt').is_child_of('mydir')
                assert_that('/path/to/mydir/myfile.txt').is_child_of('to')
                assert_that('/path/to/mydir/myfile.txt').is_child_of('path')

        Returns:
            AssertionBuilder: returns this instance to chain to the next assertion

        Raises:
            AssertionError: if val does **not** exist, or is **not** a file, or is **not** a child of the given directory
        """
        ...
