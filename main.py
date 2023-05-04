import requests
import json
API_KEY = "97662a9d5f264bea82c83440231404"
city = input("Vremea din care oraș te interesează?\n")
response = requests.get("http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + city + "&aqi=no")
processed = json.loads(response.content)
print("Vremea din",processed["location"]["name"])
print("Temperatura:", processed["current"]["temp_c"])
print("Conditia vremii:", processed["current"]["condition"]["text"])
print("Viteza vantului(km/h):", processed["current"]["wind_kph"])