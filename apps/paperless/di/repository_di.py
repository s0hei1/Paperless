from fastapi import Depends

from apps.paperless.data.db.db import get_db
from apps.paperless.data.repository.department_repository import DepartmentRepository
from apps.paperless.data.repository.user_repository import UserRepository


class RepositoryDI():

    @classmethod
    def user_repository(self, db = Depends(get_db)) -> UserRepository:
        return UserRepository(db)

    @classmethod
    def department_repository(self, db = Depends(get_db)) -> DepartmentRepository:
        return DepartmentRepository(db)




