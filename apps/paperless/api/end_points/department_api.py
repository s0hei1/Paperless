from fastapi import APIRouter, Depends, Query
from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.comon_response import DeleteSchema
from apps.paperless.business.schema.department_schema import (
    DepartmentCreate,
    DepartmentRead,
    DepartmentUpdate,
)
from apps.paperless.business.schema.fields import IdField
from apps.paperless.data.repository.department_repository import DepartmentRepository
from apps.paperless.di import RepositoryDI

department_router = APIRouter(tags=[Routes.Department.scope_name])


@department_router.post(
    path=Routes.Department.create.url, response_model=DepartmentRead
)
async def create_department(
    department_create: DepartmentCreate,
    department_repository: DepartmentRepository = Depends(
        RepositoryDI.department_repository
    ),
):
    return await department_repository.create(department_create.to_department())


@department_router.get(
    path=Routes.Department.read_one.url, response_model=DepartmentRead
)
async def read_one_department(
    id: int,
    department_repository: DepartmentRepository = Depends(
        RepositoryDI.department_repository
    ),
):
    return await department_repository.read_one(id)


@department_router.get(
    path=Routes.Department.read_many.url, response_model=list[DepartmentRead]
)
async def read_many_departments(
    department_repository: DepartmentRepository = Depends(
        RepositoryDI.department_repository
    ),
):
    return await department_repository.read_many()


@department_router.put(path=Routes.Department.update.url, response_model=DepartmentRead)
async def update_department(
    department_update: DepartmentUpdate,
    id: IdField = Query,
    department_repository: DepartmentRepository = Depends(
        RepositoryDI.department_repository
    ),
):
    return await department_repository.update(
        id=id, **department_update.to_t_value_dict()
    )


@department_router.delete(
    path=Routes.Department.delete.url, response_model=DeleteSchema
)
async def delete_department(
    id: int,
    department_repository: DepartmentRepository = Depends(
        RepositoryDI.department_repository
    ),
):
    return await department_repository.delete(id=id)
