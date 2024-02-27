from tinydb import TinyDB, Query
from tinydb.database import Document
from pprint import pprint
import json
User = Query()

db1=TinyDB('database/users.json', indent=4)
db2=TinyDB('database/products.json', indent=4)

users     = db1.table('Users')
stage     = db1.table('Stage')
index     = db1.table('Index')
products  = db2.table('Products') 

def get(table, user_id=None):

    if table == "stage":
        return stage.get(doc_id=user_id)
    elif table == "users":
        if user_id == None:
            return users.all()
        else:
            return users.get(doc_id=user_id)
    elif table == "index":
        return index.get(doc_id=user_id)
    

def insert(table, data, user_id=None, product_type=None):

    if table == "stage":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        stage.insert(doc)
    
    elif table == "users":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        users.insert(doc)
    
    elif table == "index":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        index.insert(doc)
    elif table == products:
       db2.insert(data)
       
def upd(table, data, user_id=None, product=None):
    if table == "stage":
        stage.update(data, doc_ids=[user_id])
    
    elif table == "index":
        index.update(data, doc_ids=[user_id])
    elif table == "products":
        tip = Query()
        db2.update(data, tip.type == product)
        print(db2)
  