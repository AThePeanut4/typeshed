"""Common validation functions"""

def require_string(value, value_name) -> None:
    """
    Require that value is a string

    :raises: TypeError
    """
    ...
def require_callback(callback, callback_name: str = "callback") -> None:
    """
    Require that callback is callable and is not None

    :raises: TypeError
    """
    ...
def rpc_completion_callback(callback):
    """
    Verify callback is callable if not None

    :returns: boolean indicating nowait
    :rtype: bool
    :raises: TypeError
    """
    ...
def zero_or_greater(name, value) -> None:
    """
    Verify that value is zero or greater. If not, 'name'
    will be used in error message

    :raises: ValueError
    """
    ...
