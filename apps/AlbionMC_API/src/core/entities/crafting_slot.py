from dataclasses import dataclass
import datetime


@dataclass
class CraftingSlot:
    craft_id            : int
    destination_item_id : int
    source_item_id      : int
    data_source_id      : int
    updated_at          : datetime
    updated_by          : str
    created_at          : datetime
    created_by          : str

