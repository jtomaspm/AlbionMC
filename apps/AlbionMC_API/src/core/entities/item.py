
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


@dataclass
class Item(BaseModel):
    id              : int
    unique_name     : str
    name            : str
    tags            : List[str]
    tier            : int
    enchant         : int
    description     : str
    data_source_id  : int
    updated_at      : str
    updated_by      : str
    created_at      : str
    created_by      : str

    class Config:
        arbitrary_types_allowed = True