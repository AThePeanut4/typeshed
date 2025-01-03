"""Module containing the application logic for Flake8."""

from _typeshed import Incomplete
from collections.abc import Sequence
from logging import Logger

LOG: Logger

class Application:
    """Abstract our application into a class."""
    start_time: Incomplete
    end_time: Incomplete
    plugins: Incomplete
    formatter: Incomplete
    guide: Incomplete
    file_checker_manager: Incomplete
    options: Incomplete
    result_count: int
    total_result_count: int
    catastrophic_failure: bool
    def __init__(self) -> None:
        """Initialize our application."""
        ...
    def exit_code(self) -> int:
        """Return the program exit code."""
        ...
    def make_formatter(self) -> None:
        """Initialize a formatter based on the parsed options."""
        ...
    def make_guide(self) -> None:
        """Initialize our StyleGuide."""
        ...
    def make_file_checker_manager(self, argv: Sequence[str]) -> None:
        """Initialize our FileChecker Manager."""
        ...
    def run_checks(self) -> None:
        """
        Run the actual checks with the FileChecker Manager.

        This method encapsulates the logic to make a
        :class:`~flake8.checker.Manger` instance run the checks it is
        managing.
        """
        ...
    def report_benchmarks(self) -> None:
        """Aggregate, calculate, and report benchmarks for this run."""
        ...
    def report_errors(self) -> None:
        """
        Report all the errors found by flake8 3.0.

        This also updates the :attr:`result_count` attribute with the total
        number of errors, warnings, and other messages found.
        """
        ...
    def report_statistics(self) -> None:
        """Aggregate and report statistics from this run."""
        ...
    def initialize(self, argv: Sequence[str]) -> None:
        """
        Initialize the application to be run.

        This finds the plugins, registers their options, and parses the
        command-line arguments.
        """
        ...
    def report(self) -> None:
        """Report errors, statistics, and benchmarks."""
        ...
    def run(self, argv: Sequence[str]) -> None:
        """
        Run our application.

        This method will also handle KeyboardInterrupt exceptions for the
        entirety of the flake8 application. If it sees a KeyboardInterrupt it
        will forcibly clean up the :class:`~flake8.checker.Manager`.
        """
        ...
