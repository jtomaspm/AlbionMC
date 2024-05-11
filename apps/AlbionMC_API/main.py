from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from src.router.api_router import setup_routes

load_dotenv()
app = FastAPI()
setup_routes(app, '/api')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)