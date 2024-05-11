from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class ItemPrice(BaseModel):
    item_id         : int
    price           : int
    city            : str
    data_source_id  : int
    updated_at      : str
    updated_by      : str
    created_at      : str
    created_by      : str