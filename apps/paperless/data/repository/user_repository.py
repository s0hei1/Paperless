from typing import Sequence
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from apps.paperless.data.enums.user_rolls import UserRoll
from apps.paperless.data.models.models import User
from apps.paperless.data.value.tvalue import TValue


class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user: User):

        if user.user_roll == UserRoll.SUPER_ADMINISTRATOR:
            raise Exception("You can not create user with super admin type")

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def read_one(self, user_id: int) -> User:
        q = select(User).where(User.id == user_id)
        query_result = await self.db.execute(q)
        obj = query_result.scalar_one_or_none()

        if obj is None:
            raise NoResultFound(f"User with id: {user_id} does not exist")

        return obj

    async def read_many(self) -> Sequence[User]:
        q = select(User).order_by(User.id)
        query_result = await self.db.execute(q)
        objs = query_result.scalars().all()
        return objs

    async def update_user(
        self,
        id: int,
        first_name: TValue[str] | None = None,
        last_name: TValue[str] | None = None,
        user_roll: TValue[UserRoll] | None = None,
        department_id: TValue[int] | None = None,
    ):
        user = await self.read_one(id)

        if first_name is not None:
            user.first_name = first_name.value
        if last_name is not None:
            user.last_name = last_name.value
        if user_roll is not None:
            user.user_roll = user_roll.value
        if department_id is not None:
            user.department_id = department_id.value

        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def delete(self, id: int) -> User:
        user = await self.read_one(id)

        await self.db.delete(user)

        return user

    async def change_password(self, user_id: int, password: str) -> User:

        user = await self.read_one(user_id)
        user.password = password
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def de_active_user(self, user_id: int) -> User:
        user = await self.read_one(user_id)
        user.is_active = False
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def activate_user(self, user_id: int) -> User:
        user = await self.read_one(user_id)
        user.is_active = True
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def change_user_type(self, user_id: int, user_type: UserRoll) -> User:
        if user_type == UserRoll.SUPER_ADMINISTRATOR:
            raise Exception("You can not change user type to super admin")
        user = await self.read_one(user_id)
        user.user_type = user_type
        await self.db.commit()
        await self.db.refresh(user)
        return user
