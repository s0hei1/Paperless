from pydantic import ConfigDict, BaseModel
from apps.paperless.data.enums.process import PaperlessProcess


class ApprovalUserBase(BaseModel):
    approval_process: PaperlessProcess
    user_id: int


class ApprovalUserCreate(ApprovalUserBase):
    pass


class ApprovalUserUpdate(BaseModel):
    approval_process: PaperlessProcess | None = None
    user_id: int | None = None


class ApprovalUserRead(ApprovalUserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
