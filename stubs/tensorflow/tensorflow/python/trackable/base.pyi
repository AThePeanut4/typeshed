# Internal type that is commonly used as a base class
# and some public apis the signature needs it. As type
# is internal exact module it lives in is unstable across
# versions.

"""An object-local variable management scheme."""

class Trackable:
    """
    Base class for `Trackable` objects without automatic dependencies.

    This class has no __setattr__ override for performance reasons. Dependencies
    must be added explicitly. Unless attribute assignment is performance-critical,
    use `AutoTrackable` instead. Use `Trackable` for `isinstance`
    checks.
    """
    ...
