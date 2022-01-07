from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    '''Home page'''
    return render_template('home.html')

@app.route('/products')
def products():
    '''Show ALL products'''
    products = [
        {'name': 'Classic', 'price': 25.99, 'desp': 'Our classic flow'},
        {'name': 'Medium', 'price': 29.99, 'desp': 'Medium'},
        {'name': 'Locked In', 'price': 29.99, 'desp': 'Lock in your flow for a 24 hour hold'}
    ]
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)