from sqlalchemy import select

from apps.paperless.business.exceptions import LogicalException
from apps.paperless.business.jwt.paperless_jwt import JWT
from apps.paperless.business.schema.fields import UsernameField, PasswordField
from apps.paperless.data.db.read_only_async_session import ReadOnlyAsyncSession
from apps.paperless.data.models.models import User


class AuthService:

    def __init__(self, db : ReadOnlyAsyncSession, jwt : JWT):
        self.db = db
        self._jwt = jwt


    async def login(self, user_name : UsernameField, password : PasswordField) -> User:

        q = select(User).where(User.user_name == user_name, User.password == password)
        query_result = await self.db.execute(q)
        obj = query_result.scalar_one_or_none()

        if obj is None:
            raise LogicalException(message="Username or password is incorrect")

        return obj

    async def current_user(self, token : str) -> User:
        payload = self._jwt.decode_access_token(token)
        user_name = payload["sub"]
        q = select(User).where(User.user_name == user_name)
        query_result = await self.db.execute(q)
        user = query_result.scalar_one_or_none()

        if user is None:
            raise LogicalException(f"User name is invalid")

        return user


