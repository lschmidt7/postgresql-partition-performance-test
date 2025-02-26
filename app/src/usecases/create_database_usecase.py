from entities.database_entity import DatabaseEntity

from ports.database_connection_port import DatabaseConnectionPort

class CreateDatabaseUsecase:

    def __init__(self, database_connection_port: DatabaseConnectionPort):
        self.database_connection_port = database_connection_port

    def execute(self, database_entity: DatabaseEntity) -> None:
        database_name = database_entity.get_database_name()
        self.database_connection_port.create_database(database_name)