from typing import Dict

class DatabaseConfiguration:

    def __init__(self, user: str, password: str, host: str, port: int, database: str = None):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
    
    def to_dict(self) -> Dict:
        config = {
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port
        }
        if self.database is not None:
            config['database'] = self.database
        return config