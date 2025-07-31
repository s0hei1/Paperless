from pydantic import ConfigDict, BaseModel


class DepartmentBase(BaseModel):
    name: str
    code: int

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: str | None = None
    code: int | None = None

class DepartmentRead(DepartmentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)