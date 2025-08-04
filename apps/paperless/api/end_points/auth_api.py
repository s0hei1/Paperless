from fastapi import APIRouter, Depends

from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.auth_schema import TokenSchema, LoginSchema
from apps.paperless.business.service.auth_service import AuthService
from apps.paperless.di.service_di import ServiceDI

auth_router = APIRouter(tags=[Routes.Auth.scope_name],)


@auth_router.post(path = Routes.Auth.login.url ,response_model=TokenSchema)
async def login(
        login_schema : LoginSchema,
        auth_srvice : AuthService = Depends(ServiceDI.auth_service),
):

    token = await auth_srvice.login(login_schema.user_name, login_schema.password)

    return token


