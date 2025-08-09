from urllib.request import Request

from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware


class EventsMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        route: APIRoute = request.scope.get("path")
        print(route)

        response = await call_next(request)

        return response
