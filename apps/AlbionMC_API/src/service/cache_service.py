from datetime import timedelta
import json
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

    def put(self, key:str, val: dict):
        json_val = json.dumps(val) 
        self.cache.put(key, json_val)

    def get(self, key:str) -> dict | None:
        json_val = self.cache.get(key)
        if json_val is not None:
            return json.loads(json_val)
        return None
