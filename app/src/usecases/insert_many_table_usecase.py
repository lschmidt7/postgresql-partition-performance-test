from ports.database_connection_port import DatabaseConnectionPort

class InsertManyTableUsecase:

    def __init__(self, connection: DatabaseConnectionPort):
        self.connection = connection

    def execute(self) -> None:
        pass