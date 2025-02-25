from typing import List

class Table:

    def __init__(self, table_name: str, fields: 'Fields'):
        self.table_name = table_name
        self.fields = fields
    
    def insert_many(self, values) -> str:
        sql = f"INSERT INTO {self.table_name}({self.fields.to_string_list()}) values {values};"

class Fields:

    def __init__(self, fields: List['Field'] = []):
        self.fields = fields

    def to_string_list(self):
        return ','.join([field.field_name for field in self.fields])
    
    def add(self, field: 'Field'):
        self.fields.append(field)

class Field:

    def __init__(self, field_name: str):
        self.field_name = field_name