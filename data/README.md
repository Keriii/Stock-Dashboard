# Data Directory

Handles data management and processing for the dashboard.

## Files

### stock_data.py

Stock data manager implementation:

- Data fetching from yfinance
- Technical indicator calculations
- Caching mechanism
- Error handling

### **init**.py

Package initialization

## Features

1. **Data Fetching**

   - Real-time stock data
   - Multiple timeframes
   - Historical data

2. **Technical Indicators**

   - Moving Averages (SMA)
   - RSI calculation
   - MACD implementation

3. **Caching**
   - Performance optimization
   - Memory management
   - Cache invalidation

## Usage

``` python
from data.stock_data import StockDataManager
Initialize manager
manager = StockDataManager()
Fetch data
data=manager.get_stock_data('AAPL', period='1y', interval='1d')
```
