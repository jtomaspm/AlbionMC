from fastapi import APIRouter, Depends
from src.core.settings.db_settings import DbSettings


test_router = APIRouter()

from src.dependencies import configure_injector
injector = configure_injector()


@test_router.get("/")
def read_root(conf: DbSettings = Depends(lambda: injector.get(DbSettings))):
    return {"message": conf.dbname}