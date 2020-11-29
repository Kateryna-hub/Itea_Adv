from flask import Flask, render_template
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
        print(sql)
        cursor = db.execute(sql)
        products = []
        for data in cursor:
            products.append(data[0])

    return render_template('products.html', products=products)


@app.route('/<string:category_name>/<string:product_name>')
def get_detail_product(category_name, product_name):
    with DB("shop.db") as db:
        sql = 'SELECT goods.price, goods.number, goods.available, goods.description FROM goods ' \
              'WHERE goods.name = "' + product_name + '"'

        product = (db.execute(sql)).fetchone()

    return render_template('product_detail.html', product=product)


app.run(debug=True)
