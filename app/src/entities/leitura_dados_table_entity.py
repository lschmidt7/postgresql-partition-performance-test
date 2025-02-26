from entities.table_entity import Table, Fields, Field, Constraints, Constraint, PrimaryKeys

from valueobjects.data_types import DataTypes

class LeituraDadosTableEntity(Table):

    def __init__(self, name: str):
        super().__init__(name)
        self.fields = Fields(
            [
                Field('leitura_dados_id', DataTypes.serial, True),
                Field('leitura_dados_chave', DataTypes.integer, True),
                Field('leitura_dados_valor', DataTypes.float, True),
                Field('leitura_id', DataTypes.integer, True),
            ]
        )
        self.primary_keys = PrimaryKeys(
            [
                'leitura_dados_id'
            ]
        )
        self.constraints = Constraints(
            [
                Constraint('fk_leitura_id', 'leitura_id', 'leitura', 'leitura_id')
            ]
        )