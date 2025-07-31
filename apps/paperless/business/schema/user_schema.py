from pydantic import ConfigDict, BaseModel
from apps.paperless.data.enums.user_rolls import UserRoll


class UserBase(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    user_roll: UserRoll
    department_id: int

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    user_name: str | None = None
    password: str | None = None
    user_roll: UserRoll | None = None
    department_id: int | None = None

class UserRead(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)