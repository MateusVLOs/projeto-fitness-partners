from flask import render_template, session, request, url_for, redirect, flash
from website  import app, db, bcrypt
from .models import User, Func, Ficha

import  os


@app.route('/login', methods=['GET', 'POST'])
def login():

    global tipo_da_conta
    email = request.form.get("usuario")
    senha = request.form.get("senha")

    if request.method == "POST":
        user = User.query.filter_by(email=email).first()
        if user:
            tipo_da_conta = user.tipo_da_conta
            print(tipo_da_conta)

    if request.method == "POST":
        func = Func.query.filter_by(email=email).first()
        if func:
            tipo_da_conta = func.tipo_da_conta
            print(tipo_da_conta)

    if request.method == "POST" and tipo_da_conta == 'aluno':
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.senha, senha):
            nome = user.nome
            print(nome)
            session['email'] = email
            #flash(f'login feito com sucesso','success')
            return redirect(url_for('dash_al', nome=nome))

    if request.method == "POST" and tipo_da_conta == 'funcionario':
        func = Func.query.filter_by(email=email).first()
        print(func.email)
        if func and bcrypt.check_password_hash(func.senha, senha):
            nome = func.nome
            session['email'] = email
            #flash(f'login feito com sucesso','success')
            return redirect(url_for('dash_fu', nome=nome))


    return render_template('admin/login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    global tipo_da_conta
    senha = request.form.get("password")
    confirmar_senha = request.form.get("Confirmapassword")
    female = request.form.get("gender-female")
    male = request.form.get("gender-male")
    aluno = request.form.get("type-account-aluno")
    funcionario = request.form.get("type-account-funcionario")

    if female == 'on':
        genero = 'female'
    elif male == 'on':
        genero = 'male'
    else:
        genero = 'others'

    if aluno == 'on':
        tipo_da_conta = 'aluno'

    elif funcionario == 'on':
        tipo_da_conta = 'funcionario'

    else:
        tipo_da_conta = None

    if tipo_da_conta == 'aluno':
        if request.method == 'POST' and  senha == confirmar_senha:
            hash_senha = bcrypt.generate_password_hash(senha)

            user = User(nome=request.form.get("firstname"),
                        sobrenome=request.form.get("lastname"),
                        email=request.form.get("email"),
                        celular = request.form.get("number"),
                        senha = hash_senha, genero = genero,
                        tipo_da_conta = tipo_da_conta)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

    if tipo_da_conta == 'funcionario':
        print(tipo_da_conta)
        if request.method == 'POST' and senha == confirmar_senha:
            hash_senha = bcrypt.generate_password_hash(senha)

            func = Func(nome=request.form.get("firstname"),
                        sobrenome=request.form.get("lastname"),
                        email=request.form.get("email"),
                        celular=request.form.get("number"),
                        senha=hash_senha, genero=genero,
                        tipo_da_conta=tipo_da_conta)
            db.session.add(func)
            db.session.commit()
            #flash(f'Obrigado por registrasse')
            return redirect(url_for('login'))

    return render_template('admin/cadastro.html')

@app.route('/dash_al',methods=['GET', 'POST'])
def dash_al():




    return render_template('admin/dashboard-al.html')


@app.route('/dash_fu',methods=['GET', 'POST'])
def dash_fu():



    return render_template('admin/dashboard-fu.html',ficha=Ficha.query.all())

@app.route('/contatos')
def contatos():

    return render_template('admin/contatos.html')

@app.route('/es')
def es():

    return render_template('admin/es.html')

@app.route('/ficha_al')
def ficha_al():

    return render_template('admin/ficha-al.html')

@app.route('/ficha_fu',methods=['GET', 'POST'])
def ficha_fu():



    if request.method == "POST":
        ficha = Ficha(codigo_aluno=request.form.get("codigo-aluno"), data=request.form.get("data"),
                      massa=request.form.get("massa"), estatura=request.form.get("estatura"),
                      coxa_prox_dir=request.form.get("coxa-proximal-direita"), coxa_prox_esq=request.form.get("coxa-proximal-esquerda"),
                      coxa_med_dir=request.form.get("coxa-media-direita"), coxa_med_esq=request.form.get("coxa-media-esquerda"),
                      coxa_dis_dir=request.form.get("coxa-distal-direita"), coxa_dis_esq=request.form.get("coxa-distal-esquerda"),
                      quadril=request.form.get("quadril"), abdomem=request.form.get("abdomen"),
                      torax=request.form.get("torax"), cintura=request.form.get("cintura"),
                      braco_dir_relax=request.form.get("braco-direito-relaxado"), braco_esq_relax=request.form.get("braco-esquerdo-relaxado"),
                      braco_dir_contr=request.form.get("braco-direito-contraido"), braco_esq_contr=request.form.get("braco-esquerdo-contraido"),
                      ant_braco_dir=request.form.get("antebraco-direito"), ant_braco_esq=request.form.get("antebraco-esquerdo"),
                      pant_dir=request.form.get("panturrilha-direita"), pant_esq=request.form.get("panturrilha-esquerda"),
                      resis_abs=request.form.get("resistencia-abdominal"), resis_bra_tem=request.form.get("resistencia-braquio-peitoral"))
        db.session.add(ficha)
        db.session.commit()

        return redirect(url_for('dash_fu'))

    return render_template('admin/ficha-fu.html')

@app.route('/sobre')
def sobre():

    return render_template('admin/sobre.html')