"""
AMQP Specification
==================
This module implements the constants and classes that comprise AMQP protocol
level constructs. It should rarely be directly referenced outside of Pika's
own internal use.
.. note:: Auto-generated code by codegen.py, do not edit directly. Pull
requests to this file without accompanying ``utils/codegen.py`` changes will be
rejected.
"""

import builtins
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import datetime
from decimal import Decimal
from typing import ClassVar, Final, Literal
from typing_extensions import Self, TypeAlias

from pika.amqp_object import Class, Method, Properties
from pika.delivery_mode import DeliveryMode

# Ouch. Since str = bytes at runtime, we need a type alias for "str".
_str: TypeAlias = builtins.str  # noqa: Y042
_Value: TypeAlias = _str | bytes | bool | int | Decimal | datetime | _ArgumentMapping | list[_Value] | None
_ArgumentMapping: TypeAlias = Mapping[_str, _Value]
str = builtins.bytes

PROTOCOL_VERSION: Final[tuple[int, int, int]]
PORT: Final[int]
ACCESS_REFUSED: Final[int]
CHANNEL_ERROR: Final[int]
COMMAND_INVALID: Final[int]
CONNECTION_FORCED: Final[int]
CONTENT_TOO_LARGE: Final[int]
FRAME_BODY: Final[int]
FRAME_END: Final[int]
FRAME_END_SIZE: Final[int]
FRAME_ERROR: Final[int]
FRAME_HEADER: Final[int]
FRAME_HEADER_SIZE: Final[int]
FRAME_HEARTBEAT: Final[int]
FRAME_MAX_SIZE: Final[int]
FRAME_METHOD: Final[int]
FRAME_MIN_SIZE: Final[int]
INTERNAL_ERROR: Final[int]
INVALID_PATH: Final[int]
NOT_ALLOWED: Final[int]
NOT_FOUND: Final[int]
NOT_IMPLEMENTED: Final[int]
NO_CONSUMERS: Final[int]
NO_ROUTE: Final[int]
PERSISTENT_DELIVERY_MODE: Final[int]
PRECONDITION_FAILED: Final[int]
REPLY_SUCCESS: Final[int]
RESOURCE_ERROR: Final[int]
RESOURCE_LOCKED: Final[int]
SYNTAX_ERROR: Final[int]
TRANSIENT_DELIVERY_MODE: Final[int]
UNEXPECTED_FRAME: Final[int]

class Connection(Class):
    INDEX: ClassVar[int]

    class Start(Method):
        INDEX: ClassVar[int]
        version_major: int
        version_minor: int
        server_properties: _ArgumentMapping | None
        mechanisms: _str
        locales: _str
        def __init__(
            self,
            version_major: int = 0,
            version_minor: int = 9,
            server_properties: _ArgumentMapping | None = None,
            mechanisms: _str = "PLAIN",
            locales: _str = "en_US",
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class StartOk(Method):
        INDEX: ClassVar[int]
        client_properties: _ArgumentMapping | None
        mechanism: _str
        response: _str | None
        locale: _str
        def __init__(
            self,
            client_properties: _ArgumentMapping | None = None,
            mechanism: _str = "PLAIN",
            response: _str | None = None,
            locale: _str = "en_US",
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Secure(Method):
        INDEX: ClassVar[int]
        challenge: _str | None
        def __init__(self, challenge: _str | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class SecureOk(Method):
        INDEX: ClassVar[int]
        response: _str
        def __init__(self, response: _str | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Tune(Method):
        INDEX: ClassVar[int]
        channel_max: int
        frame_max: int
        heartbeat: int
        def __init__(self, channel_max: int = 0, frame_max: int = 0, heartbeat: int = 0) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class TuneOk(Method):
        INDEX: ClassVar[int]
        channel_max: int
        frame_max: int
        heartbeat: int
        def __init__(self, channel_max: int = 0, frame_max: int = 0, heartbeat: int = 0) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Open(Method):
        INDEX: ClassVar[int]
        virtual_host: _str
        capabilities: _str
        insist: bool
        def __init__(self, virtual_host: _str = "/", capabilities: _str = "", insist: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class OpenOk(Method):
        INDEX: ClassVar[int]
        known_hosts: _str
        def __init__(self, known_hosts: _str = "") -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Close(Method):
        INDEX: ClassVar[int]
        reply_code: Incomplete
        reply_text: Incomplete
        class_id: Incomplete
        method_id: Incomplete
        def __init__(
            self,
            reply_code: Incomplete | None = None,
            reply_text: _str = "",
            class_id: Incomplete | None = None,
            method_id: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class CloseOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Blocked(Method):
        INDEX: ClassVar[int]
        reason: Incomplete
        def __init__(self, reason: _str = "") -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Unblocked(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class UpdateSecret(Method):
        INDEX: ClassVar[int]
        new_secret: Incomplete
        reason: Incomplete
        mechanisms: _str
        def __init__(self, new_secret, reason) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class UpdateSecretOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Channel(Class):
    INDEX: ClassVar[int]

    class Open(Method):
        INDEX: ClassVar[int]
        out_of_band: _str
        def __init__(self, out_of_band: _str = "") -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class OpenOk(Method):
        INDEX: ClassVar[int]
        channel_id: _str
        def __init__(self, channel_id: _str = "") -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Flow(Method):
        INDEX: ClassVar[int]
        active: bool | None
        def __init__(self, active: bool | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class FlowOk(Method):
        INDEX: ClassVar[int]
        active: bool | None
        def __init__(self, active: bool | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Close(Method):
        INDEX: ClassVar[int]
        reply_code: Incomplete
        reply_text: Incomplete
        class_id: Incomplete
        method_id: Incomplete
        def __init__(
            self,
            reply_code: Incomplete | None = None,
            reply_text: _str = "",
            class_id: Incomplete | None = None,
            method_id: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class CloseOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Access(Class):
    INDEX: ClassVar[int]

    class Request(Method):
        INDEX: ClassVar[int]
        realm: _str
        exclusive: bool
        passive: bool
        active: bool
        write: bool
        read: bool
        def __init__(
            self,
            realm: _str = "/data",
            exclusive: bool = False,
            passive: bool = True,
            active: bool = True,
            write: bool = True,
            read: bool = True,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class RequestOk(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        def __init__(self, ticket: int = 1) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Exchange(Class):
    INDEX: ClassVar[int]

    class Declare(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        exchange: Incomplete
        type: Incomplete
        passive: bool
        durable: bool
        auto_delete: bool
        internal: bool
        nowait: bool
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = 0,
            exchange: Incomplete | None = None,
            type=...,
            passive: bool = False,
            durable: bool = False,
            auto_delete: bool = False,
            internal: bool = False,
            nowait: bool = False,
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class DeclareOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Delete(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        exchange: Incomplete
        if_unused: Incomplete
        nowait: bool
        def __init__(
            self, ticket: int = 0, exchange: Incomplete | None = None, if_unused: bool = False, nowait: bool = False
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class DeleteOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Bind(Method):
        INDEX: ClassVar[int]
        ticket: int
        destination: Incomplete | None
        source: Incomplete | None
        routing_key: _str
        nowait: bool
        arguments: Incomplete | None
        def __init__(
            self,
            ticket: int = 0,
            destination: Incomplete | None = None,
            source: Incomplete | None = None,
            routing_key: _str = "",
            nowait: bool = False,
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class BindOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Unbind(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        destination: Incomplete
        source: Incomplete
        routing_key: Incomplete
        nowait: bool
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = 0,
            destination: Incomplete | None = None,
            source: Incomplete | None = None,
            routing_key: _str = "",
            nowait: bool = False,
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class UnbindOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Queue(Class):
    INDEX: ClassVar[int]

    class Declare(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        passive: bool
        durable: bool
        exclusive: bool
        auto_delete: bool
        nowait: bool
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = 0,
            queue: _str = "",
            passive: bool = False,
            durable: bool = False,
            exclusive: bool = False,
            auto_delete: bool = False,
            nowait: bool = False,
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class DeclareOk(Method):
        INDEX: ClassVar[int]
        queue: _str
        message_count: int
        consumer_count: int
        def __init__(self, queue: _str, message_count: int, consumer_count: int) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Bind(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        nowait: bool
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = 0,
            queue: _str = "",
            exchange: Incomplete | None = None,
            routing_key: _str = "",
            nowait: bool = False,
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class BindOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Purge(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        nowait: bool
        def __init__(self, ticket: int = 0, queue: _str = "", nowait: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class PurgeOk(Method):
        INDEX: ClassVar[int]
        message_count: Incomplete
        def __init__(self, message_count: Incomplete | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Delete(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        if_unused: Incomplete
        if_empty: Incomplete
        nowait: bool
        def __init__(
            self, ticket: int = 0, queue: _str = "", if_unused: bool = False, if_empty: bool = False, nowait: bool = False
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class DeleteOk(Method):
        INDEX: ClassVar[int]
        message_count: Incomplete
        def __init__(self, message_count: Incomplete | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Unbind(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = 0,
            queue: _str = "",
            exchange: Incomplete | None = None,
            routing_key: _str = "",
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class UnbindOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Basic(Class):
    INDEX: ClassVar[int]

    class Qos(Method):
        INDEX: ClassVar[int]
        prefetch_size: Incomplete
        prefetch_count: Incomplete
        global_qos: Incomplete
        def __init__(self, prefetch_size: int = 0, prefetch_count: int = 0, global_qos: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class QosOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Consume(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        consumer_tag: Incomplete
        no_local: bool
        no_ack: bool
        exclusive: bool
        nowait: bool
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = 0,
            queue: _str = "",
            consumer_tag: _str = "",
            no_local: bool = False,
            no_ack: bool = False,
            exclusive: bool = False,
            nowait: bool = False,
            arguments: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class ConsumeOk(Method):
        INDEX: ClassVar[int]
        consumer_tag: Incomplete
        def __init__(self, consumer_tag: Incomplete | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Cancel(Method):
        INDEX: ClassVar[int]
        consumer_tag: Incomplete
        nowait: bool
        def __init__(self, consumer_tag: Incomplete | None = None, nowait: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class CancelOk(Method):
        INDEX: ClassVar[int]
        consumer_tag: Incomplete
        def __init__(self, consumer_tag: Incomplete | None = None) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Publish(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        mandatory: Incomplete
        immediate: Incomplete
        def __init__(
            self, ticket: int = 0, exchange: _str = "", routing_key: _str = "", mandatory: bool = False, immediate: bool = False
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Return(Method):
        INDEX: ClassVar[int]
        reply_code: Incomplete
        reply_text: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        def __init__(
            self,
            reply_code: Incomplete | None = None,
            reply_text: _str = "",
            exchange: Incomplete | None = None,
            routing_key: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Deliver(Method):
        INDEX: ClassVar[int]
        consumer_tag: Incomplete
        delivery_tag: Incomplete
        redelivered: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        def __init__(
            self,
            consumer_tag: Incomplete | None = None,
            delivery_tag: Incomplete | None = None,
            redelivered: bool = False,
            exchange: Incomplete | None = None,
            routing_key: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Get(Method):
        INDEX: ClassVar[int]
        ticket: Incomplete
        queue: Incomplete
        no_ack: bool
        def __init__(self, ticket: int = 0, queue: _str = "", no_ack: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class GetOk(Method):
        INDEX: ClassVar[int]
        delivery_tag: Incomplete
        redelivered: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        message_count: Incomplete
        def __init__(
            self,
            delivery_tag: Incomplete | None = None,
            redelivered: bool = False,
            exchange: Incomplete | None = None,
            routing_key: Incomplete | None = None,
            message_count: Incomplete | None = None,
        ) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class GetEmpty(Method):
        INDEX: ClassVar[int]
        cluster_id: Incomplete
        def __init__(self, cluster_id: _str = "") -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Ack(Method):
        INDEX: ClassVar[int]
        delivery_tag: Incomplete
        multiple: Incomplete
        def __init__(self, delivery_tag: int = 0, multiple: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Reject(Method):
        INDEX: ClassVar[int]
        delivery_tag: Incomplete
        requeue: bool
        def __init__(self, delivery_tag: Incomplete | None = None, requeue: bool = True) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class RecoverAsync(Method):
        INDEX: ClassVar[int]
        requeue: bool
        def __init__(self, requeue: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Recover(Method):
        INDEX: ClassVar[int]
        requeue: bool
        def __init__(self, requeue: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class RecoverOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Nack(Method):
        INDEX: ClassVar[int]
        delivery_tag: Incomplete
        multiple: Incomplete
        requeue: bool
        def __init__(self, delivery_tag: int = 0, multiple: bool = False, requeue: bool = True) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Tx(Class):
    INDEX: ClassVar[int]

    class Select(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class SelectOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Commit(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class CommitOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class Rollback(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class RollbackOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class Confirm(Class):
    INDEX: ClassVar[int]

    class Select(Method):
        INDEX: ClassVar[int]
        nowait: bool
        def __init__(self, nowait: bool = False) -> None: ...
        @property
        def synchronous(self) -> Literal[True]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

    class SelectOk(Method):
        INDEX: ClassVar[int]
        def __init__(self) -> None: ...
        @property
        def synchronous(self) -> Literal[False]: ...
        def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
        def encode(self) -> list[bytes]: ...

class BasicProperties(Properties):
    CLASS: ClassVar[type[Basic]]
    INDEX: ClassVar[int]
    FLAG_CONTENT_TYPE: ClassVar[int]
    FLAG_CONTENT_ENCODING: ClassVar[int]
    FLAG_HEADERS: ClassVar[int]
    FLAG_DELIVERY_MODE: ClassVar[int]
    FLAG_PRIORITY: ClassVar[int]
    FLAG_CORRELATION_ID: ClassVar[int]
    FLAG_REPLY_TO: ClassVar[int]
    FLAG_EXPIRATION: ClassVar[int]
    FLAG_MESSAGE_ID: ClassVar[int]
    FLAG_TIMESTAMP: ClassVar[int]
    FLAG_TYPE: ClassVar[int]
    FLAG_USER_ID: ClassVar[int]
    FLAG_APP_ID: ClassVar[int]
    FLAG_CLUSTER_ID: ClassVar[int]
    content_type: _str | None
    content_encoding: _str | None
    headers: _ArgumentMapping | None
    delivery_mode: Literal[1, 2] | None
    priority: Incomplete
    correlation_id: _str | None
    reply_to: _str | None
    expiration: _str | None
    message_id: _str | None
    timestamp: Incomplete
    type: _str | None
    user_id: _str | None
    app_id: _str | None
    cluster_id: _str | None
    def __init__(
        self,
        content_type: _str | None = None,
        content_encoding: _str | None = None,
        headers: _ArgumentMapping | None = None,
        delivery_mode: DeliveryMode | Literal[1, 2] | None = None,
        priority: Incomplete | None = None,
        correlation_id: _str | None = None,
        reply_to: _str | None = None,
        expiration: _str | None = None,
        message_id: _str | None = None,
        timestamp: Incomplete | None = None,
        type: _str | None = None,
        user_id: _str | None = None,
        app_id: _str | None = None,
        cluster_id: _str | None = None,
    ) -> None: ...
    def decode(self, encoded: bytes, offset: int = 0) -> Self: ...
    def encode(self) -> list[bytes]: ...

methods: Final[dict[int, type[Method]]]
props: Final[dict[int, type[BasicProperties]]]

def has_content(methodNumber: int) -> bool: ...
