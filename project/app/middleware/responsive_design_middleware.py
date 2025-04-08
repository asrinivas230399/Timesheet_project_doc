from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class ResponsiveDesignMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        user_agent = request.headers.get('User-Agent', '').lower()
        device_type = "desktop"

        if "mobile" in user_agent:
            device_type = "mobile"
        elif "tablet" in user_agent:
            device_type = "tablet"

        response = await call_next(request)
        response.headers['X-Device-Type'] = device_type

        return response
