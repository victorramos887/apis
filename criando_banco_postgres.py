from calendar import c
import psycopg2 as pg

def conectando(host = 'localhost', user = 'postgres', password = 'postgres', database = 'alura'):
    print('Conectando ...')

    try:
         conn = pg.connect(host = host,
                        user = user,
                        password = password,
                        database = database)
         conn.autocommit = True
         return conn

    except pg.connect.Error as e:
        print(e)
        return 'Erro'


cursor = conectando().cursor()
#CRIANDO BANCO DE DADOS


cursor.execute("DROP DATABASE IF EXISTS jogoteca;")
cursor.execute("CREATE DATABASE jogoteca;")

database = 'jogoteca'

cursor.close()

cursor = conectando(database=database).cursor()

cursor.execute("""
               CREATE SCHEMA cursoflask
    AUTHORIZATION postgres;
    """)

TABLES = {}

TABLES['Jogos'] =  """CREATE TABLE IF NOT EXISTS cursoflask.jogos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        categoria VARCHAR(40) NOT NULL,
        console VARCHAR(20) NOT NULL
    )"""

TABLES['Usuarios'] = """CREATE TABLE cursoflask.usuarios(
      nome varchar(20) NOT NULL,
      nickname varchar(8) NOT NULL,
      senha varchar(100) NOT NULL,
      PRIMARY KEY (nickname)
      )"""

# print(TABLES)
# print('---')

for table_nome in TABLES.items():
    table_sql = TABLES[table_nome[0]]
    print(table_nome[0])
    try:
        print(f'Criando Table {table_nome}', end = '\n')
        cursor.execute(table_sql)
    except pg.connect.Error as err:
        print(err)

usuario_sql = 'INSERT INTO cursoflask.usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("Bruno Divino", 'BD', 'alohomora'),
    ("Camila Ferreira", 'Mila', 'paozinho'),
    ("Guilherme Louro", 'Cake', 'python_eh_vida')
]

cursor.executemany(usuario_sql, usuarios)


jogos_sql = 'INSERT INTO cursoflask.jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)