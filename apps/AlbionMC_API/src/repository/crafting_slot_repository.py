from typing import List
from src.core.entities.crafting_slot import CraftingSlot
from src.dal.posgres.db_context import DbContext
from injector import inject
from psycopg2.extensions import connection


class CraftingSlotRepository:
    conn: connection

    @inject
    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def new(self, record: CraftingSlot, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO crafting_slots (craft_id, destination_item_id, source_item_id, source_item_quantity, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(
                query=query,
                vars=[record.craft_id, record.destination_item_id, record.source_item_id, record.source_item_quantity, record.data_source_id, user_name, user_name]
            )
            self.conn.commit()

    def new_batch(self, records: List[CraftingSlot], user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "INSERT INTO crafting_slots (craft_id, destination_item_id, source_item_id, source_item_quantity, data_source_id, updated_by, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.executemany(query=query, vars_list=[[record.craft_id, record.destination_item_id, record.source_item_id, record.source_item_quantity, record.data_source_id, user_name, user_name] for record in records])
            self.conn.commit()

    def get(self, craft_id: int, destination_item_id: int, source_item_id: int) -> CraftingSlot | None:
        with self.conn.cursor() as cur:
            query = "SELECT craft_id, destination_item_id, source_item_id, source_item_quantity, data_source_id, updated_at, updated_by, created_at, created_by FROM crafting_slots WHERE craft_id = %s AND destination_item_id = %s AND source_item_id = %s"
            cur.execute(query, (craft_id, destination_item_id, source_item_id))
            row = cur.fetchone()
            if row:
                return CraftingSlot(**{
                    "craft_id" : row[0],
                    "destination_item_id" : row[1],
                    "source_item_id" : row[2],
                    "source_item_quantity" : row[3],
                    "data_source_id" : row[4],
                    "updated_at" : row[5],
                    "updated_by" : row[6],
                    "created_at" : row[7],
                    "created_by" : row[8],
                })
            else:
                return None

    def get_all(self) -> List[CraftingSlot]:
        with self.conn.cursor() as cur:
            query = "SELECT craft_id, destination_item_id, source_item_id, source_item_quantity, data_source_id, updated_at, updated_by, created_at, created_by FROM crafting_slots"
            cur.execute(query)
            rows = cur.fetchall()
            return [CraftingSlot(**{
                    "craft_id" : row[0],
                    "destination_item_id" : row[1],
                    "source_item_id" : row[2],
                    "source_item_quantity" : row[3],
                    "data_source_id" : row[4],
                    "updated_at" : row[5],
                    "updated_by" : row[6],
                    "created_at" : row[7],
                    "created_by" : row[8],
                }) for row in rows]

    def update(self, record: CraftingSlot, user_name: str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = "UPDATE crafting_slots SET source_item_quantity = %s, data_source_id = %s, updated_by = %s, updated_at = CURRENT_TIMESTAMP WHERE craft_id = %s AND destination_item_id = %s AND source_item_id = %s"
            cur.execute(query, (record.source_item_quantity, record.data_source_id, user_name, record.craft_id, record.destination_item_id, record.source_item_id))
            self.conn.commit()

    def delete(self, craft_id: int, destination_item_id: int, source_item_id: int) -> None:
        with self.conn.cursor() as cur:
            query = "DELETE FROM crafting_slots WHERE craft_id = %s AND destination_item_id = %s AND source_item_id = %s"
            cur.execute(query, (craft_id, destination_item_id, source_item_id))
            self.conn.commit()