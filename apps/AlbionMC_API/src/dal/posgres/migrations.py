import os
from pathlib import Path
import subprocess
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, connection



def ensure_database(conn:connection, dbname:str):
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
        exists = cur.fetchone()

        if exists:
            print(f"Database '{dbname}' already exists.")
        else:
            cur.execute(f"CREATE DATABASE {dbname}")
            print(f"Database '{dbname}' created successfully.")

        conn.commit()

def ensure_migrations_table(conn: connection):
    with conn.cursor() as cur:
        cur.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'migration_origin') THEN
                    CREATE TYPE migration_origin AS ENUM ('sql', 'python');
                END IF;
            END
            $$;
        """)
        cur.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'migration_type') THEN
                    CREATE TYPE migration_type AS ENUM ('schema', 'data-seed');
                END IF;
            END
            $$;
        """)
        conn.commit()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                origin migration_origin NOT NULL DEFAULT 'sql',
                type migration_type NOT NULL DEFAULT 'schema',
                applied_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()


def get_applied_migrations(conn: connection):
    with conn.cursor() as cur:
        cur.execute("SELECT name FROM migrations")
        return {row[0] for row in cur.fetchall()}


def get_migration_files(migrations_folder: str) -> tuple[list[str], list[str]]:
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
                cur.execute("INSERT INTO migrations (name, type, origin) VALUES (%s, %s, %s)", (migration_name, migration_type, 'sql'))
                conn.commit()
                print(f"[INFO] Sql migration applied: {migration_name}")
            except psycopg2.Error as e:
                conn.rollback()
                print(f"[ERROR] Failed to apply sql migration {migration_name}: {e}")
        return
    try:
        if not script_path.endswith('.py'):
            raise ValueError(f"Unsupported migration file type: {script_path}")
        script_path = os.path.abspath(script_path)
        sys.path.append(os.path.dirname(script_path))
        migration_module = Path(script_path).stem
        migration_func = __import__(migration_module, fromlist=['migrate']).migrate
        if not callable(migration_func):
            raise ValueError(f"Migration function 'migrate' not found in {migration_module}")
        migration_func(conn)

        with conn.cursor() as cur:
            cur.execute("INSERT INTO migrations (name, type, origin) VALUES (%s, %s, %s)", (migration_name, migration_type, 'python'))
            conn.commit()
            print(f"[INFO] Python migration applied: {migration_name}")
    except Exception as e:
        print(f"[ERROR] Failed to apply python migration {migration_name}: {e}")
        raise
        
def list_all_files(directory):
    return [str(path) for path in Path(directory).rglob("*") if path.is_file()]


def migrate(migrations_folder: str, conn: connection, dbname: str = 'AlbionMC'):
    ensure_database(conn, dbname)
    ensure_migrations_table(conn)

    applied = get_applied_migrations(conn)
    schema_files, data_seed_files = get_migration_files(migrations_folder)

    for file in schema_files:
        if file in applied:
            print(f"[INFO] Skipping already applied migration: {file}")
            continue
        apply_migration(conn, file, file.removeprefix(migrations_folder), 'schema')
    for file in data_seed_files:
        if file in applied:
            print(f"[INFO] Skipping already applied migration: {file}")
            continue
        apply_migration(conn, file, file.removeprefix(migrations_folder), 'data-seed')

    print("[INFO] All migrations applied successfully.")