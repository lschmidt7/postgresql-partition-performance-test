from entities.database_entity import DatabaseEntity

from ports.database_connection_port import DatabaseConnectionPort

class DropDatabaseUsecase:

    def __init__(self, connection: DatabaseConnectionPort):
        self.connection = connection
    
    def execute(self, database_entity: DatabaseEntity) -> None:
        database_name = database_entity.get_database_name()
        self.connection.drop_database(database_name)