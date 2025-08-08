from typing import ClassVar

from pyee.asyncio import AsyncIOEventEmitter

event_emitter = AsyncIOEventEmitter()


class MetaEvent(type):
    def __repr__(cls) -> str:
        return cls.__name__

class BaseEvent(metaclass=MetaEvent):
    def __str__(cls):
        return cls.__name__

class OnApproveGoodsExitEvent(BaseEvent): pass
class OnAddGoodsExitDoc(BaseEvent): pass
