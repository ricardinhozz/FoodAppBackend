from models import Meal
import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://censored:censored@cluster0.5anb5uj.mongodb.net/?retryWrites=true&w=majority")
db = client.delivery_app
collection = db.new_meals


async def fetch_one_meal(title):
    document = collection.find_one({'title': title})
    return document

async def fetch_all_meals():
    all_meals = []
    cursor = collection.find({})
    for document in cursor:
        all_meals.append(Meal(**document))
    return all_meals

async def insert_meal(meal):
    document = meal
    response = collection.insert_one(meal)
    return document

async def update_meal_info(title,new_title,description,price,photo_url):
    collection.update_one({
'title':title,},{"$set":{
'title':new_title,
'description':description,
'price':price,
'photo_url':photo_url
}})
    
    updated_meal = collection.find_one({'title':title})
    return updated_meal

async def delete_meal(title):
    collection.delete_one({'title':title})
    return True
