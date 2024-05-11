from typing import List

from src.core.item import Item
from src.dal.posgres.db_context import DbContext
from injector import inject
from psycopg2.extensions import connection


class ItemRepository:
    conn: connection

    @inject
    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def new(self, record: Item) -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO items (unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, 'item_service', 'item_service')"
            cur.execute(
                query=query,
                vars=[record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.data_source_id]
            )
            self.conn.commit()
    
    def new_batch(self, records:List[Item]):
        with self.conn.cursor() as cur:
            query = "INSERT INTO items (unique_name, english_name, tags, tier, enchant, item_description, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, 'item_service', 'item_service')"
            cur.executemany(query=query, vars=[[record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.data_source_id] for record in records])
            self.conn.commit()

    def get(self, record_id: int) -> Item | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, english_name, tags, tier, enchant, item_description, data_source_id FROM items WHERE id = %s"
            cur.execute(query, (record_id,))
            row = cur.fetchone()
            if row:
                return Item(*row)
            else:
                return None

    def get_all(self) -> List[Item]:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, english_name, tags, tier, enchant, item_description, data_source_id FROM items"
            cur.execute(query)
            rows = cur.fetchall()
            return [Item(*row) for row in rows]

    def update(self, record: Item) -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE items SET unique_name = %s, english_name = %s, tags = %s, tier = %s, enchant = %s, item_description = %s, data_source_id = %s, updated_by = 'item_service', updated_at = CURRENT_TIMESTAMP WHERE id = %s"
            cur.execute(query, (record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.data_source_id, record.id))
            self.conn.commit()

    def delete(self, record_id: int) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM items WHERE id = %s"
            cur.execute(query, (record_id,))
            self.conn.commit()