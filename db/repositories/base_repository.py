import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class BaseRepository:
    def __init__(self, name):
        cluster = MongoClient(os.getenv('DB_URL'))
        self.collection = cluster["coursework-data-bases"][name]

    def insert(self, data):
        return self.collection.insert_one(data).inserted_id

    def insert_all(self, data):
        return self.collection.insert_many(data)

    def find_one(self, query={}):
        return self.collection.find_one(query)

    def find(self, query={}):
        results = self.collection.find(query)
        return [doc for doc in results]

    def delete_one(self, query):
        self.collection.delete_one(query)

    def drop(self):
        self.collection.drop()