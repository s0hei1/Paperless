from fastapi import FastAPI

from apps.paperless.api.exception_handler.exception_handler import logical_exception_handler, auth_exception_handler
from apps.paperless.business.exceptions import LogicalException
from apps.paperless.config import Settings
from apps.paperless.security.auth_exception import AuthException


class GeneralDI:

    @classmethod
    def settings(cls) -> Settings:
        return Settings()

    @classmethod
    def app(cls) -> FastAPI:
        from apps.paperless.api.end_points.auth_api import auth_router
        from apps.paperless.api.end_points.user_api import user_router
        from apps.paperless.api.end_points.department_api import department_router
        from apps.paperless.api.end_points.goods_exit_doc_api import (
            goods_exit_doc_router,
        )
        from apps.paperless.api.middleware.event_middleware import EventsMiddleware

        fast_api_app = FastAPI()

        fast_api_app.include_router(user_router)
        fast_api_app.include_router(auth_router)
        fast_api_app.include_router(department_router)
        fast_api_app.include_router(goods_exit_doc_router)

        fast_api_app.add_middleware(EventsMiddleware)

        fast_api_app.add_exception_handler(LogicalException,logical_exception_handler)
        fast_api_app.add_exception_handler(AuthException,auth_exception_handler)

        return fast_api_app
