from fastapi import FastAPI

from src.middleware.auth_middleware import AuthenticationMiddleware


def setup_middleware(app: FastAPI):
    app.add_middleware(AuthenticationMiddleware)