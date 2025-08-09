from fastapi.params import Depends
from apps.paperless.business.service.goods_exit_doc_sevice import GoodsExitDocService
from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.models.models import GoodsExitApproval
from apps.paperless.data.repository.goods_exit_approvals import (
    GoodsExitApprovalRepository,
)
from apps.paperless.data.value.tvalue import TValue
from apps.paperless.di import RepositoryDI
from apps.paperless.di.service_di import ServiceDI
from apps.paperless.events.events_schema import OnAddGoodsExitDocSchema


async def on_approve_goods_exit_event(
    doc_id: int,
    goods_exit_doc_service: GoodsExitDocService = Depends(
        ServiceDI.goods_exit_doc_service
    ),
    goods_exit_approval_repo: GoodsExitApprovalRepository = Depends(
        RepositoryDI.good_exit_approval_repository
    ),
):
    obj = await goods_exit_doc_service.get_goods_exit_with_approvals(doc_id)

    if all(i.status == ApprovalStatus.Approved for i in obj.approvals):
        obj.status = ApprovalStatus.Approved
    elif any(i.status == ApprovalStatus.Rejected for i in obj.approvals):
        obj.status = ApprovalStatus.Rejected
    elif any(
        i.status != ApprovalStatus.Rejected and i.status == ApprovalStatus.Pending
        for i in obj.approvals
    ):
        obj.status = ApprovalStatus.Pending
    else:
        raise NotImplemented("this behavior was not implemented")

    await goods_exit_approval_repo.update(id=doc_id, status=TValue(obj.status))


async def on_create_goods_exit_doc(
    event_schema: OnAddGoodsExitDocSchema,
    goods_exit_approval_repo: GoodsExitApprovalRepository = Depends(
        RepositoryDI.good_exit_approval_repository
    ),
):
    approvals = [
        GoodsExitApproval(
            status=ApprovalStatus.Pending, user_id=user_id, doc_id=event_schema.doc_id
        )
        for user_id in event_schema.get_approvers()
    ]

    await goods_exit_approval_repo.create_many(approvals)
