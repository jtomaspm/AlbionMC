from dataclasses import dataclass
import datetime


@dataclass
class ItemPrice:
    item_id         : int
    price           : int
    city            : str
    data_source_id  : int
    updated_at      : datetime
    updated_by      : str
    created_at      : datetime
    created_by      : str