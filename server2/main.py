from fastapi import FastAPI
import datetime
database = {
    'A': {
        "name": "Product A",
        "price": 29.99,
        "details": "This is a sample product description for Product A.",
        "time": datetime.datetime.now(),
    },
    'B': {
        "name": "Product B",
        "price": 19.99,
        "details": "This is a sample product description for Product B.",
        "time": datetime.datetime.now(),
    },
    'C': {
        "name": "Product C",
        "price": 49.99,
        "details": "This is a sample product description for Product C.",
        "time": datetime.datetime.now(),
    }
}

app = FastAPI()


@app.get('/')

def my_first_api() : 
    return {'Output' : 'My first API'}


@app.get('/others')

def my_secound_api() : 
    return {'Output' : 'My secound API'}


# @app.get('/product')

# def my_third_api() : 
#     data = list(database.values())
#     return data


@app.get('/product/{item}')

def my_third_api(item: str) : 
    
    return database[item]



@app.get('/product')

def my_fourth_api(item: int) : 
    data = list(database.values())
    return data[item]


