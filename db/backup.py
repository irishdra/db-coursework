from dotenv import load_dotenv
import csv
from db.repository import ProductsRepository

load_dotenv()
PR = ProductsRepository()

def backup():
    filepath = 'db/backup.csv'
    data = PR.find()

    with open(filepath, 'w+') as file:
        writer = csv.DictWriter(file, fieldnames=['_id', 'type', 'name', 'price', 'currency'])
        writer.writeheader()
        for product in data:
            writer.writerow(product)

def restore():
    filepath = 'db/backup.csv'
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            PR.insert_one(row)