import psycopg2
from psycopg2.extensions import connection
from src.backend.core.settings.db_settings import DbSettings

class DbContext:
    config: DbSettings
    conn: connection | None
    def __init__(self, config: DbSettings) -> None:
        self.config = config

    def __enter__(self) -> connection:
        return self.open()

    def __exit__(self):
        self.close()

    def open(self):
        self.close()
        self.conn = psycopg2.connect(
            dbname      = self.config.dbname, 
            user        = self.config.user, 
            password    = self.config.password, 
            host        = self.config.host, 
            port        = self.config.port
            )
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
        self.conn = None