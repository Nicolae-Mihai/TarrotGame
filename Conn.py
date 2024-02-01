#file where the connection to the database is handled
import pymongo
import json

class Conn():

    
    def __init__(self,connstring,dbname,collName):
        self.client = pymongo.MongoClient(connstring)
        self.dbname=dbname
        self.collName=collName
        self.db=None
    
    def conn(self):
                    
        print ("Creating Database")
        self.db = self.client[self.dbname]
        print("Creating Collection")
    
        #check if the collection already exists
        if self.collName not in self.db.list_collection_names():
            self.dbColl=self.db.create_collection(self.collName)            
        else: self.dbColl=self.db[self.collName]
    
    def delete(self,choice,imgCard):
            match choice:
                case "database":
                    confirmation=input("Are you sure you want to delete it?\n 1. Yes!\n 2. No!\n  ")
                    if confirmation=="yes":
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
    
    #change the "r" thing in the open file  
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
        
        cards= miau.dbColl.find({}, fieldsToRetrieve)
        cardsArray=[]
        for card in cards:
            print("- _id: ",card["_id"])
            print("- Name:", card["name"])
            print("- Arcana:", card["arcana"])
            print("- Suit:", card["suit"])
            print("- Img:", card["img"])
            print("- Fortune Telling:", card["fortune_telling"])
            print("- Keywords:", card["keywords"])
            print("- Light meanings: ",card.get("meanings", {}).get("light", []))
            print("- Shadow meanings: ",card.get("meanings", {}).get("shadow", []))
            print("\n-----\n")
            cardsArray.append(card)
        return cardsArray
            
miau=Conn("mongodb://localhost:27017","Tarrot","Cards")
miau.conn()
# miau.insert("mewmew")
# miau.insertJSON("./colores.json")
# miau.delete("database",1) ~~ works
for x in miau.cardsList():
    print("----------------------")
    print(x["img"])
    print("----------------------")


    
    
    