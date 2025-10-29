from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
import datetime
import time

#It will implement rate limiting middleware in every request
class RateLimitingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.requests = {} 

    async def dispatch(self, request, call_next):
        ip = request.client.host
        now = time.time()

        times = self.requests.get(ip, [])
        times = [t for t in times if now - t < 10]

        if len(times) >= 3:
            return JSONResponse(
                {"message": "Too many requests, try again later"},
                status_code=429
            )

        times.append(now)
        self.requests[ip] = times

        response = await call_next(request)
        return response