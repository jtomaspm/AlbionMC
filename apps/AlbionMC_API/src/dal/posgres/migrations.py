import os
from pathlib import Path
import subprocess
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, connection



def ensure_database(conn:connection, dbname:str):
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
    exists = cur.fetchone()

    if exists:
        print(f"Database '{dbname}' already exists.")
    else:
        cur.execute(f"CREATE DATABASE {dbname}")
        print(f"Database '{dbname}' created successfully.")

    cur.close()
    conn.close()

def ensure_migrations_table(conn: connection):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TYPE migration_origin AS ENUM ('sql', 'python');
        """)
        cur.execute("""
            CREATE TYPE migration_type AS ENUM ('schema', 'data-seed');
        """)
        conn.commit()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                origin migration_origin NOT NULL DEFAULT 'sql',
                type migration_type NOT NULL DEFAULT 'migration',
                applied_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()


def get_applied_migrations(conn: connection):
    with conn.cursor() as cur:
        cur.execute("SELECT name FROM migrations")
        return {row[0] for row in cur.fetchall()}


def get_migration_files(migrations_folder: str) -> tuple[list, list]:
    return (
        sorted(
            [f for f in list_all_files(os.path.join(migrations_folder, 'schema')) if f.endswith('.sql') or f.endswith('.py')],
            key=lambda x: x
        ), 
        sorted(
            [f for f in list_all_files(os.path.join(migrations_folder, 'data-seed')) if f.endswith('.sql') or f.endswith('.py')],
            key=lambda x: x
        ))


def apply_migration(conn: connection, script_path: str, migration_name: str, migration_type='schema'):
    if script_path.endswith('.sql'):
        with open(script_path, 'r') as f:
            sql = f.read()

        with conn.cursor() as cur:
            try:
                cur.execute(sql)
                cur.execute("INSERT INTO migrations (name, type, origin) VALUES (%s)", (migration_name, migration_type, 'sql'))
                conn.commit()
                print(f"[INFO] Sql migration applied: {migration_name}")
            except psycopg2.Error as e:
                conn.rollback()
                print(f"[ERROR] Failed to apply sql migration {migration_name}: {e}")
                raise
        return
    try:
        subprocess.run(['python', script_path], check=True)
        with conn.cursor() as cur:
            cur.execute("INSERT INTO migrations (name, type, origin) VALUES (%s)", (migration_name, migration_type, 'python'))
            conn.commit()
            print(f"[INFO] Python migration applied: {migration_name}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to apply python migration {migration_name}: {e}")
        raise
        
def list_all_files(directory):
    return [str(path) for path in Path(directory).rglob("*") if path.is_file()]


def migrate(migrations_folder: str, dbname: str, user: str, password: str, host='localhost', port='5432'):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    ensure_database(conn, dbname)
    ensure_migrations_table(conn)

    applied = get_applied_migrations(conn)
    schema_files, data_seed_files = get_migration_files(migrations_folder)

    for file in schema_files:
        if file in applied:
            print(f"[INFO] Skipping already applied migration: {file}")
            continue
        apply_migration(conn, file, file, 'schema')
    for file in data_seed_files:
        if file in applied:
            print(f"[INFO] Skipping already applied migration: {file}")
            continue
        apply_migration(conn, file, file, 'data-seed')

    conn.close()
    print("[INFO] All migrations applied successfully.")