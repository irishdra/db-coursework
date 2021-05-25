from datetime import datetime
from faker import Faker
import uuid
from db.repositories.products_repository import products_repository
from db.repositories.old_prices_repository import old_prices_repository

faker = Faker()

PRODUCTS_QUANTITY = 100
OLD_PRICE_QUANTITY = 5
products = {}
old_prices = []
breads = ('baguette', 'whole-grain')
milks = ('baked', 'ordinary')
cheeses = ('mozzarella', 'dorblu', 'camambert')
market = ('ekomarket', 'silpo', 'atb', 'marketopt', 'metro')

def get_random_date():
    date = faker.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2020, 12, 31))
    return str(date)

def generate_old_prices(product_id):
    for i in range(OLD_PRICE_QUANTITY):
        old_prices.append({
            '_id': f'{uuid.uuid4()}',
            'product_id': f'{product_id}',
            'price': float(f'{faker.random_int(100, 300)}.{faker.random_int(0, 99)}'),
            'currency': 'uah',
            'date': get_random_date()
        })
    old_prices_repository.insert_all(old_prices)
    old_prices.clear()

def generate_bread():
    type = 'bread'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        product_id = uuid.uuid4()
        products[type].append({
            '_id': f'{product_id}',
            'type': type,
            'name': breads[faker.random_int(0, 1)],
            'market': market[faker.random_int(0, 4)],
            'price': float(f'{faker.random_int(50, 100)}.{faker.random_int(0, 99)}'),
            'currency': 'uah',
            'date': datetime.today().strftime('%Y-%m-%d')
        })
        generate_old_prices(product_id)
    products_repository.insert_all(products[type])

def generate_milk():
    type = 'milk'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        id = uuid.uuid4()
        products[type].append({
            '_id': f'{id}',
            'type': type,
            'name': milks[faker.random_int(0, 1)],
            'market': market[faker.random_int(0, 4)],
            'price': float(f'{faker.random_int(10, 100)}.{faker.random_int(0, 99)}'),
            'currency': 'uah',
            'date': datetime.today().strftime('%Y-%m-%d')
        })
        generate_old_prices(id)
    products_repository.insert_all(products[type])

def generate_cheese():
    type = 'cheese'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        id = uuid.uuid4()
        products[type].append({
            '_id': f'{id}',
            'type': type,
            'name': cheeses[faker.random_int(0, 2)],
            'market': market[faker.random_int(0, 4)],
            'price': float(f'{faker.random_int(100, 500)}.{faker.random_int(0, 99)}'),
            'currency': 'uah',
            'date': datetime.today().strftime('%Y-%m-%d')
        })
        generate_old_prices(id)
    products_repository.insert_all(products[type])