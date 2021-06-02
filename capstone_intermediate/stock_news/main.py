import os
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TODAY = dt.date.today()
YESTERDAY = TODAY - dt.timedelta(days=1)

## STEP 1: Use https://www.alphavantage.co
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
stock_movement = abs(stock_yesterday - stock_today)/stock_yesterday

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if stock_movement >= 0.05:
    print("Get News")
else:
    print(stock_movement, stock_yesterday, stock_today)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company=COMPANY_NAME):
    news_parameters = {
        "q": company,
        "from": str(YESTERDAY),
        "sortBy": "popularity",
        "apiKey": os.environ.get("NEWS_API")
    }

    NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    top_articles = news_data["articles"][0:3]
    headlines = {article["title"]:article["description"] for article in top_articles}

    return headlines



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

