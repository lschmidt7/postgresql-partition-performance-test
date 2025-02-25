from psycopg2 import connect

class Connection:

    def __init__(self):
        self.config = {
            "dbname": "teste",
            "user": "postgres",
            "password": "root",
            "host": "banco",  # Ou IP do servidor
            "port": "5432"  # Padrão do PostgreSQL
        }
        self.conn = None
        self.cursor = None
    
    def connect(self):
        self.conn = connect(**self.config)
        self.cursor = self.conn.cursor()
    
    def run(self, sql: str):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()