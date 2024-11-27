"""
Users are those with access to InfluxDB.

To grant a user permission to access data, add them as a member of an organization
and provide them with an authentication token.
"""

from influxdb_client import User, UserResponse, Users

class UsersApi:
    """Implementation for '/api/v2/users' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def me(self) -> User:
        """Return the current authenticated user."""
        ...
    def create_user(self, name: str) -> User:
        """Create a user."""
        ...
    def update_user(self, user: User) -> UserResponse:
        """
        Update a user.

        :param user: User update to apply (required)
        :return: User
        """
        ...
    def update_password(self, user: str | User | UserResponse, password: str) -> None:
        """
        Update a password.

        :param user: User to update password (required)
        :param password: New password (required)
        :return: None
        """
        ...
    def delete_user(self, user: str | User | UserResponse) -> None:
        """
        Delete a user.

        :param user: user id or User
        :return: None
        """
        ...
    def find_users(self, **kwargs) -> Users:
        """
        List all users.

        :key int offset: The offset for pagination. The number of records to skip.
        :key int limit: Limits the number of records returned. Default is `20`.
        :key str after: The last resource ID from which to seek from (but not including).
                        This is to be used instead of `offset`.
        :key str name: The user name.
        :key str id: The user ID.
        :return: Buckets
        """
        ...
