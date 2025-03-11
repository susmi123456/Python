from pymongo import MongoClient

client =MongoClient('mongodb://localhost:27017/')
db=client['6pm']
user_col=db['users']

users=user_col.find({'gender':'Male'})

for user in users:
    print(user['uid'],user['user'],user['gender'])