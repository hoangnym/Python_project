import os
import requests
import datetime as dt
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TODAY = dt.date.today()
YESTERDAY = TODAY - dt.timedelta(days=1)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TW_SID") # twilio account sid
auth_token = os.environ.get("TW_AUTH_T") # twilio auth_token


# Use https://newsapi.org
def get_news(company=COMPANY_NAME):
    news_parameters = {
        "q": company,
        "from": str(YESTERDAY),
        "sortBy": "popularity",
        "apiKey": os.environ.get("NEWS_API")
    }

    news_endpoint = "https://newsapi.org/v2/everything?"

    response_news = requests.get(url=news_endpoint, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    top_articles = news_data["articles"][0:3]
    headlines = {article["title"]:article["description"] for article in top_articles}

    return headlines


def send_sms(headline, message, stock_movement, direction):
    # Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)  # when hosted in cloud include: http_client=proxy_client
    message = client.messages.create(
        body=f"{STOCK}: {direction}{stock_movement}%\nHeadline: {headline} \nBrief: {message}",
        from_=os.environ.get("TW_PHONE"),  # your twilio number
        to=os.environ.get("P_PHONE")  # your verified number
    )

    print(message.status)


if __name__ == '__main__':

    # Use https://www.alphavantage.co
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": os.environ.get("API_KEY")
    }

    AV_ENDPOINT = "https://www.alphavantage.co/query?"

    response = requests.get(url=AV_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    stock_data = response.json()
    time_series = stock_data["Time Series (Daily)"]
    stock_today = float(time_series[str(TODAY)]['1. open'])
    stock_yesterday = float(time_series[str(YESTERDAY)]['1. open'])
    stock_movement = int((abs(stock_yesterday - stock_today)/stock_yesterday)*100)
    top_news = get_news()
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    for (headline, content) in top_news.items():
        if stock_movement > 0:
            send_sms(headline, content, stock_movement, "🔺")
        elif stock_movement < 0:
            send_sms(headline, content, stock_movement, "🔻")
        else:
            send_sms(headline, content, stock_movement, "~")

