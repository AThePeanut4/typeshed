"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class NotificationRuleBase:
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
        latest_completed: Incomplete | None = None,
        last_run_status: Incomplete | None = None,
        last_run_error: Incomplete | None = None,
        id: Incomplete | None = None,
        endpoint_id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        task_id: Incomplete | None = None,
        owner_id: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        status: Incomplete | None = None,
        name: Incomplete | None = None,
        sleep_until: Incomplete | None = None,
        every: Incomplete | None = None,
        offset: Incomplete | None = None,
        runbook_link: Incomplete | None = None,
        limit_every: Incomplete | None = None,
        limit: Incomplete | None = None,
        tag_rules: Incomplete | None = None,
        description: Incomplete | None = None,
        status_rules: Incomplete | None = None,
        labels: Incomplete | None = None,
        links: Incomplete | None = None,
    ) -> None:
        """NotificationRuleBase - a model defined in OpenAPI."""
        ...
    @property
    def latest_completed(self):
        """
        Get the latest_completed of this NotificationRuleBase.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)) of the latest scheduled and completed run.

        :return: The latest_completed of this NotificationRuleBase.
        :rtype: datetime
        """
        ...
    @latest_completed.setter
    def latest_completed(self, latest_completed) -> None:
        """
        Get the latest_completed of this NotificationRuleBase.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)) of the latest scheduled and completed run.

        :return: The latest_completed of this NotificationRuleBase.
        :rtype: datetime
        """
        ...
    @property
    def last_run_status(self):
        """
        Get the last_run_status of this NotificationRuleBase.

        :return: The last_run_status of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @last_run_status.setter
    def last_run_status(self, last_run_status) -> None:
        """
        Get the last_run_status of this NotificationRuleBase.

        :return: The last_run_status of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def last_run_error(self):
        """
        Get the last_run_error of this NotificationRuleBase.

        :return: The last_run_error of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @last_run_error.setter
    def last_run_error(self, last_run_error) -> None:
        """
        Get the last_run_error of this NotificationRuleBase.

        :return: The last_run_error of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def id(self):
        """
        Get the id of this NotificationRuleBase.

        :return: The id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this NotificationRuleBase.

        :return: The id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def endpoint_id(self):
        """
        Get the endpoint_id of this NotificationRuleBase.

        :return: The endpoint_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @endpoint_id.setter
    def endpoint_id(self, endpoint_id) -> None:
        """
        Get the endpoint_id of this NotificationRuleBase.

        :return: The endpoint_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def org_id(self):
        """
        Get the org_id of this NotificationRuleBase.

        The ID of the organization that owns this notification rule.

        :return: The org_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id) -> None:
        """
        Get the org_id of this NotificationRuleBase.

        The ID of the organization that owns this notification rule.

        :return: The org_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def task_id(self):
        """
        Get the task_id of this NotificationRuleBase.

        The ID of the task associated with this notification rule.

        :return: The task_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @task_id.setter
    def task_id(self, task_id) -> None:
        """
        Get the task_id of this NotificationRuleBase.

        The ID of the task associated with this notification rule.

        :return: The task_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def owner_id(self):
        """
        Get the owner_id of this NotificationRuleBase.

        The ID of creator used to create this notification rule.

        :return: The owner_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @owner_id.setter
    def owner_id(self, owner_id) -> None:
        """
        Get the owner_id of this NotificationRuleBase.

        The ID of creator used to create this notification rule.

        :return: The owner_id of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def created_at(self):
        """
        Get the created_at of this NotificationRuleBase.

        :return: The created_at of this NotificationRuleBase.
        :rtype: datetime
        """
        ...
    @created_at.setter
    def created_at(self, created_at) -> None:
        """
        Get the created_at of this NotificationRuleBase.

        :return: The created_at of this NotificationRuleBase.
        :rtype: datetime
        """
        ...
    @property
    def updated_at(self):
        """
        Get the updated_at of this NotificationRuleBase.

        :return: The updated_at of this NotificationRuleBase.
        :rtype: datetime
        """
        ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None:
        """
        Get the updated_at of this NotificationRuleBase.

        :return: The updated_at of this NotificationRuleBase.
        :rtype: datetime
        """
        ...
    @property
    def status(self):
        """
        Get the status of this NotificationRuleBase.

        :return: The status of this NotificationRuleBase.
        :rtype: TaskStatusType
        """
        ...
    @status.setter
    def status(self, status) -> None:
        """
        Get the status of this NotificationRuleBase.

        :return: The status of this NotificationRuleBase.
        :rtype: TaskStatusType
        """
        ...
    @property
    def name(self):
        """
        Get the name of this NotificationRuleBase.

        Human-readable name describing the notification rule.

        :return: The name of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this NotificationRuleBase.

        Human-readable name describing the notification rule.

        :return: The name of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def sleep_until(self):
        """
        Get the sleep_until of this NotificationRuleBase.

        :return: The sleep_until of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @sleep_until.setter
    def sleep_until(self, sleep_until) -> None:
        """
        Get the sleep_until of this NotificationRuleBase.

        :return: The sleep_until of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def every(self):
        """
        Get the every of this NotificationRuleBase.

        The notification repetition interval.

        :return: The every of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @every.setter
    def every(self, every) -> None:
        """
        Get the every of this NotificationRuleBase.

        The notification repetition interval.

        :return: The every of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def offset(self):
        """
        Get the offset of this NotificationRuleBase.

        Duration to delay after the schedule, before executing check.

        :return: The offset of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @offset.setter
    def offset(self, offset) -> None:
        """
        Get the offset of this NotificationRuleBase.

        Duration to delay after the schedule, before executing check.

        :return: The offset of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def runbook_link(self):
        """
        Get the runbook_link of this NotificationRuleBase.

        :return: The runbook_link of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @runbook_link.setter
    def runbook_link(self, runbook_link) -> None:
        """
        Get the runbook_link of this NotificationRuleBase.

        :return: The runbook_link of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def limit_every(self):
        """
        Get the limit_every of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limit cannot be empty.

        :return: The limit_every of this NotificationRuleBase.
        :rtype: int
        """
        ...
    @limit_every.setter
    def limit_every(self, limit_every) -> None:
        """
        Get the limit_every of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limit cannot be empty.

        :return: The limit_every of this NotificationRuleBase.
        :rtype: int
        """
        ...
    @property
    def limit(self):
        """
        Get the limit of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limitEvery cannot be empty.

        :return: The limit of this NotificationRuleBase.
        :rtype: int
        """
        ...
    @limit.setter
    def limit(self, limit) -> None:
        """
        Get the limit of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limitEvery cannot be empty.

        :return: The limit of this NotificationRuleBase.
        :rtype: int
        """
        ...
    @property
    def tag_rules(self):
        """
        Get the tag_rules of this NotificationRuleBase.

        List of tag rules the notification rule attempts to match.

        :return: The tag_rules of this NotificationRuleBase.
        :rtype: list[TagRule]
        """
        ...
    @tag_rules.setter
    def tag_rules(self, tag_rules) -> None:
        """
        Get the tag_rules of this NotificationRuleBase.

        List of tag rules the notification rule attempts to match.

        :return: The tag_rules of this NotificationRuleBase.
        :rtype: list[TagRule]
        """
        ...
    @property
    def description(self):
        """
        Get the description of this NotificationRuleBase.

        An optional description of the notification rule.

        :return: The description of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this NotificationRuleBase.

        An optional description of the notification rule.

        :return: The description of this NotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def status_rules(self):
        """
        Get the status_rules of this NotificationRuleBase.

        List of status rules the notification rule attempts to match.

        :return: The status_rules of this NotificationRuleBase.
        :rtype: list[StatusRule]
        """
        ...
    @status_rules.setter
    def status_rules(self, status_rules) -> None:
        """
        Get the status_rules of this NotificationRuleBase.

        List of status rules the notification rule attempts to match.

        :return: The status_rules of this NotificationRuleBase.
        :rtype: list[StatusRule]
        """
        ...
    @property
    def labels(self):
        """
        Get the labels of this NotificationRuleBase.

        :return: The labels of this NotificationRuleBase.
        :rtype: list[Label]
        """
        ...
    @labels.setter
    def labels(self, labels) -> None:
        """
        Get the labels of this NotificationRuleBase.

        :return: The labels of this NotificationRuleBase.
        :rtype: list[Label]
        """
        ...
    @property
    def links(self):
        """
        Get the links of this NotificationRuleBase.

        :return: The links of this NotificationRuleBase.
        :rtype: NotificationRuleBaseLinks
        """
        ...
    @links.setter
    def links(self, links) -> None:
        """
        Get the links of this NotificationRuleBase.

        :return: The links of this NotificationRuleBase.
        :rtype: NotificationRuleBaseLinks
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
