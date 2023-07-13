import pymongo 
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://b2d1h3:top911349@bomin.nbhxcdt.mongodb.net/?retryWrites=true&w=majority")
db = cluster["software_engineering"]
collection = db["test"]
post = {"_id":0, "name":"WoongSup", "score": 90}
collection.insert_one(post)