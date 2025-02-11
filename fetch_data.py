# Fetch stock prices & volatility using Yahoo Finance API 
import yfinance as yf 
import numpy as np

# Fetch historical stock data 
def get_stock_data(ticker): 
    """
    Fetches current stock price and historical volatility using Yahoo Finance API.
    Parameters:
        ticker: Stock ticker symbol (e.g., "AAPL")
    Returns:
        current_price: Latest closing price of the stock
        volatility: Annualized historical volatility
    """
    try: 
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d") ["Close"].iloc[-1]

        # Get historical data for volatility calculation: 
        data = stock.history(period="6mo")
        log_returns = np.log(data["Close"] / data["Close"].shift(1))
        ''' 
        Annualized volatility calculation below; given as std deviation times number of periods in a year, 
        which is 252 trading days 
        '''
        volatility = np.std(log_returns) * np.sqrt(252) 
        return current_price, volatility 
    except Exception as e: 
        raise ValueError(f"Error fetching data for {ticker}: {e}")
