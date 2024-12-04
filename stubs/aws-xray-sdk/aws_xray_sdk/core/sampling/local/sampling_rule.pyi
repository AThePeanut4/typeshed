from aws_xray_sdk.core.utils.search_pattern import wildcard_match as wildcard_match

from ...exceptions.exceptions import InvalidSamplingManifestError as InvalidSamplingManifestError
from .reservoir import Reservoir as Reservoir

class SamplingRule:
    """
    One SamolingRule represents one rule defined from local rule json file
    or from a dictionary. It can be either a custom rule or default rule.
    """
    FIXED_TARGET: str
    RATE: str
    HOST: str
    METHOD: str
    PATH: str
    SERVICE_NAME: str
    def __init__(self, rule_dict, version: int = 2, default: bool = False) -> None:
        """
        :param dict rule_dict: The dictionary that defines a single rule.
        :param bool default: Indicates if this is the default rule. A default
            rule cannot have `host`, `http_method` or `url_path`.
        """
        ...
    def applies(self, host, method, path):
        """
        Determines whether or not this sampling rule applies to
        the incoming request based on some of the request's parameters.
        Any None parameters provided will be considered an implicit match.
        """
        ...
    @property
    def fixed_target(self):
        """
        Defines fixed number of sampled segments per second.
        This doesn't count for sampling rate.
        """
        ...
    @property
    def rate(self):
        """A float number less than 1.0 defines the sampling rate."""
        ...
    @property
    def host(self):
        """The host name of the reqest to sample."""
        ...
    @property
    def method(self):
        """HTTP method of the request to sample."""
        ...
    @property
    def path(self):
        """The url path of the request to sample."""
        ...
    @property
    def reservoir(self):
        """Keeps track of used sampled targets within the second."""
        ...
    @property
    def version(self):
        """Keeps track of used sampled targets within the second."""
        ...
