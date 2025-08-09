from pydantic import ConfigDict, BaseModel


class UnitOfMeasureBase(BaseModel):
    name: str
    name_alias: str | None = None


class UnitOfMeasureCreate(UnitOfMeasureBase):
    pass


class UnitOfMeasureUpdate(BaseModel):
    name: str | None = None
    name_alias: str | None = None


class UnitOfMeasureRead(UnitOfMeasureBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
