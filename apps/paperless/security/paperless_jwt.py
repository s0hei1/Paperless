from typing import ClassVar
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, UTC, timedelta
import jwt
from sqlalchemy import select
from apps.paperless.data.db.db import get_read_only_db
from apps.paperless.data.db.read_only_async_session import ReadOnlyAsyncSession
from apps.paperless.data.models.models import User
from apps.paperless.security.auth_exception import AuthException


class JWT:
    _http_bearer: ClassVar[HTTPBearer] = HTTPBearer()
    SECRET_KEY: ClassVar[str] = "your-secret-key"
    ALGORITHM: ClassVar[str] = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: ClassVar[int] = 1440

    @classmethod
    async def authorize(
        cls,
        token: HTTPAuthorizationCredentials = Depends(_http_bearer),
        db: ReadOnlyAsyncSession = Depends(get_read_only_db),
    ) -> User:

        decoded_token = cls._decode_access_token(token.credentials)
        user_name = decoded_token["sub"]
        q = select(User).where(User.user_name == user_name)
        query_result = await db.execute(q)
        user = query_result.scalar_one_or_none()

        if user is None:
            raise AuthException(f"User name is invalid")

        return user

    @classmethod
    def create_access_token(
        self,
        user_name: str,
        expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    ):
        data = {"sub": user_name}
        to_encode = data.copy()
        expire = datetime.now(UTC) + expires_delta
        to_encode["exp"] = expire
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

    @classmethod
    def _decode_access_token(self, token: str):
        try:
            return jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        except jwt.InvalidTokenError:
            raise AuthException(f"Invalid token")
