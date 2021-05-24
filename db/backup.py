from dotenv import load_dotenv
import json
from db.repositories.products_repository import products_repository
from db.repositories.old_prices_repository import old_prices_repository

load_dotenv()

filepath = 'db/backup.json'

def backup():
    data = {
        'products': products_repository.find(),
        'old_prices': old_prices_repository.find()
    }

    with open(filepath, 'w+') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def restore():
    try:
        with open(filepath, 'r+') as file:
            data = json.load(file)

        products_repository.drop()
        old_prices_repository.drop()

        products_repository.insert_all(data['products'])
        old_prices_repository.insert_all(data['old_prices'])
    except:
        print('Some problem with backup file :(')