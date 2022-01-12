from shop import db, login_manager
from shop import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True) 
    user = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=70), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def verify_password(self, password_attempt):
        return bcrypt.check_password_hash(self.password, password_attempt)

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    desp = db.Column(db.String(length=1500), nullable=False)

    def __repr__(self):
        #override default storage name in database
        return f'Product {self.name}'
