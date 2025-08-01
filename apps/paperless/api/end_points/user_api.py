from fastapi import APIRouter

from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.user_schema import UserCreate, UserRead

user_router = APIRouter(tags = [Routes.User.scope_name])

@user_router.post(path= Routes.User.create.url, response_model=UserRead)
def create_user(user_create : UserCreate):

    return {
        "first_name" : "test",
    "last_name" : "test",
    "user_name" : "test",
    "department_id" : 1,
    "user_roll" : 1,
    }