from entities.table_entity import Table, Fields, Field, PrimaryKeys

from valueobjects.data_types import DataTypes

class LeituraTableEntity(Table):

    def __init__(self, name: str):
        super().__init__(name)
        self.fields = Fields(
            [
                Field('leitura_id', DataTypes.serial, True),
                Field('leitura_datahora', DataTypes.timestamp, True)
            ]
        )
        self.primary_keys = PrimaryKeys(
            [
                'leitura_id'
            ]
        )