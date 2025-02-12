"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class MeasurementSchema:
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
        id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        bucket_id: Incomplete | None = None,
        name: Incomplete | None = None,
        columns: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
    ) -> None:
        """MeasurementSchema - a model defined in OpenAPI."""
        ...
    @property
    def id(self):
        """
        Get the id of this MeasurementSchema.

        :return: The id of this MeasurementSchema.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this MeasurementSchema.

        :return: The id of this MeasurementSchema.
        :rtype: str
        """
        ...
    @property
    def org_id(self):
        """
        Get the org_id of this MeasurementSchema.

        The ID of the organization.

        :return: The org_id of this MeasurementSchema.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id) -> None:
        """
        Get the org_id of this MeasurementSchema.

        The ID of the organization.

        :return: The org_id of this MeasurementSchema.
        :rtype: str
        """
        ...
    @property
    def bucket_id(self):
        """
        Get the bucket_id of this MeasurementSchema.

        The ID of the bucket that the measurement schema is associated with.

        :return: The bucket_id of this MeasurementSchema.
        :rtype: str
        """
        ...
    @bucket_id.setter
    def bucket_id(self, bucket_id) -> None:
        """
        Get the bucket_id of this MeasurementSchema.

        The ID of the bucket that the measurement schema is associated with.

        :return: The bucket_id of this MeasurementSchema.
        :rtype: str
        """
        ...
    @property
    def name(self):
        """
        Get the name of this MeasurementSchema.

        :return: The name of this MeasurementSchema.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this MeasurementSchema.

        :return: The name of this MeasurementSchema.
        :rtype: str
        """
        ...
    @property
    def columns(self):
        """
        Get the columns of this MeasurementSchema.

        Ordered collection of column definitions.

        :return: The columns of this MeasurementSchema.
        :rtype: list[MeasurementSchemaColumn]
        """
        ...
    @columns.setter
    def columns(self, columns) -> None:
        """
        Get the columns of this MeasurementSchema.

        Ordered collection of column definitions.

        :return: The columns of this MeasurementSchema.
        :rtype: list[MeasurementSchemaColumn]
        """
        ...
    @property
    def created_at(self):
        """
        Get the created_at of this MeasurementSchema.

        :return: The created_at of this MeasurementSchema.
        :rtype: datetime
        """
        ...
    @created_at.setter
    def created_at(self, created_at) -> None:
        """
        Get the created_at of this MeasurementSchema.

        :return: The created_at of this MeasurementSchema.
        :rtype: datetime
        """
        ...
    @property
    def updated_at(self):
        """
        Get the updated_at of this MeasurementSchema.

        :return: The updated_at of this MeasurementSchema.
        :rtype: datetime
        """
        ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None:
        """
        Get the updated_at of this MeasurementSchema.

        :return: The updated_at of this MeasurementSchema.
        :rtype: datetime
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
