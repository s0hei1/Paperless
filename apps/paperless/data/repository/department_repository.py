from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from typing import Sequence

from apps.paperless.data.models.models import Department
from apps.paperless.data.value.tvalue import TValue


# adjust path if TValue is elsewhere

class DepartmentRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, department: Department) -> Department:
        self.db.add(department)
        await self.db.commit()
        await self.db.refresh(department)
        return department

    async def read_one(self, department_id: int) -> Department:
        q = select(Department).where(Department.id == department_id)
        result = await self.db.execute(q)
        department = result.scalar_one_or_none()

        if department is None:
            raise NoResultFound(f"Department with id: {department_id} does not exist")

        return department

    async def read_many(self) -> Sequence[Department]:
        q = select(Department).order_by(Department.id)
        result = await self.db.execute(q)
        return result.scalars().all()

    async def update(
        self,
        id: int,
        name: TValue[str] | None = None,
        code: TValue[int] | None = None,
    ) -> Department:
        department = await self.read_one(id)

        if name is not None:
            department.name = name.value
        if code is not None:
            department.code = code.value

        await self.db.commit()
        await self.db.refresh(department)
        return department

    async def delete(self, id: int) -> Department:
        department = await self.read_one(id)
        await self.db.delete(department)
        await self.db.commit()
        return department
