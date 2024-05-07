import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_router = APIRouter()
current_dir = os.path.dirname(os.path.realpath(__file__))
web_root = os.path.abspath(os.path.join(current_dir, '../'))
static_dir = os.path.abspath(os.path.join(web_root, 'vue/app/static'))

@home_router.get("/", response_class=HTMLResponse)
def home():
    print("Home controller")
    with open(static_dir+"\\index.html") as f:
        content = f.read()
        print(content)
        return content