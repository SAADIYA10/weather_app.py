import requests
api_key="0ca9625e9d9b30034bce2a3aa63eb4d1"
city=input("enter the city name:")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
data=response.json()
if data["cod"]==200:
    temp=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    weather=data["weather"][0]["description"]
    print("\ncity:",city)
    print("Temperature:",temp,"°C")
    print("Humidity:",humidity,"%")
    print("weather conditon:",weather)
else:
    print("city not found")
