import mongoengine as me
import random
from shop_models import Category, Product


me.connect('SHOP10')

fridges = {
    'fridge1': {
        'title': 'Холодильник Liebherr CBNES 6256',
        'description': 'многодверный / 289л / 114л / 2шт / A++ / 203.9см / 91см / 61.5см',
        'number': 1,
        'price': 161699.00
    },
    'fridge2': {
        'title': 'Холодильник SAMSUNG RB33J3000SA',
        'description': 'с нижней морозильной камерой / 230л / 98л / 1шт / A+ / 185см / 59.5см / 66.8см',
        'number': 5,
        'price': 12499.00
    },
    'fridge3': {
        'title': 'Холодильник BOSCH KGN36VL326',
        'description': 'с нижней морозильной камерой / 237л / 87л / 1шт / A++ / 186см / 60см / 66см',
        'number': 4,
        'price': 13999
    }
}
washing_machines = {
    'wm1': {
        'title': 'Стиральная машина INDESIT IWSB 51051',
        'description': 'автоматическая / 5кг / 1000об/мин / A / 850мм / 595мм / 420мм / нет / отдельностоящая',
        'number': 1,
        'price': 5599
    },
    'wm2': {
        'title': 'Стиральная машина ZANUSSI ZWSH 7100',
        'description': 'автоматическая / 7кг / 1100об/мин / A / 850мм / 600мм / 380мм / есть / отдельностоящая',
        'number': 3,
        'price': 7955
    }
}
cabinets = {
    'cabinet1': {
        'title': 'Книжный шкаф',
        'description': 'пять открытых полок, изготовлен из ДСП высокого качества',
        'number': 3,
        'price': 5450
    },
    'cabinet2': {
        'title': 'Шкаф для посуды',
        'description': 'Сервант BRW Ромео REG1W20/6P 59,5х198х42 орех ',
        'number': 2,
        'price': 4999
    }
}
sofas = {
    'sofa1': {
        'title': 'Диван угловой',
        'description': 'Многофункциональная модель оснащена прочными комплектующими',
        'number': 1,
        'price': 5340
    },
    'sofa2': {
        'title': 'Диван офисный',
        'description': 'одинарный небольшой диван, больше напоминающий кресло',
        'number': 3,
        'price': 4695
    }
}
pans = {
    'pan1': {
        'title': 'Кастрюля Tefal',
        'description': 'Алюминий, 5 л',
        'number': 1,
        'price': 1899
    },
    'pan2': {
        'title': 'Кастрюля Tramontina Solar',
        'description': 'Нержавеющая сталь, 2.8 л',
        'number': 2,
        'price': 999
    }
}
plates = {
    'plate1': {
        'title': 'Тарелка обеденная',
        'description': 'круглая 25 см',
        'number': 20,
        'price': 24.99
    },
    'plate2': {
        'title': 'Тарелка десертная',
        'description': 'Disney Vaiana 20 см',
        'number': 15,
        'price': 29.5
    }
}

# root1 = (Category(title='Бытовая техника')).save()
# root2 = (Category(title='Товары для дома')).save()
# category_fridges = (Category(title='Холодильники')).save()
# category_wm = (Category(title='Стиральные Машины')).save()
# category_cabinets = (Category(title='Шкафы')).save()
# category_sofas = (Category(title='Диваны')).save()
# category_pans = (Category(title='Кастрюли')).save()
# category_plates = (Category(title='Тарелки')).save()
# category_furniture = (Category(title='Мебель')).save()
# category_dishes = (Category(title='Посуда')).save()
#
# root1.add_subcategory(category_fridges)
# root1.add_subcategory(category_wm)
# root2.add_subcategory(category_furniture)
# root2.add_subcategory(category_dishes)
# category_furniture.add_subcategory(category_cabinets)
# category_furniture.add_subcategory(category_sofas)
# category_dishes.add_subcategory(category_plates)
# category_dishes.add_subcategory(category_pans)
#
#
# for fr in fridges:
#     Product(title=fridges[fr]['title'], description=fridges[fr]['description'], number=fridges[fr]['number'],
#             price=fridges[fr]['price'], category=category_fridges).save()
#
# for wm in washing_machines:
#     Product(title=washing_machines[wm]['title'], description=washing_machines[wm]['description'],
#             number=washing_machines[wm]['number'], price=washing_machines[wm]['price'], category=category_wm).save()
#
# for c in cabinets:
#     Product(title=cabinets[c]['title'], description=cabinets[c]['description'], number=cabinets[c]['number'],
#             price=cabinets[c]['price'], category=category_cabinets).save()
#
# for s in sofas:
#     Product(title=sofas[s]['title'], description=sofas[s]['description'], number=sofas[s]['number'],
#             price=sofas[s]['price'], category=category_sofas).save()
#
# for p in pans:
#     Product(title=pans[p]['title'], description=pans[p]['description'], number=pans[p]['number'],
#             price=pans[p]['price'], category=category_pans).save()
#
# for pl in plates:
#     Product(title=plates[pl]['title'], description=plates[pl]['description'], number=plates[pl]['number'],
#             price=plates[pl]['price'], category=category_plates).save()


