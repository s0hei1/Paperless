from sqlalchemy import select,func
from sqlalchemy.orm import selectinload

from apps.paperless.business.exceptions import LogicalException
from apps.paperless.data.db.read_only_async_session import ReadOnlyAsyncSession
from apps.paperless.data.enums.process import PaperlessProcess
from apps.paperless.data.models.models import GoodsExitDoc, Department, User
from apps.paperless.utils.three_digit_str import ThreeDigitStr


class GoodsExitDocService:

    def __init__(self, db : ReadOnlyAsyncSession):
        self.db = db

    async def generate_doc_code(self):
        code_prefix = PaperlessProcess.GOODS_EXIT.value.document_code_prefix
        q = select(func.max(GoodsExitDoc.doc_code))
        max_id = (await self.db.execute(q)).scalar_one_or_none()

        code = "0001" if max_id is None else str(max_id)

        return f'{code_prefix}{code}'

    async def get_department(self, id: int) -> Department:
        q = (
            select(Department,User).
            where(Department.id == id)
        )
        department = (await self.db.execute(q)).scalar_one_or_none()

        if department is None:
            raise LogicalException(f"There is no Department with id {id}")
        return department

    async def get_document_with_items(self, doc_id: int) -> GoodsExitDoc:

        q = (
            select(GoodsExitDoc).
            options(selectinload(GoodsExitDoc.items)).
            where(GoodsExitDoc.id == doc_id)
        )

        doc = (await self.db.execute(q)).scalar_one_or_none()

        return doc

    async def get_department_manager_user(self) -> User:
        q = (
            select(User)
        )








