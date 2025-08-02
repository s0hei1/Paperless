from fastapi import APIRouter

from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.comon_response import DeleteSchema
from apps.paperless.business.schema.user_schema import UserCreate, UserRead, UserUpdate

user_router = APIRouter(tags=[Routes.User.scope_name])


@user_router.post(path=Routes.User.create.url, response_model=UserRead)
def create_user(user_create: UserCreate):
    return {
        "id": 1,
        "first_name": "test",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }


@user_router.get(path=Routes.User.read_one.url, response_model=UserRead)
def read_one_user(id: int):
    return {
        "id": 1,
        "first_name": "test",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }

@user_router.get(path=Routes.User.read_many.url, response_model=list[UserRead])
def read_one_user():
    return [{
        "id": 1,
        "first_name": "test",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }]

@user_router.put(path=Routes.User.update.url, response_model=UserRead)
def update_user(user: UserUpdate):
    return {
        "id": 1,
        "first_name": "Updated Maryam",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }

@user_router.delete(path=Routes.User.delete.url, response_model=DeleteSchema)
def delete_user(id: int):
    return {
        "id": 1,
        "message": "Delete was successful",
    }
