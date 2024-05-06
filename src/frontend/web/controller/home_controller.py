from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_router = APIRouter()

@home_router.get("/", response_class=HTMLResponse)
def home():
    with open("src/frontend/web/static/html/index.html") as f:
        return f.read()