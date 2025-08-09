from typing import ClassVar

from pyee.asyncio import AsyncIOEventEmitter
from apps.paperless.events.events import Events
from apps.paperless.events.goods_exit_events import (
    on_approve_goods_exit_event,
    on_create_goods_exit_doc,
)

event_emitter = AsyncIOEventEmitter()

event_emitter.add_listener(Events.OnApproveGoodsExitEvent, on_approve_goods_exit_event)
event_emitter.add_listener(Events.OnCreateGoodsExitDoc, on_create_goods_exit_doc)
