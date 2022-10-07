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

class Func(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    sobrenome = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    celular = db.Column(db.String(20), unique=False, nullable=False)
    senha = db.Column(db.String(180), unique=False, nullable=False)
    genero = db.Column(db.String(20), unique=False, nullable=False)
    tipo_da_conta = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Func %r>' % self.funcionario

class Ficha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_aluno = db.Column(db.String(10), unique=False, nullable=False)
    data = db.Column(db.String(10), unique=False, nullable=False)
    massa = db.Column(db.Numeric(10,2), nullable=False)
    estatura = db.Column(db.Numeric(10, 2), nullable=False)
    coxa_prox_dir = db.Column(db.Numeric(10, 2), nullable=False)
    coxa_prox_esq = db.Column(db.Numeric(10, 2), nullable=False)
    coxa_med_dir = db.Column(db.Numeric(10, 2), nullable=False)
    coxa_med_esq = db.Column(db.Numeric(10, 2), nullable=False)
    coxa_dis_dir = db.Column(db.Numeric(10, 2), nullable=False)
    coxa_dis_esq = db.Column(db.Numeric(10, 2), nullable=False)
    quadril = db.Column(db.Numeric(10, 2), nullable=False)
    abdomem = db.Column(db.Numeric(10, 2), nullable=False)
    torax = db.Column(db.Numeric(10, 2), nullable=False)
    cintura = db.Column(db.Numeric(10, 2), nullable=False)
    braco_dir_relax = db.Column(db.Numeric(10, 2), nullable=False)
    braco_esq_relax = db.Column(db.Numeric(10, 2), nullable=False)
    braco_dir_contr = db.Column(db.Numeric(10, 2), nullable=False)
    braco_esq_contr= db.Column(db.Numeric(10, 2), nullable=False)
    ant_braco_dir = db.Column(db.Numeric(10, 2), nullable=False)
    ant_braco_esq = db.Column(db.Numeric(10, 2), nullable=False)
    pant_dir = db.Column(db.Numeric(10, 2), nullable=False)
    pant_esq = db.Column(db.Numeric(10, 2), nullable=False)
    resis_abs = db.Column(db.String(10), unique = False, nullable=False)
    resis_bra_tem = db.Column(db.String(10), unique = False, nullable=False)


    def __repr__(self):
        return '<Ficha %r>' % self.ficha

db.create_all()