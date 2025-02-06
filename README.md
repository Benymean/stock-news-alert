# Stock Market News Alert Script

A Python script that monitors stock price changes and fetches related news articles when significant changes are detected, using the Alpha Vantage API.

## Features

- Retrieves daily stock data for specified symbols
- Detects significant price changes between opening and closing prices
- Fetches latest news articles related to the stock symbol
- Displays formatted output with price changes and news summaries

## Prerequisites

- Python 3.x
- `requests` library
- Alpha Vantage API key (free tier available)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-news-alert.git
cd stock-news-alert
```

## Configuration
- 1-Get your free API key from Alpha Vantage
- 2-Replace the placeholder in the script

## Usage
- Run the script with default settings (AMZN):  
  ```bash
  python3 stock_news_alert.py
  ```
- To monitor a different stock:
  ``` bash
  STOCK_SYMBOL = "MSFT"  # Change the symbol at the top of the script

## Sample Output
Stock Price Changes:
2023-08-01: 1.23%
2023-07-31: 0.89%

Significant Change Detected!

Latest News:

Title: Amazon Reports Strong Q2 Earnings
URL: https://example.com/amazon-earnings
Published: 20230801T120000
Source: Financial Times
Summary: Amazon exceeds analyst expectations with record cloud revenue...

## API Key Notes
- Free tier limited to 5 requests per minute
- Daily limit of 25 requests for free keys

## Limitations
- Only checks daily time series (intraday not available in free tier)
- News search limited to current UTC day
- English language news only
