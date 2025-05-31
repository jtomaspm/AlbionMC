from pydantic import BaseModel

from src.core.entities.item_price import ItemPrice


class ItemPriceFromTarget(BaseModel):
    target: str
    item_price: ItemPrice