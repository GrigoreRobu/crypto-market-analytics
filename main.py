import pandas as pd
import yfinance as yf

btc = yf.Ticker("BTC-USD")
data = btc.history(period="1mo", interval="1h")

data['SMA_24'] = data['Close'].rolling(window=24).mean()
data['Signal'] = (data['Close'] > data['SMA_24']).astype(int)

data.to_csv("crypto_data.csv")