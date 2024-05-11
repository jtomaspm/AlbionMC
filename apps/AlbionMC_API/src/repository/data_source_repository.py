from typing import List

from injector import inject

from src.core.entities.data_source import DataSource
from src.dal.posgres.db_context import DbContext
from psycopg2.extensions import connection


class DataSourceRepository:
    conn: connection

    @inject
    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def new(self, record: DataSource, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO data_sources (data_source_name, trust_level, updated_by, created_by) VALUES (%s, %s, %s, %s)"
            cur.execute(
                query=query,
                vars=[record.name, record.trust_level, user_name, user_name]
            )
            self.conn.commit()

    def new_batch(self, records: List[DataSource], user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO data_sources (data_source_name, trust_level, updated_by, created_by) VALUES (%s, %s, %s, %s)"
            cur.executemany(query=query, vars=[[record.name, record.trust_level, user_name, user_name] for record in records])
            self.conn.commit()

    def get(self, record_id: int) -> DataSource | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, data_source_name, trust_level, updated_at, updated_by, created_at, created_by FROM data_sources WHERE id = %s"
            cur.execute(query, (record_id,))
            row = cur.fetchone()
            if row:
                return DataSource(*row)
            else:
                return None

    def get_all(self) -> List[DataSource]:
        with self.conn.cursor() as cur:
            query = "SELECT id, data_source_name, trust_level, updated_at, updated_by, created_at, created_by FROM data_sources"
            cur.execute(query)
            rows = cur.fetchall()
            return [DataSource(*row) for row in rows]

    def update(self, record: DataSource, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE data_sources SET data_source_name = %s, trust_level = %s, updated_by = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s"
            cur.execute(query, (record.name, record.trust_level, user_name, record.id))
            self.conn.commit()

    def delete(self, record_id: int) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM data_sources WHERE id = %s"
            cur.execute(query, (record_id,))
            self.conn.commit()