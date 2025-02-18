from psycopg2 import connect

class Database:

    def __init__(self):
        self.config = {
            "dbname": "teste",
            "user": "postgres",
            "password": "root",
            "host": "banco",  # Ou IP do servidor
            "port": "5432"  # Padrão do PostgreSQL
        }
    
    def connect(self):
        self.conn = connect(**self.config)
    
    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()