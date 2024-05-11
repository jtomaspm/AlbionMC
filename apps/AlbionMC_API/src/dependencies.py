from src.core.settings.db_settings import DbSettings
from src.dal.posgres.db_context import DbContext
from src.repository.data_source_repository import DataSourceRepository
from src.repository.item_repository import ItemRepository
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
        binder.bind(DataSourceRepository)
        binder.bind(ItemRepository)

def configure_injector() -> Injector:
    injector = Injector(modules=[AppModule()])
    return injector