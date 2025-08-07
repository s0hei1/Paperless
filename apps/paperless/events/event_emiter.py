from typing import ClassVar

from pyee.asyncio import AsyncIOEventEmitter

event_emitter = AsyncIOEventEmitter()


class Events:
    on_approve_goods_exit_event : ClassVar[str] = "on_approve_goods_exit_event"

