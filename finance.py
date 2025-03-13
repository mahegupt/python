import yfinance as yf
import pandas as pd
import talib

# Define your watchlist
stocks = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']

# Define a function to check for bullish trend
def is_bull_trending(ticker):
    data = yf.download(ticker, period="6mo", interval="1d")
    
    # Calculate moving averages
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    
    # Calculate RSI
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    
    # Calculate MACD
    data['MACD'], data['Signal'], _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    # Define bull trend conditions
    if (
        data['Close'].iloc[-1] > data['MA50'].iloc[-1] > data['MA200'].iloc[-1] and  # Price above both MAs
        data['RSI'].iloc[-1] > 50 and  # RSI > 50
        data['MACD'].iloc[-1] > data['Signal'].iloc[-1]  # MACD above signal line
    ):
        return True
    return False

# Filter stocks
bull_stocks = [stock for stock in stocks if is_bull_trending(stock)]
print("Bull Trending Stocks:", bull_stocks)
