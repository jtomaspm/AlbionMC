from injector import Injector, Module, singleton
from src.backend.service.item_service import ItemService
from src.backend.service.data_source_service import DataSourceService
from src.backend.core.settings.db_settings import DbSettings
from src.backend.dal.posgres.db_context import DbContext


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