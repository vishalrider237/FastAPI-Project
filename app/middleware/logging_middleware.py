import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class LoggingMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        logging.info(f'Request: {request.method} {request.url}')
        response=await call_next(request)
        logging.info(f'Response: {response.status_code}')
        return response
    
