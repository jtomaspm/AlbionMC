import datetime
from typing import List
from src.core.entities.item_price import ItemPrice
from src.dal.posgres.db_context import DbContext
from injector import inject
from psycopg2.extensions import connection

class ItemPriceRepository:
    conn: connection

    @inject
    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def new(self, record: ItemPrice, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO item_prices (item_id, price, city, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(
                query=query,
                vars=[record.item_id, record.price, record.city, record.data_source_id, user_name, user_name]
            )
            self.conn.commit()

    def new_batch(self, records: List[ItemPrice], user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO item_prices (item_id, price, city, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.executemany(query=query, vars=[[record.item_id, record.price, record.city, record.data_source_id, user_name, user_name] for record in records])
            self.conn.commit()

    def get(self, item_id: int, created_at: datetime) -> ItemPrice | None:
        with self.conn.cursor() as cur:
            query = "SELECT item_id, price, city, data_source_id, updated_at, updated_by, created_at, created_by FROM item_prices WHERE item_id = %s AND created_at = %s"
            cur.execute(query, (item_id, created_at))
            row = cur.fetchone()
            if row:
                return ItemPrice(**{
                    "item_id" : row[0],
                    "price" : row[1],
                    "city" : row[2],
                    "data_source_id" : row[3],
                    "updated_at" : row[4],
                    "updated_by" : row[5],
                    "created_at" : row[6],
                    "created_by" : row[7],
                })
            else:
                return None

    def get_all(self) -> List[ItemPrice]:
        with self.conn.cursor() as cur:
            query = "SELECT item_id, price, city, data_source_id, updated_at, updated_by, created_at, created_by FROM item_prices"
            cur.execute(query)
            rows = cur.fetchall()
            return [ItemPrice(*row) for row in rows]

    def update(self, record: ItemPrice, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE item_prices SET price = %s, city = %s, data_source_id = %s, updated_by = %s, updated_at = CURRENT_TIMESTAMP WHERE item_id = %s AND created_at = %s"
            cur.execute(query, (record.price, record.city, record.data_source_id, user_name, record.item_id, record.created_at))
            self.conn.commit()

    def delete(self, item_id: int, created_at: datetime) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM item_prices WHERE item_id = %s AND created_at = %s"
            cur.execute(query, (item_id, created_at))
            self.conn.commit()