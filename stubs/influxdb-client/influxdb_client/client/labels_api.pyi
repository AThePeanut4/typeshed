"""Labels are a way to add visual metadata to dashboards, tasks, and other items in the InfluxDB UI."""

from influxdb_client import Label

class LabelsApi:
    """Implementation for '/api/v2/labels' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def create_label(self, name: str, org_id: str, properties: dict[str, str] | None = None) -> Label:
        """
        Create a new label.

        :param name: label name
        :param org_id: organization id
        :param properties: optional label properties
        :return: created label
        """
        ...
    def update_label(self, label: Label):
        """
        Update an existing label name and properties.

        :param label: label
        :return: the updated label
        """
        ...
    def delete_label(self, label: str | Label):
        """
        Delete the label.

        :param label: label id or Label
        """
        ...
    def clone_label(self, cloned_name: str, label: Label) -> Label:
        """
        Create the new instance of the label as a copy existing label.

        :param cloned_name: new label name
        :param label: existing label
        :return: clonned Label
        """
        ...
    def find_labels(self, **kwargs) -> list[Label]:
        """
        Get all available labels.

        :key str org_id: The organization ID.

        :return: labels
        """
        ...
    def find_label_by_id(self, label_id: str):
        """
        Retrieve the label by id.

        :param label_id:
        :return: Label
        """
        ...
    def find_label_by_org(self, org_id) -> list[Label]:
        """
        Get the list of all labels for given organization.

        :param org_id: organization id
        :return: list of labels
        """
        ...
