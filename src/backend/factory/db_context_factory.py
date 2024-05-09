from src.backend.core.settings.db_settings import DbSettings
from src.backend.dal.posgres.db_context import DbContext

class DbContextFactory:
    config: DbSettings
    def __init__(self, config:DbSettings) -> None:
        self.config = config

    def new(self) -> DbContext:
        return DbContext(self.config)
