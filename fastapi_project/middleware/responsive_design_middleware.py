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

        # Optionally modify the response content based on device type
        # For example, you could adjust the response JSON or HTML here

        return response