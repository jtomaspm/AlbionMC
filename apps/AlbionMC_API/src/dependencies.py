import os
from time import sleep
from src.service.item_service import ItemService
from src.repository.user_preferences_repository import UserPreferencesRepository
from src.service.cache_service import CacheService
from src.service.auth_service import GithubAuthService
from src.core.settings.app_settings import AppSettings
from src.repository.crafting_slot_repository import CraftingSlotRepository
from src.repository.item_price_repository import ItemPriceRepository
from src.core.settings.db_settings import DbSettings
from src.dal.posgres.db_context import DbContext
from src.repository.data_source_repository import DataSourceRepository
from src.repository.item_repository import ItemRepository
from injector import Injector, Module
from pyignite import Client


class AppModule(Module):
    def configure(self, binder):
        db_config = DbSettings(**{
            'dbname'    : os.environ.get('POSTGRES_DBNAME') or '',
            'user'      : os.environ.get('POSTGRES_USER') or '',
            'password'  : os.environ.get('POSTGRES_PASSWORD') or '',
            'host'      : os.environ.get('POSTGRES_HOST') or '',
            'port'      : os.environ.get('POSTGRES_PORT') or '',
        })
        app_config = AppSettings(**{
            'github_client_id'      : os.environ.get('GITHUB_CLIENT_ID') or '',
            'github_client_secret'  : os.environ.get('GITHUB_CLIENT_SECRET') or '',
        })
        cache_con = None
        while cache_con == None:
            try:
                cache_con = Client()
                cache_con.connect('ignite', 10800)
            except:
                cache_con=None
                print('Failed to connect to ignite, trying again in 5 seconds...')
                sleep(5)

        ########## Binds ##########
        binder.bind(DbSettings, to=db_config)
        binder.bind(AppSettings, to=app_config)
        binder.bind(Client, to=cache_con)
        binder.bind(CacheService)
        binder.bind(DbContext)
        binder.bind(DataSourceRepository)
        binder.bind(ItemRepository)
        binder.bind(CraftingSlotRepository)
        binder.bind(ItemPriceRepository)
        binder.bind(GithubAuthService)
        binder.bind(ItemService)
        binder.bind(UserPreferencesRepository)
        ###########################

def configure_injector() -> Injector:
    injector = Injector(modules=[AppModule()])
    return injector