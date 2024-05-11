
from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class Item:
    id              : int | None
    unique_name     : str
    name            : str
    tags            : List[str]
    tier            : int
    enchant         : int
    description     : str
    data_source_id  : int
    updated_at      : datetime
    updated_by      : str
    created_at      : datetime
    created_by      : str