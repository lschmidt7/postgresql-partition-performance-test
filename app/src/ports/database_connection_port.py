from abc import ABC, abstractmethod

class DatabaseConnectionPort(ABC):

    @abstractmethod
    def connect() -> None:
        pass

    @abstractmethod
    def disconnect() -> None:
        pass

    @abstractmethod
    def create_database(self, database_name: str) -> None:
        pass

    @abstractmethod
    def drop_database(self, database_name: str) -> None:
        pass