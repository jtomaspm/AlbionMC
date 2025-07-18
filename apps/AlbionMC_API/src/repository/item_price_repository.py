import datetime
from typing import Dict, List

from fastapi import HTTPException
from src.core.entities.item import Item
from src.repository.item_repository import ItemRepository
from src.core.entities.item_price import ItemPrice
from src.dal.posgres.db_context import DbContext
from injector import inject
from psycopg2.extensions import connection

class ItemPriceRepository:
    conn: connection
    item_repo: ItemRepository

    @inject
    def __init__(self, ctx: DbContext, item_repo: ItemRepository) -> None:
        self.conn = ctx.conn
        self.item_repo = item_repo

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
            cur.executemany(query=query, vars_list=[[record.item_id, record.price, record.city, record.data_source_id, user_name, user_name] for record in records])
            self.conn.commit()

    def get(self, item_id: int, created_at: datetime.datetime) -> ItemPrice | None:
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
            return [ItemPrice(**{
                "item_id" : row[0],
                "price" : row[1],
                "city" : row[2],
                "data_source_id" : row[3],
                "updated_at" : row[4],
                "updated_by" : row[5],
                "created_at" : row[6],
                "created_by" : row[7],
            }) for row in rows]

    def update(self, record: ItemPrice, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE item_prices SET price = %s, city = %s, data_source_id = %s, updated_by = %s, updated_at = CURRENT_TIMESTAMP WHERE item_id = %s AND created_at = %s"
            cur.execute(query, (record.price, record.city, record.data_source_id, user_name, record.item_id, record.created_at))
            self.conn.commit()

    def delete(self, item_id: int, created_at: datetime.datetime) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM item_prices WHERE item_id = %s AND created_at = %s"
            cur.execute(query, (item_id, created_at))
            self.conn.commit()

    def new_from_item(self, item: Item, record: ItemPrice, user_name: str) -> None:
        result = None
        if(item.id):
            pass
        elif(item.unique_name != ""):
            result = self.item_repo.get_by_unique_name(item.unique_name)
        elif(item.name != ""):
            result = self.item_repo.get_by_name(item.name)
        else:
            raise HTTPException(status_code=404, detail={"error":"Item not found..."})
        if result == None:
            raise HTTPException(status_code=404, detail={"error":"Item not found..."})
        record.item_id = item.id
        self.new(record=record,user_name=user_name)
        
    def new_batch_from_items(self, data: Dict[Item, ItemPrice], user_name: str) -> None:
        for item, record in data.items():
            if(item.id):
                pass
            elif(item.unique_name != ""):
                item = self.item_repo.get_by_unique_name(item.unique_name)
            elif(item.name != ""):
                item = self.item_repo.get_by_name(item.name)
            else:
                raise HTTPException(status_code=404, detail={"error":"Item not found..."})
            if item == None:
                raise HTTPException(status_code=404, detail={"error":"Item not found..."})
            record.item_id = item.id
        self.new_batch(records=list(data.values()), user_name=user_name)
        

