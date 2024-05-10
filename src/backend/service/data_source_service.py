from typing import List
from src.backend.factory.db_context_factory import DbContextFactory
from src.backend.core.data_source import DataSource
from src.backend.core.settings.db_settings import DbSettings


class DataSourceService:
    db_ctx_factory:DbContextFactory

    def __init__(self, db_config: DbSettings) -> None:
        self.db_ctx_factory = DbContextFactory(db_config)

    def new(self, record:DataSource):
        insert_query = "INSERT INTO data_sources (data_source_name, trust_level, updated_by, created_by) VALUES (%s, %s, 'data_source_service', 'data_source_service')"
        with self.db_ctx_factory.new() as conn:
            cur = conn.cursor()
            cur.execute(query=insert_query, vars=[record.name, record.trust_level])
            conn.commit()
        
    def new_batch(self, records:List[DataSource]):
        insert_query = "INSERT INTO data_sources (data_source_name, trust_level, updated_by, created_by) VALUES (%s, %s, 'data_source_service', 'data_source_service')"
        with self.db_ctx_factory.new() as conn:
            cur = conn.cursor()
            cur.executemany(query=insert_query, vars=[[record.name, record.trust_level] for record in records])
            conn.commit()

    def get(self, record_id: int) -> DataSource | None:
        with self.db_ctx_factory.new() as conn:
            cur = conn.cursor()
            query = "SELECT id, data_source_name, trust_level FROM data_sources WHERE id = %s"
            cur.execute(query, (record_id,))
            row = cur.fetchone()
            if row:
                return DataSource(*row)
            else:
                return None

    def get_all(self) -> List[DataSource]:
        with self.db_ctx_factory.new() as conn:
            cur = conn.cursor()
            query = "SELECT id, data_source_name, trust_level FROM data_sources"
            cur.execute(query)
            rows = cur.fetchall()
            return [DataSource(*row) for row in rows]

    def update(self, data_source: DataSource) -> None:
        with self.db_ctx_factory.new() as conn:
            cur = conn.cursor()
            query = "UPDATE data_sources SET data_source_name = %s, trust_level = %s WHERE id = %s"
            cur.execute(query, (data_source.name, data_source.trust_level, data_source.id))
            conn.commit()

    def delete(self, data_source_id: int) -> None:
        with self.db_ctx_factory.new() as conn:
            cur = conn.cursor()
            query = "DELETE FROM data_sources WHERE id = %s"
            cur.execute(query, (data_source_id,))
            conn.commit()