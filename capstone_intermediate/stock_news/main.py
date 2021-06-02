import os
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TODAY = dt.date.today()
YESTERDAY = TODAY - dt.timedelta(days=1)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": os.environ.get("API_KEY")
}

AV_ENDPOINT = "https://www.alphavantage.co/query?"

response = requests.get(url=AV_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()
time_series = stock_data["Time Series (Daily)"]
stock_today = time_series[str(TODAY)]['1. open']
stock_yesterday = time_series[str(YESTERDAY)]['1. open']
print(stock_today, stock_yesterday)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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

