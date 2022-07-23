#!/usr/bin/env python3
from connect import myclient

mydb = myclient["node-app"]
mycollection = mydb["products"]

#select one record .findone()
for i in mycollection.find(): 
    print(i)
# custom selection:
for j in mycollection.find({},{"_id":0,"name":1,"price":1}): 
    print(j)
#custom selection with only 0:
for k in mycollection.find({},{"_id":0,"name":0}): #select all records except id and name
    print(k)

