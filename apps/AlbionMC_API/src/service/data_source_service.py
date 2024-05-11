from typing import List

from src.core.data_source import DataSource
from src.dal.posgres.db_context import DbContext
from injector import Injector
from psycopg2.extensions import connection


class DataSourceService:
    conn: connection

    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def new(self, record:DataSource):
        with self.conn.cursor() as cur:
            query = "INSERT INTO data_sources (data_source_name, trust_level, updated_by, created_by) VALUES (%s, %s, 'data_source_service', 'data_source_service')"
            cur.execute(query=query, vars=[record.name, record.trust_level])
            self.conn.commit()
        
    def new_batch(self, records:List[DataSource]):
        with self.conn.cursor() as cur:
            query = "INSERT INTO data_sources (data_source_name, trust_level, updated_by, created_by) VALUES (%s, %s, 'data_source_service', 'data_source_service')"
            cur.executemany(query=query, vars=[[record.name, record.trust_level] for record in records])
            self.conn.commit()

    def get(self, record_id: int) -> DataSource | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, data_source_name, trust_level FROM data_sources WHERE id = %s"
            cur.execute(query, (record_id,))
            row = cur.fetchone()
            if row:
                return DataSource(*row)
            else:
                return None

    def get_all(self) -> List[DataSource]:
        with self.conn.cursor() as cur:
            query = "SELECT id, data_source_name, trust_level FROM data_sources"
            cur.execute(query)
            rows = cur.fetchall()
            return [DataSource(*row) for row in rows]

    def update(self, record: DataSource) -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE data_sources SET data_source_name = %s, trust_level = %s WHERE id = %s"
            cur.execute(query, (record.name, record.trust_level, record.id))
            self.conn.commit()

    def delete(self, record_id: int) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM data_sources WHERE id = %s"
            cur.execute(query, (record_id,))
            self.conn.commit()