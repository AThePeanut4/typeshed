"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Routes:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        authorizations: Incomplete | None = None,
        buckets: Incomplete | None = None,
        dashboards: Incomplete | None = None,
        external: Incomplete | None = None,
        variables: Incomplete | None = None,
        me: Incomplete | None = None,
        flags: Incomplete | None = None,
        orgs: Incomplete | None = None,
        query: Incomplete | None = None,
        setup: Incomplete | None = None,
        signin: Incomplete | None = None,
        signout: Incomplete | None = None,
        sources: Incomplete | None = None,
        system: Incomplete | None = None,
        tasks: Incomplete | None = None,
        telegrafs: Incomplete | None = None,
        users: Incomplete | None = None,
        write: Incomplete | None = None,
    ) -> None:
        """Routes - a model defined in OpenAPI."""
        ...
    @property
    def authorizations(self):
        """
        Get the authorizations of this Routes.

        :return: The authorizations of this Routes.
        :rtype: str
        """
        ...
    @authorizations.setter
    def authorizations(self, authorizations) -> None:
        """
        Get the authorizations of this Routes.

        :return: The authorizations of this Routes.
        :rtype: str
        """
        ...
    @property
    def buckets(self):
        """
        Get the buckets of this Routes.

        :return: The buckets of this Routes.
        :rtype: str
        """
        ...
    @buckets.setter
    def buckets(self, buckets) -> None:
        """
        Get the buckets of this Routes.

        :return: The buckets of this Routes.
        :rtype: str
        """
        ...
    @property
    def dashboards(self):
        """
        Get the dashboards of this Routes.

        :return: The dashboards of this Routes.
        :rtype: str
        """
        ...
    @dashboards.setter
    def dashboards(self, dashboards) -> None:
        """
        Get the dashboards of this Routes.

        :return: The dashboards of this Routes.
        :rtype: str
        """
        ...
    @property
    def external(self):
        """
        Get the external of this Routes.

        :return: The external of this Routes.
        :rtype: RoutesExternal
        """
        ...
    @external.setter
    def external(self, external) -> None:
        """
        Get the external of this Routes.

        :return: The external of this Routes.
        :rtype: RoutesExternal
        """
        ...
    @property
    def variables(self):
        """
        Get the variables of this Routes.

        :return: The variables of this Routes.
        :rtype: str
        """
        ...
    @variables.setter
    def variables(self, variables) -> None:
        """
        Get the variables of this Routes.

        :return: The variables of this Routes.
        :rtype: str
        """
        ...
    @property
    def me(self):
        """
        Get the me of this Routes.

        :return: The me of this Routes.
        :rtype: str
        """
        ...
    @me.setter
    def me(self, me) -> None:
        """
        Get the me of this Routes.

        :return: The me of this Routes.
        :rtype: str
        """
        ...
    @property
    def flags(self):
        """
        Get the flags of this Routes.

        :return: The flags of this Routes.
        :rtype: str
        """
        ...
    @flags.setter
    def flags(self, flags) -> None:
        """
        Get the flags of this Routes.

        :return: The flags of this Routes.
        :rtype: str
        """
        ...
    @property
    def orgs(self):
        """
        Get the orgs of this Routes.

        :return: The orgs of this Routes.
        :rtype: str
        """
        ...
    @orgs.setter
    def orgs(self, orgs) -> None:
        """
        Get the orgs of this Routes.

        :return: The orgs of this Routes.
        :rtype: str
        """
        ...
    @property
    def query(self):
        """
        Get the query of this Routes.

        :return: The query of this Routes.
        :rtype: RoutesQuery
        """
        ...
    @query.setter
    def query(self, query) -> None:
        """
        Get the query of this Routes.

        :return: The query of this Routes.
        :rtype: RoutesQuery
        """
        ...
    @property
    def setup(self):
        """
        Get the setup of this Routes.

        :return: The setup of this Routes.
        :rtype: str
        """
        ...
    @setup.setter
    def setup(self, setup) -> None:
        """
        Get the setup of this Routes.

        :return: The setup of this Routes.
        :rtype: str
        """
        ...
    @property
    def signin(self):
        """
        Get the signin of this Routes.

        :return: The signin of this Routes.
        :rtype: str
        """
        ...
    @signin.setter
    def signin(self, signin) -> None:
        """
        Get the signin of this Routes.

        :return: The signin of this Routes.
        :rtype: str
        """
        ...
    @property
    def signout(self):
        """
        Get the signout of this Routes.

        :return: The signout of this Routes.
        :rtype: str
        """
        ...
    @signout.setter
    def signout(self, signout) -> None:
        """
        Get the signout of this Routes.

        :return: The signout of this Routes.
        :rtype: str
        """
        ...
    @property
    def sources(self):
        """
        Get the sources of this Routes.

        :return: The sources of this Routes.
        :rtype: str
        """
        ...
    @sources.setter
    def sources(self, sources) -> None:
        """
        Get the sources of this Routes.

        :return: The sources of this Routes.
        :rtype: str
        """
        ...
    @property
    def system(self):
        """
        Get the system of this Routes.

        :return: The system of this Routes.
        :rtype: RoutesSystem
        """
        ...
    @system.setter
    def system(self, system) -> None:
        """
        Get the system of this Routes.

        :return: The system of this Routes.
        :rtype: RoutesSystem
        """
        ...
    @property
    def tasks(self):
        """
        Get the tasks of this Routes.

        :return: The tasks of this Routes.
        :rtype: str
        """
        ...
    @tasks.setter
    def tasks(self, tasks) -> None:
        """
        Get the tasks of this Routes.

        :return: The tasks of this Routes.
        :rtype: str
        """
        ...
    @property
    def telegrafs(self):
        """
        Get the telegrafs of this Routes.

        :return: The telegrafs of this Routes.
        :rtype: str
        """
        ...
    @telegrafs.setter
    def telegrafs(self, telegrafs) -> None:
        """
        Get the telegrafs of this Routes.

        :return: The telegrafs of this Routes.
        :rtype: str
        """
        ...
    @property
    def users(self):
        """
        Get the users of this Routes.

        :return: The users of this Routes.
        :rtype: str
        """
        ...
    @users.setter
    def users(self, users) -> None:
        """
        Get the users of this Routes.

        :return: The users of this Routes.
        :rtype: str
        """
        ...
    @property
    def write(self):
        """
        Get the write of this Routes.

        :return: The write of this Routes.
        :rtype: str
        """
        ...
    @write.setter
    def write(self, write) -> None:
        """
        Get the write of this Routes.

        :return: The write of this Routes.
        :rtype: str
        """
        ...
    def to_dict(self):
        """Return the model properties as a dict."""
        ...
    def to_str(self):
        """Return the string representation of the model."""
        ...
    def __eq__(self, other):
        """Return true if both objects are equal."""
        ...
    def __ne__(self, other):
        """Return true if both objects are not equal."""
        ...
