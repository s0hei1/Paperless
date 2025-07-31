from pydantic import ConfigDict, BaseModel
from datetime import datetime

class GoodsExitDocBase(BaseModel):
    doc_code: str
    sending_department_id: int | None = None
    sending_department_name: str
    exit_reason: str | None = None
    destination: str | None = None
    address: str | None = None
    sending_user_fullname: str | None = None

class GoodsExitDocCreate(GoodsExitDocBase):
    pass

class GoodsExitDocUpdate(BaseModel):
    doc_code: str | None = None
    sending_department_id: int | None = None
    sending_department_name: str | None = None
    exit_reason: str | None = None
    destination: str | None = None
    address: str | None = None
    sending_user_fullname: str | None = None

class GoodsExitDocRead(GoodsExitDocBase):
    id: int
    creation_date_time: datetime
    model_config = ConfigDict(from_attributes=True)
