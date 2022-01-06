from flask import Flask, render_template, request 
from pymongo import MongoClient

client = MongoClient()
db = client.floconutpomade
products = db.products

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    '''Home page'''
    return render_template('home.html')

@app.route('/products')
def products():
    '''Show ALL products'''
    return render_template('products.html', products=products.find())

if __name__ == '__main__':
    app.run(debug=True)