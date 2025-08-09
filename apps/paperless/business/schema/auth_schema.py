from pydantic import BaseModel

from apps.paperless.business.schema.fields import UsernameField, PasswordField


class TokenSchema(BaseModel):
    token: str


class LoginSchema(BaseModel):
    user_name: UsernameField
    password: PasswordField
