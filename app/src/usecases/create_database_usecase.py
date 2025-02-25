from entities.database_entity import DatabaseEntity

from ports.database_connection_port import DatabaseConnectionPort

class CreateDatabaseUsecase:

    def __init__(self, database_connection_port: DatabaseConnectionPort):
        self.database_connection_port = database_connection_port

    def execute(self, database_entity: DatabaseEntity):
        sql = database_entity.get_create_sql()
        self.database_connection_port.run(sql)