from typing import List

from injector import Injector
from src.backend.core.item import Item
from src.backend.dal.posgres.db_context import DbContext
from psycopg2.extensions import connection


class ItemService:
    conn: connection

    def __init__(self, injector: Injector) -> None:
        self.conn = injector.get(DbContext).conn

    def new(self, record) -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO items (unique_name, name, tags, tier, enchant, description) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(
                query=query,
                vars=[record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description]
            )
            self.conn.commit()

    def get(self, record_id: int) -> Item | None:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, name, tags, tier, enchant, description FROM items WHERE id = %s"
            cur.execute(query, (record_id,))
            row = cur.fetchone()
            if row:
                return Item(*row)
            else:
                return None

    def get_all(self) -> List[Item]:
        with self.conn.cursor() as cur:
            query = "SELECT id, unique_name, name, tags, tier, enchant, description FROM items"
            cur.execute(query)
            rows = cur.fetchall()
            return [Item(*row) for row in rows]

    def update(self, record: Item) -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE items SET unique_name = %s, name = %s, tags = %s, tier = %s, enchant = %s, description = %s WHERE id = %s"
            cur.execute(query, (record.unique_name, record.name, record.tags, record.tier, record.enchant, record.description, record.id))
            self.conn.commit()

    def delete(self, record_id: int) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM items WHERE id = %s"
            cur.execute(query, (record_id,))
            self.conn.commit()