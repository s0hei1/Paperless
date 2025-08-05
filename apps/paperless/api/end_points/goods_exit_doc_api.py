from fastapi import APIRouter, Depends, Query
from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.goods_exit_doc_schema import GoodsExitDocRead, GoodsExitDocCreate
from apps.paperless.business.service.goods_exit_doc_sevice import GoodsExitDocService
from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.enums.unit_of_measure import UOMs
from apps.paperless.data.models.models import User, GoodsExitDoc, GoodsExit, GoodsExitApproval
from apps.paperless.data.repository.goods_exit import GoodsExitRepository
from apps.paperless.data.repository.goods_exit_approvals import GoodsExitApprovalRepository
from apps.paperless.data.repository.goods_exit_docs import GoodsExitDocRepository
from apps.paperless.di import RepositoryDI
from apps.paperless.di.service_di import ServiceDI
from apps.paperless.security.paperless_jwt import JWT

goods_exit_doc_router = APIRouter(tags=[Routes.GoodsExitDoc.scope_name])

@goods_exit_doc_router.post(path=Routes.GoodsExitDoc.create.url, response_model=GoodsExitDocRead)
async def create_goods_exit_doc(
        doc_create: GoodsExitDocCreate,
        goods_exit_doc_repo: GoodsExitDocRepository = Depends(RepositoryDI.goods_exit_doc_repository),
        goods_exit_repo: GoodsExitRepository = Depends(RepositoryDI.goods_exit_repository),
        goods_exit_approval_repo: GoodsExitApprovalRepository = Depends(RepositoryDI.good_exit_approval_repository),
        goods_exit_doc_service: GoodsExitDocService = Depends(ServiceDI.goods_exit_doc_service),
        creator_user: User = Depends(JWT.authorize)
):
    code = await goods_exit_doc_service.generate_doc_code()
    department = await goods_exit_doc_service.get_department(doc_create.sending_department_id)

    doc = GoodsExitDoc(
        doc_code=code,
        sending_department_id=department.id,
        sending_department_name=department.name,
        exit_reason=doc_create.exit_reason,
        destination=doc_create.destination,
        address_=doc_create.address,
        sending_user_fullname=f"{creator_user.first_name} {creator_user.last_name}",
        exit_for_ever=doc_create.exit_for_ever,
        receiver_name=doc_create.receiver_name,
        status=ApprovalStatus.Pending,
        approval_status=ApprovalStatus.Pending
    )

    doc = await goods_exit_doc_repo.create(doc)

    items = doc_create.items

    [(await goods_exit_repo.create(
        GoodsExit(
            description=item.description,
            sap_code=item.sap_code,
            count=item.count,
            unit_of_measure=UOMs.get_uom_by_id(item.unit_of_measure_id),
            goods_exit_doc_id=doc.id,
        )
    )) for item in items]

    # approver_users = [
    #     department.department_manager_id,
    #     doc_create.approver_guard_id,
    #     doc_create.approver_manager_id,
    # ]
    #
    # [(await goods_exit_approval_repo.create(
    #     GoodsExitApproval(
    #         status=ApprovalStatus.Pending,
    #         user_id=user_id,
    #         doc_id=doc.id,
    #     )
    # )) for user_id in approver_users]

    return await goods_exit_doc_service.get_document_with_items(doc_id=doc.id)
