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
    
    def __iter__(self):
        return iter(self.fields)

class Field:

    def __init__(self, name: str, type: str, not_null: bool):
        self.name = name
        self.type = type
        self.not_null = not_null

class Constraints:

    def __init__(self, constraints: List['Constraint'] = []):
        self.constraints = constraints
    
    def __iter__(self):
        return iter(self.constraints)

    def __len__(self):
        return len(self.constraints)

class Constraint:

    def __init__(self, name: str, table_field_name: str, referenced_table_name: str, referenced_table_field_name: str):
        self.name = name
        self.table_field_name = table_field_name
        self.referenced_table_name = referenced_table_name
        self.referenced_table_field_name = referenced_table_field_name

class PrimaryKeys:

    def __init__(self, names: List[str]):
        self.names = names
    
    def __len__(self):
        return len(self.names)