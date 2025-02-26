from typing import List

class Table:

    def __init__(self, name: str):
        self.name : str = name
        self.fields : Fields = None
        self.constraints : Constraints = None
        self.primary_keys : PrimaryKeys = None
    
    def get_table_name(self) -> str:
        return self.name

    def __getitem__(self, key: str):
        return self.fields[key]

class Fields:

    def __init__(self, fields: List['Field'] = []):
        self.fields = fields

    def to_list(self):
        return ','.join([field.name for field in self.fields])
    
    def add(self, field: 'Field'):
        self.fields.append(field)

class Field:

    def __init__(self, name: str, type: str, not_null: bool):
        self.name = name
        self.type = type
        self.not_null = not_null

class Constraints:

    def __init__(self, constraints: List['Constraint'] = []):
        self.constraints = constraints

class Constraint:

    def __init__(self, name: str, table_field_name: str, referenced_table_name: str, referenced_table_field_name: str):
        self.name = name
        self.table_field_name = table_field_name
        self.referenced_table_name = referenced_table_name
        self.referenced_table_field_name = referenced_table_field_name

class PrimaryKeys:

    def __init__(self, names: List[str]):
        self.names = names