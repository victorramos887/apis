import psycopg2 as pg

print('Conectando ...')

try:
    conn = pg.connect(host = 'localhost',
                      user = 'postgres',
                      password = 'postgres',
                      database = 'alura')

except pg.connect.Error as e:
    print(e)


cursor = conn.cursor()

#CRIANDO BANCO DE DADOS

cursor.execute("DROP DATABASE IF EXISTS 'jogoteca';")
cursor.execute("CREATE DATADBASE 'jogoteca';")
cursor.execute("USER 'jogoteca';")


TABLES = {}

TABLES['Jogos'] = (
    """
    CRETE TABLE cursoflask.'jogos' (
        'id' SERIAL PRIMARY KEY,
        'nome' VARCHAR(50) NOT NULL,
        'categoria' VARCHAR(40) NOT NULL,
        'console' VARCHAR(20) NOT NULL,
    )
    """
)


TABLES['Usuarios'] = (

    """
        CREATE TABLE cursoflask.'jogos' (
            'id' SERIAL PRIMARY KEY,
            'nome' VARCHAR(50) NOT NULL,
            'nickname' VARCHAR(8) NOT NULL UNIQUE,
            'senha' VARCHAR(100) NOT NULL
        )
    """
)

for table_nome in TABLES.items:
    table_sql = TABLES[table_nome]

    try:
        print(f'Criando Table {table_nome}', end = ' ')
        cursor.execute(table_sql)
    except pg.connect.Error as err:
        print(e)

usuario_sql = 'INSERT INTO cursoflask.usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("Bruno Divino", 'BD', 'alohomora'),
    ('Camila Ferreira', 'Mila', 'paozinho'),
    ('Guilherme Louro', 'Cake', 'python_eh_vida')
]

cursor.execute()