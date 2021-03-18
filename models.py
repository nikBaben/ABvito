from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String, nullable = False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(255),nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)



    def check_password(self, password):
        return check_password_hash(self.password, password)


class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    about = db.Column(db.String,nullable=False)
    name_item = db.Column(db.String,nullable=False)
    adress = db.Column(db.String,nullable=False)



