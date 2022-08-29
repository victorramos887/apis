from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

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

class Jogos(db.Model):
    
    __table_args__ = {'schema':'cursoflask'}
    __tablename__ = 'jogos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Usuarios(db.Model):
    __table_args__ = {'schema':'cursoflask'}
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(8), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' %self.nome

@app.route('/')
def index():
    jogos = Jogos.query.order_by(Jogos.id).all()
    print(jogos)
    return render_template('lista_jogos.html', jogos= jogos)


#>>> stmt = delete(user_table).where(user_table.c.name == 'patrick')


@app.route('/apagar/<id>')
def apagar(id):
    delete = db.delete(Jogos).where(Jogos.id == id)
    db.session.execute(delete)
    db.session.commit()
    return f'Informação apagar do id = {id}'

app.run(debug=True)