from flask import Flask, render_template, request, redirect, session
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


@app.route('/login')
def login():
#proxima = 'lista_jogos.html'
    return render_template('login.html')


@app.route('/autenticar', methods= ['POST'])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['usuario'] in usuarios:
            usuario = usuarios[request.form['usuario']]
            if request.form['senha'] == usuario.senha:
                session['usuario_logado'] = usuario.nickname
                flash(usuario.nickname + 'logado com sucesso!')
                proxima_pagina = request.form['proxima']
                return rdirect(proxima_pagina)
        else:
            flask('Usuário não logado.')
            return redirect('Naõ achado')

@app.route('/logout')
def logout():
    session['usuarios_logado'] = None
    flask('Logout efetuado com sucesso!!')
    return redirect(url_for('index'))

@app.route('/apagar/<id>')
def apagar(id):
    delete = db.delete(Jogos).where(Jogos.id == id)
    db.session.execute(delete)
    db.session.commit()
    return f'Informação apagar do id = {id}'

app.run(debug=True)