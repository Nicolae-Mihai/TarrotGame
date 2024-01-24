#file where the connection to the database is handled
import pymongo

def conenectToDatabase():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["Tarrot"]
