"""Simple function decorators to make Python programming easier."""

RESULTS_ATTRIBUTE: str

def cached(function):
    """
    Rudimentary caching decorator for functions.

    :param function: The function whose return value should be cached.
    :returns: The decorated function.

    The given function will only be called once, the first time the wrapper
    function is called. The return value is cached by the wrapper function as
    an attribute of the given function and returned on each subsequent call.

    .. note:: Currently no function arguments are supported because only a
              single return value can be cached. Accepting any function
              arguments at all would imply that the cache is parametrized on
              function arguments, which is not currently the case.
    """
    ...
