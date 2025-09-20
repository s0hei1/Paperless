from typing import TypedDict, Protocol, Any, runtime_checkable

@runtime_checkable
class CQProtocol(Protocol):
    async def __call__(self) -> Any : ...

class Header(TypedDict):
    current_user_id : int

class Request:
    header: Header
    CQs : list[CQProtocol]



class Hub:
    pass

