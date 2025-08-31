#Python needs a MongoDB driver to access the MongoDB database
import pymongo

#create a database called "dbFernandoVivancoL00385757"
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["dbFernandoVivancoL00385757"] #dbFernandoVivancoL00385757

#Return a list of your system's databases
print(myclient.list_database_names())

#check if "dbFernandoVivancoL00385757" exists
dbList = myclient.list_database_names()
if "miscelanea" in dbList:
    print("The database exists.")

#Return a list of all collections in your database
print(mydb.list_collection_names())