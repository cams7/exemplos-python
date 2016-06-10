#http://www.bogotobogo.com/DevOps/MongoDB/MongoDB_Management_Tool_RoboMongo.php

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# data base name : 'bogotobogo'
mydb = client['bogotobogo']

import datetime

myrecord = {
        "author": "Duke",
        "title" : "PyMongo 101",
        "tags" : ["MongoDB", "PyMongo", "Tutorial"],
        "date" : datetime.datetime.utcnow()
        }

record_id = mydb.mytable.insert(myrecord)

print (record_id)
print (myrecord)
print (mydb.collection_names())