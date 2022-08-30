from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{user}:{password}@{localhost}/{namedatabase}'.format(
        SGBD = 'postgresql',
        user = 'postgres',
        password = 'postgres',
        localhost = 'localhost',
        namedatabase = 'jogoteca'
    )

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)