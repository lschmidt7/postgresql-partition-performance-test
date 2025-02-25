class DatabaseEntity:

    def __init__(self, database_name: str):
        self.database_name = database_name
    
    def create(self):
        sql = f'CREATE DATABASE #{self.database_name}'
        return sql