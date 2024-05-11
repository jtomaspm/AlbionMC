import os
from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException


github_router = APIRouter(prefix="/users/github", tags=["GitHub"])

from src.service.auth_service import GithubAuthService
from src.controller.models.auth_token import AuthToken
from src.dependencies import configure_injector
injector = configure_injector()

@github_router.get("/login",description="Endpoint used to login with github.")
async def github_login(auth_service: GithubAuthService = Depends(lambda: injector.get(GithubAuthService))):
    return auth_service.login_user()

@github_router.get("/code", description="Retrieves the user auth token.")
async def handle_github_code(code: str, auth_service: GithubAuthService = Depends(lambda: injector.get(GithubAuthService))) -> Dict[str, Any]:
    return auth_service.handle_code(code)

@github_router.get("/info")
async def get_user_info(token: str, auth_service: GithubAuthService = Depends(lambda: injector.get(GithubAuthService))) -> Dict[str, Any]:
    user = auth_service.get_user_info(token=token)
    if user:
        return user
    raise HTTPException(status_code=401, detail="Not authenticated")
