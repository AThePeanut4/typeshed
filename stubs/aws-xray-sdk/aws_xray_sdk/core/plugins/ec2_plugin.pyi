from _typeshed import Incomplete
from typing import Any

log: Any
SERVICE_NAME: str
ORIGIN: str
IMDS_URL: str

def initialize() -> None:
    """
    Try to get EC2 instance-id and AZ if running on EC2
    by querying http://169.254.169.254/latest/meta-data/.
    If not continue.
    """
    ...
def get_token():
    """
    Get the session token for IMDSv2 endpoint valid for 60 seconds
    by specifying the X-aws-ec2-metadata-token-ttl-seconds header.
    """
    ...
def get_metadata(token: Incomplete | None = None): ...
def parse_metadata_json(json_str): ...
def do_request(url, headers: Incomplete | None = None, method: str = "GET"): ...
