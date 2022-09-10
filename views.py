from flask import flash, render_template, request, redirect, session, url_for
from jogoteca import app
from models import *

@app.route('/')
def index():
    jogos = Jogos.query.order_by(Jogos.id).all()
    print(jogos)
    return render_template('lista.html', jogos= jogos)


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima= proxima)


@app.route('/autenticar', methods= ['POST'])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect('Naõ achado')

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogos.query.filter_by(nome = nome).first()

    if jogo:
        flash('Jogo Já existente!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome = nome, categoria = categoria, console = console)

    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    arquivo.save(f'uploads/{arquivo.filename}')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    jogo = Jogos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Novo Jogo', jogo=jogo)

#UPDATE
@app.route('/atualizar', methods=['POST',])
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form["id"]).first()
    jogo.nome = request.form["nome"]
    jogo.categoria = request.form["categoria"]
    jogo.console = request.form["console"]

    db.session.add(jogo)
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo Deletado com sucesso!!!')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuarios_logado'] = None
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!!')
    print(session)
    return redirect(url_for('index'))


# @app.route('/apagar/<id>')
# def apagar(id):
#     delete = db.delete(Jogos).where(Jogos.id == id)
#     db.session.execute(delete)
#     db.session.commit()
#     return f'Informação apagar do id = {id}'