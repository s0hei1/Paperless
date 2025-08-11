from numpy.random.mtrand import Sequence
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from apps.paperless.business.exceptions import LogicalException
from apps.paperless.data.db.read_only_async_session import ReadOnlyAsyncSession
from apps.paperless.data.enums.process import PaperlessProcess
from apps.paperless.data.models.models import (
    GoodsExitDoc,
    Department,
    User,
    GoodsExitApproval,
    GoodsExit,
)
from apps.paperless.utils.three_digit_str import ThreeDigitStr


class GoodsExitDocService:

    def __init__(self, db: ReadOnlyAsyncSession):
        self.db = db

    async def generate_doc_code(self):
        code_prefix = PaperlessProcess.GOODS_EXIT.value.document_code_prefix
        q = select(func.max(GoodsExitDoc.doc_code))
        max_id = (await self.db.execute(q)).scalar_one_or_none()

        code = "0001" if max_id is None else str(max_id)

        return f"{code_prefix}{code}"

    async def get_department(self, id: int) -> Department:
        q = select(Department).where(Department.id == id)
        department = (await self.db.execute(q)).scalar_one_or_none()

        if department is None:
            raise LogicalException(f"There is no Department with id {id}")
        return department

    async def get_document_with_items(self, doc_id: int) -> GoodsExitDoc:

        q = (
            select(GoodsExitDoc)
            .options(selectinload(GoodsExitDoc.items))
            .where(GoodsExitDoc.id == doc_id)
        )

        doc = (await self.db.execute(q)).scalar_one_or_none()

        return doc

    async def get_department_manager_user(self) -> User:
        pass

    """
    query:
    select * from goods_exit_approvals as apr
    join good_exit_docs as doc on apr.doc_id = doc.id
    join good_exits as item on item.doc_id = doc.id
    where apr.user_id = {user_id}
    order by apr.modification_date_time desc
    """

    async def get_current_user_approvals(self, user_id) -> Sequence[GoodsExitApproval]:
        q = (
            select(GoodsExitApproval)
            .options(
                selectinload(GoodsExitApproval.doc).selectinload(GoodsExitDoc.items)
            )
            .where(GoodsExitApproval.user_id == user_id)
            .order_by(GoodsExitApproval.modification_date_time.desc())
        )
        query_result = await self.db.execute(q)
        approvals =  query_result.scalars().all()

        return approvals

    async def get_goods_exit_with_approvals(self, doc_id: int) -> GoodsExitDoc:
        q = (
            select(GoodsExitDoc)
            .options(selectinload(GoodsExitDoc.approvals))
            .where(GoodsExitDoc.id == doc_id)
        )
        query_result = await self.db.execute(q)
        obj = query_result.scalar_one_or_none()
        if obj is None:
            raise LogicalException(f"there is no goods exit doc with id {doc_id}")

        return obj



    async def validate_approval_with_user_id(self, user_id : int, approval_id : int) -> None:
        approvals = await self.get_current_user_approvals(user_id)

        if approval_id is not None:
            if approval_id not in [i.id for i in approvals]:
                raise LogicalException(
                    f"there is no approvals with id {approval_id} for user id {user_id}")

