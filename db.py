import pymongo
from pymongo import MongoClient

import csv

import os
from dotenv import load_dotenv
load_dotenv()

def get_data():
    cluster = MongoClient(os.getenv('DB_URL'))
    collection = cluster["coursework-data-bases"]
    return collection["products"]

def backup():
    filepath = 'backup.csv'
    cluster = MongoClient(os.getenv('DB_URL'))
    data = cluster["coursework-data-bases"]["products"].find()

    with open(filepath, 'w+') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price', 'currency'])
        writer.writeheader()
        for product in data:
            del product['_id']
            writer.writerow(product)

def restore():
    filepath = 'backup.csv'
    cluster = pymongo.MongoClient(os.getenv('DB_URL'))
    collection = cluster["coursework-data-bases"]["products"]
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            collection.insert_one(row)