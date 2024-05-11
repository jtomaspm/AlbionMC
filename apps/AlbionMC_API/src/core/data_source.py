from dataclasses import dataclass


@dataclass
class DataSource:
    id          : int | None
    name        : str
    trust_level : int
    def __init__(self, id:int | None = None, name:str = "", trust_level:int = 0) -> None:
        self.id             = id
        self.name           = name
        self.trust_level    = trust_level