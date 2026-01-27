from typing import ClassVar

from gunicorn.http.parser import Parser
from gunicorn.uwsgi.message import UWSGIRequest

class UWSGIParser(Parser):
    """Parser for uWSGI protocol requests."""
    mesg_class: ClassVar[type[UWSGIRequest]]  # type: ignore[assignment]
