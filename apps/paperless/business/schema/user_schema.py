from pydantic import ConfigDict, BaseModel
from apps.paperless.data.enums.user_rolls import UserRoll
from apps.paperless.business.schema.fields import IdField, ShortStringField, PasswordField,UsernameField

class UserCreate(BaseModel):
    first_name: ShortStringField
    last_name: ShortStringField
    user_name: UsernameField
    password: PasswordField
    user_roll: UserRoll
    department_id: IdField


class UserUpdate(BaseModel):
    id : IdField
    first_name: ShortStringField | None = None
    last_name: ShortStringField | None = None
    user_roll: UserRoll | None = None
    department_id: IdField | None = None

class UserRead(BaseModel):
    id : IdField
    first_name: ShortStringField
    last_name: ShortStringField
    user_name: UsernameField
    department_id: IdField
    user_roll: UserRoll

    model_config = ConfigDict(from_attributes=True)