import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS="miscelanea"
MONGO_COLLECTION="books"
cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos=cliente[MONGO_BASEDATOS]
coleccion=baseDatos[MONGO_COLLECTION]
#return a list of all collections in your database
print(baseDatos.list_collection_names())

collist = baseDatos.list_collection_names()
if "books" in collist:
    print("The collection exists.")
    
#find the first document in the books collection
x = coleccion.find_one()
print(x)

#return all documents in the books collection, and print each document
#for x in coleccion.find():
    #print(x)
    
#Return only some fields
#for x in coleccion.find({},{"status":1}):
    #print(x)
    
#Query
myquery = { "status": "NAMES"}
mydoc = coleccion.find(myquery)
for names in mydoc:
    print(names)
    
