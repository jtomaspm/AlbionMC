from typing import List

from src.core.entities.item import Item
from src.dal.posgres.db_context import DbContext
from injector import inject
from psycopg2.extensions import connection


class ItemRepository:
    conn: connection

    @inject
    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def new(self, record: Item, user_name:str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO items (unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(
                query=query,
                vars=[record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.data_source_id, user_name, user_name]
            )
            self.conn.commit()
    
    def new_batch(self, records:List[Item], user_name: str = "repository"):
        with self.conn.cursor() as cur:
            query = "INSERT INTO items (unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.executemany(query=query, vars=[[record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.data_source_id, user_name, user_name] for record in records])
            self.conn.commit()

    def get(self, record_id: int) -> Item | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_at, updated_by, created_at, created_by  FROM items WHERE id = %s"
            cur.execute(query, (record_id,))
            row = cur.fetchone()
            if row:
                return Item(**{
                    "id" : row[0],
                    "unique_name" : row[1],
                    "name" : row[2],
                    "tags" : row[3],
                    "tier" : row[4],
                    "enchant" : row[5],
                    "description" : row[6],
                    "data_source_id" : row[7],
                    "updated_at" : row[8],
                    "updated_by" : row[9],
                    "created_at" : row[10],
                    "created_by" : row[11],
                })
            else:
                return None

    def get_all(self) -> List[Item]:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_at, updated_by, created_at, created_by FROM items"
            cur.execute(query)
            rows = cur.fetchall()
            return [Item(**{
                    "id" : row[0],
                    "unique_name" : row[1],
                    "name" : row[2],
                    "tags" : row[3],
                    "tier" : row[4],
                    "enchant" : row[5],
                    "description" : row[6],
                    "data_source_id" : row[7],
                    "updated_at" : row[8],
                    "updated_by" : row[9],
                    "created_at" : row[10],
                    "created_by" : row[11],
                }) for row in rows]

    def update(self, record: Item, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE items SET unique_name = %s, english_name = %s, tags = %s, tier = %s, enchant = %s, item_description = %s, data_source_id = %s, updated_by = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s"
            cur.execute(query, (record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.data_source_id, user_name, record.id))
            self.conn.commit()

    def delete(self, record_id: int) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM items WHERE id = %s"
            cur.execute(query, (record_id,))
            self.conn.commit()

    def get_by_unique_name(self, unique_name: str) -> Item | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_at, updated_by, created_at, created_by  FROM items WHERE unique_name = %s"
            cur.execute(query, (unique_name,))
            row = cur.fetchone()
            if row:
                return Item(**{
                    "id" : row[0],
                    "unique_name" : row[1],
                    "name" : row[2],
                    "tags" : row[3],
                    "tier" : row[4],
                    "enchant" : row[5],
                    "description" : row[6],
                    "data_source_id" : row[7],
                    "updated_at" : row[8],
                    "updated_by" : row[9],
                    "created_at" : row[10],
                    "created_by" : row[11],
                })
            else:
                return None

    def get_by_name(self, name: str) -> Item | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_at, updated_by, created_at, created_by  FROM items WHERE name = %s"
            cur.execute(query, (name,))
            row = cur.fetchone()
            if row:
                return Item(**{
                    "id" : row[0],
                    "unique_name" : row[1],
                    "name" : row[2],
                    "tags" : row[3],
                    "tier" : row[4],
                    "enchant" : row[5],
                    "description" : row[6],
                    "data_source_id" : row[7],
                    "updated_at" : row[8],
                    "updated_by" : row[9],
                    "created_at" : row[10],
                    "created_by" : row[11],
                })
            else:
                return None