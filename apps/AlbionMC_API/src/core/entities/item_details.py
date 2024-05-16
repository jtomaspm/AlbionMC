from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ItemDetailsPrice(BaseModel):
    city: str
    price: int

class ItemDetails(BaseModel):
    id              : Optional[int] = None
    unique_name     : str
    name            : str
    tags            : List[str]
    tier            : Optional[int] = None
    enchant         : Optional[int] = None
    description     : Optional[str] = None
    data_source     : str
    prices          : List[ItemDetailsPrice]
    updated_at      : Optional[datetime] = None
    updated_by      : Optional[str] = None
    created_at      : Optional[datetime] = None
    created_by      : Optional[str] = None
