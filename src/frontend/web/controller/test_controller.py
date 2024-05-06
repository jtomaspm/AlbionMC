from fastapi import APIRouter

test_router = APIRouter()

@test_router.get("/test")
def test():
    return {"message": "Hello, FRONTEND!"}