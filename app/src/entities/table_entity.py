from typing import List

class Table:

    def __init__(self, table_name: str, fields: 'Fields'):
        self.table_name = table_name
        self.fields = fields
    
    def get_table_name(self) -> str:
        return self.table_name

class Fields:

    def __init__(self, fields: List['Field'] = []):
        self.fields = fields

    def to_list(self):
        return ','.join([field.name for field in self.fields])
    
    def add(self, field: 'Field'):
        self.fields.append(field)

class Field:

    def __init__(self, name: str):
        self.name = name