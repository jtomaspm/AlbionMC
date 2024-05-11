import os
from fastapi import APIRouter
from fastapi.responses import RedirectResponse


user_router = APIRouter(prefix="/users", tags=["Users"])
github_client_id = os.environ.get("GITHUB_CLIENT_ID")

from src.dependencies import configure_injector
injector = configure_injector()

@user_router.get("/github-login")
async def github_login():
    return RedirectResponse(f'https://github.com/login/oauth/authorize?client_id={github_client_id}', status_code=302)
