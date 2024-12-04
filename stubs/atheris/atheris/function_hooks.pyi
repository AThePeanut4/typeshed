"""Provides Atheris instrumentation hooks for particular functions like regex."""

from typing import Any

def hook_re_module() -> None:
    """Adds Atheris instrumentation hooks to the `re` module."""
    ...

class EnabledHooks:
    """Manages the set of enabled hooks."""
    def __init__(self) -> None: ...
    def add(self, hook: str) -> None: ...
    def __contains__(self, hook: str) -> bool: ...

enabled_hooks: EnabledHooks

# args[1] is an arbitrary string method that is called
# with the subsequent arguments, so they will vary
def _hook_str(*args: Any, **kwargs: Any) -> bool:
    """
    Proxy routing str functions through Atheris tracing.

    Even though bytecode is modified for hooking the str methods, we use this
    proxy function for typechecking the caller at runtime.

    Args:
      *args: The positional arguments
      **kwargs: The keyword arguments

    Returns:
      The result of s (args[0]) calling str_method (args[1]) with *args[2:],
      **kwargs
    """
    ...
