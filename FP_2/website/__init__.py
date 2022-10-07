from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

with app.app_context():

    db = SQLAlchemy()


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitnessPartnes.db'
    app.config['SECRET_KEY'] = 'asdasdasd'
    db.init_app(app)
    bcrypt = Bcrypt(app)

    from website.admin import rotas

