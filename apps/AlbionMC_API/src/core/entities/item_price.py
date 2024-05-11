from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemPrice(BaseModel):
    item_id         : int
    price           : int
    city            : str
    data_source_id  : int
    updated_at      : Optional[datetime] = None
    updated_by      : Optional[str] = None
    created_at      : Optional[datetime] = None
    created_by      : Optional[str] = None