from fastapi import FastAPI
import uvicorn

from backend.router import router as backend_router
from frontend.web.router import router as frontend_router
from frontend.web.vue.build_app import build_vue_app


def setup():
    build_vue_app()


if __name__ == "__main__":
    setup()
    app = FastAPI()
    backend_router.setup_routes(app, '/api')
    frontend_router.setup_routes(app, '')
    uvicorn.run(app, host="127.0.0.1", port=3000)