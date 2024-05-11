import os
from src.repository.crafting_slot_repository import CraftingSlotRepository
from src.repository.item_price_repository import ItemPriceRepository
from src.core.settings.db_settings import DbSettings
from src.dal.posgres.db_context import DbContext
from src.repository.data_source_repository import DataSourceRepository
from src.repository.item_repository import ItemRepository
from injector import Injector, Module, singleton


class AppModule(Module):
    def configure(self, binder):
        db_config = DbSettings(
            dbname=os.environ.get('POSTGRES_DBNAME'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            host=os.environ.get('POSTGRES_HOST'),
            port=os.environ.get('POSTGRES_PORT'),
        )

        ########## Binds ##########
        binder.bind(DbSettings, to=db_config)
        binder.bind(DbContext)
        binder.bind(DataSourceRepository)
        binder.bind(ItemRepository)
        binder.bind(CraftingSlotRepository)
        binder.bind(ItemPriceRepository)
        ###########################

def configure_injector() -> Injector:
    injector = Injector(modules=[AppModule()])
    return injector