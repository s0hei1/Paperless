from fastapi import APIRouter, Depends
from fastapi.params import Query
from fastapi.security import HTTPBearer
from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.comon_response import DeleteSchema
from apps.paperless.business.schema.fields import IdField
from apps.paperless.business.schema.user_schema import UserCreate, UserRead, UserUpdate
from apps.paperless.data.models.models import User
from apps.paperless.data.repository.user_repository import UserRepository
from apps.paperless.di.repository_di import RepositoryDI
from apps.paperless.security.paperless_jwt import JWT

user_router = APIRouter(tags=[Routes.User.scope_name])

@user_router.post(path=Routes.User.create.url, response_model=UserRead)
async def create_user(
        user_create: UserCreate,
        user_repository : UserRepository = Depends(RepositoryDI.user_repository)
):
    user = await user_repository.create(user_create.to_user())

    return user

@user_router.get(path=Routes.User.read_one.url, response_model=UserRead)
async def read_one_user(
        id: int,
        user_repository: UserRepository = Depends(RepositoryDI.user_repository)
):
    user = await user_repository.read_one(id)
    return user

@user_router.get(path=Routes.User.read_many.url, response_model=list[UserRead])
async def read_many_users(
        user_repository: UserRepository = Depends(RepositoryDI.user_repository)
):
    return await user_repository.read_many()

@user_router.put(path=Routes.User.update.url, response_model=UserRead)
async def update_user(
        user_update: UserUpdate,
        id : IdField = Query,
        user_repository: UserRepository = Depends(RepositoryDI.user_repository)
):
    updated_user = await user_repository.update_user(id = id, **user_update.to_t_value_dict())
    return updated_user

@user_router.delete(path=Routes.User.delete.url, response_model=DeleteSchema)
async def delete_user(
        id: int,
        user_repository: UserRepository = Depends(RepositoryDI.user_repository)
):
    user = await user_repository.delete(id)
    return user
