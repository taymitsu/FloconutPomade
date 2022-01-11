from shop import app 
from flask import render_template, redirect, url_for
from shop.models import Product, User
from shop.forms import RegisterForm
from shop import db

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

#@app.route('/signin')
#def signin():
    #"""Sign into EXISTING account"""
    #return redirect('/account')

@app.route('/register')
def register():
    """Create new account"""
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email = form.email.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('register.html', form=form)
