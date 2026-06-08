import yfinance as yf
import pandas as pd

def get_price_data(tickers, start="2020-01-01", end="2025-01-01"):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)
    close = data["Close"]
    volume = data["Volume"]
    return close, volume