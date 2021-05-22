from faker import Faker
import uuid
from db.repository import ProductsRepository

faker = Faker()
PR = ProductsRepository()

PRODUCTS_QUANTITY = 100
products = {}
breads = ('baguette', 'whole-grain')
milks = ('baked', 'ordinary')
cheeses = ('mozzarella', 'dorblu', 'camambert')
market = ('ekomarket', 'silpo', 'atb', 'marketopt', 'metro')

def generate_bread():
    type = 'bread'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        products[type].append({
            '_id': uuid.uuid4(),
            'type': type,
            'name': breads[faker.random_int(0, 1)],
            'market': market[faker.random_int(0, 4)],
            'price': float(f'{faker.random_int(50, 100)}.{faker.random_int(0, 99)}'),
            'currency': 'uah'
        })
    write_data_to_db(type)

def generate_milk():
    type = 'milk'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        products[type].append({
            '_id': uuid.uuid4(),
            'type': type,
            'name': milks[faker.random_int(0, 1)],
            'market': market[faker.random_int(0, 4)],
            'price': float(f'{faker.random_int(10, 100)}.{faker.random_int(0, 99)}'),
            'currency': 'uah'
        })
    write_data_to_db(type)

def generate_cheese():
    type = 'cheese'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        products[type].append({
            '_id': uuid.uuid4(),
            'type': type,
            'name': cheeses[faker.random_int(0, 2)],
            'market': market[faker.random_int(0, 4)],
            'price': float(f'{faker.random_int(100, 500)}.{faker.random_int(0, 99)}'),
            'currency': 'uah'
        })
    write_data_to_db(type)

def write_data_to_db(type):
    for p in products[type]:
        PR.insert_one(p)