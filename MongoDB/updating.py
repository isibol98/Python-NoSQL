#!/usr/bin/env python3
from connect import myclient

mydb = myclient["node-app"]
mycollection = mydb["products"]

#update one data
"""
mycollection.update_one(
    {"name": "Samsung S6"}, 
    {"$set": {
        "name": "Samsung S6+",
        "price": 5500
        }}
    ) #(find_data, update_data)

for i in mycollection.find():
    print(i)
"""
"""
#update many data:
mycollection.update_many(
    {"name": "iPhone 6"}, 
    {"$set": {
        "name": "iPhone 6 Plus",
        "price": 4800
        }}
    )

for i in mycollection.find():
    print(i)
"""
#update query and new_values:
query = {"name": "iPhone 7"}
new_values = {"$set":{
    "name": "iPhone 7 Plus",
    "price": 6000
}}
result = mycollection.update_many(query, new_values)
print(f"{result.modified_count} datas updates!")
for i in mycollection.find():
    print(i)
