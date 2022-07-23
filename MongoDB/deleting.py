#!/usr/bin/env python3
from connect import myclient

mydb = myclient["node-app"]
mycollection = mydb["products"]

"""
#delete one:
mycollection.delete_one({"name": "Samsung S6+"})
for i in mycollection.find():
    print(i)
"""
"""
#delete many:
result = mycollection.delete_many({"name": {"$regex": "^S"}})
for i in mycollection.find():
    print(i)
print(f"{result.deleted_count} datas deleted!")
"""
#delete all:
result = mycollection.delete_many({})
for i in mycollection.find():
    print(i)
print(f"{result.deleted_count} datas deleted!")