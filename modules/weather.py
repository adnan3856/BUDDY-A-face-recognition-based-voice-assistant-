import requests
api_key="d77d30eee6a5b556317532f136dcea06"
base_url="https://api.openweathermap.org/data/2.5/weather?"
city_name="Bangalore"
complete_url=base_url+"appid="+api_key+"&q="+city_name
response = requests.get(complete_url)
x=response.json()
if x["cod"]!="404":
    y=x["main"]
    current_temperature = int(y["temp"] - 273.15)
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
