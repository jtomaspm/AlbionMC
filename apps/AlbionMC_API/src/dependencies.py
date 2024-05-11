from src.core.settings.db_settings import DbSettings
from src.dal.posgres.db_context import DbContext
from src.service.data_source_service import DataSourceService
from src.service.item_service import ItemService
from injector import Injector, Module, singleton


class AppModule(Module):
    def configure(self, binder):
        db_config = DbSettings(
            dbname='AlbionMC',
            user='admin',
            password='Albionmc123?',
            host='localhost',
            port='5432',
        )
        binder.bind(DbSettings, to=db_config)
        binder.bind(DbContext)
        binder.bind(DataSourceService)
        binder.bind(ItemService)

def configure_injector() -> Injector:
    injector = Injector(modules=[AppModule()])
    return injector