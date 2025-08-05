from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from typing import Sequence
from apps.paperless.data.models.models import GoodsExitDoc
from apps.paperless.data.value.tvalue import TValue

class GoodsExitDocRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, doc: GoodsExitDoc) -> GoodsExitDoc:
        self.db.add(doc)
        await self.db.commit()
        await self.db.refresh(doc)
        return doc

    async def read_one(self, doc_id: int) -> GoodsExitDoc:
        q = select(GoodsExitDoc).where(GoodsExitDoc.id == doc_id)
        result = await self.db.execute(q)
        doc = result.scalar_one_or_none()

        if doc is None:
            raise NoResultFound(f"GoodsExitDoc with id: {doc_id} does not exist")

        return doc

    async def read_many(self) -> Sequence[GoodsExitDoc]:
        q = select(GoodsExitDoc).order_by(GoodsExitDoc.id)
        result = await self.db.execute(q)
        return result.scalars().all()

    async def update(
        self,
        id: int,
        doc_code: TValue[str] | None = None,
        sending_department_id: TValue[int] | None = None,
        sending_department_name: TValue[str] | None = None,
        exit_reason: TValue[str] | None = None,
        destination: TValue[str] | None = None,
        address: TValue[str] | None = None,
        sending_user_fullname: TValue[str] | None = None
    ) -> GoodsExitDoc:
        doc = await self.read_one(id)

        if doc_code is not None:
            doc.doc_code = doc_code.value
        if sending_department_id is not None:
            doc.sending_department_id = sending_department_id.value
        if sending_department_name is not None:
            doc.sending_department_name = sending_department_name.value
        if exit_reason is not None:
            doc.exit_reason = exit_reason.value
        if destination is not None:
            doc.destination = destination.value
        if address is not None:
            doc.address = address.value
        if sending_user_fullname is not None:
            doc.sending_user_fullname = sending_user_fullname.value

        await self.db.commit()
        await self.db.refresh(doc)
        return doc

    async def delete(self, id: int) -> GoodsExitDoc:
        doc = await self.read_one(id)
        await self.db.delete(doc)
        await self.db.commit()
        return doc
