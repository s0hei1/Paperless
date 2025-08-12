from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from apps.paperless.business.exceptions import LogicalException
from apps.paperless.business.schema.failure_schema import ErrorResponse, ErrorDetail
from apps.paperless.security.auth_exception import AuthException


async def logical_exception_handler(request : Request, e : LogicalException) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            detail=[
                ErrorDetail(
                    type="logical_exception",
                    msg=e.message,
                )
            ]
        ).model_dump(exclude_unset=True)
    )

async def auth_exception_handler(request : Request, e : AuthException) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content=ErrorResponse(
            detail=[
                ErrorDetail(
                    type= "auth_exception",
                    msg=e.message,

                )
            ]
        ).model_dump(exclude_unset = True)
    )
