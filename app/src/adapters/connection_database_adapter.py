from psycopg2 import connect

class ConnectionDatabaseAdapter:

    def __init__(self):
        self.config = {
            "user": "postgres",
            "password": "root",
            "host": "banco",  # Ou IP do servidor
            "port": "5432"  # Padrão do PostgreSQL
        }
        self.conn = None
        self.cursor = None
    
    def connect(self):
        self.conn = connect(**self.config)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
    
    def run(self, sql: str):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()