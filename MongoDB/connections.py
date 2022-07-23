#!/usr/bin/env python3
import pymongo
from connect import myclient

#myclient = pymongo.MongoClient("mongodb://localhost:27017") #local connection
#myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<username>.htclc3v.mongodb.net/?retryWrites=true&w=majority") #Free server from Mongo Atlas

mydb = myclient["node-app"]
my_collection = mydb["products"]


#print(mydb.list_database_names())
#print(mydb.list_collection_names())

"""
product = {"name":"Samsung S6", "price": 5000}

result = my_collection.insert_one(product) #add one product
print(result.inserted_id) #get product id
"""

product_list = [
    {"name": "iPhone 6", "price": 4500},
    {"name": "iPhone 7", "price": 5500},
    {"name": "iPhone 8", "price": 6500},
    {"name": "iPhone X", "price": 10500},
    {"_id": 1, "name": "iPhone 11", "price": 15000} #add with custom id
]

#result = my_collection.insert_many(product_list) #add list of products
#print(result.inserted_ids)

product_list2 = [
    {"name": "iPhone 6", "price": 4500, "descrpition": "best seller"},
    {"name": "iPhone 7", "price": 5500, "categories": ['electronic', 'phone']} #additional infos
]

result = my_collection.insert_many(product_list2)
print(result.inserted_ids)