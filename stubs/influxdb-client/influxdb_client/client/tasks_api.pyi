"""
Process and analyze your data with tasks in the InfluxDB task engine.

Use tasks (scheduled Flux queries) to input a data stream and then analyze, modify, and act on the data accordingly.
"""

from datetime import datetime

from influxdb_client import LabelResponse, LogEvent, Run, TaskCreateRequest, TaskUpdateRequest
from influxdb_client.domain.task import Task

from ._pages import _PageIterator

class TasksApi:
    """Implementation for '/api/v2/tasks' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def find_task_by_id(self, task_id) -> Task:
        """Retrieve a task."""
        ...
    def find_tasks(
        self, *, name: str = ..., after: str = ..., user: str = ..., org: str = ..., org_id: str = ..., limit: int = ..., **kwargs
    ) -> list[Task]:
        """
        List all tasks up to set limit (max 500).

        :key str name: only returns tasks with the specified name
        :key str after: returns tasks after specified ID
        :key str user: filter tasks to a specific user ID
        :key str org: filter tasks to a specific organization name
        :key str org_id: filter tasks to a specific organization ID
        :key int limit: the number of tasks to return
        :return: Tasks
        """
        ...
    def find_tasks_iter(
        self, *, name: str = ..., after: str | None = None, user: str = ..., org: str = ..., org_id: str = ..., limit: int = ...
    ) -> _PageIterator[Task]:
        """
        Iterate over all tasks with pagination.

        :key str name: only returns tasks with the specified name
        :key str after: returns tasks after specified ID
        :key str user: filter tasks to a specific user ID
        :key str org: filter tasks to a specific organization name
        :key str org_id: filter tasks to a specific organization ID
        :key int limit: the number of tasks in one page
        :return: Tasks iterator
        """
        ...
    def create_task(self, task: Task | None = None, task_create_request: TaskCreateRequest | None = None) -> Task:
        """Create a new task."""
        ...
    def create_task_every(self, name, flux, every, organization) -> Task:
        """Create a new task with every repetition schedule."""
        ...
    def create_task_cron(self, name: str, flux: str, cron: str, org_id: str) -> Task:
        """Create a new task with cron repetition schedule."""
        ...
    def delete_task(self, task_id: str):
        """Delete a task."""
        ...
    def update_task(self, task: Task) -> Task:
        """Update a task."""
        ...
    def update_task_request(self, task_id, task_update_request: TaskUpdateRequest) -> Task:
        """Update a task."""
        ...
    def clone_task(self, task: Task) -> Task:
        """Clone a task."""
        ...
    def get_labels(self, task_id):
        """List all labels for a task."""
        ...
    def add_label(self, label_id: str, task_id: str) -> LabelResponse:
        """Add a label to a task."""
        ...
    def delete_label(self, label_id: str, task_id: str):
        """Delete a label from a task."""
        ...
    def get_members(self, task_id: str):
        """List all task members."""
        ...
    def add_member(self, member_id, task_id):
        """Add a member to a task."""
        ...
    def delete_member(self, member_id, task_id):
        """Remove a member from a task."""
        ...
    def get_owners(self, task_id):
        """List all owners of a task."""
        ...
    def add_owner(self, owner_id, task_id):
        """Add an owner to a task."""
        ...
    def delete_owner(self, owner_id, task_id):
        """Remove an owner from a task."""
        ...
    def get_runs(self, task_id, **kwargs) -> list[Run]:
        """
        Retrieve list of run records for a task.

        :param task_id: task id
        :key str after: returns runs after specified ID
        :key int limit: the number of runs to return
        :key datetime after_time: filter runs to those scheduled after this time, RFC3339
        :key datetime before_time: filter runs to those scheduled before this time, RFC3339
        """
        ...
    def get_run(self, task_id: str, run_id: str) -> Run:
        """
        Get run record for specific task and run id.

        :param task_id: task id
        :param run_id: run id
        :return: Run for specified task and run id
        """
        ...
    def get_run_logs(self, task_id: str, run_id: str) -> list[LogEvent]:
        """Retrieve all logs for a run."""
        ...
    def run_manually(self, task_id: str, scheduled_for: datetime | None = None):
        """
        Manually start a run of the task now overriding the current schedule.

        :param task_id:
        :param scheduled_for: planned execution
        """
        ...
    def retry_run(self, task_id: str, run_id: str):
        """
        Retry a task run.

        :param task_id: task id
        :param run_id: run id
        """
        ...
    def cancel_run(self, task_id: str, run_id: str):
        """
        Cancel a currently running run.

        :param task_id:
        :param run_id:
        """
        ...
    def get_logs(self, task_id: str) -> list[LogEvent]:
        """
        Retrieve all logs for a task.

        :param task_id: task id
        """
        ...
    def find_tasks_by_user(self, task_user_id):
        """List all tasks by user."""
        ...
