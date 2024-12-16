import yfinance as yf
import talib as ta
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
