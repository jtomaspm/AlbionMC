from src.backend.factory.db_context_factory import DbContextFactory
from src.backend.core.data_source import DataSource
from src.backend.core.settings.db_settings import DbSettings

def new_data_source(ds:DataSource, db_config: DbSettings):
    dbcf = DbContextFactory(db_config)
    with dbcf.new() as conn:
        pass