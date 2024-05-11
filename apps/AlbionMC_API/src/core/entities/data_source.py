from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class DataSource(BaseModel):
    id          : int
    name        : str
    trust_level : int
    updated_at  : str
    updated_by  : str
    created_at  : str
    created_by  : str