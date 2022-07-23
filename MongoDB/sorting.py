#!/usr/bin/env python3
from connect import myclient

mydb = myclient["node-app"]
mycollection = mydb["products"]

#sort as alphabetic:
result = mycollection.find().sort("name")
for i in result:
    print(i)
print("*"*60)
result = mycollection.find().sort("name", -1) #reverse
for i in result:
    print(i)

#sort as asc price:
result = mycollection.find().sort("price")
for i in result:
    print(i)
print("*"*60)

#sort as desc price:
result = mycollection.find().sort("price", -1)
for i in result:
    print(i)
print("*"*60)

#sort as name and price:
result = mycollection.find().sort(("name", 1), ("price", -1))
for i in result:
    print(i)
print("*"*60)