from fastapi import FastAPI
from apps.paperless.config import Settings


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

        return fast_api_app
