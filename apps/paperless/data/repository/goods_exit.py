from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from typing import Sequence

from apps.paperless.data.models.models import GoodsExit
from apps.paperless.data.value.tvalue import TValue


class GoodsExitRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, exit_item: GoodsExit) -> GoodsExit:
        self.db.add(exit_item)
        await self.db.commit()
        await self.db.refresh(exit_item)
        return exit_item

    async def read_one(self, item_id: int) -> GoodsExit:
        q = select(GoodsExit).where(GoodsExit.id == item_id)
        result = await self.db.execute(q)
        item = result.scalar_one_or_none()

        if item is None:
            raise NoResultFound(f"GoodsExit with id: {item_id} does not exist")

        return item

    async def read_many(self) -> Sequence[GoodsExit]:
        q = select(GoodsExit).order_by(GoodsExit.id)
        result = await self.db.execute(q)
        return result.scalars().all()

    async def update(
        self,
        id: int,
        description: TValue[str] | None = None,
        sap_code: TValue[str] | None = None,
        count: TValue[int] | None = None,
        unit_of_measure: TValue[str] | None = None,
        goods_exit_doc_id: TValue[int] | None = None,
    ) -> GoodsExit:
        item = await self.read_one(id)

        if description is not None:
            item.description = description.value
        if sap_code is not None:
            item.sap_code = sap_code.value
        if count is not None:
            item.count = count.value
        if unit_of_measure is not None:
            item.unit_of_measure = unit_of_measure.value
        if goods_exit_doc_id is not None:
            item.goods_exit_doc_id = goods_exit_doc_id.value

        await self.db.commit()
        await self.db.refresh(item)
        return item

    async def delete(self, id: int) -> GoodsExit:
        item = await self.read_one(id)
        await self.db.delete(item)
        await self.db.commit()
        return item
