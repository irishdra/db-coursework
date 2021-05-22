from faker import Faker
import uuid
from db.repository import ProductsRepository

faker = Faker()
PR = ProductsRepository()

PRODUCTS_QUANTITY = 100
products = {}

def generate_cheese():
    type = 'cheese'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        products[type].append({
            '_id': uuid.uuid4(),
            'type': type,
            'name': faker.words(1)[0],
            'price': f'{faker.random_int(30, 1000)},{faker.random_int(0, 99)}',
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
            'name': faker.words(1)[0],
            'price': f'{faker.random_int(10, 100)},{faker.random_int(0, 99)}',
            'currency': 'uah'
        })
    write_data_to_db(type)

def generate_bread():
    type = 'bread'
    products[type] = []
    for i in range(PRODUCTS_QUANTITY):
        products[type].append({
            '_id': uuid.uuid4(),
            'type': type,
            'name': faker.words(1)[0],
            'price': f'{faker.random_int(10, 500)},{faker.random_int(0, 99)}',
            'currency': 'uah'
        })
    write_data_to_db(type)

def write_data_to_db(type):
    for p in products[type]:
        PR.insert_one(p)