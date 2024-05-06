from fastapi import APIRouter

testRouter = APIRouter()

@testRouter.get("/")
def read_root():
    return {"message": "Hello, FRONTEND!"}