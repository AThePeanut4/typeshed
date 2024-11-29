def fetch_build_egg(dist, req):
    """
    Fetch an egg needed for building.

    Use pip/wheel to fetch/build a wheel.
    """
    ...
def strip_marker(req):
    """
    Return a new requirement without the environment marker to avoid
    calling pip with something like `babel; extra == "i18n"`, which
    would always be ignored.
    """
    ...
