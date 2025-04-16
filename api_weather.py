import requests

API_KEY = "Put your API key here"
city = "Taipei"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=zh_tw"

response = requests.get(url)
data = response.json()

print(f"{data['name']} Current Temperature：{data['main']['temp']}°C")
print(f"Weather Description：{data['weather'][0]['description']}")
