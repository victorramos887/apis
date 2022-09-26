import os

SECRET_KEY = 'postgres'
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{localhost}/{namedatabase}'.format(
        SGBD = 'postgresql',
        user = 'postgres',
        password = 'postgres',
        localhost = 'localhost',
        namedatabase = 'jogoteca'
    )


UPLOAD_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/uploads'