import requests
from pprint import pprint

API_Key = "d4abbe913da9feb3d26ab9be4737e064"
city = input('Digite a cidade em qual deseja saber o tempo:\n')

base_URL = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_URL).json()

# cidade =
print("Cidade:\n", weather_data['name'])
# temp =
temperatura = round(273.15 - weather_data['main']['temp'],2)
print("Temperatura Atual:\n", f"{temperatura}ºC")
# temp_max =
temperatura_max = round(273.15 - weather_data['main']['temp_max'],2)
print("Temperatura Máxima:\n",f"{temperatura_max}ºC")
# temp_min =
temperatura_min = round(273.15 - weather_data['main']['temp_min'],2)
print("Temperatura Mínima:\n",f"{temperatura_min}ºC")

# pprint(weather_data)
