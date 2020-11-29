from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = 'Anton'
    return render_template('index.html', name=name)


@app.route('/goodbye')
def bye():
    return 'bye'


products = {'Onion': {
    'price': 12,
    'in_stock': 1000,
    'description': 'Лук'

},
    'Tomato': {
        'price': 4,
        'in_stock': 10000,
        'description': 'Tomatoes'

    }, 'Cucumber': {
        'price': 10,
        'in_stock': 500,
        'description': 'Cucumbers'

    }}


@app.route('/products')
def get_products():
    return render_template('products.html', products=products)


@app.route('/products/<string:product_name>')
def get_detail_product(product_name):
    return render_template('product_detail.html', product=products[product_name])
    # return str(products[product_name])


app.run(debug=True)
