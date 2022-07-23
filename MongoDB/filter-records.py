#!/usr/bin/env python3
from connect import myclient
from bson.objectid import ObjectId
mydb = myclient["node-app"]
mycollection = mydb["products"]

# filter name
filter = {"name": "iPhone 6"}
result = mycollection.find(filter)

for i in result:
    print(i)

#filter id,  from bson.objectid import ObjectId:

result = mycollection.find_one({"_id": ObjectId("62dc02c56bdc90e8d1ce7a99")}) #else cant get data because server needs objectid not string
print(result)
print("*"*20)
#filter query:
result = mycollection.find({
    "name": {
        "$in": ["Samsung S6", "iPhone X"]
    }
})
for j in result:
    print(j)
print("*"*20)

#filter with operators:
result = mycollection.find({
    "price": {
        "$gt": 5000  #greater than
    }
})
for k in result:
    print(k) # $lt -> lessthan, $eq -> equal, for more operators -> mongodb operators
print("*"*40)
#filter with regular expressions:
result = mycollection.find({
    "name": {"$regex": "^S"}
    })
for l in result:
    print(l)
