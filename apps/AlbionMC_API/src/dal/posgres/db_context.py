from src.core.settings.db_settings import DbSettings
from injector import inject
import psycopg2
from psycopg2.extensions import connection

class DbContext:
    config: DbSettings
    conn: connection
    @inject
    def __init__(self, config: DbSettings) -> None:
        self.config = config
        self.conn = self.open()

    def open(self) -> connection:
        self.conn = psycopg2.connect(
            dbname      = self.config.dbname, 
            user        = self.config.user, 
            password    = self.config.password, 
            host        = self.config.host, 
            port        = self.config.port
            )
        return self.conn

    def __del__(self):
        if self.conn:
            self.conn.close()