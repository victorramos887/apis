from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'{SGBD}://{user}:{password}@{localhost}/{namedatabase}'.format(
        SBGB = 'psotgresql',
        user = 'postgres',
        password = 'postgres',
        localhost = 'localhost',
        namedatabase = 'jogoteca'
    )

db = SqlAlchemy(app)

