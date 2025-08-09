from typing import ClassVar
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


class Password:

    crypto_context: ClassVar[CryptContext] = CryptContext(
        schemes=["bcrypt"], deprecated="auto"
    )
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.crypto_context.hash(password)

    @classmethod
    def verify_password(cls, password: str, hashed_password: str):
        return cls.crypto_context.verify(password, hashed_password)
