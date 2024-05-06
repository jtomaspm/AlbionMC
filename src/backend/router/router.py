from fastapi import FastAPI

from ..controller.test_controller import testRouter


def setup_routes(app: FastAPI, prefix: str):
   app.include_router(testRouter, prefix=prefix)