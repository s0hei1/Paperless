from fastapi import APIRouter

from apps.paperless.api.route_path.route_path import Routes
from apps.paperless.business.schema.auth_schema import TokenSchema, LoginSchema

auth_router = APIRouter(tags=[Routes.Auth.scope_name],)


@auth_router.post(path = Routes.Auth.login.url ,response_model=TokenSchema)
async def login(login_schema : LoginSchema):
    return {"token" : "some hipnghjdgfjhasdgjhadsgdjas"}
