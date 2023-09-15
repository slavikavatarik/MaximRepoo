
import requests
import json
city = "Moscow"
url = f'https://openweathermap.org/find?q={city}&units=metric&lang=ru&appid=79011035a9af358337c2c8495c308c71'

weather_data = requests.get(url)

json_dat = weather_data.json()

weather_data_struc = json.dumps(weather_data, indent=2)
print(weather_data_struc)