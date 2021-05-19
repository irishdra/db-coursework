from dotenv import load_dotenv
import csv
from repository import ProductsRepository

load_dotenv()
PR = ProductsRepository()

def backup():
    filepath = 'db/backup.csv'
    data = PR.find()

    with open(filepath, 'w+') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price', 'currency'])
        writer.writeheader()
        for product in data:
            del product['_id']
            writer.writerow(product)
            print(product)

def restore():
    filepath = 'db/backup.csv'
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            PR.insert_one(row)