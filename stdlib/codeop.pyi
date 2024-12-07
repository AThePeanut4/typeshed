import sys
from types import CodeType

__all__ = ["compile_command", "Compile", "CommandCompiler"]

def compile_command(source: str, filename: str = "<input>", symbol: str = "single") -> CodeType | None:
    r"""
    Compile a command and determine whether it is incomplete.

    Arguments:

    source -- the source string; may contain \n characters
    filename -- optional filename from which source was read; default
                "<input>"
    symbol -- optional grammar start symbol; "single" (default), "exec"
              or "eval"

    Return value / exceptions raised:

    - Return a code object if the command is complete and valid
    - Return None if the command is incomplete
    - Raise SyntaxError, ValueError or OverflowError if the command is a
      syntax error (OverflowError and ValueError can be produced by
      malformed literals).
    """
    ...

class Compile:
    """
    Instances of this class behave much like the built-in compile
    function, but if one is used to compile text containing a future
    statement, it "remembers" and compiles all subsequent program texts
    with the statement in force.
    """
    flags: int
    if sys.version_info >= (3, 13):
        def __call__(self, source: str, filename: str, symbol: str, flags: int = 0) -> CodeType: ...
    else:
        def __call__(self, source: str, filename: str, symbol: str) -> CodeType: ...

class CommandCompiler:
    """
    Instances of this class have __call__ methods identical in
    signature to compile_command; the difference is that if the
    instance compiles program text containing a __future__ statement,
    the instance 'remembers' and compiles all subsequent program texts
    with the statement in force.
    """
    compiler: Compile
    def __call__(self, source: str, filename: str = "<input>", symbol: str = "single") -> CodeType | None:
        r"""
        Compile a command and determine whether it is incomplete.

        Arguments:

        source -- the source string; may contain \n characters
        filename -- optional filename from which source was read;
                    default "<input>"
        symbol -- optional grammar start symbol; "single" (default) or
                  "eval"

        Return value / exceptions raised:

        - Return a code object if the command is complete and valid
        - Return None if the command is incomplete
        - Raise SyntaxError, ValueError or OverflowError if the command is a
          syntax error (OverflowError and ValueError can be produced by
          malformed literals).
        """
        ...
