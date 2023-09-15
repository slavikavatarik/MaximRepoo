from fastapi import FastAPI, Query, HTTPException
import requests

Api = 'a91c1752c84fea7efe626fcf268f2313'

app = FastAPI()

@app.get("/")
async def weather(City: str = Query()):
    
    #inCity = input('Введите город: ')

    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={City}&appid={Api}')
    json_data = weather.json()
    
    if json_data['cod'] == '404':
        raise HTTPException(status_code=404, detail="Item not found")
    
    lat = json_data['coord']['lat']
    lon = json_data['coord']['lon']
    city = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Api}&units=metric')
    json_city = city.json()
    
    return(f"Температура в городе {City}: ", str(json_city['main']['temp']) + "C°")


import requests
from fastapi import FastAPI

Api = 'ab965cadaf6e16b9ae7a994b7598885f'

app = FastAPI()

@app.get("/")

async def read_item(City):
    tempCls = getTemperature(City)
    if tempCls != "Error":
      tempOut = f"Температура в городе {City}: ", tempCls + "C°"
    else:
        tempOut = f"The city {City} not found !"
    return tempOut

def getTemperature(city):
    value = ""
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api}')
    json_data = weather.json()
    try:
      lat = json_data['coord']['lat']
    except Exception as exc:
        value = "Error"
    if (value != ""):
       return value

    try:
      lon = json_data['coord']['lon']
    except Exception as exc:
        value = "Error"
    if (value != ""):
       return value

    city = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Api}&units=metric')
    json_city = city.json()

    value = str(json_city['main']['temp'])
    return value