from fastapi import FastAPI # type: ignore
import random

app = FastAPI()
# we will build to get simp[le end point
# side hassal
# money quotes
side_hustles = [
    "Freelance Writing",
    "Graphic Design",
    "Photography",
    "Voice Over Work",
    "Tutoring",
    "Pet Sitting",
    "House Sitting",
    "Selling Products Online",
    "Delivery Work",
    "House Cleaning",
    "Lawn Care",
    "Yard Work",
    "Handyman Services",
    "House Painting",

]
money_quotes = [
    "Money can't buy happiness, but it does bring you a more pleasant choice of misery.",
    "I'd rather be a failure in something I love than a success in something I hate.",
    "The way to get started is to quit talking and begin doing.",
    "The biggest risk is not taking any risk.",
    "The best way to predict the future is to invent it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts",
    "The only way to do great work is to love what you do.",
    "The biggest adventure you can take is to live the life of your dreams.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The best and most beautiful things in the world cannot be seen or even touched.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall",
    "The biggest risk is not taking any risk.",
    "The best way to predict the future is to invent it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts",



]

@app.get("/side_hustles")
def get_side_hustles(apikey:str):
        """Return a random side hustle idea"""
        if apikey != "12345":   
         return {"error": "Invalid API key"}
        return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quote"""
    return{"money_quote": random.choice(money_quotes)}


