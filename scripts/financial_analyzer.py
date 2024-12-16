   #task -2 ,
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

def retrieve_stock_data(ticker, start_date, end_date):
    """
    Retrieve historical stock data using yfinance.

    Parameters:
    - ticker (str): The stock ticker symbol (e.g., 'AAPL').
    - start_date (str): The start date for historical data in 'YYYY-MM-DD' format.
    - end_date (str): The end date for historical data in 'YYYY-MM-DD' format.

    Returns:
    - pandas.DataFrame: Historical stock data.
    """
    return yf.download(ticker, start=start_date, end=end_date)

def plot_stock_and_sma(df):
    """Plot stock closing price and 14-day SMA"""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_14'], label='14-Day SMA', color='orange')
    plt.title('AAPL Stock Price and 14-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price ')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rsi(df):
    """Plot RSI (Relative Strength Index)"""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['RSI'], label='RSI (14)', color='green')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='blue', linestyle='--', label='Oversold (30)')
    plt.title('RSI (14) for AAPL Stock')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_macd(df):
    """Plot MACD and Signal Line"""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['MACD'], label='MACD', color='blue')
    plt.plot(df['Date'], df['MACD_signal'], label='MACD Signal', color='orange')
    plt.bar(df['Date'], df['MACD_hist'], label='MACD Histogram', color='gray', alpha=0.3)
    plt.title('MACD and Signal Line for AAPL Stock')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
