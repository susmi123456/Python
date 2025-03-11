from pymongo import MongoClient

client =MongoClient('mongodb://localhost:27017/')
db=client['6pm']
user_col=db['users']

#delete ine document
status=user_col.delete_one({'uid':1})
print(status)
print("Deleted Successfully")

