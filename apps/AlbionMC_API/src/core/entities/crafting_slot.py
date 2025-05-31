from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CraftingSlot(BaseModel):
    craft_id            : int
    destination_item_id : int
    source_item_id      : int
    source_item_quantity: int
    data_source_id      : int
    updated_at          : Optional[datetime] = None
    updated_by          : Optional[str] = None
    created_at          : Optional[datetime] = None
    created_by          : Optional[str] = None