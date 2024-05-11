import os
import psycopg2

MIGRATIONS_FOLDER = os.path.dirname(os.path.realpath(__file__))

def execute_sql_script(connection, script_path: str):
    with open(script_path, 'r') as f:
        sql_script = f.read()
        cursor = connection.cursor()
        try:
            cursor.execute(sql_script)
            connection.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error executing script '{script_path}': {e}")
            connection.rollback()
            return False

def run_migrations(connection):
    sql_files = sorted([file for file in os.listdir(MIGRATIONS_FOLDER) if file.endswith('.sql')], key=lambda x: int(x[:3]))

    for script_file in sql_files:
        script_path = os.path.join(MIGRATIONS_FOLDER, script_file)
        execute_sql_script(connection, script_path)
        print(f"Executed script: {script_file}")