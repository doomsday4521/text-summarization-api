from fastapi import Request

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.errors import ErrorResponse
async def validation_exception_handler(
        request:Request,
        exc:RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            error="validation_error",
            message="invalid request data"
        ).model_dump()
    )

async def internal_exception_handler(
        request:Request,
        exc:Exception
):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="internal_server_error",
            message="Something went wrong"
        ).model_dump()
    )