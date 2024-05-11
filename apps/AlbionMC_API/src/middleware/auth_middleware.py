from typing import Awaitable, Callable, List, Optional
from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from jose import jwt



oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://github.com/login/oauth/authorize",
    tokenUrl="https://github.com/login/oauth/access_token",
    scopes={"read:user": "Read user information"}  
)

from src.service.auth_service import GithubAuthService
from src.dependencies import configure_injector
injector = configure_injector()

class AuthenticationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.excluded_routes: List[str] = ["/api/users/github", "/docks"]

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        if not any(request.url.path.startswith(route) for route in self.excluded_routes):
            auth_service: GithubAuthService = injector.get(GithubAuthService)
            token = await oauth2_scheme(request)
            jwt.decode(token=token)
            request.state.user = auth_service.get_user_info(token)
            if not request.state.user:    
                return Response("Not authenticated", status_code=401)
        return await call_next(request)
