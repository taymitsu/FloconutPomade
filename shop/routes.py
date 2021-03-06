from shop import app
from flask import render_template, redirect, url_for, flash
from shop.models import Product, User
from shop.forms import RegisterForm, LoginForm
from shop import db
from flask_login import login_user

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Create new account"""
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(user=form.user.data, email=form.email.data, password=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        return redirect(url_for('products'))
    #handle input form errors
    if form.errors != {}: 
        for error_msg in form.errors.values():
            flash(f'Error: {error_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Sign into Exisiting Account"""
    form = LoginForm()
    if form.validate_on_submit():
        user_attempt = User.query.filter_by(user=form.user.data).first()
        if user_attempt and user_attempt.verify_password(password_attempt=form.password.data):
            login_user(user_attempt)
            flash('Welcome, {user_attempt.user}!', category='success')
            return redirect(url_for('products'))
        else:
            flash('Username and password do not match! Please try again', category='danger')
    return render_template('signin.html', form=form)