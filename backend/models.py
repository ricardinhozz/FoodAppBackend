from pydantic import BaseModel

class Meal(BaseModel):
    title: str
    price: float
    description: str
    photo_url: str