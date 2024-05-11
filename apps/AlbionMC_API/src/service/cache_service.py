from datetime import timedelta
from typing import Dict, List
from injector import inject
from pyignite import Client
from pyignite.cache import Cache
from pyignite.datatypes.expiry_policy import ExpiryPolicy

class CacheService:
    client: Client
    cache: Cache
    
    @inject
    def __init__(self, client: Client) -> None:
        self.client = client
        self.cache = client.get_or_create_cache('users').with_expire_policy(expiry_policy=ExpiryPolicy(create=600000))

    def put(self, key:str, val: Dict | List | str):
        self.cache.put(key, val)

    def get(self, key:str) -> Dict | List | str | None:
        return self.cache.get(key)
