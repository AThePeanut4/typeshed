""""""

from _typeshed import Incomplete

from .asynchronous import AsyncStrategy
from .mockBase import MockBaseStrategy

class MockAsyncStrategy(MockBaseStrategy, AsyncStrategy):
    """
    This strategy create a mock LDAP server, with asynchronous access
    It can be useful to test LDAP without accessing a real Server
    """
    def __init__(self, ldap_connection) -> None: ...
    def post_send_search(self, payload): ...
    bound: Incomplete
    def post_send_single_response(self, payload): ...
    def get_response(self, message_id, timeout=None, get_request: bool = False): ...
