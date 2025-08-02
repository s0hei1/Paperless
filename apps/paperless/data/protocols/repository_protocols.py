from collections.abc import Sequence
from typing import Protocol,TypeVar,Generic

T = TypeVar("T")

class CreateProtocol(Protocol[T]):
    async def create(self, model : T) -> T:
        ...

class ReadOneProtocol(Protocol[T]):
    async def read_one(self, id) -> T:
        ...

class ReadManyProtocol(Protocol[T]):
    async def read_many(self) -> Sequence[T]:
        ...

class UpdateProtocol(Protocol[T]):
    async def update(self, *args, **kwargs) -> T:
        ...

class DeleteProtocol(Protocol[T]):
    async def delete(self, id) -> T:
        ...

