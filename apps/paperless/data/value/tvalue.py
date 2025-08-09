from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class TValue(Generic[T]):
    value: T

    def __init__(self, value: T):
        self.value = value

    def __repr__(self) -> T:
        return self.value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other: "TValue[T]"):
        return self.value == other.value

    def unwrap(self) -> T:
        return self.value
