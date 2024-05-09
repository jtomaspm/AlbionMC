from typing import List
from src.backend.factory.db_context_factory import DbContextFactory
from src.backend.core.data_source import DataSource
from src.backend.core.settings.db_settings import DbSettings

insert_query = """
INSERT INTO data_sources 
    (data_source_name, trust_level, updated_by, created_by) 
VALUES 
    (%s, %s, 'data_source_service', 'data_source_service')
"""

def new_data_source(ds:DataSource, db_config: DbSettings):
    dbcf = DbContextFactory(db_config)
    with dbcf.new() as conn:
        cur = conn.cursor()
        cur.execute(query=insert_query, vars=[ds.name, ds.trust_level])
        conn.commit()
        
def new_data_sources(dss:List[DataSource], db_config: DbSettings):
    dbcf = DbContextFactory(db_config)
    with dbcf.new() as conn:
        cur = conn.cursor()
        cur.executemany(query=insert_query, vars=[[ds.name, ds.trust_level] for ds in dss])
        conn.commit()
        