from fastapi import FastAPI

from apps.paperless.api.end_points.auth_api import auth_router
from apps.paperless.api.end_points.user_api import user_router
from apps.paperless.config import Settings

class GeneralDI:

    @classmethod
    def settings(cls) -> Settings:
        return Settings()


    @classmethod
    def app(cls) -> FastAPI:

        fast_api_app = FastAPI()

        fast_api_app.include_router(user_router)
        fast_api_app.include_router(auth_router)

        return fast_api_app
