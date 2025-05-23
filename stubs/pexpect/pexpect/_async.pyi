"""
Facade that provides coroutines implementation pertinent to running Py version.

Python 3.5 introduced the async def/await syntax keyword.
With later versions coroutines and methods to get the running asyncio loop are
being deprecated, not supported anymore.

For Python versions later than 3.6, coroutines and objects that are defined via
``async def``/``await`` keywords are imported.

Here the code is just imported, to provide the same interface to older code.
"""

import asyncio
from typing import AnyStr, Generic

from .expect import Expecter

async def expect_async(expecter: Expecter[AnyStr], timeout: float | None = None) -> int: ...
async def repl_run_command_async(repl, cmdlines, timeout: float | None = -1): ...

class PatternWaiter(asyncio.Protocol, Generic[AnyStr]):
    transport: asyncio.ReadTransport | None
    expecter: Expecter[AnyStr]
    fut: asyncio.Future[int]
    def set_expecter(self, expecter: Expecter[AnyStr]) -> None: ...
    def found(self, result: int) -> None: ...
    def error(self, exc: BaseException | type[BaseException]) -> None: ...
    def connection_made(self, transport: asyncio.BaseTransport) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def eof_received(self) -> None: ...
    def connection_lost(self, exc: BaseException | type[BaseException] | None) -> None: ...
