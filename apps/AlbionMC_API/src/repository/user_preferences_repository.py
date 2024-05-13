from src.core.entities.user_preference import UserPreference
from src.dal.posgres.db_context import DbContext
from injector import inject
from psycopg2.extensions import connection


class UserPreferencesRepository:
    conn: connection

    @inject
    def __init__(self, ctx: DbContext) -> None:
        self.conn = ctx.conn

    def set(self, record: UserPreference, user_name:str = "repository") -> None:
        with self.conn.cursor() as cur:
            query = f"""
                    IF EXISTS(SELECT * FROM user_preferences WHERE user_id=%s) THEN
                        UPDATE user_preferences SET theme=%s, updated_at=CURRENT_TIMESTAMP, updated_by=%s WHERE user_id=%s;
                    ELSE
                        INSERT INTO user_preferences(user_id, theme, updated_by, created_by) VALUES(%s,%s,%s,%s);
                    END IF;
                    """
            select_vars = [record.user_id]
            update_vars = [record.theme, user_name,record.user_id]
            insert_vars = [record.user_id, record.theme, user_name, user_name]
            cur.execute(
                query=query,
                vars=select_vars+update_vars+insert_vars
            )
            self.conn.commit()
    
    def get(self, user_id: int) -> UserPreference | None:
        with self.conn.cursor() as cur:
            query = "SELECT user_id, theme FROM item_prices WHERE user_id=%s"
            cur.execute(query, (user_id))
            row = cur.fetchone()
            if row:
                return UserPreference(**{
                    "user_id" : row[0],
                    "theme" : row[1],
                })
            else:
                return None