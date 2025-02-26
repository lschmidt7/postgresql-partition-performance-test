class DatabaseEntity:

    def __init__(self, database_name: str):
        self.database_name = database_name
    
    def get_database_name(self) -> str:
        return self.database_name