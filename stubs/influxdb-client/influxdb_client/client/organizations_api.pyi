"""
An organization is a workspace for a group of users.

All dashboards, tasks, buckets, members, etc., belong to an organization.
"""

from influxdb_client import Organization

class OrganizationsApi:
    """Implementation for '/api/v2/orgs' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def me(self):
        """Return the current authenticated user."""
        ...
    def find_organization(self, org_id):
        """Retrieve an organization."""
        ...
    def find_organizations(self, **kwargs):
        """
        List all organizations.

        :key int offset: Offset for pagination
        :key int limit: Limit for pagination
        :key bool descending:
        :key str org: Filter organizations to a specific organization name.
        :key str org_id: Filter organizations to a specific organization ID.
        :key str user_id: Filter organizations to a specific user ID.
        """
        ...
    def create_organization(self, name: str | None = None, organization: Organization | None = None) -> Organization:
        """Create an organization."""
        ...
    def update_organization(self, organization: Organization) -> Organization:
        """
        Update an organization.

        :param organization: Organization update to apply (required)
        :return: Organization
        """
        ...
    def delete_organization(self, org_id: str):
        """Delete an organization."""
        ...
