import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.append(project_root)


import psycopg2
from src.backend.dal.posgres.migrations.migrations import run_migrations

def test_migrations():
    dbname = 'AlbionMC'
    user = 'admin'
    password = 'Albionmc123?'
    host = 'localhost' 
    port = '5432' 

    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    run_migrations(connection=connection)

    connection.close()

if __name__ == "__main__":
    test_migrations()