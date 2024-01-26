#file where the connection to the database is handled
import pymongo

# class Conn():
    
# def conn(self):
client = pymongo.MongoClient("mongodb://localhost:27017/")


if "miau" in client.list_databases():
    print("it doesn't connect")
    db = client["miau_dem"]
    print(db.create_collection("miau"))
# def insert(self):
# pass
# def delete(self):
# pass
