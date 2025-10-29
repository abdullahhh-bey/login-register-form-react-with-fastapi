from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

#It stores the log into a file in the folder
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"")