from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class UnitOfMeasure:
    id : int
    name : str
    alias_name : str

class UOMs(Enum):
    QTY = UnitOfMeasure(id = 1, name="Qty", alias_name="عددی")
    METER = UnitOfMeasure(id = 1, name="Meter", alias_name="متر")
    LITER = UnitOfMeasure(id = 1, name="Liter", alias_name="لیتر")
    COUPLE = UnitOfMeasure(id = 1, name="Couple", alias_name="جفت")


