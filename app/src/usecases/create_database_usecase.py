from src.entities.database_entity import DatabaseEntity

from src.ports.database_connection_port import DatabaseConnectionPort

class CreateDatabaseUsecase:

    def __ini__(self, database_entity: DatabaseEntity, database_connection_port: DatabaseConnectionPort):
        pass