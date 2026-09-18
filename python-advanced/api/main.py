from fastapi import FastAPI
from enum import Enum


app=FastAPI()

@app.get("/hello") #it is the end point of the url if u add "/hello" at the end of the url it will run the below func'''
def hello():
    return "Hello Kshitish"

@app.get("/hello/{name}")
def hello_name(name):
    return f"Hello {name}"

@app.get("/")

def home():
    return "Hello World"

food_items = {
    'indian' : [ "Samosa", "Dosa" ],
    'american' : [ "Hot Dog", "Apple Pie"],
    'italian' : [ "Ravioli", "Pizza"]
}

class AvailableCuisine(str, Enum):
    indian = 'indian'
    american = 'american'
    italian= 'italian'

@app.get("/get_items/{cuisine}")

def get_items(cuisine :AvailableCuisine):
    return food_items[cuisine]

    # if cuisine in food_items:
    #     return food_items[cuisine]
    # else:
#         #print(f"{cuisine} items not available")
# print() only prints something in the server terminal.
# It does not send that message back to the person making the API request.
# So the client might receive an unexpected empty/null response instead of a proper error.
#         return f"{cuisine} items not available"


coupon_code={
    1:'10 %',
    2:'20 %',
    3:'30 %',
}

@app.get("/get_coupon/{code}")

async def get_coupon(code : int):
    return { 'coupon' : coupon_code[code] }