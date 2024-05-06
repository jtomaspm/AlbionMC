from fastapi import APIRouter

test_router = APIRouter()

@test_router.get("/")
def read_root():
    return {"message": "Hello, BACKEND!"}