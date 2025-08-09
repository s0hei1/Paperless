from enum import Enum
from dataclasses import dataclass

from more_itertools import first


@dataclass(frozen=True)
class UnitOfMeasure:
    id: int
    name: str
    alias_name: str


class UOMs(Enum):
    QTY = UnitOfMeasure(id=1, name="Qty", alias_name="عددی")
    METER = UnitOfMeasure(id=1, name="Meter", alias_name="متر")
    LITER = UnitOfMeasure(id=1, name="Liter", alias_name="لیتر")
    COUPLE = UnitOfMeasure(id=1, name="Couple", alias_name="جفت")

    @classmethod
    def get_uom_by_id(cls, id: int) -> "UOMs":
        return first([i for i in cls if i.value.id == id])
