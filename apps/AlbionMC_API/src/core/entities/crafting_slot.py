from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class CraftingSlot(BaseModel):
    craft_id            : int
    destination_item_id : int
    source_item_id      : int
    source_item_quantity: int
    data_source_id      : int
    updated_at          : str
    updated_by          : str
    created_at          : str
    created_by          : str