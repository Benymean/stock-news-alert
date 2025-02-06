import requests

# API Configuration
API_KEY = "VMG718GQSTK5RY6R"  # free tier API Key
STOCK_SYMBOL = "AMZN"
BASE_URL = "https://www.alphavantage.co/query"


# Fetch stock data
def get_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json().get("Time Series (Daily)", {})

    if not data:
        print("No stock data found.")
        return None

    return list(data.items())[:2]  # Get the last two days' data


# Fetch related news
def get_news(from_date, to_date):
    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": STOCK_SYMBOL,
        "time_from": from_date,
        "time_to": to_date,
        "apikey": API_KEY,
        "sort": "LATEST",
        "limit": 5
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("feed", [])
    print("Failed to fetch news.")
    return []


# Check for significant stock change
def big_change_check(stock_data):
    dates = [date.replace('-', '') + "T0000" for date, _ in stock_data]
    changes = []

    for _, day in stock_data:
        open_price = float(day["1. open"])
        close_price = float(day["4. close"])
        percentage_change = ((open_price - close_price) / close_price) * 100
        changes.append(percentage_change)

    # Display stock change
    print("\nStock Price Changes:")
    for i, change in enumerate(changes):
        print(f"{stock_data[i][0]}: {change:.2f}%")

    # Fetch news if significant change detected
    for change in changes:
        if abs(change) > 0.1:
            print("\nSignificant Change Detected!")
            news_articles = get_news(dates[1], dates[0])
            if news_articles:
                print("\nLatest News:")
                for article in news_articles:
                    print(f"\nTitle: {article['title']}")
                    print(f"URL: {article['url']}")
                    print(f"Published: {article['time_published']}")
                    print(f"Source: {article['source']}")
                    print(f"Summary: {article['summary']}")
            else:
                print("No relevant news articles found.")


# Execute script
stock_data = get_stock_data(STOCK_SYMBOL)
if stock_data:
    big_change_check(stock_data)
