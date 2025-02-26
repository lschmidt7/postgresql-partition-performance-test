from psycopg2 import connect

from valueobjects.database_configuration import DatabaseConfiguration

class PostgresConnectionAdapter:

    def __init__(self, database_configuration: DatabaseConfiguration):
        self.config = database_configuration.to_dict()
        self.conn = None
        self.cursor = None
    
    def connect(self) -> None:
        self.conn = connect(**self.config)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        
    def create_database(self, database_name: str):
        sql = f'CREATE DATABASE {database_name}'
        self.run(sql)

    def drop_database(self, database_name: str):
        sql = f'DROP DATABASE {database_name}'
        self.run(sql)

    def run(self, sql: str):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()