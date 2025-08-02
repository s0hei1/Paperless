from fastapi import APIRouter, Depends
from sqlalchemy.util import await_only

from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.comon_response import DeleteSchema
from apps.paperless.business.schema.user_schema import UserCreate, UserRead, UserUpdate
from apps.paperless.data.repository.user_repository import UserRepository
from apps.paperless.di.repository_di import RepositoryDI

user_router = APIRouter(tags=[Routes.User.scope_name])


@user_router.post(path=Routes.User.create.url, response_model=UserRead)
async def create_user(
        user_create: UserCreate,
        user_repository : UserRepository = Depends(RepositoryDI.user_repository)
):

    user = await user_repository.create(user_create.to_user())

    return user


@user_router.get(path=Routes.User.read_one.url, response_model=UserRead)
async def read_one_user(id: int):
    return {
        "id": 1,
        "first_name": "test",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }

@user_router.get(path=Routes.User.read_many.url, response_model=list[UserRead])
async def read_one_user():
    return [{
        "id": 1,
        "first_name": "test",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }]

@user_router.put(path=Routes.User.update.url, response_model=UserRead)
async def update_user(user: UserUpdate):
    return {
        "id": 1,
        "first_name": "Updated Maryam",
        "last_name": "test",
        "user_name": "test",
        "department_id": 1,
        "user_roll": 1,
    }

@user_router.delete(path=Routes.User.delete.url, response_model=DeleteSchema)
async def delete_user(id: int):
    return {
        "id": 1,
        "message": "Delete was successful",
    }
