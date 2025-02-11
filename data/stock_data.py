import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class StockDataManager:
    def __init__(self):
        self.default_stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
        self.cache = {}
        
    def get_stock_data(self, symbol, period='1y', interval='1d'):
        """Fetch stock data from Yahoo Finance"""
        cache_key = f"{symbol}_{period}_{interval}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            stock = yf.Ticker(symbol)
            df = stock.history(period=period, interval=interval)
            df.reset_index(inplace=True)
            
            # Add technical indicators
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df['SMA_50'] = df['Close'].rolling(window=50).mean()
            df['RSI'] = self.calculate_rsi(df['Close'])
            df['MACD'], df['Signal_Line'] = self.calculate_macd(df['Close'])
            
            self.cache[cache_key] = df
            return df
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return pd.DataFrame()
    
    def get_stock_info(self, symbol):
        """Get company information"""
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            return {
                'name': info.get('longName', symbol),
                'sector': info.get('sector', 'N/A'),
                'industry': info.get('industry', 'N/A'),
                'market_cap': info.get('marketCap', 0),
                'pe_ratio': info.get('trailingPE', 0),
                'dividend_yield': info.get('dividendYield', 0)
            }
        except:
            return {}
    
    @staticmethod
    def calculate_rsi(prices, period=14):
        """Calculate Relative Strength Index"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    @staticmethod
    def calculate_macd(prices, fast=12, slow=26, signal=9):
        """Calculate MACD and Signal Line"""
        exp1 = prices.ewm(span=fast, adjust=False).mean()
        exp2 = prices.ewm(span=slow, adjust=False).mean()
        macd = exp1 - exp2
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        return macd, signal_line 