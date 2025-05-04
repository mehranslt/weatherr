import requests

API_KEY = 'b79f94dc57599f81cd3ee37fa5b931da'

def get_weather(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fa'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"آب‌وهوای {city_name}: {weather}، دما: {temp} درجه سانتی‌گراد")
    except Exception as e:
        print("خطا در دریافت اطلاعات:", e)

city = input("نام شهر را وارد کنید: ")
get_weather(city)
print ("update version")