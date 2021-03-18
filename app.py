from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

from models import db, User, Item
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import locale
from os import environ, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
db.init_app(app)
migarte = Migrate(app, db)


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



@app.route('/')
def index():
    items = Item.query.all()
    return render_template("index.html", data = items )


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reg")
def register():
    form  = RegisterForm()

    return render_template('reg.html', form = form)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        title = request.form['name_item']
        about = request.form['about']
        adress = request.form['adress']

        item = Item(about = about, name_item = title, adress = adress)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect("/")
        except:
            return "Получилась ошибка"
    else:
        return render_template('add.html')


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")








if __name__ == '__main__':
    app.run()