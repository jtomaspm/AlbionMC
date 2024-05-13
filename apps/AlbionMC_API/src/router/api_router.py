from fastapi import FastAPI

from src.controller.item_controller  import item_router
from src.controller.data_source_controller import data_source_router
from src.controller.item_price_controller import item_price_router
from src.controller.crafting_slot_controller import crafting_slot_router
from src.controller.user_controller import github_router
from src.controller.user_preferences_controller import user_preference_router


def setup_routes(app: FastAPI, prefix: str):
   app.include_router(item_router, prefix=prefix)
   app.include_router(data_source_router, prefix=prefix)
   app.include_router(item_price_router, prefix=prefix)
   app.include_router(crafting_slot_router, prefix=prefix)
   app.include_router(github_router, prefix=prefix)
   app.include_router(user_preference_router, prefix=prefix)