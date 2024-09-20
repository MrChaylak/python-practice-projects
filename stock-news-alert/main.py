import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/PyNotes/.env")
BOT_TOKEN = os.getenv("MyStocksBotToken")
CHATID = os.getenv("MyStocksChatID")
STOCKS_API_KEY = os.getenv("MyStockApiKey")
NEWS_API_KEY = os.getenv("MyNewsApiKey")


def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = CHATID
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID
                 + '&parse_mode=Markdown&text=' + bot_message)


    response = requests.get(send_text)

    return response.json()


AV_Endpoint = "https://www.alphavantage.co/query"

STOCK = "AMD"
COMPANY_NAME = "Advanced Micro Devices Inc"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}

News_Endpoint = "https://newsapi.org/v2/everything"

news_params = {
    "q": f"{STOCK} OR {COMPANY_NAME}",
    'searchIn': 'title,description',
    "sortBy": "popularity",
    "pageSize": 3,
    "apikey": NEWS_API_KEY
}

stocks_response = requests.get(AV_Endpoint, params=stock_params)
stocks_response.raise_for_status()
stock_data = stocks_response.json()

last_two_days = list(stock_data["Time Series (Daily)"].items())[0:2]
last_close_price = float(last_two_days[0][1]["4. close"])
old_close_price = float(last_two_days[1][1]["4. close"])
print(last_close_price, old_close_price)
change_amount = last_close_price - old_close_price
print(f"{change_amount:.2f}")
change_percentage = ((last_close_price - old_close_price) / old_close_price) * 100
print(f"{change_percentage:.2f}%")
if change_percentage > 0:
    arrow = "🔺"
else:
    arrow = "🔻"
if change_percentage >= 5 or change_percentage <= -5:
    news_response = requests.get(News_Endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    for news in news_data["articles"]:
        news_title = news["title"]
        news_description = news["description"]
        message = telegram_bot_sendtext(
            f"{STOCK}: ${last_close_price} {arrow}{change_amount:.2f} {arrow}{change_percentage:.2f}%\nHeadline: {news_title}"
            f"\nBrief: {news_description}")
else:
    message = telegram_bot_sendtext(f"{STOCK}: ${last_close_price} {arrow}{change_amount:.2f} {arrow}{change_percentage:.2f}%"
                                    f"\nThere was no significant change in the {STOCK} stock price.")
