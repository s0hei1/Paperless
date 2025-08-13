from dependency_injector import containers
from dependency_injector.providers import Factory,Singleton
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from apps.paperless.business.service.auth_service import AuthService
from apps.paperless.business.service.goods_exit_doc_sevice import GoodsExitDocService
from apps.paperless.config import Settings
from apps.paperless.data.db.db import get_db, get_read_only_db
from apps.paperless.data.db.read_only_async_session import ReadOnlyAsyncSession
from apps.paperless.data.repository.department_repository import DepartmentRepository
from apps.paperless.data.repository.goods_exit import GoodsExitRepository
from apps.paperless.data.repository.goods_exit_approvals import GoodsExitApprovalRepository
from apps.paperless.data.repository.goods_exit_docs import GoodsExitDocRepository
from apps.paperless.data.repository.user_repository import UserRepository


class Container(containers.DeclarativeContainer):

    settings : Singleton[Settings] = Singleton(Settings)

    app : Singleton[FastAPI] = Singleton(FastAPI)

    db : Factory[AsyncSession] = Factory(get_db)
    read_only_db : Factory[ReadOnlyAsyncSession] = Factory(get_read_only_db)

    user_repository : Factory[UserRepository] = Factory(UserRepository, db = db)
    goods_exit_doc_repository : Factory[DepartmentRepository] = Factory(DepartmentRepository, db =db)
    goods_exit_repository : Factory[GoodsExitDocRepository] = Factory(GoodsExitDocRepository, db =db)
    good_exit_approval_repository : Factory[GoodsExitRepository] = Factory(GoodsExitRepository, db =db)
    department_repository : Factory[GoodsExitApprovalRepository] = Factory(GoodsExitApprovalRepository, db =db)

    auth_service : Factory[AuthService] = Factory(AuthService,db = read_only_db)
    goods_exit_doc_service : Factory[GoodsExitDocService] = Factory(GoodsExitDocService, db = read_only_db)




