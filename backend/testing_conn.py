import pymongo


client = pymongo.MongoClient("mongodb+srv://censored:censored@cluster0.5anb5uj.mongodb.net/?retryWrites=true&w=majority")
db = client.delivery_app
collection = db.meals



results = collection.find({})

for i in results:
    print(i)

    







