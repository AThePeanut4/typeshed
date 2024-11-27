"""Authorization is about managing the security of your InfluxDB instance."""

from _typeshed import Incomplete

from influxdb_client import Authorization, Organization, User

class AuthorizationsApi:
    """Implementation for '/api/v2/authorizations' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def create_authorization(
        self,
        org_id: Incomplete | None = None,
        permissions: list[Incomplete] | None = None,
        authorization: Authorization | None = None,
    ) -> Authorization:
        """
        Create an authorization.

        :type permissions: list of Permission
        :param org_id: organization id
        :param permissions: list of permissions
        :type authorization: authorization object
        """
        ...
    def find_authorization_by_id(self, auth_id: str) -> Authorization:
        """
        Find authorization by id.

        :param auth_id: authorization id
        :return: Authorization
        """
        ...
    def find_authorizations(self, **kwargs):
        """
        Get a list of all authorizations.

        :key str user_id: filter authorizations belonging to a user id
        :key str user: filter authorizations belonging to a user name
        :key str org_id: filter authorizations belonging to a org id
        :key str org: filter authorizations belonging to a org name
        :return: Authorizations
        """
        ...
    def find_authorizations_by_user(self, user: User):
        """
        Find authorization by User.

        :return: Authorization list
        """
        ...
    def find_authorizations_by_user_id(self, user_id: str):
        """
        Find authorization by user id.

        :return: Authorization list
        """
        ...
    def find_authorizations_by_user_name(self, user_name: str):
        """
        Find authorization by user name.

        :return: Authorization list
        """
        ...
    def find_authorizations_by_org(self, org: Organization):
        """
        Find authorization by user name.

        :return: Authorization list
        """
        ...
    def find_authorizations_by_org_name(self, org_name: str):
        """
        Find authorization by org name.

        :return: Authorization list
        """
        ...
    def find_authorizations_by_org_id(self, org_id: str):
        """
        Find authorization by org id.

        :return: Authorization list
        """
        ...
    def update_authorization(self, auth):
        """
        Update authorization object.

        :param auth:
        :return:
        """
        ...
    def clone_authorization(self, auth) -> Authorization:
        """Clone an authorization."""
        ...
    def delete_authorization(self, auth):
        """Delete a authorization."""
        ...
