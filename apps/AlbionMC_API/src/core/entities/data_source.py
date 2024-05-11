from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel


class DataSource(BaseModel):
    id          : Optional[int] = None
    name        : str
    trust_level : int
    updated_at  : Optional[datetime] = None
    updated_by  : Optional[str] = None
    created_at  : Optional[datetime] = None
    created_by  : Optional[str] = None
