from typing import Awaitable, Callable, List, Optional
from fastapi import HTTPException, Request
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from jose import jwt



oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://github.com/login/oauth/authorize",
    tokenUrl="https://github.com/login/oauth/access_token",
    scopes={"read:user": "Read user information"}  
)


class AuthenticationMiddleware(BaseHTTPMiddleware):
    excluded_routes : List[str] = ["/api/users/github"]

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        if not any(request.url.path.startswith(route) for route in self.excluded_routes):
            try:
                token = await oauth2_scheme(request)
                request.state.user = await self.get_current_user(token)
            except HTTPException as exc:
                if exc.status_code == 401:
                    return Response("Not authenticated", status_code=401)
                raise  
        return await call_next(request)

    async def get_current_user(self, token: str) -> Optional[str]:
        try:
            payload = jwt.decode(token, verify=True)
            return payload.get("sub")
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid token")


    def exclude(self, routes: List[str]):
        if not self.excluded_routes:
            self.excluded_routes = []
        self.excluded_routes.append(routes)
        return self
