from db import Database

inserts = 10000000
batch = 10000

database = Database()
database.connect()

cur = database.get_cursor()

sql = "INSERT INTO leitura (leitura_datahora) VALUES %s;"

segundo = 1
minuto = 0
hora = 0
dia = 1
mes = 1
ano = 2025

for i in range(0, inserts, batch):

    dados = []

    for j in range(batch):
        dados.append(f"('{str(ano).zfill(2)}-{str(mes).zfill(2)}-{str(dia).zfill(2)} {str(hora).zfill(2)}:{str(minuto).zfill(2)}:{str(segundo).zfill(2)}')")

        segundo += 1
        
        if segundo >= 60:
            segundo = 0
            minuto += 1
        
        if minuto >= 60:
            minuto = 0
            hora += 1
        
        if hora >= 24:
            hora = 0
            dia += 1
        
        if dia >= 28:
            dia = 1
            mes += 1
        
        if mes > 12:
            mes = 1
            ano += 1
    
    dados = ','.join(dados)

    insert = sql % dados

    cur.execute(insert)

    database.commit()

    print(f'{i / inserts}:.2f')