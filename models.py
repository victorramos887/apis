from jogoteca import db


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