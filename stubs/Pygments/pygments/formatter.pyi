from _typeshed import Incomplete
from typing import Generic, TypeVar, overload

_T = TypeVar("_T", str, bytes)

class Formatter(Generic[_T]):
    name: Incomplete
    aliases: Incomplete
    filenames: Incomplete
    unicodeoutput: bool
    style: Incomplete
    full: Incomplete
    title: Incomplete
    encoding: Incomplete
    options: Incomplete
    @overload
    def __init__(self: Formatter[str], *, encoding: None = None, outencoding: None = None, **options) -> None:
        """
        As with lexers, this constructor takes arbitrary optional arguments,
        and if you override it, you should first process your own options, then
        call the base class implementation.
        """
        ...
    @overload
    def __init__(self: Formatter[bytes], *, encoding: str, outencoding: None = None, **options) -> None:
        """
        As with lexers, this constructor takes arbitrary optional arguments,
        and if you override it, you should first process your own options, then
        call the base class implementation.
        """
        ...
    @overload
    def __init__(self: Formatter[bytes], *, encoding: None = None, outencoding: str, **options) -> None:
        """
        As with lexers, this constructor takes arbitrary optional arguments,
        and if you override it, you should first process your own options, then
        call the base class implementation.
        """
        ...
    def get_style_defs(self, arg: str = ""):
        """
        This method must return statements or declarations suitable to define
        the current style for subsequent highlighted text (e.g. CSS classes
        in the `HTMLFormatter`).

        The optional argument `arg` can be used to modify the generation and
        is formatter dependent (it is standardized because it can be given on
        the command line).

        This method is called by the ``-S`` :doc:`command-line option <cmdline>`,
        the `arg` is then given by the ``-a`` option.
        """
        ...
    def format(self, tokensource, outfile):
        """
        This method must format the tokens from the `tokensource` iterable and
        write the formatted version to the file object `outfile`.

        Formatter options can control how exactly the tokens are converted.
        """
        ...
