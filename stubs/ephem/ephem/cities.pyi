"""Modest database of more than a hundred world cities."""

from . import Observer

def city(name: str) -> Observer: ...
def lookup(address: str) -> None:
    """
    DEPRECATED: Google, alas, no longer supports anonymous lat/lon lookup.

    Because looking up an address is really a problem in geography, not
    astronomy, PyEphem is not planning on repairing this routine.  Look
    for a good Python geolocation library if you need to turn strings
    into latitudes and longitudes.
    """
    ...
def lookup_with_geonames(q: str, username: str) -> Observer:
    """
    Given a string `q`, do a geonames lookup and return an Observer.

    Free geonames queries require registration with an email address
    at this url: https://www.geonames.org/login

    After registration, you also must enable the free webservices
    through your user account
    """
    ...
