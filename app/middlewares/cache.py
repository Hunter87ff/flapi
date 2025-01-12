from fastapi import  Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class CacheControlMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, cache_control_header: str = "public, max-age=3600"):
        super().__init__(app)
        self.cache_control_header = cache_control_header

    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)  # Type hint for clarity

        # Only set Cache-Control for successful GET requests
        if request.method == "GET" and response.status_code == 200:
            response.headers["Cache-Control"] = self.cache_control_header
        else:
            # Explicitly prevent caching for other methods/status codes
            response.headers["Cache-Control"] = "no-store"  # Or "no-cache" if needed
            response.headers["Pragma"] = "no-cache" # also add pragma for backward compatibility
            response.headers["Expires"] = "0"

        return response
