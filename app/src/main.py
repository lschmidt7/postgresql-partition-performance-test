from usecases.drop_database_usecase import DropDatabaseUsecase
from usecases.create_database_usecase import CreateDatabaseUsecase

from entities.database_entity import DatabaseEntity

from adapters.connection_database_adapter import ConnectionDatabaseAdapter

connection_database_adapter = ConnectionDatabaseAdapter()
connection_database_adapter.connect()

database_entity = DatabaseEntity('cloud')

drop_database_usecase = DropDatabaseUsecase(connection_database_adapter)
drop_database_usecase.execute(database_entity)

create_database_usecase = CreateDatabaseUsecase(connection_database_adapter)
create_database_usecase.execute(database_entity)

# from app.src.adapters.connection import Database
# from generators.leitura import Leitura
# from generators.leitura_dados import LeituraDados

# inserts = 10000000
# batch = 10000

# database = Database()
# database.connect()

# cur = database.get_cursor()

# sql_leitura = "INSERT INTO leitura (leitura_datahora) VALUES %s;"
# sql_leitura_dados = "INSERT INTO leitura_dados (leitura_dados_chave, leitura_dados_valor, leitura_id) VALUES %s;"

# leitura = Leitura()
# leitura_dados = LeituraDados()

# leitura_id = 1

# for i in range(0, inserts, batch):

#     dados = []
#     for j in range(batch):
#         leitura_atual = leitura.mount()
#         dados.append(leitura_atual)
#         leitura.incrase()
#     dados = ','.join(dados)
#     insert_leituras = sql_leitura % dados

#     dados = []
#     for j in range(batch):
#         for k in range(10):
#             leitura_atual = leitura_dados.mount(k,leitura_id)
#             dados.append(leitura_atual)
#         leitura_id += 1
#     dados = ','.join(dados)
#     insert_leituras_dados = sql_leitura_dados % dados

#     cur.execute(insert_leituras)
#     cur.execute(insert_leituras_dados)

#     database.commit()

#     print(f'{i / inserts}:.2f')