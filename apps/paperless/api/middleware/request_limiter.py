from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class CountryLimiterMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request : Request, call_next) -> Response:
        ip = request.client

        response = await call_next(request)

        return response