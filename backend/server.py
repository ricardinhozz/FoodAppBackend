from fastapi import FastAPI, HTTPException
from exceptions import *
from fastapi.middleware.cors import CORSMiddleware
from database import (
    delete_meal,
    update_meal_info,
    insert_meal,
    fetch_all_meals,
    fetch_one_meal,
    Meal)

app = FastAPI()


origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get('/')
async def home():
    return {'This is':'working'}

@app.get('/api/meals')
async def get_all_meals():
    response = await fetch_all_meals()
    return response

@app.get('/api/meals{title}', response_model = Meal)
async def get_meal_by_title(title):
    response = await fetch_one_meal(title)
    if response:
        return response
    raise HTTPException(404, exception_404_message )

@app.post('/api/meals', response_model= Meal)
async def post_meal(meal: Meal):
    response = await insert_meal(meal.dict())
    if response:
        return response
    raise HTTPException(400, exception_400_message )

@app.put('/api/meals{title}')
async def update_meal_infomations(title:str,new_title:str,description:str,price:float,photo_url:str):
    response = await update_meal_info(title,new_title,description,price,photo_url)
    if response:
        return response
    raise HTTPException(400, exception_400_message)  

@app.delete('/api/meals{title}')
async def delete_meal_by_title(title):
    response = await delete_meal(title)
    if response:
        return True
    raise HTTPException(404, exception_404_message)