class DatabaseEntity:

    def __init__(self, database_name: str):
        self.database_name = database_name
    
    def get_create_sql(self):
        sql = f'CREATE DATABASE {self.database_name}'
        return sql

    def get_drop_sql(self):
        sql = f'DROP DATABASE IF EXISTS {self.database_name}'
        return sql