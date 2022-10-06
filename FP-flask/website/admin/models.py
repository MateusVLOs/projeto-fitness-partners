from website import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    sobrenome = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    celular = db.Column(db.String(20), unique=False, nullable=False)
    senha = db.Column(db.String(180), unique=False, nullable=False)
    genero = db.Column(db.String(20), unique=False, nullable=False)
    tipo_da_conta = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()