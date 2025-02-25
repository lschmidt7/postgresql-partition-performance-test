from entities.database_entity import DatabaseEntity

from ports.database_connection_port import DatabaseConnectionPort

class DropDatabaseUsecase:

    def __init__(self, connection: DatabaseConnectionPort):
        self.connection = connection
    
    def execute(self, database_entity: DatabaseEntity) -> None:
        sql = database_entity.get_drop_sql()
        self.connection.run(sql)