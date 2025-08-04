from pydantic import ConfigDict, BaseModel
from apps.paperless.business.schema.fields import IdField,ShortStringField,PositiveShortIntField
from apps.paperless.business.base.pydantic_base_model import Model



class DepartmentCreate(Model):
    name:ShortStringField
    code: PositiveShortIntField

class DepartmentUpdate(Model):
    name: ShortStringField | None = None
    code: PositiveShortIntField | None = None

class DepartmentRead(Model):
    id: IdField
    name:ShortStringField
    code: PositiveShortIntField
    model_config = ConfigDict(from_attributes=True)
