"""
For backward compatibility, expose main functions from
``setuptools.config.setupcfg``
"""

from .setupcfg import parse_configuration as parse_configuration, read_configuration as read_configuration

__all__ = ("parse_configuration", "read_configuration")
