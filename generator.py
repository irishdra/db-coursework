from faker import Faker
import uuid
import json

faker = Faker()

PRODUCTS_QUANTITY = 10
file = 'products.json'
products = {}

def generate_cheese():
    products['cheese'] = []
    for i in range(PRODUCTS_QUANTITY):
        products['cheese'].append({
            'id': f'{uuid.uuid4()}',
            'type': 'cheese',
            'name': faker.words(1)[0],
            'price': f'{faker.random_int(30, 1000)},{faker.random_int(0, 99)}',
            'currency': 'uah'
        })
    write_to_json()

def generate_milk():
    products['milk'] = []
    for i in range(PRODUCTS_QUANTITY):
        products['milk'].append({
            'id': f'{uuid.uuid4()}',
            'type': 'milk',
            'name': faker.words(1)[0],
            'price': f'{faker.random_int(10, 100)},{faker.random_int(0, 99)}',
            'currency': 'uah'
        })
    write_to_json()

def generate_bread():
    products['bread'] = []
    for i in range(PRODUCTS_QUANTITY):
        products['bread'].append({
            'id': f'{uuid.uuid4()}',
            'type': 'bread',
            'name': faker.words(1)[0],
            'price': f'{faker.random_int(10, 500)},{faker.random_int(0, 99)}',
            'currency': 'uah'
        })
    write_to_json()

def write_to_json():
    with open('data.json', 'w+') as outfile:
        json.dump(products, outfile, ensure_ascii=False, indent=4)