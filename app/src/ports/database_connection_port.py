from abc import ABC, abstractmethod

class DatabaseConnectionPort(ABC):

    @abstractmethod
    def run(self):
        pass