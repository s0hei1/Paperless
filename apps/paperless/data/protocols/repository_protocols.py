from collections.abc import Sequence
from typing import Protocol, TypeVar, Generic, runtime_checkable

T = TypeVar("T")

@runtime_checkable
class CreateProtocol(Protocol[T]):
    async def create(self, model : T) -> T:
        ...
@runtime_checkable
class ReadOneProtocol(Protocol[T]):
    async def read_one(self, id) -> T:
        ...
@runtime_checkable
class ReadManyProtocol(Protocol[T]):
    async def read_many(self) -> Sequence[T]:
        ...
@runtime_checkable
class UpdateProtocol(Protocol[T]):
    async def update(self, *args, **kwargs) -> T:
        ...
@runtime_checkable
class DeleteProtocol(Protocol[T]):
    async def delete(self, id) -> T:
        ...
