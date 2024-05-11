from fastapi import FastAPI

from src.controller.test_controller import test_router


def setup_routes(app: FastAPI, prefix: str):
   app.include_router(test_router, prefix=prefix)