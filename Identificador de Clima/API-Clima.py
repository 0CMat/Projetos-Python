import requests
from pprint import pprint

API_Key = "3e11b826325aa41cabc9fe966022b2ea"
city = input('Digite a cidade em qual deseja saber o tempo:\n')

base_URL = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_URL).json()

# cidade = 
# temp =
# temp_max = 
# temp_min =

pprint(weather_data)
