import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/PyNotes/.env")
BOT_TOKEN = os.getenv("MyWeatherBotToken")
CHATID = os.getenv("MyWeatherChatID")
API_KEY = os.getenv("MyWeatherApiKey")
LATITUDE = float(os.getenv("MyLat"))
LONGITUDE = float(os.getenv("MyLon"))


def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = CHATID
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID
                 + '&parse_mode=Markdown&text=' + bot_message)

    response = requests.get(send_text)

    return response.json()


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 5,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
weather_list = [time["weather"][0]["id"] for time in weather_data["list"]]
print(weather_list)
if any(code < 300 for code in weather_list):
    print("Extremely Bad Weather")
    message = telegram_bot_sendtext(f"{weather_list}\nEXTREMELY BAD WEATHER TODAY, THUNDERSTORM!🌩⛈🌪🌬☔")
elif any(code < 500 for code in weather_list):
    print("Light Drizzle")
    message = telegram_bot_sendtext(f"{weather_list}\nLight drizzle today, maybe take an umbrella with you!🌦☂☔")
elif any(code < 600 for code in weather_list):
    print("Bad Rain")
    message = telegram_bot_sendtext(f"{weather_list}\nBad rain today, take an umbrella with you!🌧☂☔💧")
elif any(code < 700 for code in weather_list):
    print("Snow Incoming")
    message = telegram_bot_sendtext(f"{weather_list}\nSnowy weather today, keep warm and take an umbrella with you!🌨☂☔💧❄")
elif any(code < 800 for code in weather_list):
    print("Blurry Air")
    message = telegram_bot_sendtext(f"{weather_list}\nThe air is not so great, expect low visibility!🌫🌫🌫")
elif any(code == 800 for code in weather_list):
    print("Clear Sky")
    message = telegram_bot_sendtext(f"{weather_list}\nThe weather is great today, CLEAR SKIES!☀☀☀")
else:
    print("Cloudy Sky")
    message = telegram_bot_sendtext(f"{weather_list}\nThe weather cloudy today!☁⛅🌥")
