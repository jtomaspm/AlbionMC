from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ..controller.test_controller import test_router
from ..controller.home_controller import home_router


def setup_routes(app: FastAPI, prefix: str):
   app.mount("/static", StaticFiles(directory="frontend/web/vue/app/static"))
   app.include_router(test_router, prefix=prefix)
   app.include_router(home_router, prefix=prefix)