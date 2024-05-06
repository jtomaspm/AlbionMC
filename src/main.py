from fastapi import FastAPI

from .backend.router import router as backend_router
from .frontend.web.router import router as frontend_router


app = FastAPI()
backend_router.setup_routes(app, '/api')
frontend_router.setup_routes(app, '')
