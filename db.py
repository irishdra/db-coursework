from pymongo import MongoClient

import os
from dotenv import load_dotenv
load_dotenv()

cluster = MongoClient(os.getenv('DB_URL'))
db = cluster["coursework-data-bases"]
collection = db["products"]

post = {
    "name": "milk",
    "price": "20.00",
    "currency": "uah"
 }

collection.insert_one(post)