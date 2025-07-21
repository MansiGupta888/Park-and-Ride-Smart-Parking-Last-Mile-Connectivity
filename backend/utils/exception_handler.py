# backend/utils/exception_handler.py
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status

async def custom_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal Server Error"}
    )
