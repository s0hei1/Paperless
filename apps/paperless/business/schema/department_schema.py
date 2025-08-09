from pydantic import ConfigDict, BaseModel
from apps.paperless.business.schema.fields import (
    IdField,
    ShortStringField,
    PositiveShortIntField,
)
from apps.paperless.business.base.pydantic_base_model import Model
from apps.paperless.data.models.models import Department


class DepartmentCreate(Model):
    name: ShortStringField
    code: PositiveShortIntField
    manager_id: IdField | None = None

    def to_department(self) -> Department:
        return Department(
            name=self.name,
            code=self.code,
            manager_id=self.manager_id,
        )


class DepartmentUpdate(Model):
    name: ShortStringField | None = None
    code: PositiveShortIntField | None = None
    manager_id: IdField | None = None


class DepartmentRead(Model):
    id: IdField
    name: ShortStringField
    code: PositiveShortIntField
    manager_id: IdField | None = None

    model_config = ConfigDict(from_attributes=True)
