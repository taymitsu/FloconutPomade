from flask import Flask, render_template, request, url_for, redirect
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SECRET_KEY'] = '622a05368bddd00c722f371a'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True) 
    user = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=70), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    desp = db.Column(db.String(length=1500), nullable=False)

    def __repr__(self):
        #override default storage name in database
        return f'Product {self.name}'

@app.route('/')
@app.route('/home')
def home():
    '''Home page'''
    return render_template('home.html')

@app.route('/products')
def products():
    '''Show ALL products'''
    products = Product.query.all()
    #products = [
        #{'name': 'Classic', 'price': 25.99, 'desp': 'Our classic flow'},
        #{'name': 'Medium', 'price': 29.99, 'desp': 'Medium'},
        #{'name': 'Locked In', 'price': 29.99, 'desp': 'Lock in your flow for a 24 hour hold'}
    #]
    return render_template('products.html', products=products)

@app.route('/signin')
def signin():
    """Sign into EXISTING account"""
    return redirect('/account')

@app.route('register')
def register():
    """Create new account"""
    form = RegisterForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)