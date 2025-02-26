from ports.database_connection_port import DatabaseConnectionPort

from entities.table_entity

class CreateTableUsecase:

    def __init__(self, database_connection_port: DatabaseConnectionPort):
        self.database_connection_port = database_connection_port
    
    def execute(self, table_entity: T):
        pass