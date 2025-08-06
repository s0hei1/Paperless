from typing import Annotated
from pydantic import ConfigDict, BaseModel, Field
from datetime import datetime,date
from apps.paperless.business.base.pydantic_base_model import Model
from apps.paperless.business.schema.fields import IdField, ShortStringField, StringField, BooleanField, \
    PositiveShortIntField
from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.enums.unit_of_measure import UOMs

class GoodExitFieldCreate(Model):
    description : StringField
    sap_code : StringField | None = None
    count : PositiveShortIntField
    unit_of_measure_id : IdField

class GoodExitFieldRead(Model):
    id : IdField
    description : StringField
    sap_code : StringField | None = None
    count : PositiveShortIntField
    unit_of_measure : UOMs

    model_config = ConfigDict(from_attributes=True)

class GoodsExitDocCreate(Model):
    doc_date : date
    sending_department_id : IdField
    exit_reason : StringField
    destination : StringField
    address : StringField
    exit_for_ever : BooleanField
    items : Annotated[list[GoodExitFieldCreate] , Field(frozen=True, min_length=1, max_length=10)]
    receiver_name : StringField | None = None
    approver_guard_id : IdField
    approver_manager_id : IdField

class GoodsExitDocUpdate(BaseModel):
    doc_code: str | None = None
    sending_department_id: int | None = None
    sending_department_name: str | None = None
    exit_reason: str | None = None
    destination: str | None = None
    address: str | None = None
    sending_user_fullname: str | None = None

class GoodsExitDocRead(Model):
    id: IdField
    sending_department_name : StringField
    exit_reason : StringField
    destination : StringField
    exit_for_ever : BooleanField
    items : list[GoodExitFieldRead]
    receiver_name : StringField
    status : ApprovalStatus

    model_config = ConfigDict(from_attributes=True)

