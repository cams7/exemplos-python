# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
# http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php

import pymongo
# sudo apt-get install python-setuptools
# sudo easy_install pymongo

# https://api.mongodb.com/python/current/installation.html
# sudo apt-get install python3-pip
# sudo python3 -m pip install pymongo

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.bogotobogo
    return db

def add_country(db):
    db.countries.insert({"name" : "Canada"})
    
def get_country(db):
    return db.countries.find_one()

if __name__ == "__main__":
    db = get_db() 
    add_country(db)
    print (get_country(db))