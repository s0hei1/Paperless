from sqlalchemy import select

from apps.paperless.business.exceptions import LogicalException
from apps.paperless.business.schema.auth_schema import TokenSchema
from apps.paperless.business.schema.fields import UsernameField, PasswordField
from apps.paperless.data.db.read_only_async_session import ReadOnlyAsyncSession
from apps.paperless.data.models.models import User
from apps.paperless.security.auth_exception import AuthException
from apps.paperless.security.paperless_jwt import JWT


class AuthService:

    def __init__(self, db: ReadOnlyAsyncSession):
        self.db = db

    async def login(
        self, user_name: UsernameField, password: PasswordField
    ) -> TokenSchema:

        q = select(User).where(User.user_name == user_name, User.password == password)
        query_result = await self.db.execute(q)
        obj = query_result.scalar_one_or_none()

        if obj is None:
            raise AuthException(message="Username or password is incorrect")

        token = JWT.create_access_token(obj.user_name)
        return TokenSchema(token=token)
