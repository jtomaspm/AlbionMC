from typing import Optional
from AlbionMC_game.craft.price import Price

# if Price is None => this means that there is no information about the item's price

class Item:
    def __init__(self, item_id: int, name: str):
        self.item_id = item_id
        self.name = name

    def fetch_cost(self, city: Optional[str] = None) -> Optional[Price]:
        cost = self.fetch_price_from_cache(city)
        if cost is not None:
            return cost
        
        cost = self.fetch_price_from_api(city)
        if cost is not None:
            return cost

        return None

    def fetch_price_from_cache(self, city: Optional[str]) -> Optional[Price]:
        return None

    def fetch_price_from_api(self, city: Optional[str]) -> Optional[Price]:
        return None

    def __repr__(self):
        return f"Item(id={self.item_id}, name='{self.name}')"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.item_id == other.item_id