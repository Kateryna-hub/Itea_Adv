import json

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


products_json = json.dumps(products)
products1 = json.loads(products_json)
print(type(products))
for p in products:
    print(type(p))


print('_' * 20)
print(products_json)
print('_' * 20)
print(products1)
#
# print(type(products))
#
# f = open('myjson.json', 'r')
# #json.dump(products, f)
# data = json.load(f)
# print(data)
# f.close()
