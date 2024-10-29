# Creating A Weather Forecast System
import requests
from datetime import datetime
def keltocel(kelvin):
    celsius = kelvin - 273.15
    return celsius
def sectotim(second):
    date_time = str(datetime.fromtimestamp(second))
    time = date_time.split(" ")[1]


    hours = time.split(":")[0]
    hours = int(hours)
    if hours > 12:
        hours = hours - 12

    time = time.split(":")
    time[0] = str(hours)
    time = ':'.join(time)


    return time

city = input("Enter the city name you want weather forecast of: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fc36475fee525d450be594f664f83c4b"
response = requests.get(url)

if response.status_code == 200:
    pass
else:
    print("Invalid Region")
    exit(0)

response = response.json()



print(f"Country: {response['sys']['country']}")
print(f"Region: {response['name']}")
print(f"The Temperature is {int(keltocel(response['main']['temp']))} C°")
print(f"The Humidity is {response['main']['humidity']}%")
print(f"The Wind Speed is {response['wind']['speed']} Km/h ")
print(f"The Pressure is {response['main']['pressure']} hPa ")
print(f"The Timing of Sunrise is {sectotim(response['sys']['sunrise'])} AM")
print(f"The Timing of Sunset is {sectotim(response['sys']['sunset'])} PM")
print(f"Longitude is {response['coord']['lon']}° ")
print(f"Latitude is {response['coord']['lat']}° ")
print(f"Visibility: {response['visibility']} Meter")

