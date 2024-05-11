from dataclasses import dataclass
import datetime


@dataclass
class DataSource:
    id          : int | None
    name        : str
    trust_level : int
    updated_at  : datetime
    updated_by  : str
    created_at  : datetime
    created_by  : str