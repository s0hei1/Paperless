from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from typing import Sequence

from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.models.models import GoodsExitApproval
from apps.paperless.data.value.tvalue import TValue


class GoodsExitApprovalRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, approval: GoodsExitApproval) -> GoodsExitApproval:
        self.db.add(approval)
        await self.db.commit()
        await self.db.refresh(approval)
        return approval

    async def create_many(
        self, approvals: list[GoodsExitApproval]
    ) -> Sequence[GoodsExitApproval]:
        response = [await self.create(i) for i in approvals]
        return response

    async def read_one(self, approval_id: int) -> GoodsExitApproval:
        q = select(GoodsExitApproval).where(GoodsExitApproval.id == approval_id)
        result = await self.db.execute(q)
        approval = result.scalar_one_or_none()

        if approval is None:
            raise NoResultFound(
                f"GoodsExitApproval with id: {approval_id} does not exist"
            )

        return approval

    async def read_many(self) -> Sequence[GoodsExitApproval]:
        q = select(GoodsExitApproval).order_by(GoodsExitApproval.id)
        result = await self.db.execute(q)
        return result.scalars().all()

    async def update(
        self,
        id: int,
        status: (
            TValue[ApprovalStatus] | None
        ) = None,  # You can change to TValue[ApprovalStatus] if preferred
        user_id: TValue[int] | None = None,
        doc_id: TValue[int] | None = None,
    ) -> GoodsExitApproval:
        approval = await self.read_one(id)

        if status is not None:
            approval.status = status.value
        if user_id is not None:
            approval.user_id = user_id.value
        if doc_id is not None:
            approval.doc_id = doc_id.value

        await self.db.commit()
        await self.db.refresh(approval)
        return approval

    async def delete(self, id: int) -> GoodsExitApproval:
        approval = await self.read_one(id)
        await self.db.delete(approval)
        await self.db.commit()
        return approval
