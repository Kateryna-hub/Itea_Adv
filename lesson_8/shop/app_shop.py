from flask import Flask, render_template, request, redirect, url_for
from DB import DB

app = Flask(__name__)


@app.route('/')
def get_categories():
    with DB("shop.db") as db:
        cursor = db.execute('SELECT name FROM categories')
        categories = []
        for data in cursor:
            categories.append(data[0])

    return render_template('categories.html', categories=categories)


@app.route('/<string:category_name>')
def get_products(category_name):
    with DB("shop.db") as db:
        sql = 'SELECT goods.name FROM goods INNER JOIN categories ON goods.category_id = categories.id ' \
              'WHERE goods.category_id = ' \
              '(SELECT categories.id FROM categories WHERE categories.name LIKE "' + category_name + '")'
        cursor = db.execute(sql)
        products = []
        for data in cursor:
            products.append(data[0])

    return render_template('products.html', products=products)


@app.route('/<string:category_name>/<string:product_name>')
def get_detail_product(category_name, product_name):
    with DB("shop.db") as db:
        sql = ('SELECT goods.name, goods.price, goods.number, goods.available, goods.description FROM goods '
               'WHERE goods.name = ?', (product_name,))

        product = (db.execute(* sql)).fetchone()

    return render_template('product_detail.html', product=product)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    name = request.form.get('name')
    if request.method == 'POST':
        with DB("shop.db") as db:
            db.execute(* ('INSERT INTO categories (name) VALUES (?)', (name,)))
        return redirect(url_for('get_categories'))
    return render_template('add_category.html')


@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    category = request.form.get('category')
    name = request.form.get('name')
    price = request.form.get('price')
    number = request.form.get('number')
    available = request.form.get('available')
    description = request.form.get('description')
    if request.method == 'POST':
        with DB("shop.db") as db:
            category_id = (db.execute(* ('SELECT categories.id FROM categories WHERE categories.name = ?',
                                         (category,)))).fetchone()
            db.execute(* ('INSERT INTO goods (name, price, number, available, description, category_id) '
                          'VALUES (?, ?, ?, ?, ?, ?)', (name, price, number, available, description, category_id[0],)))
        return redirect(url_for('get_products', category_name=category))
    return render_template('add_product.html')


app.run(debug=True)
