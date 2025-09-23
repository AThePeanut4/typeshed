from typing import Any

from .._types import _WSGIAppType

def get_wsgi_app(config_uri: str, name: str | None = None, defaults: dict[str, Any] | None = None) -> _WSGIAppType: ...
def has_logging_config(config_file: str) -> bool: ...
def serve(app: _WSGIAppType, global_conf: dict[str, Any], **local_conf: Any) -> None:
    """
    A Paste Deployment server runner.

    Example configuration:

        [server:main]
        use = egg:gunicorn#main
        host = 127.0.0.1
        port = 5000
    """
    ...
