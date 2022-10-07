from flask import render_template, session, request, url_for, redirect, flash
from website  import app, db, bcrypt
from .models import User

import  os


@app.route('/login', methods=['GET', 'POST'])
def login():

    email = request.form.get("usuario")
    senha = request.form.get("senha")

    if request.method == "POST":
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.senha, senha):
            nome = user.nome
            session['email'] = email
            flash(f'login feito com sucesso','success')
            return redirect(url_for('dash_al', nome=nome))

    return render_template('admin/login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    senha = request.form.get("password")
    confirmar_senha = request.form.get("Confirmapassword")
    female = request.form.get("gender-female")
    male = request.form.get("gender-male")
    aluno = request.form.get("type-account-aluno")

    if female == 'on':
        genero = 'female'
    elif male == 'on':
        genero = 'male'
    else:
        genero = 'others'

    if aluno == 'on':
        tipo_da_conta = 'aluno'
    else:
        tipo_da_conta = 'funcionario'


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


        #flash(f'Obrigado por registrasse')
        return redirect(url_for('login'))


    return render_template('admin/cadastro.html')

@app.route('/dash_al')
def dash_al():

    return render_template('admin/page-dashboard-al.html')