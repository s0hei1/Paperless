from pydantic import ConfigDict, BaseModel
from apps.paperless.data.enums.approval_status import ApprovalStatus


class GoodsExitApprovalBase(BaseModel):
    status: ApprovalStatus
    user_id: int
    doc_id: int

class GoodsExitApprovalCreate(GoodsExitApprovalBase):
    pass

class GoodsExitApprovalUpdate(BaseModel):
    status: ApprovalStatus | None = None
    user_id: int | None = None
    doc_id: int | None = None

class GoodsExitApprovalRead(GoodsExitApprovalBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
