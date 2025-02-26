from psycopg2 import connect

from valueobjects.database_configuration import DatabaseConfiguration

from entities.table_entity import Table

class PostgresConnectionAdapter:

    def __init__(self, database_configuration: DatabaseConfiguration):
        self.config = database_configuration.to_dict()
        self.conn = None
        self.cursor = None
    
    def connect(self, autocommit: bool = True) -> None:
        self.conn = connect(**self.config)
        self.conn.autocommit = autocommit
        self.cursor = self.conn.cursor()
        
    def create_database(self, database_name: str):
        sql = f'CREATE DATABASE {database_name}'
        self.run(sql)

    def drop_database(self, database_name: str):
        sql = f'DROP DATABASE {database_name}'
        self.run(sql)
    
    def create_table(self, table_entity: Table):
        fields = ',\n'.join([f'{field.name} {field.type} {'NOT NULL' if field.not_null else ''}' for field in table_entity.fields])

        primary_keys = ''
        primary_key_pattern = ', PRIMARY KEY({})'
        if table_entity.primary_keys and len(table_entity.primary_keys) > 0:
            primary_keys = primary_key_pattern.format(','.join(table_entity.primary_keys.names))
        
        constraints = ''
        constraint_pattern = 'CONSTRAINT {} FOREIGN KEY ({}) REFERENCES {}({})'
        if table_entity.constraints and len(table_entity.constraints) > 0:
            constraints = ',\n'.join([constraint_pattern.format(constraint.name, constraint.table_field_name, constraint.referenced_table_name, constraint.referenced_table_field_name) for constraint in table_entity.constraints])
        
        has_constraints = ',' if len(constraints) > 0 else ''

        sql = f'''
            CREATE TABLE {table_entity.name} (
                {fields}
                {primary_keys} {has_constraints}
                {constraints}
            );
        '''
        self.run(sql)

    def run(self, sql: str):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()