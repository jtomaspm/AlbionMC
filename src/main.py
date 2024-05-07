from fastapi import FastAPI
import uvicorn

from backend.router import router as backend_router
from frontend.web.router import router as frontend_router


app = FastAPI()
backend_router.setup_routes(app, '/api')
frontend_router.setup_routes(app, '')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)