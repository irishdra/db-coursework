import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class ProductsRepository:
    def __init__(self):
        cluster = MongoClient(os.getenv('DB_URL'))
        self.collection = cluster["coursework-data-bases"]["products"]

    def find(self, query={}):
        return self.collection.find(query)

    def find_one(self, query={}):
        return self.collection.find_one(query)

    def insert_one(self, data):
        return self.collection.insert_one(data).inserted_id

    def delete_one(self, query):
        self.collection.delete_one(query)

    def drop(self):
        self.collection.drop()