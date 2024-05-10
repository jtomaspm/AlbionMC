from injector import Injector, singleton
from src.backend.core.settings.db_settings import DbSettings
from src.backend.dal.posgres.db_context import DbContext

def configure_injector() -> Injector:
    return Injector([
            singleton( 
                lambda: DbSettings(
                    dbname = 'AlbionMC',
                    user = 'admin',
                    password = 'Albionmc123?',
                    host = 'localhost',
                    port = '5432',
            )),
            singleton(
                DbContext
            )
         ])