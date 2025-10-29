from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import time

#It stores the log, method info, path, user ip
# it also stores the repsonse headers, executes the latency and headers
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        print(f"Request\nmethod: {request.method}\npath: {request.url.path}\nuser ip : {request.client.host}")
        
        response = await call_next(request)
        result = round((time.time() - start))
        print(f"\n\nResponse\nresponse code: {response.status_code}\nheaders: {response.headers}\nlatency: {result:.2f}")
        return response