#file where the connection to the database is handled
import pymongo
import json

class Conn():
    
    def __init__(self,connstring,dbname,collName):
        self.client = pymongo.MongoClient(connstring)
        self.dbname=dbname
        self.db = self.client[self.dbname]
        
        if collName not in self.db.list_collection_names():
            self.dbColl=self.db.create_collection(collName)            
        else: self.dbColl=self.db[collName]
        
    def delete(self,choice,imgCard):
            match choice:
                case "database":
                    self.client.drop_database(self.dbname)
                case "card":
                    confirmation=input("Are you sure you want to delete the card? \n 1. Yes!\n 2. No!\n  ")
                    if confirmation=="yes":
                        self.dbColl.delete_one({"img":imgCard})
                        print("Card deleted successfully!")
                case "collection":
                    confirmation=input("Are you sure you want to delete it?\n 1. Yes!\n 2. No!\n  ")
                    if confirmation == "yes":                    
                        self.db.drop_collection(self.collName)
                case _:
                    print("Se ha producido un error al elegir que borrar!")
    
    def insertForm(self):
        self.dbf=["name","number","arcana", "suit", "img", "fortune_telling", "keywords", "meanings","light", "shadow"]
        name=number=arcana=suit=img=fortune_telling=""
        keywords=light=shadow=[]
        values={
            "name":name,
            "number":number,
            "arcana":arcana,
            "suit":suit,
            "img":img,
            "fortune_telling":fortune_telling,
            "keywords":keywords,
            "meanings":{
                "light":light,
                "shadow":shadow
            }
        }
        for x in values: 
            # print(x)
            values[x]=(str(input("Could you please provide me with the card's " + x + " value ")))
        return values
            
    def insertOne(self):
        if self.db is not None:
            print ("it's not null")
            # self.db.create_collection(newColl)
            self.dbColl.insert_one(self.insertForm())
    
    #the "r" in open file indicates that the file is only to be read from  
    def insertJSON(self,pathFile):
        
        with open(pathFile,"r") as file:
            data=json.load(file) 
        
        if isinstance(data,list):
            self.dbColl.insert_many(data)
        else:
            self.dbColl.insert_one(data)          

    def cardsList(self):
        
        fieldsToRetrieve={
            "_id":True,
            "name":True,
            "arcana":True,
            "suit":True,
            "img":True,
            "fortune_telling":True,
            "keywords":True,
            "meanings.light":True,
            "meanings.shadow":True
        }
        
        cards= self.dbColl.find({}, fieldsToRetrieve)
        cardsArray=[]
        for card in cards:
            cardsArray.append(card)
        return cardsArray
            
# miau=Conn("mongodb://localhost:27017","Tarrot","Cards")
# miau.conn()
# miau.insert("mewmew")
# miau.insertJSON("./colores.json")
# miau.delete("database",1) 
# for x in miau.cardsList():
#     print("----------------------")
#     print(x["img"])
#     print("----------------------")


    
    
    